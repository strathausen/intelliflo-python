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
from swagger_client.api.withdrawals_api import WithdrawalsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestWithdrawalsApi(unittest.TestCase):
    """WithdrawalsApi unit test stubs"""

    def setUp(self):
        self.api = WithdrawalsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_plan_withdrawals(self):
        """Test case for create_plan_withdrawals

        Creates a withdrawal for a given client and plan.   # noqa: E501
        """
        pass

    def test_delete_client_plan_withdrawal(self):
        """Test case for delete_client_plan_withdrawal

        Deletes a withdrawal for a given client, plan and withdrawal.   # noqa: E501
        """
        pass

    def test_get_client_plan_withdrawal(self):
        """Test case for get_client_plan_withdrawal

        Returns a withdrawal for a given client, plan and withdrawal.   # noqa: E501
        """
        pass

    def test_list_client_plan_withdrawals(self):
        """Test case for list_client_plan_withdrawals

        Returns a list of withdrawal for a given client and plan.   # noqa: E501
        """
        pass

    def test_update_client_plan_withdrawal(self):
        """Test case for update_client_plan_withdrawal

        Updates a withdrawal for a given client, plan and withdrawal.   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
