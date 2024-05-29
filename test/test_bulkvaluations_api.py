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
from swagger_client.api.bulkvaluations_api import BulkvaluationsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBulkvaluationsApi(unittest.TestCase):
    """BulkvaluationsApi unit test stubs"""

    def setUp(self):
        self.api = BulkvaluationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_valuation_batch(self):
        """Test case for delete_valuation_batch

        Deletes an existing valuationbatch and undo any related valuations and transactions  # noqa: E501
        """
        pass

    def test_enqueue_valuation_batch(self):
        """Test case for enqueue_valuation_batch

        Creates a new valuationbatch and enqueues it for importing  # noqa: E501
        """
        pass

    def test_get_valuation_batch(self):
        """Test case for get_valuation_batch

        Returns a single valuationbatch  # noqa: E501
        """
        pass

    def test_list_valuation_batch_results(self):
        """Test case for list_valuation_batch_results

        Returns the results for a single valuationbatch.  # noqa: E501
        """
        pass

    def test_list_valuation_batches(self):
        """Test case for list_valuation_batches

        Returns a list of valuationbatch  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
