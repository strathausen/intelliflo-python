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
from swagger_client.api.dpa_api import DPAApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDPAApi(unittest.TestCase):
    """DPAApi unit test stubs"""

    def setUp(self):
        self.api = DPAApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_client_dpa_policy_agreement(self):
        """Test case for create_client_dpa_policy_agreement

        Creates a new DPA policy agreement for a client.  # noqa: E501
        """
        pass

    def test_create_dpa_policy(self):
        """Test case for create_dpa_policy

        Creates a new DPA policy which will become the current DPA policy when created (see notes on party type above).  # noqa: E501
        """
        pass

    def test_delete_dpa_policy(self):
        """Test case for delete_dpa_policy

        Deletes an existing DPA policy. Only policies that are not associated with client agreements can be deleted.  # noqa: E501
        """
        pass

    def test_get_client_dpa_policy_agreement(self):
        """Test case for get_client_dpa_policy_agreement

        Returns a single DPA policy agreement for a client.  # noqa: E501
        """
        pass

    def test_get_current_dpa_policy(self):
        """Test case for get_current_dpa_policy

        Returns the current default DPA policy (see notes on party type above).  # noqa: E501
        """
        pass

    def test_get_dpa_policy(self):
        """Test case for get_dpa_policy

        Returns a single DPA policy.  # noqa: E501
        """
        pass

    def test_list_client_dpa_policy_agreements(self):
        """Test case for list_client_dpa_policy_agreements

        Returns a list of client's DPA policy agreements.  # noqa: E501
        """
        pass

    def test_list_dpa_policies(self):
        """Test case for list_dpa_policies

        Returns a list of DPA policies.  # noqa: E501
        """
        pass

    def test_patch_dpa_policy(self):
        """Test case for patch_dpa_policy

        Updates an existing DPA policy.  # noqa: E501
        """
        pass

    def test_update_dpa_policy(self):
        """Test case for update_dpa_policy

        Updates an existing DPA policy.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
