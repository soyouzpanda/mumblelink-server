# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mumble_link_server.models.base_model_ import Model
from mumble_link_server.models.server import Server
from mumble_link_server import util

from mumble_link_server.models.server import Server  # noqa: E501

class ServersGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, servers=None):  # noqa: E501
        """ServersGet200Response - a model defined in OpenAPI

        :param servers: The servers of this ServersGet200Response.  # noqa: E501
        :type servers: List[Server]
        """
        self.openapi_types = {
            'servers': List[Server]
        }

        self.attribute_map = {
            'servers': 'servers'
        }

        self._servers = servers

    @classmethod
    def from_dict(cls, dikt) -> 'ServersGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _servers_get_200_response of this ServersGet200Response.  # noqa: E501
        :rtype: ServersGet200Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def servers(self):
        """Gets the servers of this ServersGet200Response.


        :return: The servers of this ServersGet200Response.
        :rtype: List[Server]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this ServersGet200Response.


        :param servers: The servers of this ServersGet200Response.
        :type servers: List[Server]
        """
        if servers is None:
            raise ValueError("Invalid value for `servers`, must not be `None`")  # noqa: E501

        self._servers = servers
