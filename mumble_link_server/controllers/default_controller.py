import logging
import uuid

import Ice
import connexion
import flask
import six
from typing import Dict
from typing import Tuple
from typing import Union

from flask import current_app

from mumble_link_server.mumble.murmur_connector import MurmurConnector
from mumble_link_server.models.ban import Ban  # noqa: E501
from mumble_link_server.models.channel import Channel  # noqa: E501
from mumble_link_server.models.error import Error  # noqa: E501
from mumble_link_server.models.group import Group  # noqa: E501
from mumble_link_server.models.server import Server  # noqa: E501
from mumble_link_server.models.server_create_post_request import ServerCreatePostRequest  # noqa: E501
from mumble_link_server.models.server_server_id_channel_channel_id_put_request import \
    ServerServerIdChannelChannelIdPutRequest  # noqa: E501
from mumble_link_server.models.server_server_id_channel_create_post_request import \
    ServerServerIdChannelCreatePostRequest  # noqa: E501
from mumble_link_server.models.server_server_id_group_create_post_request import \
    ServerServerIdGroupCreatePostRequest  # noqa: E501
from mumble_link_server.models.server_server_id_group_group_id_put_request import \
    ServerServerIdGroupGroupIdPutRequest  # noqa: E501
from mumble_link_server.models.server_server_id_put_request import ServerServerIdPutRequest  # noqa: E501
from mumble_link_server.models.server_server_id_user_user_id_ban_post_request import \
    ServerServerIdUserUserIdBanPostRequest  # noqa: E501
from mumble_link_server.models.server_server_id_user_user_id_kick_post_request import \
    ServerServerIdUserUserIdKickPostRequest  # noqa: E501
from mumble_link_server.models.server_server_id_user_user_id_move_post_request import \
    ServerServerIdUserUserIdMovePostRequest  # noqa: E501
from mumble_link_server.models.server_server_id_users_get200_response import \
    ServerServerIdUsersGet200Response  # noqa: E501
from mumble_link_server.models.servers_get200_response import ServersGet200Response  # noqa: E501
from mumble_link_server.models.user import User  # noqa: E501
from mumble_link_server import util
from mumble_link_server.mumble.murmur_server import MurmurServer


def server_create_post():  # noqa: E501
    """Create a new server

     # noqa: E501

    :param server_create_post_request: 
    :type server_create_post_request: dict | bytes

    :rtype: Union[Server, Tuple[Server, int], Tuple[Server, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        server_create_post_request = ServerCreatePostRequest.from_dict(connexion.request.get_json())  # noqa: E501
        if not isinstance(server_create_post_request, ServerCreatePostRequest):
            return flask.jsonify(Error("Invalid json")), 400

        try:
            with current_app.app_context():
                murmur_connector: MurmurConnector = current_app.murmur_connector

                new_server = murmur_connector.new_server(name=server_create_post_request.name,
                                                         max_users=server_create_post_request.max_users,
                                                         server_password=server_create_post_request.server_password,
                                                         superuser_password=server_create_post_request.superuser_password)

                return flask.jsonify(new_server.to_api_server()), 200
        except (Ice.Exception, AttributeError, IOError) as e:
            log = logging.getLogger('murmur')
            log.error("Got an error in /servers")
            log.exception(e)
            return flask.jsonify(Error("Internal server error")), 500
    else:
        return flask.jsonify(Error("Invalid json")), 400


def server_server_id_channel_channel_id_delete(server_id, channel_id):  # noqa: E501
    """server_server_id_channel_channel_id_delete

    Delete a channel # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str
    :param channel_id: 
    :type channel_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def server_server_id_channel_channel_id_get(server_id, channel_id):  # noqa: E501
    """server_server_id_channel_channel_id_get

    Get channel info # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str
    :param channel_id: 
    :type channel_id: int

    :rtype: Union[Channel, Tuple[Channel, int], Tuple[Channel, int, Dict[str, str]]
    """
    return 'do some magic!'


def server_server_id_channel_channel_id_put(server_id, channel_id,
                                            server_server_id_channel_channel_id_put_request=None):  # noqa: E501
    """server_server_id_channel_channel_id_put

    Modify channel parameters # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str
    :param channel_id: 
    :type channel_id: int
    :param server_server_id_channel_channel_id_put_request: 
    :type server_server_id_channel_channel_id_put_request: dict | bytes

    :rtype: Union[Channel, Tuple[Channel, int], Tuple[Channel, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        server_server_id_channel_channel_id_put_request = ServerServerIdChannelChannelIdPutRequest.from_dict(
            connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def server_server_id_channel_create_post(server_id, server_server_id_channel_create_post_request):  # noqa: E501
    """server_server_id_channel_create_post

    Create a new channel # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str
    :param server_server_id_channel_create_post_request: 
    :type server_server_id_channel_create_post_request: dict | bytes

    :rtype: Union[Channel, Tuple[Channel, int], Tuple[Channel, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        server_server_id_channel_create_post_request = ServerServerIdChannelCreatePostRequest.from_dict(
            connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def server_server_id_channels_get(server_id):  # noqa: E501
    """server_server_id_channels_get

    Get list of channels # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str

    :rtype: Union[List[Channel], Tuple[List[Channel], int], Tuple[List[Channel], int, Dict[str, str]]
    """
    return 'do some magic!'


def server_server_id_delete(server_id):  # noqa: E501
    """server_server_id_delete

    Delete a server # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    try:
        server_id = uuid.UUID(server_id)
        with current_app.app_context():
            murmur_connector: MurmurConnector = current_app.murmur_connector

            murmur_connector.delete_server(server_id)

            return (), 200

    except (RuntimeError, AttributeError) as e:
        log = logging.getLogger('murmur')
        log.error("Got an error in /servers")
        log.exception(e)
        return flask.jsonify(Error("Internal server error")), 500

    except ValueError:
        return flask.jsonify(Error("Badly formed server_id")), 400

    except KeyError:
        return flask.jsonify(Error("Server not found")), 404


def server_server_id_get(server_id):  # noqa: E501
    """server_server_id_get

    Get server info # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str

    :rtype: Union[Server, Tuple[Server, int], Tuple[Server, int, Dict[str, str]]
    """
    try:
        server_id = uuid.UUID(server_id)
        with current_app.app_context():
            murmur_connector: MurmurConnector = current_app.murmur_connector

            server = murmur_connector.get_server(server_id)
            if server is None:
                return flask.jsonify(Error("Server not found")), 404

            return flask.jsonify(server.to_api_server()), 200

    except (Ice.Exception, AttributeError) as e:
        log = logging.getLogger('murmur')
        log.error("Got an error in /servers")
        log.exception(e)
        return flask.jsonify(Error("Internal server error")), 500

    except ValueError:
        return flask.jsonify(Error("Badly formed server_id")), 400


def server_server_id_group_create_post(server_id, server_server_id_group_create_post_request):  # noqa: E501
    """server_server_id_group_create_post

    Create a new group # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str
    :param server_server_id_group_create_post_request: 
    :type server_server_id_group_create_post_request: dict | bytes

    :rtype: Union[Group, Tuple[Group, int], Tuple[Group, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        server_server_id_group_create_post_request = ServerServerIdGroupCreatePostRequest.from_dict(
            connexion.request.get_json())  # noqa: E501
    else:
        return flask.jsonify(Error("Invalid json")), 400


def server_server_id_group_group_id_delete(server_id, group_id):  # noqa: E501
    """server_server_id_group_group_id_delete

    Delete a group # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str
    :param group_id: 
    :type group_id: str
    :type group_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def server_server_id_group_group_id_get(server_id, group_id):  # noqa: E501
    """server_server_id_group_group_id_get

    Get group info # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str
    :param group_id: 
    :type group_id: str
    :type group_id: str

    :rtype: Union[Group, Tuple[Group, int], Tuple[Group, int, Dict[str, str]]
    """
    return 'do some magic!'


def server_server_id_group_group_id_put(server_id, group_id,
                                        server_server_id_group_group_id_put_request=None):  # noqa: E501
    """server_server_id_group_group_id_put

    Modify group parameters # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str
    :param group_id: 
    :type group_id: str
    :type group_id: str
    :param server_server_id_group_group_id_put_request: 
    :type server_server_id_group_group_id_put_request: dict | bytes

    :rtype: Union[Group, Tuple[Group, int], Tuple[Group, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        server_server_id_group_group_id_put_request = ServerServerIdGroupGroupIdPutRequest.from_dict(
            connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def server_server_id_groups_get(server_id):  # noqa: E501
    """server_server_id_groups_get

    Get list of groups # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str

    :rtype: Union[List[Group], Tuple[List[Group], int], Tuple[List[Group], int, Dict[str, str]]
    """
    return 'do some magic!'


def server_server_id_put(server_id, server_server_id_put_request=None):  # noqa: E501
    """server_server_id_put

    Modify server parameters # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str
    :param server_server_id_put_request: 
    :type server_server_id_put_request: dict | bytes

    :rtype: Union[Server, Tuple[Server, int], Tuple[Server, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        server_server_id_put_request = ServerServerIdPutRequest.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            server_id = uuid.UUID(server_id)
            with current_app.app_context():
                murmur_connector: MurmurConnector = current_app.murmur_connector

                server: MurmurServer = murmur_connector.get_server(server_id)
                if server is None:
                    return flask.jsonify(Error("Server not found")), 404

                server.set_server_name(server_server_id_put_request.name)
                server.set_max_users(server_server_id_put_request.max_users)
                server.set_server_password(server_server_id_put_request.server_password)
                server.set_superuser_password(server_server_id_put_request.superuser_password)

                return flask.jsonify(server.to_api_server()), 200
        except (Ice.Exception, AttributeError) as e:
            log = logging.getLogger('murmur')
            log.error("Got an error in /servers")
            log.exception(e)
            return flask.jsonify(Error("Internal server error")), 500

        except ValueError:
            return flask.jsonify(Error("Badly formed server_id")), 400
    else:
        return flask.jsonify(Error("Invalid json")), 400

def server_server_id_user_user_id_ban_post(server_id, user_id,
                                           server_server_id_user_user_id_ban_post_request):  # noqa: E501
    """server_server_id_user_user_id_ban_post

    Ban a user # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str
    :param user_id: 
    :type user_id: int
    :param server_server_id_user_user_id_ban_post_request: 
    :type server_server_id_user_user_id_ban_post_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        server_server_id_user_user_id_ban_post_request = ServerServerIdUserUserIdBanPostRequest.from_dict(
            connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def server_server_id_user_user_id_bans_get(server_id):  # noqa: E501
    """server_server_id_user_user_id_bans_get

    Get list of banned users # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str

    :rtype: Union[List[Ban], Tuple[List[Ban], int], Tuple[List[Ban], int, Dict[str, str]]
    """
    return 'do some magic!'


def server_server_id_user_user_id_get(server_id, user_id):  # noqa: E501
    """server_server_id_user_user_id_get

    Get user info # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str
    :param user_id: 
    :type user_id: int

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    return 'do some magic!'


def server_server_id_user_user_id_kick_post(server_id, user_id,
                                            server_server_id_user_user_id_kick_post_request):  # noqa: E501
    """server_server_id_user_user_id_kick_post

    Kick a user # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str
    :param user_id: 
    :type user_id: int
    :param server_server_id_user_user_id_kick_post_request: 
    :type server_server_id_user_user_id_kick_post_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        server_server_id_user_user_id_kick_post_request = ServerServerIdUserUserIdKickPostRequest.from_dict(
            connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def server_server_id_user_user_id_move_post(server_id, user_id,
                                            server_server_id_user_user_id_move_post_request):  # noqa: E501
    """server_server_id_user_user_id_move_post

    Move a user to another channel # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str
    :param user_id: 
    :type user_id: int
    :param server_server_id_user_user_id_move_post_request: 
    :type server_server_id_user_user_id_move_post_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        server_server_id_user_user_id_move_post_request = ServerServerIdUserUserIdMovePostRequest.from_dict(
            connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def server_server_id_user_user_id_mute_post(server_id, user_id):  # noqa: E501
    """server_server_id_user_user_id_mute_post

    Mute a user # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str
    :param user_id: 
    :type user_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def server_server_id_user_user_id_unmute_post(server_id, user_id):  # noqa: E501
    """server_server_id_user_user_id_unmute_post

    Unmute a user # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str
    :param user_id: 
    :type user_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def server_server_id_users_get(server_id):  # noqa: E501
    """server_server_id_users_get

    Get list of connected users # noqa: E501

    :param server_id: 
    :type server_id: str
    :type server_id: str

    :rtype: Union[ServerServerIdUsersGet200Response, Tuple[ServerServerIdUsersGet200Response, int], Tuple[ServerServerIdUsersGet200Response, int, Dict[str, str]]
    """
    try:
        server_id = uuid.UUID(server_id)
        with current_app.app_context():
            murmur_connector: MurmurConnector = current_app.murmur_connector

            server = murmur_connector.get_server(server_id)
            if server is None:
                return flask.jsonify(Error("Server not found")), 404

            return flask.jsonify(ServerServerIdUsersGet200Response(server.get_users())), 200

    except (Ice.Exception, AttributeError) as e:
        log = logging.getLogger('murmur')
        log.error("Got an error in /servers")
        log.exception(e)
        return flask.jsonify(Error("Internal server error")), 500

    except ValueError:
        return flask.jsonify(Error("Badly formed server_id")), 400


def servers_get():  # noqa: E501
    """Get list of servers

     # noqa: E501


    :rtype: Union[ServersGet200Response, Tuple[ServersGet200Response, int], Tuple[ServersGet200Response, int, Dict[str, str]]
    """
    try:
        with current_app.app_context():
            murmur_connector: MurmurConnector = current_app.murmur_connector

            return flask.jsonify(ServersGet200Response([server.to_api_server() for (server_id, server) in murmur_connector.get_servers().items()])), 200

    except (Ice.Exception, AttributeError) as e:
        log = logging.getLogger('murmur')
        log.error("Got an error in /servers")
        log.exception(e)
        return flask.jsonify(Error("Internal server error")), 500
