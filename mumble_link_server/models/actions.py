# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mumble_link_server.models.base_model_ import Model
from mumble_link_server import util


class Actions(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    WRITE = "write"
    TRAVERSE = "traverse"
    ENTER = "enter"
    SPEAK = "speak"
    MUTE_DEAFEN = "mute_deafen"
    MOVE = "move"
    MAKE_CHANNEL = "make_channel"
    LINK_CHANNEL = "link_channel"
    WHISPER = "whisper"
    TEXT_MESSAGE = "text_message"
    MAKE_TEMP_CHANNEL = "make_temp_channel"
    KICK = "kick"
    BAN = "ban"
    REGISTER = "register"
    REGISTER_SELF = "register_self"
    def __init__(self):  # noqa: E501
        """Actions - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'Actions':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The actions of this Actions.  # noqa: E501
        :rtype: Actions
        """
        return util.deserialize_model(dikt, cls)