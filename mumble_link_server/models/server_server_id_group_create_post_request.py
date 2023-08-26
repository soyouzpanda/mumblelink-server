# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mumble_link_server.models.base_model_ import Model
from mumble_link_server.models.actions import Actions
from mumble_link_server import util

from mumble_link_server.models.actions import Actions  # noqa: E501

class ServerServerIdGroupCreatePostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, allowed_actions=None, denied_actions=None):  # noqa: E501
        """ServerServerIdGroupCreatePostRequest - a model defined in OpenAPI

        :param name: The name of this ServerServerIdGroupCreatePostRequest.  # noqa: E501
        :type name: str
        :param allowed_actions: The allowed_actions of this ServerServerIdGroupCreatePostRequest.  # noqa: E501
        :type allowed_actions: List[Actions]
        :param denied_actions: The denied_actions of this ServerServerIdGroupCreatePostRequest.  # noqa: E501
        :type denied_actions: List[Actions]
        """
        self.openapi_types = {
            'name': str,
            'allowed_actions': List[Actions],
            'denied_actions': List[Actions]
        }

        self.attribute_map = {
            'name': 'name',
            'allowed_actions': 'allowed_actions',
            'denied_actions': 'denied_actions'
        }

        self._name = name
        self._allowed_actions = allowed_actions
        self._denied_actions = denied_actions

    @classmethod
    def from_dict(cls, dikt) -> 'ServerServerIdGroupCreatePostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _server__server_id__group_create_post_request of this ServerServerIdGroupCreatePostRequest.  # noqa: E501
        :rtype: ServerServerIdGroupCreatePostRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this ServerServerIdGroupCreatePostRequest.


        :return: The name of this ServerServerIdGroupCreatePostRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServerServerIdGroupCreatePostRequest.


        :param name: The name of this ServerServerIdGroupCreatePostRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def allowed_actions(self):
        """Gets the allowed_actions of this ServerServerIdGroupCreatePostRequest.


        :return: The allowed_actions of this ServerServerIdGroupCreatePostRequest.
        :rtype: List[Actions]
        """
        return self._allowed_actions

    @allowed_actions.setter
    def allowed_actions(self, allowed_actions):
        """Sets the allowed_actions of this ServerServerIdGroupCreatePostRequest.


        :param allowed_actions: The allowed_actions of this ServerServerIdGroupCreatePostRequest.
        :type allowed_actions: List[Actions]
        """

        self._allowed_actions = allowed_actions

    @property
    def denied_actions(self):
        """Gets the denied_actions of this ServerServerIdGroupCreatePostRequest.


        :return: The denied_actions of this ServerServerIdGroupCreatePostRequest.
        :rtype: List[Actions]
        """
        return self._denied_actions

    @denied_actions.setter
    def denied_actions(self, denied_actions):
        """Sets the denied_actions of this ServerServerIdGroupCreatePostRequest.


        :param denied_actions: The denied_actions of this ServerServerIdGroupCreatePostRequest.
        :type denied_actions: List[Actions]
        """

        self._denied_actions = denied_actions
