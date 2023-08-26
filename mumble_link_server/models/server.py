# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mumble_link_server.models.base_model_ import Model
from mumble_link_server import util


class Server(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, server_id=None, server_name=None, max_users=None, user_count=None, server_password=None, superuser_password=None):  # noqa: E501
        """Server - a model defined in OpenAPI

        :param server_id: The server_id of this Server.  # noqa: E501
        :type server_id: str
        :param server_name: The server_name of this Server.  # noqa: E501
        :type server_name: str
        :param max_users: The max_users of this Server.  # noqa: E501
        :type max_users: int
        :param user_count: The user_count of this Server.  # noqa: E501
        :type user_count: int
        :param server_password: The server_password of this Server.  # noqa: E501
        :type server_password: str
        :param superuser_password: The superuser_password of this Server.  # noqa: E501
        :type superuser_password: str
        """
        self.openapi_types = {
            'server_id': str,
            'server_name': str,
            'max_users': int,
            'user_count': int,
            'server_password': str,
            'superuser_password': str
        }

        self.attribute_map = {
            'server_id': 'server_id',
            'server_name': 'server_name',
            'max_users': 'max_users',
            'user_count': 'user_count',
            'server_password': 'server_password',
            'superuser_password': 'superuser_password'
        }

        self._server_id = server_id
        self._server_name = server_name
        self._max_users = max_users
        self._user_count = user_count
        self._server_password = server_password
        self._superuser_password = superuser_password

    @classmethod
    def from_dict(cls, dikt) -> 'Server':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Server of this Server.  # noqa: E501
        :rtype: Server
        """
        return util.deserialize_model(dikt, cls)

    @property
    def server_id(self):
        """Gets the server_id of this Server.


        :return: The server_id of this Server.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this Server.


        :param server_id: The server_id of this Server.
        :type server_id: str
        """
        if server_id is None:
            raise ValueError("Invalid value for `server_id`, must not be `None`")  # noqa: E501

        self._server_id = server_id

    @property
    def server_name(self):
        """Gets the server_name of this Server.


        :return: The server_name of this Server.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this Server.


        :param server_name: The server_name of this Server.
        :type server_name: str
        """
        if server_name is None:
            raise ValueError("Invalid value for `server_name`, must not be `None`")  # noqa: E501

        self._server_name = server_name

    @property
    def max_users(self):
        """Gets the max_users of this Server.


        :return: The max_users of this Server.
        :rtype: int
        """
        return self._max_users

    @max_users.setter
    def max_users(self, max_users):
        """Sets the max_users of this Server.


        :param max_users: The max_users of this Server.
        :type max_users: int
        """
        if max_users is None:
            raise ValueError("Invalid value for `max_users`, must not be `None`")  # noqa: E501

        self._max_users = max_users

    @property
    def user_count(self):
        """Gets the user_count of this Server.


        :return: The user_count of this Server.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this Server.


        :param user_count: The user_count of this Server.
        :type user_count: int
        """
        if user_count is None:
            raise ValueError("Invalid value for `user_count`, must not be `None`")  # noqa: E501

        self._user_count = user_count

    @property
    def server_password(self):
        """Gets the server_password of this Server.


        :return: The server_password of this Server.
        :rtype: str
        """
        return self._server_password

    @server_password.setter
    def server_password(self, server_password):
        """Sets the server_password of this Server.


        :param server_password: The server_password of this Server.
        :type server_password: str
        """

        self._server_password = server_password

    @property
    def superuser_password(self):
        """Gets the superuser_password of this Server.


        :return: The superuser_password of this Server.
        :rtype: str
        """
        return self._superuser_password

    @superuser_password.setter
    def superuser_password(self, superuser_password):
        """Sets the superuser_password of this Server.


        :param superuser_password: The superuser_password of this Server.
        :type superuser_password: str
        """

        self._superuser_password = superuser_password