# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from mumble_link_server.models.error import Error  # noqa: E501
from mumble_link_server.models.server_info import ServerInfo  # noqa: E501
from mumble_link_server.models.server_server_id_users_get200_response import ServerServerIdUsersGet200Response  # noqa: E501
from mumble_link_server.models.servers_create_post_request import ServersCreatePostRequest  # noqa: E501
from mumble_link_server.models.servers_get200_response import ServersGet200Response  # noqa: E501
from mumble_link_server.models.user_info import UserInfo  # noqa: E501
from mumble_link_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_server_server_id_delete(self):
        """Test case for server_server_id_delete

        
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/server/{server_id}'.format(server_id='server_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_server_server_id_get(self):
        """Test case for server_server_id_get

        
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/server/{server_id}'.format(server_id='server_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_server_server_id_user_user_id_get(self):
        """Test case for server_server_id_user_user_id_get

        
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/server/{server_id}/user/{user_id}'.format(server_id='server_id_example', user_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_server_server_id_user_user_id_mute_post(self):
        """Test case for server_server_id_user_user_id_mute_post

        
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/server/{server_id}/user/{user_id}/mute'.format(server_id='server_id_example', user_id=56),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_server_server_id_user_user_id_unmute_post(self):
        """Test case for server_server_id_user_user_id_unmute_post

        
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/server/{server_id}/user/{user_id}/unmute'.format(server_id='server_id_example', user_id=56),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_server_server_id_users_get(self):
        """Test case for server_server_id_users_get

        
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/server/{server_id}/users'.format(server_id='server_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_servers_create_post(self):
        """Test case for servers_create_post

        Create a new server
        """
        servers_create_post_request = mumble_link_server.ServersCreatePostRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/servers/create',
            method='POST',
            headers=headers,
            data=json.dumps(servers_create_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_servers_get(self):
        """Test case for servers_get

        Get list of servers
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/servers',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
