# coding: utf-8

"""
    public-v2-prd-gb-01

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2016-08-19T00:00:00Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.tags_api import TagsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTagsApi(unittest.TestCase):
    """TagsApi unit test stubs"""

    def setUp(self):
        self.api = TagsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_client_tag(self):
        """Test case for add_client_tag

        Creates a new tag for a given client.  # noqa: E501
        """
        pass

    def test_add_lead_tag(self):
        """Test case for add_lead_tag

        Creates a new tag for a given lead.  # noqa: E501
        """
        pass

    def test_list_client_tags(self):
        """Test case for list_client_tags

        Returns a list of tags for a given client.  # noqa: E501
        """
        pass

    def test_list_lead_tags(self):
        """Test case for list_lead_tags

        Returns a list of tags for a given lead.  # noqa: E501
        """
        pass

    def test_list_tags(self):
        """Test case for list_tags

        Returns a list of tags for the client and lead resources.  # noqa: E501
        """
        pass

    def test_remove_client_tag(self):
        """Test case for remove_client_tag

        Deletes an existing tag for a given client.  # noqa: E501
        """
        pass

    def test_remove_lead_tag(self):
        """Test case for remove_lead_tag

        Deletes an existing tag for a given lead.  # noqa: E501
        """
        pass

    def test_update_client_tags(self):
        """Test case for update_client_tags

        Updates/Creates client's tags.  # noqa: E501
        """
        pass

    def test_update_lead_tags(self):
        """Test case for update_lead_tags

        Updates/Creates lead's tags.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
