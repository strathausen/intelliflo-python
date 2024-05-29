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
from swagger_client.api.fees_api import FeesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestFeesApi(unittest.TestCase):
    """FeesApi unit test stubs"""

    def setUp(self):
        self.api = FeesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_client_fees(self):
        """Test case for create_client_fees

        Creates a fee for a given client.   # noqa: E501
        """
        pass

    def test_create_client_plan_fee(self):
        """Test case for create_client_plan_fee

        Creates an association on a fee with a client and plan.   # noqa: E501
        """
        pass

    def test_delete_client_plan_fee(self):
        """Test case for delete_client_plan_fee

        Deletes the association on the fee with a client and plan.   # noqa: E501
        """
        pass

    def test_get_client_fee(self):
        """Test case for get_client_fee

        Returns a fee for a given client and fee.   # noqa: E501
        """
        pass

    def test_get_client_plan_fee(self):
        """Test case for get_client_plan_fee

        Returns a fee for a given plan.   # noqa: E501
        """
        pass

    def test_list_client_fees(self):
        """Test case for list_client_fees

        Returns a list of fees for a given client.   # noqa: E501
        """
        pass

    def test_list_client_plan_fees(self):
        """Test case for list_client_plan_fees

        Returns a list of fees for a given client and plan.   # noqa: E501
        """
        pass

    def test_update_client_fee(self):
        """Test case for update_client_fee

        Updates a fee for a given client and fee.   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
