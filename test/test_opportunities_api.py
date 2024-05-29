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
from swagger_client.api.opportunities_api import OpportunitiesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestOpportunitiesApi(unittest.TestCase):
    """OpportunitiesApi unit test stubs"""

    def setUp(self):
        self.api = OpportunitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_campaign_channel(self):
        """Test case for create_campaign_channel

        Creates a new Campaign Channel.  # noqa: E501
        """
        pass

    def test_create_campaign_type(self):
        """Test case for create_campaign_type

        Creates a new Campaign Type.  # noqa: E501
        """
        pass

    def test_create_client_opportunity(self):
        """Test case for create_client_opportunity

        Creates a new Opportunity for the given client.  # noqa: E501
        """
        pass

    def test_create_lead_opportunity(self):
        """Test case for create_lead_opportunity

        Creates a new Opportunity for the given Lead.  # noqa: E501
        """
        pass

    def test_create_opportunity_campaign(self):
        """Test case for create_opportunity_campaign

        Creates a new Opportunity campaign for a tenant.  # noqa: E501
        """
        pass

    def test_create_opportunity_proposition(self):
        """Test case for create_opportunity_proposition

        Creates a new Opportunity proposition for a tenant.  # noqa: E501
        """
        pass

    def test_create_opportunity_status(self):
        """Test case for create_opportunity_status

        Creates a new Opportunity Status.  # noqa: E501
        """
        pass

    def test_create_opportunity_type(self):
        """Test case for create_opportunity_type

        Creates a new Opportunity Type for a tenant.  # noqa: E501
        """
        pass

    def test_delete_campaign_channel(self):
        """Test case for delete_campaign_channel

        Deletes Campaign Channel for a given tenant  # noqa: E501
        """
        pass

    def test_delete_campaign_type(self):
        """Test case for delete_campaign_type

        Deletes Campaign Type for a given tenant  # noqa: E501
        """
        pass

    def test_delete_opportunity_campaign(self):
        """Test case for delete_opportunity_campaign

        Deletes an Opportunity campaign. Only Opportunity campaigns that are not in use can be deleted.  # noqa: E501
        """
        pass

    def test_delete_opportunity_proposition(self):
        """Test case for delete_opportunity_proposition

        Deletes an existing Opportunity proposition for a tenant.  # noqa: E501
        """
        pass

    def test_delete_opportunity_status(self):
        """Test case for delete_opportunity_status

        Deletes an opportunity status for a given tenant  # noqa: E501
        """
        pass

    def test_delete_opportunity_type(self):
        """Test case for delete_opportunity_type

        Deletes an Opportunity type. Only opportunity types that are not in use can be deleted.  # noqa: E501
        """
        pass

    def test_get_client_opportunity(self):
        """Test case for get_client_opportunity

        Returns opportunity documents for a given client and document.   # noqa: E501
        """
        pass

    def test_get_lead_opportunity(self):
        """Test case for get_lead_opportunity

        Returns an opportunity document for a given lead.   # noqa: E501
        """
        pass

    def test_get_opportunity_type(self):
        """Test case for get_opportunity_type

        Returns the requested Opportunity type for a tenant.  # noqa: E501
        """
        pass

    def test_list_campaign_channels(self):
        """Test case for list_campaign_channels

        Returns a list of campaign channel for a given tenant.  # noqa: E501
        """
        pass

    def test_list_campaign_types(self):
        """Test case for list_campaign_types

        Returns a list of campaign types for a given tenant.  # noqa: E501
        """
        pass

    def test_list_client_opportunities(self):
        """Test case for list_client_opportunities

        Returns list of opportunities for a given client.   # noqa: E501
        """
        pass

    def test_list_lead_opportunities(self):
        """Test case for list_lead_opportunities

        Returns a list of opportunity documents for a given lead.   # noqa: E501
        """
        pass

    def test_list_opportunity_campaigns(self):
        """Test case for list_opportunity_campaigns

        Returns a list of the Opportunity campaigns for a tenant.  # noqa: E501
        """
        pass

    def test_list_opportunity_propositions(self):
        """Test case for list_opportunity_propositions

        Returns a list of the opportunity propositions for a tenant.  # noqa: E501
        """
        pass

    def test_list_opportunity_statuses(self):
        """Test case for list_opportunity_statuses

        Returns a list of opportunity statuses for a given tenant  # noqa: E501
        """
        pass

    def test_list_opportunity_types(self):
        """Test case for list_opportunity_types

        Returns a list of the opportunity types for a tenant.  # noqa: E501
        """
        pass

    def test_update_campaign_channel(self):
        """Test case for update_campaign_channel

        Updates an existing Campaign Channel.  # noqa: E501
        """
        pass

    def test_update_campaign_type(self):
        """Test case for update_campaign_type

        Updates an existing Campaign Type.  # noqa: E501
        """
        pass

    def test_update_client_opportunity(self):
        """Test case for update_client_opportunity

        Updates an existing Opportunity for the given client.  # noqa: E501
        """
        pass

    def test_update_lead_opporunity(self):
        """Test case for update_lead_opporunity

        Updates an existing Opportunity for the given Lead.  # noqa: E501
        """
        pass

    def test_update_opportunity_campaign(self):
        """Test case for update_opportunity_campaign

        Updates an Opportunity campaign for a tenant.  # noqa: E501
        """
        pass

    def test_update_opportunity_proposition(self):
        """Test case for update_opportunity_proposition

        Updates an existing Opportunity proposition for a tenant.  # noqa: E501
        """
        pass

    def test_update_opportunity_status(self):
        """Test case for update_opportunity_status

        Updates an existing Opportunity Status.  # noqa: E501
        """
        pass

    def test_update_opportunity_type(self):
        """Test case for update_opportunity_type

        Updates an Opportunity Type for a tenant.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
