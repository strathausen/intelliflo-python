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
from swagger_client.api.livesassured_api import LivesassuredApi  # noqa: E501
from swagger_client.rest import ApiException


class TestLivesassuredApi(unittest.TestCase):
    """LivesassuredApi unit test stubs"""

    def setUp(self):
        self.api = LivesassuredApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_client_plans_lives_assured(self):
        """Test case for list_client_plans_lives_assured

        Returns a list of Lives Assured for the plan.  # noqa: E501
        """
        pass

    def test_update_client_plans_lives_assured(self):
        """Test case for update_client_plans_lives_assured

        Creates or updates the list of Lives Assured for the plan. A maximum of 6 lives assured can be added.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
