import uuid

from mumble_link_server.models import Server, User


class MurmurServer:
    def __init__(self,
                 server_id: uuid = None,
                 name: str = None,
                 port: int = None,
                 max_users: int = None,
                 server_password: str = None,
                 superuser_password: str = None,
                 server=None):
        self._server = server
        self._server_id = server_id
        self._server_name = name
        self._port = port
        self._max_users = max_users
        self._server_password = server_password
        self._superuser_password = superuser_password

    def get_server_id(self):
        return self._server_id

    def get_server_name(self):
        return self._server_name

    def set_server_name(self, server_name: str = None):
        if server_name is not None:
            self._server.setConf("registername", server_name)
            self._server_name = server_name

    def get_port(self):
        return self._port

    def get_max_users(self):
        return self._max_users

    def set_max_users(self, max_users: int = None):
        if max_users is not None:
            self._server.setConf("users", str(max_users))
            self._max_users = max_users

    def get_server_password(self):
        return self._server_password

    def set_server_password(self, server_password: str = None):
        if server_password is not None:
            self._server.setConf("serverpassword", server_password)
            self._server_password = server_password

    def get_superuser_password(self):
        return self._superuser_password

    def set_superuser_password(self, superuser_password: str = None):
        if superuser_password is not None:
            self._server.setSuperuserPassword(superuser_password)
            self._superuser_password = superuser_password

    def get_server(self):
        return self._server

    def get_users(self):
        users = self._server.getUsers()
        return [User(user.userid, user.name, user.mute, user.deaf, user.selfMute, user.selfDeaf, str(uuid.uuid4()),
                     user.channel) for (_, user) in users.items()]

    def to_api_server(self):
        return Server(str(self._server_id), self._server_name, self._max_users, len(self._server.getUsers()),
                      self._server_password, self._superuser_password)

    def delete(self):
        self._server.stop()
        self._server.delete()
