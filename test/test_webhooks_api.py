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
from swagger_client.api.webhooks_api import WebhooksApi  # noqa: E501
from swagger_client.rest import ApiException


class TestWebhooksApi(unittest.TestCase):
    """WebhooksApi unit test stubs"""

    def setUp(self):
        self.api = WebhooksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_webhook(self):
        """Test case for create_webhook

        Creates or updates an existing webhook subscription.  # noqa: E501
        """
        pass

    def test_delete_webhook(self):
        """Test case for delete_webhook

        Deletes a specific webhook subscription by id (Unsubscribe).  # noqa: E501
        """
        pass

    def test_get_webhook(self):
        """Test case for get_webhook

        Returns a specific webhook subscription by id.  # noqa: E501
        """
        pass

    def test_list_webhooks(self):
        """Test case for list_webhooks

        Returns the list of webhook subscriptions.  # noqa: E501
        """
        pass

    def test_subscribe_unsubscribe_web_sub(self):
        """Test case for subscribe_unsubscribe_web_sub

        A WebSub compliant endpoint which creates or updates an existing webhook subscription.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
