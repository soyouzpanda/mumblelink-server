import logging
import os
import socket
import tempfile
import uuid

import Ice
import IcePy

from mumble_link_server.mumble.murmur_server import MurmurServer


class MurmurConnector:
    def __init__(self, ip: str, port: int, secret: str | None = None):
        self._log = logging.getLogger('murmur')
        self._ip = ip
        self._port = port
        self._secret = secret
        self._loaded = False
        self._murmur = None
        self._proxy = None
        self._meta = None
        self._ice = None
        self._servers = {}
        self._base_port = 64738

    def generate_murmur(self, ice_file: str):
        try:
            Ice.loadSlice(f"-I {Ice.getSliceDir()}", [ice_file])
            self._loaded = True
            self._log.debug(f"Loaded slice from {ice_file}")
        except Ice.Exception:
            raise RuntimeError(f"Could not generate python module Murmur for {ice_file}")

    def generate_murmur_remote(self):
        self._log.info("Loading slice from server")
        try:
            initdata = Ice.InitializationData()
            initdata.properties = Ice.createProperties([], initdata.properties)

            initdata.properties.setProperty('Ice.ImplicitContext', 'Shared')
            initdata.properties.setProperty('Ice.Default.EncodingVersion', '1.0')
            initdata.logger = MurmurLogger()

            ice = Ice.initialize(initdata)

            if self._secret:
                ice.getImplicitContext().put('secret', self._secret)

            proxy = ice.stringToProxy(f"Meta:tcp -h {self._ip} -p {self._port}")

            op = IcePy.Operation('getSlice', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, None, (),
                                 (), (), ((), IcePy._t_string, False, 0), ())
            slice = op.invoke(proxy, ((), None))

            (slice_desc, slice_path) = tempfile.mkstemp(suffix='.ice')
            slice_file = os.fdopen(slice_desc, 'w')
            slice_file.write(slice)
            slice_file.flush()

            self.generate_murmur(slice_path)

            slice_file.close()
            os.remove(slice_path)

            ice.destroy()

        except (Ice.Exception, OSError, IOError) as e:
            self._log.critical("Failed to load slice remotely")
            raise RuntimeError

    def import_murmur(self):
        if self._loaded and not self._murmur:
            try:
                import MumbleServer
            except ModuleNotFoundError:
                import Murmur as MumbleServer
            self._murmur = MumbleServer
            self._log.debug(f"Imported Murmur module")
        elif self._loaded:
            pass
        else:
            raise RuntimeError("Tried to import Murmur when it wasn't generated")

    def next_free_port(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = self._base_port
        while port <= 65535:
            try:
                sock.bind(('', port))
                sock.close()
                return port
            except OSError:
                port += 1
        raise IOError('No free ports')

    def get_murmur(self):
        return self._murmur

    def connect(self):
        if not self._murmur:
            raise RuntimeError("Cannot connect to murmur without Murmur module not loaded")

        initdata = Ice.InitializationData()
        initdata.properties = Ice.createProperties([], initdata.properties)

        initdata.properties.setProperty('Ice.ImplicitContext', 'Shared')
        initdata.properties.setProperty('Ice.Default.EncodingVersion', '1.0')
        initdata.logger = MurmurLogger()

        self._ice = Ice.initialize(initdata)

        if self._secret:
            self._ice.getImplicitContext().put('secret', self._secret)

        self._proxy = self._ice.stringToProxy(f"Meta:tcp -h {self._ip} -p {self._port}")
        self._meta = self._murmur.MetaPrx.uncheckedCast(self._proxy)
        self._log.debug(f"Connected to Murmur server {self._ip}:{self._port}")

        for server in self._meta.getAllServers():
            server.stopAsync()
            server.deleteAsync()

    def disconnect(self):
        if self._meta:
            for (_, server) in self._servers.items():
                server.delete()
        if self._ice:
            self._ice.destroy()
            self._log.debug(f"Disconnect from Murmur server {self._ip}:{self._port}")

    def get_meta(self):
        return self._meta

    def get_servers(self):
        return self._servers

    def get_server(self, server_id: uuid.UUID):
        return self._servers.get(server_id, None)

    def new_server(self, name: str = None, port: int = None, max_users: int = None, server_password: str = None, superuser_password: str = None):
        if self._meta:
            if not name:
                name = "Mumble Server"

            if not max_users:
                max_users = 100

            if not port:
                port = self.next_free_port()

            murmur_server = self._meta.newServer()
            murmur_server.setConf("port", str(port))
            murmur_server.setConf("registername", name)
            murmur_server.setConf("users", str(max_users))

            if server_password:
                murmur_server.setConf("serverpassword", server_password)

            if superuser_password:
                murmur_server.setSuperuserPassword(superuser_password)

            server_id = uuid.uuid4()
            server = MurmurServer(server_id, name, port, max_users, server_password, superuser_password, murmur_server)

            self._servers[server_id] = server

            # TODO: Adding callbacks
            # callback = self._murmur.ServerCallbackPrx.uncheckedCast(MurmurCallback(self, server))
            # murmur_server.addCallback(callback)

            murmur_server.startAsync()

            return server
        else:
            raise RuntimeError("self._meta is uninitialized")

    def delete_server(self, server_id: uuid.UUID):
        server = self._servers.pop(server_id, None)
        if server:
            try:
                server.delete()
            except (Ice.Exception, self._murmur.ServerBootedException) as e:
                self._log.warning(f"Error while deleting server {server_id}")
                self._log.exception(e)
                raise RuntimeError
        else:
            raise KeyError


class MurmurCallback:
    def __init__(self, connector: MurmurConnector, server: MurmurServer):
        self._connector = connector
        self._server = server

    def userStateChanged(self, u, current=None):
        pass

    def userDisconnected(self, u, current=None):
        pass

    def userConnected(self, u, current=None):
        self._server.get_server().registerUser({"UserName": u.name})

    def channelCreated(self, c, current=None):
        pass

    def channelRemoved(self, c, current=None):
        pass

    def channelStateChanged(self, c, current=None):
        pass

    def userTextMessage(self, u, m, current=None):
        pass


class MurmurLogger(Ice.Logger):
    def __init__(self):
        Ice.Logger.__init__(self)
        self._log = logging.getLogger('murmur')

    def _print(self, message):
        self._log.info(message)

    def trace(self, category, message):
        self._log.debug('Trace %s: %s', category, message)

    def warning(self, message):
        self._log.warning(message)

    def error(self, message):
        self._log.error(message)
