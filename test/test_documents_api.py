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
from swagger_client.api.documents_api import DocumentsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDocumentsApi(unittest.TestCase):
    """DocumentsApi unit test stubs"""

    def setUp(self):
        self.api = DocumentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_client_document(self):
        """Test case for create_client_document

        Creates a document for a given client.   # noqa: E501
        """
        pass

    def test_get_client_document(self):
        """Test case for get_client_document

        Returns a document for a given client and document.   # noqa: E501
        """
        pass

    def test_list_client_documents(self):
        """Test case for list_client_documents

        Returns a list of documents for a given client.   # noqa: E501
        """
        pass

    def test_update_client_document(self):
        """Test case for update_client_document

        Updates a document for a given client and document.   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
