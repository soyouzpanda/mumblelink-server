# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mumble_link_server.models.base_model_ import Model
from mumble_link_server.models.actions import Actions
from mumble_link_server import util

from mumble_link_server.models.actions import Actions  # noqa: E501

class Group(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, group_id=None, group_name=None, allowed_actions=None, denied_actions=None):  # noqa: E501
        """Group - a model defined in OpenAPI

        :param group_id: The group_id of this Group.  # noqa: E501
        :type group_id: str
        :param group_name: The group_name of this Group.  # noqa: E501
        :type group_name: str
        :param allowed_actions: The allowed_actions of this Group.  # noqa: E501
        :type allowed_actions: List[Actions]
        :param denied_actions: The denied_actions of this Group.  # noqa: E501
        :type denied_actions: List[Actions]
        """
        self.openapi_types = {
            'group_id': str,
            'group_name': str,
            'allowed_actions': List[Actions],
            'denied_actions': List[Actions]
        }

        self.attribute_map = {
            'group_id': 'group_id',
            'group_name': 'group_name',
            'allowed_actions': 'allowed_actions',
            'denied_actions': 'denied_actions'
        }

        self._group_id = group_id
        self._group_name = group_name
        self._allowed_actions = allowed_actions
        self._denied_actions = denied_actions

    @classmethod
    def from_dict(cls, dikt) -> 'Group':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Group of this Group.  # noqa: E501
        :rtype: Group
        """
        return util.deserialize_model(dikt, cls)

    @property
    def group_id(self):
        """Gets the group_id of this Group.


        :return: The group_id of this Group.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this Group.


        :param group_id: The group_id of this Group.
        :type group_id: str
        """
        if group_id is None:
            raise ValueError("Invalid value for `group_id`, must not be `None`")  # noqa: E501

        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this Group.


        :return: The group_name of this Group.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this Group.


        :param group_name: The group_name of this Group.
        :type group_name: str
        """
        if group_name is None:
            raise ValueError("Invalid value for `group_name`, must not be `None`")  # noqa: E501

        self._group_name = group_name

    @property
    def allowed_actions(self):
        """Gets the allowed_actions of this Group.


        :return: The allowed_actions of this Group.
        :rtype: List[Actions]
        """
        return self._allowed_actions

    @allowed_actions.setter
    def allowed_actions(self, allowed_actions):
        """Sets the allowed_actions of this Group.


        :param allowed_actions: The allowed_actions of this Group.
        :type allowed_actions: List[Actions]
        """
        if allowed_actions is None:
            raise ValueError("Invalid value for `allowed_actions`, must not be `None`")  # noqa: E501

        self._allowed_actions = allowed_actions

    @property
    def denied_actions(self):
        """Gets the denied_actions of this Group.


        :return: The denied_actions of this Group.
        :rtype: List[Actions]
        """
        return self._denied_actions

    @denied_actions.setter
    def denied_actions(self, denied_actions):
        """Sets the denied_actions of this Group.


        :param denied_actions: The denied_actions of this Group.
        :type denied_actions: List[Actions]
        """
        if denied_actions is None:
            raise ValueError("Invalid value for `denied_actions`, must not be `None`")  # noqa: E501

        self._denied_actions = denied_actions