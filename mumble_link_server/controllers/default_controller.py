import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from mumble_link_server.models.error import Error  # noqa: E501
from mumble_link_server.models.server_info import ServerInfo  # noqa: E501
from mumble_link_server.models.server_server_id_users_get200_response import ServerServerIdUsersGet200Response  # noqa: E501
from mumble_link_server.models.servers_create_post_request import ServersCreatePostRequest  # noqa: E501
from mumble_link_server.models.servers_get200_response import ServersGet200Response  # noqa: E501
from mumble_link_server.models.user_info import UserInfo  # noqa: E501
from mumble_link_server import util


def server_server_id_delete(server_id):  # noqa: E501
    """server_server_id_delete

     # noqa: E501

    :param server_id: 
    :type server_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def server_server_id_get(server_id):  # noqa: E501
    """server_server_id_get

     # noqa: E501

    :param server_id: 
    :type server_id: str

    :rtype: Union[ServerInfo, Tuple[ServerInfo, int], Tuple[ServerInfo, int, Dict[str, str]]
    """
    return 'do some magic!'


def server_server_id_user_user_id_get(server_id, user_id):  # noqa: E501
    """server_server_id_user_user_id_get

     # noqa: E501

    :param server_id: 
    :type server_id: str
    :param user_id: 
    :type user_id: int

    :rtype: Union[UserInfo, Tuple[UserInfo, int], Tuple[UserInfo, int, Dict[str, str]]
    """
    return 'do some magic!'


def server_server_id_user_user_id_mute_post(server_id, user_id):  # noqa: E501
    """server_server_id_user_user_id_mute_post

     # noqa: E501

    :param server_id: 
    :type server_id: str
    :param user_id: 
    :type user_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def server_server_id_user_user_id_unmute_post(server_id, user_id):  # noqa: E501
    """server_server_id_user_user_id_unmute_post

     # noqa: E501

    :param server_id: 
    :type server_id: str
    :param user_id: 
    :type user_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def server_server_id_users_get(server_id):  # noqa: E501
    """server_server_id_users_get

     # noqa: E501

    :param server_id: 
    :type server_id: str

    :rtype: Union[ServerServerIdUsersGet200Response, Tuple[ServerServerIdUsersGet200Response, int], Tuple[ServerServerIdUsersGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def servers_create_post(servers_create_post_request):  # noqa: E501
    """Create a new server

     # noqa: E501

    :param servers_create_post_request: 
    :type servers_create_post_request: dict | bytes

    :rtype: Union[ServerInfo, Tuple[ServerInfo, int], Tuple[ServerInfo, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        servers_create_post_request = ServersCreatePostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def servers_get():  # noqa: E501
    """Get list of servers

     # noqa: E501


    :rtype: Union[ServersGet200Response, Tuple[ServersGet200Response, int], Tuple[ServersGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'
