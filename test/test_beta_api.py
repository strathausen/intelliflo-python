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
from swagger_client.api.beta_api import BetaApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBetaApi(unittest.TestCase):
    """BetaApi unit test stubs"""

    def setUp(self):
        self.api = BetaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_client_quote_applicant(self):
        """Test case for add_client_quote_applicant

        Adds a secondary client owner to a given quote.  # noqa: E501
        """
        pass

    def test_batch_create_client_transactions(self):
        """Test case for batch_create_client_transactions

        Creates a batch of transactions for different plans for a particular client.  # noqa: E501
        """
        pass

    def test_batch_create_transactions(self):
        """Test case for batch_create_transactions

        Creates a batch of transactions for different plans.  # noqa: E501
        """
        pass

    def test_client_plan_transaction_exists(self):
        """Test case for client_plan_transaction_exists

        Check to see if a transaction exists.  # noqa: E501
        """
        pass

    def test_client_quote_exists(self):
        """Test case for client_quote_exists

        Checks that a quote exists for a given client.  # noqa: E501
        """
        pass

    def test_client_quote_results_exists(self):
        """Test case for client_quote_results_exists

        Checks that a quote result exists for a client quote.  # noqa: E501
        """
        pass

    def test_create_client_dependant(self):
        """Test case for create_client_dependant

        Creates a dependant for a given client.  # noqa: E501
        """
        pass

    def test_create_client_dpa_policy_agreement(self):
        """Test case for create_client_dpa_policy_agreement

        Creates a new DPA policy agreement for a client.  # noqa: E501
        """
        pass

    def test_create_client_expenditure(self):
        """Test case for create_client_expenditure

        Creates an expenditure record for a client.  # noqa: E501
        """
        pass

    def test_create_client_fees(self):
        """Test case for create_client_fees

        Creates a fee for a given client.   # noqa: E501
        """
        pass

    def test_create_client_income(self):
        """Test case for create_client_income

        Creates an income record for a client.  # noqa: E501
        """
        pass

    def test_create_client_plan_fee(self):
        """Test case for create_client_plan_fee

        Creates an association on a fee with a client and plan.   # noqa: E501
        """
        pass

    def test_create_client_quote(self):
        """Test case for create_client_quote

        Creates a new client quote.  # noqa: E501
        """
        pass

    def test_create_client_quote_result(self):
        """Test case for create_client_quote_result

        Creates a new client quote result.  # noqa: E501
        """
        pass

    def test_create_dpa_policy(self):
        """Test case for create_dpa_policy

        Creates a new DPA policy which will become the current DPA policy when created (see notes on party type above).  # noqa: E501
        """
        pass

    def test_create_income_statement(self):
        """Test case for create_income_statement

        Creates a new income statement.  # noqa: E501
        """
        pass

    def test_create_income_statement_items(self):
        """Test case for create_income_statement_items

        Creates income statement items for an income statement.  # noqa: E501
        """
        pass

    def test_create_provider_model(self):
        """Test case for create_provider_model

        Creates a new provider model.  # noqa: E501
        """
        pass

    def test_delete_client_dependant(self):
        """Test case for delete_client_dependant

        Deletes a dependant for a given client.  # noqa: E501
        """
        pass

    def test_delete_client_expenditure(self):
        """Test case for delete_client_expenditure

        Deletes a client's expenditure record.  # noqa: E501
        """
        pass

    def test_delete_client_income(self):
        """Test case for delete_client_income

        Deletes a client's income record.  # noqa: E501
        """
        pass

    def test_delete_client_plan_fee(self):
        """Test case for delete_client_plan_fee

        Deletes the association on the fee with a client and plan.   # noqa: E501
        """
        pass

    def test_delete_dpa_policy(self):
        """Test case for delete_dpa_policy

        Deletes an existing DPA policy. Only policies that are not associated with client agreements can be deleted.  # noqa: E501
        """
        pass

    def test_delete_income_statement(self):
        """Test case for delete_income_statement

        Deletes an existing income statement.  # noqa: E501
        """
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

    def test_exist_installed_app(self):
        """Test case for exist_installed_app

        Checks if an installed app exists  # noqa: E501
        """
        pass

    def test_get_client_dependant(self):
        """Test case for get_client_dependant

        Returns a dependant for a given client and dependant.  # noqa: E501
        """
        pass

    def test_get_client_dpa_policy_agreement(self):
        """Test case for get_client_dpa_policy_agreement

        Returns a single DPA policy agreement for a client.  # noqa: E501
        """
        pass

    def test_get_client_expenditure(self):
        """Test case for get_client_expenditure

        Retrieves a client's expenditure record.  # noqa: E501
        """
        pass

    def test_get_client_fee(self):
        """Test case for get_client_fee

        Returns a fee for a given client and fee.   # noqa: E501
        """
        pass

    def test_get_client_income(self):
        """Test case for get_client_income

        Returns the income for a given client and income.   # noqa: E501
        """
        pass

    def test_get_client_marketing_preferences(self):
        """Test case for get_client_marketing_preferences

        Returns client's current marketing preferences.  # noqa: E501
        """
        pass

    def test_get_client_plan_fee(self):
        """Test case for get_client_plan_fee

        Returns a fee for a given plan.   # noqa: E501
        """
        pass

    def test_get_client_plan_transaction(self):
        """Test case for get_client_plan_transaction

        Gets a single transaction by id.  # noqa: E501
        """
        pass

    def test_get_client_quote(self):
        """Test case for get_client_quote

        Returns a client quote.  # noqa: E501
        """
        pass

    def test_get_client_quote_result(self):
        """Test case for get_client_quote_result

        Returns a client quote result.  # noqa: E501
        """
        pass

    def test_get_client_quote_result_product_benefits(self):
        """Test case for get_client_quote_result_product_benefits

        This endpoint allows an API user to retrieve product details of a specific quote result or illustration result for a client.  # noqa: E501
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

    def test_get_income_statement(self):
        """Test case for get_income_statement

        Returns an income statement.  # noqa: E501
        """
        pass

    def test_get_income_statement_item(self):
        """Test case for get_income_statement_item

        Returns a given item for a given income statement.  # noqa: E501
        """
        pass

    def test_get_installed_app(self):
        """Test case for get_installed_app

        Returns an installed app  # noqa: E501
        """
        pass

    def test_get_installed_app_group_settings(self):
        """Test case for get_installed_app_group_settings

        Returns group settings for a given installed app and group  # noqa: E501
        """
        pass

    def test_get_installed_app_user_settings(self):
        """Test case for get_installed_app_user_settings

        Returns user settings for a given installed app and user  # noqa: E501
        """
        pass

    def test_get_lead_marketing_preferences(self):
        """Test case for get_lead_marketing_preferences

        Returns lead's current marketing preferences.  # noqa: E501
        """
        pass

    def test_get_lifecycle(self):
        """Test case for get_lifecycle

        Returns a lifecycle.  # noqa: E501
        """
        pass

    def test_get_provider_model(self):
        """Test case for get_provider_model

        Returns a provider model.  # noqa: E501
        """
        pass

    def test_get_provider_models(self):
        """Test case for get_provider_models

        Returns a list of provider models.  # noqa: E501
        """
        pass

    def test_get_tenant(self):
        """Test case for get_tenant

        Retrieves the tenant resource specified   # noqa: E501
        """
        pass

    def test_get_valuation_batch(self):
        """Test case for get_valuation_batch

        Returns a single valuationbatch  # noqa: E501
        """
        pass

    def test_list_client_dependants(self):
        """Test case for list_client_dependants

        Returns a list of dependants for a given client.  # noqa: E501
        """
        pass

    def test_list_client_dpa_policy_agreements(self):
        """Test case for list_client_dpa_policy_agreements

        Returns a list of client's DPA policy agreements.  # noqa: E501
        """
        pass

    def test_list_client_expenditures(self):
        """Test case for list_client_expenditures

        Returns a list of expenditure records for a client. The returned list may be filtered.  # noqa: E501
        """
        pass

    def test_list_client_fees(self):
        """Test case for list_client_fees

        Returns a list of fees for a given client.   # noqa: E501
        """
        pass

    def test_list_client_incomes(self):
        """Test case for list_client_incomes

        Returns a list of incomes for a given client.   # noqa: E501
        """
        pass

    def test_list_client_plan_contributions(self):
        """Test case for list_client_plan_contributions

        Returns list of contributions for a given client and plan.   # noqa: E501
        """
        pass

    def test_list_client_plan_fees(self):
        """Test case for list_client_plan_fees

        Returns a list of fees for a given client and plan.   # noqa: E501
        """
        pass

    def test_list_client_plan_transactions(self):
        """Test case for list_client_plan_transactions

        Returns a list of transactions for a client plan.  # noqa: E501
        """
        pass

    def test_list_client_plan_withdrawals(self):
        """Test case for list_client_plan_withdrawals

        Returns a list of withdrawal for a given client and plan.   # noqa: E501
        """
        pass

    def test_list_client_quote_results(self):
        """Test case for list_client_quote_results

        Returns a list of client quote results.  # noqa: E501
        """
        pass

    def test_list_client_quotes(self):
        """Test case for list_client_quotes

        Returns a list of quotes.  # noqa: E501
        """
        pass

    def test_list_client_transactions(self):
        """Test case for list_client_transactions

        Returns a list of transactions for a client.  # noqa: E501
        """
        pass

    def test_list_dpa_policies(self):
        """Test case for list_dpa_policies

        Returns a list of DPA policies.  # noqa: E501
        """
        pass

    def test_list_income_statement_items(self):
        """Test case for list_income_statement_items

        Returns a list of items for a given income statement.  # noqa: E501
        """
        pass

    def test_list_income_statements(self):
        """Test case for list_income_statements

        Returns a list of income statements.  # noqa: E501
        """
        pass

    def test_list_installed_app_group_settings(self):
        """Test case for list_installed_app_group_settings

        Returns a list of group settings for a given installed app  # noqa: E501
        """
        pass

    def test_list_installed_app_user_settings(self):
        """Test case for list_installed_app_user_settings

        Returns a lists of user settings for a given installed app  # noqa: E501
        """
        pass

    def test_list_installed_apps(self):
        """Test case for list_installed_apps

        Returns a list of installed apps  # noqa: E501
        """
        pass

    def test_list_lifecycles(self):
        """Test case for list_lifecycles

        Returns a list of lifecycles.  # noqa: E501
        """
        pass

    def test_list_plantype_lifecycles(self):
        """Test case for list_plantype_lifecycles

        Retrieves a list of lifecycles associated with the specified planType  # noqa: E501
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

    def test_patch_dpa_policy(self):
        """Test case for patch_dpa_policy

        Updates an existing DPA policy.  # noqa: E501
        """
        pass

    def test_set_client_quote_status(self):
        """Test case for set_client_quote_status

        Sets a new status for the client quote.  # noqa: E501
        """
        pass

    def test_update_client_dependant(self):
        """Test case for update_client_dependant

        Updates a dependant for a given client.  # noqa: E501
        """
        pass

    def test_update_client_expenditure(self):
        """Test case for update_client_expenditure

        Updates a client's expenditure record.  # noqa: E501
        """
        pass

    def test_update_client_fee(self):
        """Test case for update_client_fee

        Updates a fee for a given client and fee.   # noqa: E501
        """
        pass

    def test_update_client_income(self):
        """Test case for update_client_income

        Updates a client's income record.  # noqa: E501
        """
        pass

    def test_update_client_marketing_preferences(self):
        """Test case for update_client_marketing_preferences

        Updates client's marketing preferences.  # noqa: E501
        """
        pass

    def test_update_client_plan(self):
        """Test case for update_client_plan

        Updates a plan for a given client.   # noqa: E501
        """
        pass

    def test_update_client_plan_transaction(self):
        """Test case for update_client_plan_transaction

        Updates a client plan transaction.  # noqa: E501
        """
        pass

    def test_update_client_quote_result_product_benefits(self):
        """Test case for update_client_quote_result_product_benefits

        This endpoint allows an API user to update product details of a specific quote result or illustration result for a client.  # noqa: E501
        """
        pass

    def test_update_dpa_policy(self):
        """Test case for update_dpa_policy

        Updates an existing DPA policy.  # noqa: E501
        """
        pass

    def test_update_income_statement(self):
        """Test case for update_income_statement

        Updates an income statement.  # noqa: E501
        """
        pass

    def test_update_income_statement_item(self):
        """Test case for update_income_statement_item

        Updates an income statement item for a given income statement.  # noqa: E501
        """
        pass

    def test_update_installed_app_group_settings(self):
        """Test case for update_installed_app_group_settings

        Updates group settings for a given installed app and group  # noqa: E501
        """
        pass

    def test_update_installed_app_user_settings(self):
        """Test case for update_installed_app_user_settings

        Updates user settings for a given installed app and user  # noqa: E501
        """
        pass

    def test_update_lead_marketing_preferences(self):
        """Test case for update_lead_marketing_preferences

        Updates lead's marketing preferences.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
