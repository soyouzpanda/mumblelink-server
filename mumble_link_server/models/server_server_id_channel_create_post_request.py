# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mumble_link_server.models.base_model_ import Model
from mumble_link_server import util


class ServerServerIdChannelCreatePostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, parent=None):  # noqa: E501
        """ServerServerIdChannelCreatePostRequest - a model defined in OpenAPI

        :param name: The name of this ServerServerIdChannelCreatePostRequest.  # noqa: E501
        :type name: str
        :param parent: The parent of this ServerServerIdChannelCreatePostRequest.  # noqa: E501
        :type parent: int
        """
        self.openapi_types = {
            'name': str,
            'parent': int
        }

        self.attribute_map = {
            'name': 'name',
            'parent': 'parent'
        }

        self._name = name
        self._parent = parent

    @classmethod
    def from_dict(cls, dikt) -> 'ServerServerIdChannelCreatePostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _server__server_id__channel_create_post_request of this ServerServerIdChannelCreatePostRequest.  # noqa: E501
        :rtype: ServerServerIdChannelCreatePostRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this ServerServerIdChannelCreatePostRequest.


        :return: The name of this ServerServerIdChannelCreatePostRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServerServerIdChannelCreatePostRequest.


        :param name: The name of this ServerServerIdChannelCreatePostRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def parent(self):
        """Gets the parent of this ServerServerIdChannelCreatePostRequest.


        :return: The parent of this ServerServerIdChannelCreatePostRequest.
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ServerServerIdChannelCreatePostRequest.


        :param parent: The parent of this ServerServerIdChannelCreatePostRequest.
        :type parent: int
        """

        self._parent = parent
