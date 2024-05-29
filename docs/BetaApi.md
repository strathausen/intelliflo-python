# swagger_client.BetaApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_client_quote_applicant**](BetaApi.md#add_client_quote_applicant) | **POST** /clients/{clientId}/quotes/{quoteId} | Adds a secondary client owner to a given quote.
[**batch_create_client_transactions**](BetaApi.md#batch_create_client_transactions) | **POST** /clients/{clientId}/transactions | Creates a batch of transactions for different plans for a particular client.
[**batch_create_transactions**](BetaApi.md#batch_create_transactions) | **POST** /transactions | Creates a batch of transactions for different plans.
[**client_plan_transaction_exists**](BetaApi.md#client_plan_transaction_exists) | **HEAD** /clients/{clientId}/plans/{planId}/transactions/{transactionId} | Check to see if a transaction exists.
[**client_quote_exists**](BetaApi.md#client_quote_exists) | **HEAD** /clients/{clientId}/quotes/{quoteId} | Checks that a quote exists for a given client.
[**client_quote_results_exists**](BetaApi.md#client_quote_results_exists) | **HEAD** /clients/{clientId}/quotes/{quoteId}/results/{quoteResultId} | Checks that a quote result exists for a client quote.
[**create_client_dependant**](BetaApi.md#create_client_dependant) | **POST** /clients/{clientId}/dependants | Creates a dependant for a given client.
[**create_client_dpa_policy_agreement**](BetaApi.md#create_client_dpa_policy_agreement) | **POST** /clients/{clientId}/dpa_agreements | Creates a new DPA policy agreement for a client.
[**create_client_expenditure**](BetaApi.md#create_client_expenditure) | **POST** /clients/{clientId}/expenditures | Creates an expenditure record for a client.
[**create_client_fees**](BetaApi.md#create_client_fees) | **POST** /clients/{clientId}/fees | Creates a fee for a given client. 
[**create_client_income**](BetaApi.md#create_client_income) | **POST** /clients/{clientId}/incomes | Creates an income record for a client.
[**create_client_plan_fee**](BetaApi.md#create_client_plan_fee) | **POST** /clients/{clientId}/plans/{planId}/fees/{feeId} | Creates an association on a fee with a client and plan. 
[**create_client_quote**](BetaApi.md#create_client_quote) | **POST** /clients/{clientId}/quotes | Creates a new client quote.
[**create_client_quote_result**](BetaApi.md#create_client_quote_result) | **POST** /clients/{clientId}/quotes/{quoteId}/results | Creates a new client quote result.
[**create_dpa_policy**](BetaApi.md#create_dpa_policy) | **POST** /dpa_policies | Creates a new DPA policy which will become the current DPA policy when created (see notes on party type above).
[**create_income_statement**](BetaApi.md#create_income_statement) | **POST** /incomestatements | Creates a new income statement.
[**create_income_statement_items**](BetaApi.md#create_income_statement_items) | **POST** /incomestatements/{incomeStatementId}/items | Creates income statement items for an income statement.
[**create_provider_model**](BetaApi.md#create_provider_model) | **POST** /apps/{appId}/models | Creates a new provider model.
[**delete_client_dependant**](BetaApi.md#delete_client_dependant) | **DELETE** /clients/{clientId}/dependants/{dependantId} | Deletes a dependant for a given client.
[**delete_client_expenditure**](BetaApi.md#delete_client_expenditure) | **DELETE** /clients/{clientId}/expenditures/{expenditureId} | Deletes a client&#x27;s expenditure record.
[**delete_client_income**](BetaApi.md#delete_client_income) | **DELETE** /clients/{clientId}/incomes/{incomeId} | Deletes a client&#x27;s income record.
[**delete_client_plan_fee**](BetaApi.md#delete_client_plan_fee) | **DELETE** /clients/{clientId}/plans/{planId}/fees/{feeId} | Deletes the association on the fee with a client and plan. 
[**delete_dpa_policy**](BetaApi.md#delete_dpa_policy) | **DELETE** /dpa_policies/{policyId} | Deletes an existing DPA policy. Only policies that are not associated with client agreements can be deleted.
[**delete_income_statement**](BetaApi.md#delete_income_statement) | **DELETE** /incomestatements/{incomeStatementId} | Deletes an existing income statement.
[**delete_valuation_batch**](BetaApi.md#delete_valuation_batch) | **DELETE** /valuations/batches/{batchId} | Deletes an existing valuationbatch and undo any related valuations and transactions
[**enqueue_valuation_batch**](BetaApi.md#enqueue_valuation_batch) | **POST** /valuations/batches | Creates a new valuationbatch and enqueues it for importing
[**exist_installed_app**](BetaApi.md#exist_installed_app) | **HEAD** /installed_apps/{appId} | Checks if an installed app exists
[**get_client_dependant**](BetaApi.md#get_client_dependant) | **GET** /clients/{clientId}/dependants/{dependantId} | Returns a dependant for a given client and dependant.
[**get_client_dpa_policy_agreement**](BetaApi.md#get_client_dpa_policy_agreement) | **GET** /clients/{clientId}/dpa_agreements/{agreementId} | Returns a single DPA policy agreement for a client.
[**get_client_expenditure**](BetaApi.md#get_client_expenditure) | **GET** /clients/{clientId}/expenditures/{expenditureId} | Retrieves a client&#x27;s expenditure record.
[**get_client_fee**](BetaApi.md#get_client_fee) | **GET** /clients/{clientId}/fees/{feeId} | Returns a fee for a given client and fee. 
[**get_client_income**](BetaApi.md#get_client_income) | **GET** /clients/{clientId}/incomes/{incomeId} | Returns the income for a given client and income. 
[**get_client_marketing_preferences**](BetaApi.md#get_client_marketing_preferences) | **GET** /clients/{clientId}/marketing_preferences | Returns client&#x27;s current marketing preferences.
[**get_client_plan_fee**](BetaApi.md#get_client_plan_fee) | **GET** /clients/{clientId}/plans/{planId}/fees/{feeId} | Returns a fee for a given plan. 
[**get_client_plan_transaction**](BetaApi.md#get_client_plan_transaction) | **GET** /clients/{clientId}/plans/{planId}/transactions/{transactionId} | Gets a single transaction by id.
[**get_client_quote**](BetaApi.md#get_client_quote) | **GET** /clients/{clientId}/quotes/{quoteId} | Returns a client quote.
[**get_client_quote_result**](BetaApi.md#get_client_quote_result) | **GET** /clients/{clientId}/quotes/{quoteId}/results/{quoteResultId} | Returns a client quote result.
[**get_client_quote_result_product_benefits**](BetaApi.md#get_client_quote_result_product_benefits) | **GET** /clients/{clientId}/quotes/{quoteId}/results/{quoteResultId}/benefits | This endpoint allows an API user to retrieve product details of a specific quote result or illustration result for a client.
[**get_current_dpa_policy**](BetaApi.md#get_current_dpa_policy) | **GET** /dpa_policies/current | Returns the current default DPA policy (see notes on party type above).
[**get_dpa_policy**](BetaApi.md#get_dpa_policy) | **GET** /dpa_policies/{policyId} | Returns a single DPA policy.
[**get_income_statement**](BetaApi.md#get_income_statement) | **GET** /incomestatements/{incomeStatementId} | Returns an income statement.
[**get_income_statement_item**](BetaApi.md#get_income_statement_item) | **GET** /incomestatements/{incomeStatementId}/items/{incomeStatementItemId} | Returns a given item for a given income statement.
[**get_installed_app**](BetaApi.md#get_installed_app) | **GET** /installed_apps/{appId} | Returns an installed app
[**get_installed_app_group_settings**](BetaApi.md#get_installed_app_group_settings) | **GET** /installed_apps/{appId}/group_settings/{groupId} | Returns group settings for a given installed app and group
[**get_installed_app_user_settings**](BetaApi.md#get_installed_app_user_settings) | **GET** /installed_apps/{appId}/user_settings/{userId} | Returns user settings for a given installed app and user
[**get_lead_marketing_preferences**](BetaApi.md#get_lead_marketing_preferences) | **GET** /leads/{leadId}/marketing_preferences | Returns lead&#x27;s current marketing preferences.
[**get_lifecycle**](BetaApi.md#get_lifecycle) | **GET** /lifecycles/{lifecycleId} | Returns a lifecycle.
[**get_provider_model**](BetaApi.md#get_provider_model) | **GET** /apps/{appId}/models/{modelId} | Returns a provider model.
[**get_provider_models**](BetaApi.md#get_provider_models) | **GET** /apps/{appId}/models | Returns a list of provider models.
[**get_tenant**](BetaApi.md#get_tenant) | **GET** /tenants/{tenantId} | Retrieves the tenant resource specified 
[**get_valuation_batch**](BetaApi.md#get_valuation_batch) | **GET** /valuations/batches/{batchId} | Returns a single valuationbatch
[**list_client_dependants**](BetaApi.md#list_client_dependants) | **GET** /clients/{clientId}/dependants | Returns a list of dependants for a given client.
[**list_client_dpa_policy_agreements**](BetaApi.md#list_client_dpa_policy_agreements) | **GET** /clients/{clientId}/dpa_agreements | Returns a list of client&#x27;s DPA policy agreements.
[**list_client_expenditures**](BetaApi.md#list_client_expenditures) | **GET** /clients/{clientId}/expenditures | Returns a list of expenditure records for a client. The returned list may be filtered.
[**list_client_fees**](BetaApi.md#list_client_fees) | **GET** /clients/{clientId}/fees | Returns a list of fees for a given client. 
[**list_client_incomes**](BetaApi.md#list_client_incomes) | **GET** /clients/{clientId}/incomes | Returns a list of incomes for a given client. 
[**list_client_plan_contributions**](BetaApi.md#list_client_plan_contributions) | **GET** /clients/{clientId}/plans/{planId}/contributions | Returns list of contributions for a given client and plan. 
[**list_client_plan_fees**](BetaApi.md#list_client_plan_fees) | **GET** /clients/{clientId}/plans/{planId}/fees | Returns a list of fees for a given client and plan. 
[**list_client_plan_transactions**](BetaApi.md#list_client_plan_transactions) | **GET** /clients/{clientId}/plans/{planId}/transactions | Returns a list of transactions for a client plan.
[**list_client_plan_withdrawals**](BetaApi.md#list_client_plan_withdrawals) | **GET** /clients/{clientId}/plans/{planId}/withdrawals | Returns a list of withdrawal for a given client and plan. 
[**list_client_quote_results**](BetaApi.md#list_client_quote_results) | **GET** /clients/{clientId}/quotes/{quoteId}/results | Returns a list of client quote results.
[**list_client_quotes**](BetaApi.md#list_client_quotes) | **GET** /clients/{clientId}/quotes | Returns a list of quotes.
[**list_client_transactions**](BetaApi.md#list_client_transactions) | **GET** /clients/{clientId}/transactions | Returns a list of transactions for a client.
[**list_dpa_policies**](BetaApi.md#list_dpa_policies) | **GET** /dpa_policies | Returns a list of DPA policies.
[**list_income_statement_items**](BetaApi.md#list_income_statement_items) | **GET** /incomestatements/{incomeStatementId}/items | Returns a list of items for a given income statement.
[**list_income_statements**](BetaApi.md#list_income_statements) | **GET** /incomestatements | Returns a list of income statements.
[**list_installed_app_group_settings**](BetaApi.md#list_installed_app_group_settings) | **GET** /installed_apps/{appId}/group_settings | Returns a list of group settings for a given installed app
[**list_installed_app_user_settings**](BetaApi.md#list_installed_app_user_settings) | **GET** /installed_apps/{appId}/user_settings | Returns a lists of user settings for a given installed app
[**list_installed_apps**](BetaApi.md#list_installed_apps) | **GET** /installed_apps | Returns a list of installed apps
[**list_lifecycles**](BetaApi.md#list_lifecycles) | **GET** /lifecycles | Returns a list of lifecycles.
[**list_plantype_lifecycles**](BetaApi.md#list_plantype_lifecycles) | **GET** /plantypes/{name}/lifecycles | Retrieves a list of lifecycles associated with the specified planType
[**list_valuation_batch_results**](BetaApi.md#list_valuation_batch_results) | **GET** /valuations/batches/{batchId}/results | Returns the results for a single valuationbatch.
[**list_valuation_batches**](BetaApi.md#list_valuation_batches) | **GET** /valuations/batches | Returns a list of valuationbatch
[**patch_dpa_policy**](BetaApi.md#patch_dpa_policy) | **PATCH** /dpa_policies/{policyId} | Updates an existing DPA policy.
[**set_client_quote_status**](BetaApi.md#set_client_quote_status) | **POST** /clients/{clientId}/quotes/{quoteId}/status/{status} | Sets a new status for the client quote.
[**update_client_dependant**](BetaApi.md#update_client_dependant) | **PUT** /clients/{clientId}/dependants/{dependantId} | Updates a dependant for a given client.
[**update_client_expenditure**](BetaApi.md#update_client_expenditure) | **PUT** /clients/{clientId}/expenditures/{expenditureId} | Updates a client&#x27;s expenditure record.
[**update_client_fee**](BetaApi.md#update_client_fee) | **PUT** /clients/{clientId}/fees/{feeId} | Updates a fee for a given client and fee. 
[**update_client_income**](BetaApi.md#update_client_income) | **PUT** /clients/{clientId}/incomes/{incomeId} | Updates a client&#x27;s income record.
[**update_client_marketing_preferences**](BetaApi.md#update_client_marketing_preferences) | **PUT** /clients/{clientId}/marketing_preferences | Updates client&#x27;s marketing preferences.
[**update_client_plan**](BetaApi.md#update_client_plan) | **PUT** /clients/{clientId}/plans/{planId} | Updates a plan for a given client. 
[**update_client_plan_transaction**](BetaApi.md#update_client_plan_transaction) | **PATCH** /clients/{clientId}/plans/{planId}/transactions/{transactionId} | Updates a client plan transaction.
[**update_client_quote_result_product_benefits**](BetaApi.md#update_client_quote_result_product_benefits) | **PUT** /clients/{clientId}/quotes/{quoteId}/results/{quoteResultId}/benefits | This endpoint allows an API user to update product details of a specific quote result or illustration result for a client.
[**update_dpa_policy**](BetaApi.md#update_dpa_policy) | **PUT** /dpa_policies/{policyId} | Updates an existing DPA policy.
[**update_income_statement**](BetaApi.md#update_income_statement) | **PUT** /incomestatements/{incomeStatementId} | Updates an income statement.
[**update_income_statement_item**](BetaApi.md#update_income_statement_item) | **PUT** /incomestatements/{incomeStatementId}/items/{incomeStatementItemId} | Updates an income statement item for a given income statement.
[**update_installed_app_group_settings**](BetaApi.md#update_installed_app_group_settings) | **PUT** /installed_apps/{appId}/group_settings/{groupId} | Updates group settings for a given installed app and group
[**update_installed_app_user_settings**](BetaApi.md#update_installed_app_user_settings) | **PUT** /installed_apps/{appId}/user_settings/{userId} | Updates user settings for a given installed app and user
[**update_lead_marketing_preferences**](BetaApi.md#update_lead_marketing_preferences) | **PUT** /leads/{leadId}/marketing_preferences | Updates lead&#x27;s marketing preferences.

# **add_client_quote_applicant**
> Quote add_client_quote_applicant(authorization, client_id, quote_id, x_api_key, accept=accept)

Adds a secondary client owner to a given quote.

This endpoint allows an API user to add a secondary owner for the quote or illustration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Adds a secondary client owner to a given quote.
    api_response = api_instance.add_client_quote_applicant(authorization, client_id, quote_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->add_client_quote_applicant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Quote**](Quote.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_create_client_transactions**
> TransactionBatchResponse batch_create_client_transactions(body, authorization, x_api_key, client_id, accept=accept, x_iflo_batch_ignore_error=x_iflo_batch_ignore_error, tenant_id=tenant_id)

Creates a batch of transactions for different plans for a particular client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransactionBatch() # TransactionBatch | A collection of transactions.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client Id
accept = 'accept_example' # str |  (optional)
x_iflo_batch_ignore_error = false # bool | You can choose to set \"x-iflo-ignore-error=true\" when posting a batch of transactions.              This processes the entire batch and skip any row containing transaction we cannot match against the plan or underlying holding. (optional) (default to false)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Creates a batch of transactions for different plans for a particular client.
    api_response = api_instance.batch_create_client_transactions(body, authorization, x_api_key, client_id, accept=accept, x_iflo_batch_ignore_error=x_iflo_batch_ignore_error, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->batch_create_client_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionBatch**](TransactionBatch.md)| A collection of transactions. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client Id | 
 **accept** | **str**|  | [optional] 
 **x_iflo_batch_ignore_error** | **bool**| You can choose to set \&quot;x-iflo-ignore-error&#x3D;true\&quot; when posting a batch of transactions.              This processes the entire batch and skip any row containing transaction we cannot match against the plan or underlying holding. | [optional] [default to false]
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

[**TransactionBatchResponse**](TransactionBatchResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_create_transactions**
> TransactionBatchResponse batch_create_transactions(body, authorization, x_api_key, accept=accept, x_iflo_batch_ignore_error=x_iflo_batch_ignore_error, tenant_id=tenant_id)

Creates a batch of transactions for different plans.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransactionBatch() # TransactionBatch | A collection of transactions.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
x_iflo_batch_ignore_error = false # bool | You can choose to set \"x-iflo-ignore-error=true\" when posting a batch of transactions.              This processes the entire batch and skip any row containing transaction we cannot match against the plan or underlying holding. (optional) (default to false)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Creates a batch of transactions for different plans.
    api_response = api_instance.batch_create_transactions(body, authorization, x_api_key, accept=accept, x_iflo_batch_ignore_error=x_iflo_batch_ignore_error, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->batch_create_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionBatch**](TransactionBatch.md)| A collection of transactions. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **x_iflo_batch_ignore_error** | **bool**| You can choose to set \&quot;x-iflo-ignore-error&#x3D;true\&quot; when posting a batch of transactions.              This processes the entire batch and skip any row containing transaction we cannot match against the plan or underlying holding. | [optional] [default to false]
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

[**TransactionBatchResponse**](TransactionBatchResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_plan_transaction_exists**
> client_plan_transaction_exists(authorization, client_id, plan_id, transaction_id, x_api_key, accept=accept, tenant_id=tenant_id)

Check to see if a transaction exists.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id - the special value \\\"me\\\" can be used to indicate the authenticated user.
plan_id = 56 # int | Plan Id - the id of the plan.
transaction_id = 789 # int | Transaction Id - the id of the transaction.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Check to see if a transaction exists.
    api_instance.client_plan_transaction_exists(authorization, client_id, plan_id, transaction_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling BetaApi->client_plan_transaction_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id - the special value \\\&quot;me\\\&quot; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| Plan Id - the id of the plan. | 
 **transaction_id** | **int**| Transaction Id - the id of the transaction. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_quote_exists**
> client_quote_exists(authorization, client_id, quote_id, x_api_key, accept=accept)

Checks that a quote exists for a given client.

This endpoint allows an API user to check if a specific quote or illustration exists for a client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Checks that a quote exists for a given client.
    api_instance.client_quote_exists(authorization, client_id, quote_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling BetaApi->client_quote_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_quote_results_exists**
> client_quote_results_exists(authorization, client_id, quote_id, quote_result_id, x_api_key, accept=accept)

Checks that a quote result exists for a client quote.

This endpoint allows an API user to check if the results for a quote or illustration for a client exists.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
quote_result_id = 56 # int | Quote result identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Checks that a quote result exists for a client quote.
    api_instance.client_quote_results_exists(authorization, client_id, quote_id, quote_result_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling BetaApi->client_quote_results_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **quote_result_id** | **int**| Quote result identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_dependant**
> Dependant create_client_dependant(body, authorization, x_api_key, client_id, accept=accept)

Creates a dependant for a given client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.Dependant() # Dependant | Dependant document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier
accept = 'accept_example' # str |  (optional)

try:
    # Creates a dependant for a given client.
    api_response = api_instance.create_client_dependant(body, authorization, x_api_key, client_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->create_client_dependant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dependant**](Dependant.md)| Dependant document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **accept** | **str**|  | [optional] 

### Return type

[**Dependant**](Dependant.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_dpa_policy_agreement**
> DPAPolicyAgreement create_client_dpa_policy_agreement(body, authorization, x_api_key, client_id, accept=accept)

Creates a new DPA policy agreement for a client.

Creates a new DPA policy agreement for a client. A DPA policy agreement is a client's response to a firm's DPA policy.                **Notes:**  * The firm's existing DPA policy should be specified for an agreement to be created.  * In order to be valid, an agreement should contain 'Yes' answers to all policy statements and the agreement date populated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.DPAPolicyAgreement() # DPAPolicyAgreement | DPA policy Agreement document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | The client that agreed to the DPA policy. The special value 'me' can be used to indicate the authenticated user.
accept = 'accept_example' # str |  (optional)

try:
    # Creates a new DPA policy agreement for a client.
    api_response = api_instance.create_client_dpa_policy_agreement(body, authorization, x_api_key, client_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->create_client_dpa_policy_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DPAPolicyAgreement**](DPAPolicyAgreement.md)| DPA policy Agreement document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| The client that agreed to the DPA policy. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **accept** | **str**|  | [optional] 

### Return type

[**DPAPolicyAgreement**](DPAPolicyAgreement.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_expenditure**
> Expenditure create_client_expenditure(body, authorization, x_api_key, client_id, accept=accept, prefer=prefer)

Creates an expenditure record for a client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.Expenditure() # Expenditure | Details of the expenditure to be created.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | The client identifier. The special value \"me\" can be used to indicate the authenticated user.
accept = 'accept_example' # str |  (optional)
prefer = 'prefer_example' # str | Used to indicate which format the expenditure categories are returned in. Valid options are: 'x-iflo-apiversion=1' or 'x-iflo-apiversion=2'. If not specified the default is 'x-iflo-apiversion=1' (optional)

try:
    # Creates an expenditure record for a client.
    api_response = api_instance.create_client_expenditure(body, authorization, x_api_key, client_id, accept=accept, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->create_client_expenditure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Expenditure**](Expenditure.md)| Details of the expenditure to be created. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| The client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **accept** | **str**|  | [optional] 
 **prefer** | **str**| Used to indicate which format the expenditure categories are returned in. Valid options are: &#x27;x-iflo-apiversion&#x3D;1&#x27; or &#x27;x-iflo-apiversion&#x3D;2&#x27;. If not specified the default is &#x27;x-iflo-apiversion&#x3D;1&#x27; | [optional] 

### Return type

[**Expenditure**](Expenditure.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_fees**
> FeeDocument create_client_fees(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)

Creates a fee for a given client. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.FeeDocument() # FeeDocument | Fee
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier.
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier. (optional)

try:
    # Creates a fee for a given client. 
    api_response = api_instance.create_client_fees(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->create_client_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeeDocument**](FeeDocument.md)| Fee | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier. | [optional] 

### Return type

[**FeeDocument**](FeeDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_income**
> Income create_client_income(body, authorization, x_api_key, client_id, accept=accept, prefer=prefer)

Creates an income record for a client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateIncome() # CreateIncome | The created income record.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | The client identifier. The special value \"me\" can be used to indicate the authenticated user.
accept = 'accept_example' # str |  (optional)
prefer = 'prefer_example' # str | Used to indicate which format the income categories are returned in. Valid options are: 'x-iflo-apiversion=1' or 'x-iflo-apiversion=2'. If not specified the default is 'x-iflo-apiversion=1' (optional)

try:
    # Creates an income record for a client.
    api_response = api_instance.create_client_income(body, authorization, x_api_key, client_id, accept=accept, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->create_client_income: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateIncome**](CreateIncome.md)| The created income record. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| The client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **accept** | **str**|  | [optional] 
 **prefer** | **str**| Used to indicate which format the income categories are returned in. Valid options are: &#x27;x-iflo-apiversion&#x3D;1&#x27; or &#x27;x-iflo-apiversion&#x3D;2&#x27;. If not specified the default is &#x27;x-iflo-apiversion&#x3D;1&#x27; | [optional] 

### Return type

[**Income**](Income.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_plan_fee**
> FeeDocument create_client_plan_fee(authorization, client_id, fee_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)

Creates an association on a fee with a client and plan. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
fee_id = 56 # int | Fee identifier.
plan_id = 56 # int | Plan identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier. (optional)

try:
    # Creates an association on a fee with a client and plan. 
    api_response = api_instance.create_client_plan_fee(authorization, client_id, fee_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->create_client_plan_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **fee_id** | **int**| Fee identifier. | 
 **plan_id** | **int**| Plan identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier. | [optional] 

### Return type

[**FeeDocument**](FeeDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_quote**
> Quote create_client_quote(body, authorization, x_api_key, client_id, accept=accept)

Creates a new client quote.

This endpoint allows an API user to create a quote or illustration for a client using the document in the body of this request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.Quote() # Quote | Request document with quote details.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
accept = 'accept_example' # str |  (optional)

try:
    # Creates a new client quote.
    api_response = api_instance.create_client_quote(body, authorization, x_api_key, client_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->create_client_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Quote**](Quote.md)| Request document with quote details. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **accept** | **str**|  | [optional] 

### Return type

[**Quote**](Quote.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_quote_result**
> QuoteResult create_client_quote_result(body, authorization, x_api_key, client_id, quote_id, accept=accept)

Creates a new client quote result.

This endpoint allows an API user to create the results for a quote or illustration using the document supplied in the body of the request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuoteResult() # QuoteResult | Request document with quote result details.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
accept = 'accept_example' # str |  (optional)

try:
    # Creates a new client quote result.
    api_response = api_instance.create_client_quote_result(body, authorization, x_api_key, client_id, quote_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->create_client_quote_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuoteResult**](QuoteResult.md)| Request document with quote result details. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **accept** | **str**|  | [optional] 

### Return type

[**QuoteResult**](QuoteResult.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dpa_policy**
> DPAPolicy create_dpa_policy(body, authorization, x_api_key, accept=accept)

Creates a new DPA policy which will become the current DPA policy when created (see notes on party type above).

If a party type is specified the DPA policy will be related to that party type. If no party type is specified it becomes the default DPA policy for the tenant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.DPAPolicy() # DPAPolicy | A DPA policy document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Creates a new DPA policy which will become the current DPA policy when created (see notes on party type above).
    api_response = api_instance.create_dpa_policy(body, authorization, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->create_dpa_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DPAPolicy**](DPAPolicy.md)| A DPA policy document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**DPAPolicy**](DPAPolicy.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_income_statement**
> IncomeStatement create_income_statement(body, authorization, x_api_key, accept=accept)

Creates a new income statement.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.IncomeStatement() # IncomeStatement | Income statement document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Creates a new income statement.
    api_response = api_instance.create_income_statement(body, authorization, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->create_income_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IncomeStatement**](IncomeStatement.md)| Income statement document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**IncomeStatement**](IncomeStatement.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_income_statement_items**
> create_income_statement_items(body, authorization, x_api_key, income_statement_id, accept=accept)

Creates income statement items for an income statement.

Add income statement items to an existing income statement.  There is a limit of 10000 items per post, however you can make multiple posts.  You cannot post if the statement is matched or any of the items are analysed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.IncomeStatementItemBatch() # IncomeStatementItemBatch | A batch of income statement items
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
income_statement_id = 56 # int | Income statement identifier
accept = 'accept_example' # str |  (optional)

try:
    # Creates income statement items for an income statement.
    api_instance.create_income_statement_items(body, authorization, x_api_key, income_statement_id, accept=accept)
except ApiException as e:
    print("Exception when calling BetaApi->create_income_statement_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IncomeStatementItemBatch**](IncomeStatementItemBatch.md)| A batch of income statement items | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **income_statement_id** | **int**| Income statement identifier | 
 **accept** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_provider_model**
> ProviderModel create_provider_model(body, authorization, x_api_key, app_id, accept=accept)

Creates a new provider model.

Create a new provider model or a new version of an existing model.  To create a new version of an existing model make sure that the model.code is the same.  This will then archive the previous version and the firm can then approve the new version.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProviderModel() # ProviderModel | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
app_id = 'app_id_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Creates a new provider model.
    api_response = api_instance.create_provider_model(body, authorization, x_api_key, app_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->create_provider_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProviderModel**](ProviderModel.md)|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **app_id** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**ProviderModel**](ProviderModel.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_dependant**
> delete_client_dependant(authorization, client_id, dependant_id, x_api_key, accept=accept)

Deletes a dependant for a given client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
dependant_id = 56 # int | Dependant identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes a dependant for a given client.
    api_instance.delete_client_dependant(authorization, client_id, dependant_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling BetaApi->delete_client_dependant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **dependant_id** | **int**| Dependant identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_expenditure**
> delete_client_expenditure(authorization, client_id, expenditure_id, x_api_key, accept=accept)

Deletes a client's expenditure record.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client identifier. The special value \"me\" can be used to indicate the authenticated user.
expenditure_id = 56 # int | The identifier of the expenditure record.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes a client's expenditure record.
    api_instance.delete_client_expenditure(authorization, client_id, expenditure_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling BetaApi->delete_client_expenditure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| The client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **expenditure_id** | **int**| The identifier of the expenditure record. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_income**
> delete_client_income(authorization, client_id, income_id, x_api_key, accept=accept)

Deletes a client's income record.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client identifier. The special value \"me\" can be used to indicate the authenticated user.
income_id = 56 # int | The identifier for the income record.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes a client's income record.
    api_instance.delete_client_income(authorization, client_id, income_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling BetaApi->delete_client_income: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| The client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **income_id** | **int**| The identifier for the income record. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_plan_fee**
> delete_client_plan_fee(authorization, client_id, fee_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)

Deletes the association on the fee with a client and plan. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
fee_id = 56 # int | Fee identifier.
plan_id = 56 # int | Plan identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier. (optional)

try:
    # Deletes the association on the fee with a client and plan. 
    api_instance.delete_client_plan_fee(authorization, client_id, fee_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling BetaApi->delete_client_plan_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **fee_id** | **int**| Fee identifier. | 
 **plan_id** | **int**| Plan identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dpa_policy**
> delete_dpa_policy(authorization, policy_id, x_api_key, accept=accept)

Deletes an existing DPA policy. Only policies that are not associated with client agreements can be deleted.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
policy_id = 56 # int | DPA policy Identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes an existing DPA policy. Only policies that are not associated with client agreements can be deleted.
    api_instance.delete_dpa_policy(authorization, policy_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling BetaApi->delete_dpa_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **policy_id** | **int**| DPA policy Identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_income_statement**
> delete_income_statement(authorization, income_statement_id, x_api_key, accept=accept)

Deletes an existing income statement.

You can only delete an income statement if it is not matched and none of the items are analysed.  This will delete the income statement and the associated items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
income_statement_id = 56 # int | Income statement identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes an existing income statement.
    api_instance.delete_income_statement(authorization, income_statement_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling BetaApi->delete_income_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **income_statement_id** | **int**| Income statement identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_valuation_batch**
> delete_valuation_batch(authorization, batch_id, x_api_key, accept=accept)

Deletes an existing valuationbatch and undo any related valuations and transactions

Use this endpoint to undo any valuations and transactions.                * Only valuationbatches in `completed` state can be undone.  * This is **NOT** meant as a regular use case, instead should only be used when incorrect data was sent in a previous batch.  * Any such incorrect data must be undone within 3 months of creating the valuationbatch or it will be `expired` and then it can no longer be undone.  * If you need to undo the batch, make sure you have spoken to the tenant first so they can take appropriate actions if they have already used the incorrect data when advising a client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
batch_id = 56 # int | Batch Id
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes an existing valuationbatch and undo any related valuations and transactions
    api_instance.delete_valuation_batch(authorization, batch_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling BetaApi->delete_valuation_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **batch_id** | **int**| Batch Id | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enqueue_valuation_batch**
> ValuationBatch enqueue_valuation_batch(body, authorization, x_api_key, x_iflo_product_provider_id, tenant_id, accept=accept, x_iflo_planmatch_includeportalreference=x_iflo_planmatch_includeportalreference, x_iflo_planmatch_normalised=x_iflo_planmatch_normalised)

Creates a new valuationbatch and enqueues it for importing

Use this endpoint to upload large batches of valuation data.    ### Request Headers  In addition to standard headers like `Authorization` and `x-api-key` there are some additional `headers` required for bulk valuation.  Please see **Request Headers** section below for details.    ### Request Body  * Header must be provided in the first line separated with `single tab` and must be as below.  `PolicyNumber    PortalReference CodeType    Code    Name    Units   UnitsDate   UnitPrice   CurrencyCode`  * Data must be of the product provider  and/or of any its linked product providers.  * Maximum size supported per batch is 10 MB.  * Data can be split in multiple batches, but ensure single policy's holdings are NOT split between batches.  * Any duplicate holdings for a single policy must be merged.  * Unit price can be omitted if the fund can be matched to a feed fund or equity or an existing manual fund.    #### Details of schema    | Field Name     | Type  |Description |  |:-----------------|:-------------------|:---------|  | PolicyNumber    | string(255) | **Required**.  Unique number to identify the plan |  | PortalReference | string(255) | **Optional**.  Any additional provider reference|  | CodeType        | string(15) | **Required**.  Allowed values are ` 'ISIN','SEDOL','CITI','MEX','EPIC','ProviderCode','APIR','TICKER' depending on region.`|  | Code | string(50) | **Required**.|  | Name | string(255) | **Required**.|  | Units | decimal(18,4) | **Required**.|  | UnitsDate | string(10) | **Required**.  Must be in ISO 8601 Date format (` 'YYYY-MM-DD' `) |  | UnitPrice | decimal(18,4) | **Optional**.|  | CurrencyCode | string(3) | **Required**. Must be the three letter ISO 4217 alphabetic code, We also support `GBX` |  ### Example   Note: A full list of regional URL's are available [here](docs/URLs).  ```curl  $YOUR_API_KEY='your Intelliflo API access key'  $YOUR_AUTHENTICATION_TOKEN='your JSON Web Token'  $PRODUCT_PROVIDER_ID='correct product provider id - double check if you are not sure'  curl -X POST \\    https://api.intelliflo.com/v2/valuations/batches \\    -H 'Authorization: $YOUR_AUTHENTICATION_TOKEN' \\    -H 'x-api-key: $YOUR_API_KEY' \\    -H 'Content-Type: text/tab-separated-values' \\    -H 'x-iflo-productProviderId: $PRODUCT_PROVIDER_ID' \\    -d '  PolicyNumber PortalReference CodeType Code Name Units UnitsDate UnitPrice CurrencyCode  isa01  isin IE00BGJWXV08 Metzler Cap 100 2019-02-28 85 GBP  isa01  Epic 0JGD ISHARES GLOBAL 50 2019-02-26 77.00 EUR  isa01  ProviderCode Cash Cash 75 2019-02-26 1 GBX  '  ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppId() # AppId | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
x_iflo_product_provider_id = 56 # int | Id of the Product Provider  You can list the available product providers using the [ProductProviders API](/apis?tags=productproviders#ListProductproviders)
tenant_id = 56 # int | 
accept = 'accept_example' # str |  (optional)
x_iflo_planmatch_includeportalreference = true # bool | Determines whether to include the portal reference in matching algorithm.  Default is `false` and plans will be matched only on `PolicyNumber`.  By providing `true` in here plans will be matched on `PolicyNumber`  and `PortalReference`.  You may want to consider this when `PolicyNumber` is not unique to the product provider. (optional)
x_iflo_planmatch_normalised = true # bool | Determines whether to sanitize the field values in the matching algorithm.  Default is `false` and will be an exact (but not case sensitive) match on the matching fields.  By providing `true` in here we will remove any spaces and any leading zeroes in IO before matching.  In such case ensure the batch has them already removed in the matching fields. (optional)

try:
    # Creates a new valuationbatch and enqueues it for importing
    api_response = api_instance.enqueue_valuation_batch(body, authorization, x_api_key, x_iflo_product_provider_id, tenant_id, accept=accept, x_iflo_planmatch_includeportalreference=x_iflo_planmatch_includeportalreference, x_iflo_planmatch_normalised=x_iflo_planmatch_normalised)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->enqueue_valuation_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppId**](AppId.md)|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_iflo_product_provider_id** | **int**| Id of the Product Provider  You can list the available product providers using the [ProductProviders API](/apis?tags&#x3D;productproviders#ListProductproviders) | 
 **tenant_id** | **int**|  | 
 **accept** | **str**|  | [optional] 
 **x_iflo_planmatch_includeportalreference** | **bool**| Determines whether to include the portal reference in matching algorithm.  Default is &#x60;false&#x60; and plans will be matched only on &#x60;PolicyNumber&#x60;.  By providing &#x60;true&#x60; in here plans will be matched on &#x60;PolicyNumber&#x60;  and &#x60;PortalReference&#x60;.  You may want to consider this when &#x60;PolicyNumber&#x60; is not unique to the product provider. | [optional] 
 **x_iflo_planmatch_normalised** | **bool**| Determines whether to sanitize the field values in the matching algorithm.  Default is &#x60;false&#x60; and will be an exact (but not case sensitive) match on the matching fields.  By providing &#x60;true&#x60; in here we will remove any spaces and any leading zeroes in IO before matching.  In such case ensure the batch has them already removed in the matching fields. | [optional] 

### Return type

[**ValuationBatch**](ValuationBatch.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: text/tab-separated-values, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exist_installed_app**
> exist_installed_app(app_id, authorization, x_api_key, accept=accept)

Checks if an installed app exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Checks if an installed app exists
    api_instance.exist_installed_app(app_id, authorization, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling BetaApi->exist_installed_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_dependant**
> Dependant get_client_dependant(authorization, client_id, dependant_id, x_api_key, accept=accept)

Returns a dependant for a given client and dependant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
dependant_id = 56 # int | Dependant identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a dependant for a given client and dependant.
    api_response = api_instance.get_client_dependant(authorization, client_id, dependant_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_client_dependant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **dependant_id** | **int**| Dependant identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Dependant**](Dependant.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_dpa_policy_agreement**
> DPAPolicyAgreement get_client_dpa_policy_agreement(agreement_id, authorization, client_id, x_api_key, accept=accept)

Returns a single DPA policy agreement for a client.

Returns a single DPA policy agreement for a client. A DPA policy agreement is a client's response to a firm's DPA policy.                **Notes:**  * DPA policy agreement has a maximum of 5 statements with Yes/No responses and an agreement date.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
agreement_id = 56 # int | DPA Policy Agreement identifier. The special value 'current' can be used to indicate the latest agreement.
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client that agreed to the DPA policy. The special value 'me' can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a single DPA policy agreement for a client.
    api_response = api_instance.get_client_dpa_policy_agreement(agreement_id, authorization, client_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_client_dpa_policy_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agreement_id** | **int**| DPA Policy Agreement identifier. The special value &#x27;current&#x27; can be used to indicate the latest agreement. | 
 **authorization** | **str**|  | 
 **client_id** | **int**| The client that agreed to the DPA policy. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**DPAPolicyAgreement**](DPAPolicyAgreement.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_expenditure**
> Expenditure get_client_expenditure(authorization, client_id, expenditure_id, x_api_key, accept=accept, prefer=prefer)

Retrieves a client's expenditure record.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client identifier. The special value \"me\" can be used to indicate the authenticated user.
expenditure_id = 56 # int | The id of the expenditure record.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
prefer = 'prefer_example' # str | Used to indicate which format the expenditure categories are returned in. Valid options are: 'x-iflo-apiversion=1' or 'x-iflo-apiversion=2'. If not specified the default is 'x-iflo-apiversion=1' (optional)

try:
    # Retrieves a client's expenditure record.
    api_response = api_instance.get_client_expenditure(authorization, client_id, expenditure_id, x_api_key, accept=accept, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_client_expenditure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| The client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **expenditure_id** | **int**| The id of the expenditure record. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **prefer** | **str**| Used to indicate which format the expenditure categories are returned in. Valid options are: &#x27;x-iflo-apiversion&#x3D;1&#x27; or &#x27;x-iflo-apiversion&#x3D;2&#x27;. If not specified the default is &#x27;x-iflo-apiversion&#x3D;1&#x27; | [optional] 

### Return type

[**Expenditure**](Expenditure.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_fee**
> FeeDocument get_client_fee(authorization, client_id, fee_id, x_api_key, accept=accept, tenant_id=tenant_id)

Returns a fee for a given client and fee. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
fee_id = 56 # int | Fee identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier. (optional)

try:
    # Returns a fee for a given client and fee. 
    api_response = api_instance.get_client_fee(authorization, client_id, fee_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_client_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **fee_id** | **int**| Fee identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier. | [optional] 

### Return type

[**FeeDocument**](FeeDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_income**
> Income get_client_income(authorization, client_id, income_id, x_api_key, accept=accept, prefer=prefer)

Returns the income for a given client and income. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client identifier. The special value \"me\" can be used to indicate the authenticated user.
income_id = 56 # int | The identifier for the income record.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
prefer = 'prefer_example' # str | Used to indicate which format the income categories are returned in. Valid options are: 'x-iflo-apiversion=1' or 'x-iflo-apiversion=2'. If not specified the default is 'x-iflo-apiversion=1' (optional)

try:
    # Returns the income for a given client and income. 
    api_response = api_instance.get_client_income(authorization, client_id, income_id, x_api_key, accept=accept, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_client_income: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| The client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **income_id** | **int**| The identifier for the income record. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **prefer** | **str**| Used to indicate which format the income categories are returned in. Valid options are: &#x27;x-iflo-apiversion&#x3D;1&#x27; or &#x27;x-iflo-apiversion&#x3D;2&#x27;. If not specified the default is &#x27;x-iflo-apiversion&#x3D;1&#x27; | [optional] 

### Return type

[**Income**](Income.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_marketing_preferences**
> ClientMarketingPreferences get_client_marketing_preferences(authorization, client_id, x_api_key, accept=accept)

Returns client's current marketing preferences.

Use this endpoint to return  a client's marketing preferences broken down by medium where appropriate.  A successful response (200) will return client's  marketing preferences document.  If a client has not yet provided their preferences and/or consent, the returned preferences will be defaulted to a suitable privacy configuration.  The returned configuration should be adhered to regardless of whether consent has been given yet or not.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier. The special value 'me' can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns client's current marketing preferences.
    api_response = api_instance.get_client_marketing_preferences(authorization, client_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_client_marketing_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**ClientMarketingPreferences**](ClientMarketingPreferences.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_plan_fee**
> FeeDocument get_client_plan_fee(authorization, client_id, fee_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)

Returns a fee for a given plan. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
fee_id = 56 # int | Fee identifier.
plan_id = 56 # int | Plan identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier. (optional)

try:
    # Returns a fee for a given plan. 
    api_response = api_instance.get_client_plan_fee(authorization, client_id, fee_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_client_plan_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **fee_id** | **int**| Fee identifier. | 
 **plan_id** | **int**| Plan identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier. | [optional] 

### Return type

[**FeeDocument**](FeeDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_plan_transaction**
> Transaction get_client_plan_transaction(authorization, client_id, plan_id, transaction_id, x_api_key, accept=accept, tenant_id=tenant_id)

Gets a single transaction by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id - the special value \\\"me\\\" can be used to indicate the authenticated user.
plan_id = 56 # int | Plan Id - the id of the plan.
transaction_id = 789 # int | Transaction Id - the id of the transaction.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Gets a single transaction by id.
    api_response = api_instance.get_client_plan_transaction(authorization, client_id, plan_id, transaction_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_client_plan_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id - the special value \\\&quot;me\\\&quot; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| Plan Id - the id of the plan. | 
 **transaction_id** | **int**| Transaction Id - the id of the transaction. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_quote**
> Quote get_client_quote(authorization, client_id, quote_id, x_api_key, accept=accept)

Returns a client quote.

This endpoint allows an API user to retrieve a specific quote or illustration for a client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a client quote.
    api_response = api_instance.get_client_quote(authorization, client_id, quote_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_client_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Quote**](Quote.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_quote_result**
> QuoteResult get_client_quote_result(authorization, client_id, quote_id, quote_result_id, x_api_key, accept=accept)

Returns a client quote result.

This endpoint allows an API user to retrieve a specific quote result or illustration result for a client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
quote_result_id = 56 # int | Quote result identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a client quote result.
    api_response = api_instance.get_client_quote_result(authorization, client_id, quote_id, quote_result_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_client_quote_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **quote_result_id** | **int**| Quote result identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**QuoteResult**](QuoteResult.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_quote_result_product_benefits**
> ProductBenefitFeatures get_client_quote_result_product_benefits(authorization, client_id, quote_id, quote_result_id, x_api_key, accept=accept)

This endpoint allows an API user to retrieve product details of a specific quote result or illustration result for a client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
quote_result_id = 56 # int | Quote result identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # This endpoint allows an API user to retrieve product details of a specific quote result or illustration result for a client.
    api_response = api_instance.get_client_quote_result_product_benefits(authorization, client_id, quote_id, quote_result_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_client_quote_result_product_benefits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **quote_result_id** | **int**| Quote result identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**ProductBenefitFeatures**](ProductBenefitFeatures.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_dpa_policy**
> DPAPolicy get_current_dpa_policy(authorization, x_api_key, accept=accept, prefer=prefer)

Returns the current default DPA policy (see notes on party type above).

To retrieve the current DPA policy for a specific party type rather than the default DPA policy, specify the party type in a preference header. The current DPA policy is most recent active policy.                To specify a preference header add a header named 'prefer'  header to one of the following options:   * partytype=Corporate   * partytype=Persons   * partytype=Trust

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
prefer = 'prefer_example' # str | Used to indicate the party type associated with the DPA for the request. Options: PartyType=Person (optional)

try:
    # Returns the current default DPA policy (see notes on party type above).
    api_response = api_instance.get_current_dpa_policy(authorization, x_api_key, accept=accept, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_current_dpa_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **prefer** | **str**| Used to indicate the party type associated with the DPA for the request. Options: PartyType&#x3D;Person | [optional] 

### Return type

[**DPAPolicy**](DPAPolicy.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dpa_policy**
> DPAPolicy get_dpa_policy(authorization, policy_id, x_api_key, accept=accept)

Returns a single DPA policy.

To retrieve the active DPA policy use  the /dpa_policies/current'endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
policy_id = 56 # int | The DPA policy identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a single DPA policy.
    api_response = api_instance.get_dpa_policy(authorization, policy_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_dpa_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **policy_id** | **int**| The DPA policy identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**DPAPolicy**](DPAPolicy.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_income_statement**
> IncomeStatement get_income_statement(authorization, income_statement_id, x_api_key, accept=accept)

Returns an income statement.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
income_statement_id = 56 # int | Income statement identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns an income statement.
    api_response = api_instance.get_income_statement(authorization, income_statement_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_income_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **income_statement_id** | **int**| Income statement identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**IncomeStatement**](IncomeStatement.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_income_statement_item**
> IncomeStatementItem get_income_statement_item(authorization, income_statement_id, income_statement_item_id, x_api_key, accept=accept)

Returns a given item for a given income statement.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
income_statement_id = 56 # int | Income statement identifier
income_statement_item_id = 56 # int | Income statement item identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a given item for a given income statement.
    api_response = api_instance.get_income_statement_item(authorization, income_statement_id, income_statement_item_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_income_statement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **income_statement_id** | **int**| Income statement identifier | 
 **income_statement_item_id** | **int**| Income statement item identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**IncomeStatementItem**](IncomeStatementItem.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installed_app**
> App get_installed_app(app_id, authorization, x_api_key, accept=accept)

Returns an installed app

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns an installed app
    api_response = api_instance.get_installed_app(app_id, authorization, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_installed_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**App**](App.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installed_app_group_settings**
> AppSettingsDocument get_installed_app_group_settings(app_id, authorization, group_id, tenant_id, x_api_key, accept=accept, x_iflo_decrypt=x_iflo_decrypt)

Returns group settings for a given installed app and group

Give Apps the ability to define and capture their own dynamic group settings data using JSON schema definitions. For more detail and usage refer to [AppSettingsExtension](https://developer.gb.intelliflo.net/docs/ExtensionReference#iflo:store:AppSettingsExtension)  When called with this will return the specific group settings for the group. This endpoint will not traverse the hierarchy to find the first instance. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
authorization = 'authorization_example' # str | 
group_id = 'group_id_example' # str | 
tenant_id = 56 # int | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
x_iflo_decrypt = false # bool |  (optional) (default to false)

try:
    # Returns group settings for a given installed app and group
    api_response = api_instance.get_installed_app_group_settings(app_id, authorization, group_id, tenant_id, x_api_key, accept=accept, x_iflo_decrypt=x_iflo_decrypt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_installed_app_group_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **authorization** | **str**|  | 
 **group_id** | **str**|  | 
 **tenant_id** | **int**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **x_iflo_decrypt** | **bool**|  | [optional] [default to false]

### Return type

[**AppSettingsDocument**](AppSettingsDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installed_app_user_settings**
> AppSettingsDocument get_installed_app_user_settings(app_id, authorization, tenant_id, user_id, x_api_key, accept=accept, x_iflo_decrypt=x_iflo_decrypt)

Returns user settings for a given installed app and user

Give Apps the ability to define and capture their own dynamic user settings data using JSON schema definitions. For more detail and usage refer to [AppSettingsExtension](https://developer.gb.intelliflo.net/docs/ExtensionReference#iflo:store:AppSettingsExtension)  When called with [Authorization Code flow](https://developer.gb.intelliflo.net/docs/Authentication#CodeFlow) then this will allow the retrieval of the current users settings only. If called with [Tenant Client Credentials flow](https://developer.gb.intelliflo.net/docs/Authentication#TCCFlow) then it will return the user settings for the requested user within a tenant. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
authorization = 'authorization_example' # str | 
tenant_id = 56 # int | 
user_id = 'user_id_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
x_iflo_decrypt = false # bool |  (optional) (default to false)

try:
    # Returns user settings for a given installed app and user
    api_response = api_instance.get_installed_app_user_settings(app_id, authorization, tenant_id, user_id, x_api_key, accept=accept, x_iflo_decrypt=x_iflo_decrypt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_installed_app_user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **authorization** | **str**|  | 
 **tenant_id** | **int**|  | 
 **user_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **x_iflo_decrypt** | **bool**|  | [optional] [default to false]

### Return type

[**AppSettingsDocument**](AppSettingsDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lead_marketing_preferences**
> LeadMarketingPreferences get_lead_marketing_preferences(authorization, lead_id, x_api_key, accept=accept)

Returns lead's current marketing preferences.

Use this endpoint to return  a lead's marketing preferences broken down by medium where appropriate.  A successful response (200) will return lead's  marketing preferences document.  If a lead has not yet provided their preferences and/or consent, the returned preferences will be defaulted to a suitable privacy configuration.  The returned configuration should be adhered to regardless of whether consent has been given yet or not.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
lead_id = 56 # int | Lead identifier. The special value 'me' can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns lead's current marketing preferences.
    api_response = api_instance.get_lead_marketing_preferences(authorization, lead_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_lead_marketing_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **lead_id** | **int**| Lead identifier. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**LeadMarketingPreferences**](LeadMarketingPreferences.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lifecycle**
> Lifecycle get_lifecycle(authorization, lifecycle_id, x_api_key, accept=accept)

Returns a lifecycle.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
lifecycle_id = 56 # int | Lifecycle identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a lifecycle.
    api_response = api_instance.get_lifecycle(authorization, lifecycle_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_lifecycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **lifecycle_id** | **int**| Lifecycle identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Lifecycle**](Lifecycle.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_model**
> ProviderModel get_provider_model(app_id, authorization, model_id, x_api_key, accept=accept)

Returns a provider model.

Gives model providers the ability to view and manage their models.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
authorization = 'authorization_example' # str | 
model_id = 56 # int | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a provider model.
    api_response = api_instance.get_provider_model(app_id, authorization, model_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_provider_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **authorization** | **str**|  | 
 **model_id** | **int**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**ProviderModel**](ProviderModel.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_models**
> ProviderModelCollection get_provider_models(app_id, authorization, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of provider models.

This will only allow a maximum resulting page size of 500.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:   * __id__ ( in, eq, ne, gt, ge, lt, le )   * __isAccepted__ ( in, eq, ne )   * __appId__ (in, eq, ne, startswith )   * __code__ ( in, eq, ne, startswith )   * __name__ ( in, eq, ne, startswith )   * __atr.code__ ( in, eq, startswith )  Usage example: `filter=appId eq 'a13f242' and code startswith 'abc'` (optional)
orderby = 'orderby_example' # str | By default the list will be ordered desc by Id.    However it can be changed using one or more supported fields below.  Supported fields:   * __id__  * __isAccepted__  * __code__  * __name__    Usage example: `orderby=name asc` (optional)
skip = 0 # int | Index from which the results will start. (optional) (default to 0)
top = 100 # int | Number of records to retrieve (optional) (default to 100)

try:
    # Returns a list of provider models.
    api_response = api_instance.get_provider_models(app_id, authorization, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_provider_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:   * __id__ ( in, eq, ne, gt, ge, lt, le )   * __isAccepted__ ( in, eq, ne )   * __appId__ (in, eq, ne, startswith )   * __code__ ( in, eq, ne, startswith )   * __name__ ( in, eq, ne, startswith )   * __atr.code__ ( in, eq, startswith )  Usage example: &#x60;filter&#x3D;appId eq &#x27;a13f242&#x27; and code startswith &#x27;abc&#x27;&#x60; | [optional] 
 **orderby** | **str**| By default the list will be ordered desc by Id.    However it can be changed using one or more supported fields below.  Supported fields:   * __id__  * __isAccepted__  * __code__  * __name__    Usage example: &#x60;orderby&#x3D;name asc&#x60; | [optional] 
 **skip** | **int**| Index from which the results will start. | [optional] [default to 0]
 **top** | **int**| Number of records to retrieve | [optional] [default to 100]

### Return type

[**ProviderModelCollection**](ProviderModelCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant**
> Tenant get_tenant(authorization, tenant_id, x_api_key, accept=accept)

Retrieves the tenant resource specified 

Retrieves the tenant resource specified. Tenants are typically resources that represent a firm, legal entity or network. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
tenant_id = 56 # int | Tenant identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Retrieves the tenant resource specified 
    api_response = api_instance.get_tenant(authorization, tenant_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **tenant_id** | **int**| Tenant identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_valuation_batch**
> ValuationBatch get_valuation_batch(authorization, batch_id, tenant_id, x_api_key, accept=accept)

Returns a single valuationbatch

Use this endpoint to view the status of a batch.                Batch can have one of the following status  * Queued  * InProgress  * Failed  * Completed  * DeleteInProgress  * DeleteFailed  * Expired (When a batch is older than 3 months batch data will be removed and the batch state will be set to `Expired` by system)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
batch_id = 56 # int | batch id
tenant_id = 56 # int | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a single valuationbatch
    api_response = api_instance.get_valuation_batch(authorization, batch_id, tenant_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->get_valuation_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **batch_id** | **int**| batch id | 
 **tenant_id** | **int**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**ValuationBatch**](ValuationBatch.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_dependants**
> DependantCollection list_client_dependants(authorization, client_id, x_api_key, accept=accept, skip=skip, top=top)

Returns a list of dependants for a given client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
top = 100 # int | The number of records to retrieve (default 100, max 500) (optional) (default to 100)

try:
    # Returns a list of dependants for a given client.
    api_response = api_instance.list_client_dependants(authorization, client_id, x_api_key, accept=accept, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_client_dependants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **top** | **int**| The number of records to retrieve (default 100, max 500) | [optional] [default to 100]

### Return type

[**DependantCollection**](DependantCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_dpa_policy_agreements**
> DPAPolicyAgreementCollection list_client_dpa_policy_agreements(authorization, client_id, x_api_key, accept=accept, skip=skip, top=top)

Returns a list of client's DPA policy agreements.

Returns a list of client's DPA policy agreements.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client that agreed to the DPA policy. The special value 'me' can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
top = 250 # int | Number of records to retrieve (default '25', max '100'). (optional) (default to 250)

try:
    # Returns a list of client's DPA policy agreements.
    api_response = api_instance.list_client_dpa_policy_agreements(authorization, client_id, x_api_key, accept=accept, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_client_dpa_policy_agreements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| The client that agreed to the DPA policy. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **top** | **int**| Number of records to retrieve (default &#x27;25&#x27;, max &#x27;100&#x27;). | [optional] [default to 250]

### Return type

[**DPAPolicyAgreementCollection**](DPAPolicyAgreementCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_expenditures**
> ExpenditureCollection list_client_expenditures(authorization, client_id, x_api_key, accept=accept, filter=filter, prefer=prefer, skip=skip, top=top)

Returns a list of expenditure records for a client. The returned list may be filtered.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client identifier. The special value \"me\" can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | The returned list of questions can be filtered using one or more of the following supported fields and operators:                * `id` (`in`)  * `frequency` (`in`, `eq`, `ne`)                Usage examples:  * `filter=id in (1,2)`  * `filter=frequency eq 'Monthly' or frequency in ('Weekly','Monthly')`.                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). (optional)
prefer = 'prefer_example' # str | Used to indicate which format the expenditure categories are returned in. Valid options are: 'x-iflo-apiversion=1' or 'x-iflo-apiversion=2'. If not specified the default is 'x-iflo-apiversion=1' (optional)
skip = 0 # int | Optional. Number of records to skip. Must be greater than or equal to zero. Defaults to zero if not specified. (optional) (default to 0)
top = 100 # int | Optional. The number of records to retrieve (max 500). Defaults to 100 if not specified. (optional) (default to 100)

try:
    # Returns a list of expenditure records for a client. The returned list may be filtered.
    api_response = api_instance.list_client_expenditures(authorization, client_id, x_api_key, accept=accept, filter=filter, prefer=prefer, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_client_expenditures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| The client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| The returned list of questions can be filtered using one or more of the following supported fields and operators:                * &#x60;id&#x60; (&#x60;in&#x60;)  * &#x60;frequency&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;, &#x60;ne&#x60;)                Usage examples:  * &#x60;filter&#x3D;id in (1,2)&#x60;  * &#x60;filter&#x3D;frequency eq &#x27;Monthly&#x27; or frequency in (&#x27;Weekly&#x27;,&#x27;Monthly&#x27;)&#x60;.                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). | [optional] 
 **prefer** | **str**| Used to indicate which format the expenditure categories are returned in. Valid options are: &#x27;x-iflo-apiversion&#x3D;1&#x27; or &#x27;x-iflo-apiversion&#x3D;2&#x27;. If not specified the default is &#x27;x-iflo-apiversion&#x3D;1&#x27; | [optional] 
 **skip** | **int**| Optional. Number of records to skip. Must be greater than or equal to zero. Defaults to zero if not specified. | [optional] [default to 0]
 **top** | **int**| Optional. The number of records to retrieve (max 500). Defaults to 100 if not specified. | [optional] [default to 100]

### Return type

[**ExpenditureCollection**](ExpenditureCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_fees**
> FeeCollection list_client_fees(authorization, client_id, x_api_key, accept=accept, filter=filter, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of fees for a given client. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported Filters:  * `id` (`in`, `eq`, `ne`, `gt`, `ge`, `lt`, `le`)    `status` (`in`, `eq`, `ne`, `startswith`)    `feeType.Name` (`in`, `eq`, `ne`, `startswith`)    `feeType.Category` (`in`, `eq`, `ne`)    `feeChargingType.Name` (`eq`)    `clients.id` (`in`)  See[QueryLang] (docs/ApiQueryLang) for further usage details. (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
tenant_id = 56 # int | Tenant Identifier. (optional)
top = 100 # int | The number of records to retrieve (default 100, max 500). (optional) (default to 100)

try:
    # Returns a list of fees for a given client. 
    api_response = api_instance.list_client_fees(authorization, client_id, x_api_key, accept=accept, filter=filter, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_client_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported Filters:  * &#x60;id&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;gt&#x60;, &#x60;ge&#x60;, &#x60;lt&#x60;, &#x60;le&#x60;)    &#x60;status&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;startswith&#x60;)    &#x60;feeType.Name&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;startswith&#x60;)    &#x60;feeType.Category&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;, &#x60;ne&#x60;)    &#x60;feeChargingType.Name&#x60; (&#x60;eq&#x60;)    &#x60;clients.id&#x60; (&#x60;in&#x60;)  See[QueryLang] (docs/ApiQueryLang) for further usage details. | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **tenant_id** | **int**| Tenant Identifier. | [optional] 
 **top** | **int**| The number of records to retrieve (default 100, max 500). | [optional] [default to 100]

### Return type

[**FeeCollection**](FeeCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_incomes**
> IncomeCollection list_client_incomes(authorization, client_id, x_api_key, accept=accept, filter=filter, prefer=prefer, skip=skip, top=top)

Returns a list of incomes for a given client. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client identifier. The special value \"me\" can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | The returned list of questions can be filtered using one or more of the following supported fields and operators:                * `id` (`in`)  * `employment.id` (`in`, `eq`)  * `frequency` (`in`, `eq`, `ne`)                Usage examples:  * `filter=id in (1,2)`  * `filter=employment.id eq 22 and id in (1,2)`  * `filter=frequency eq 'Single' or frequency in ('Single','Monthly')`.                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). (optional)
prefer = 'prefer_example' # str | Used to indicate which format the income categories are returned in. Valid options are: 'x-iflo-apiversion=1' or 'x-iflo-apiversion=2'. If not specified the default is 'x-iflo-apiversion=1' (optional)
skip = 0 # int | Optional. Number of records to skip. Must be greater than or equal to zero. Defaults to zero if not specified. (optional) (default to 0)
top = 100 # int | Optional. The number of records to retrieve (max 500). Defaults to 100 if not specified. (optional) (default to 100)

try:
    # Returns a list of incomes for a given client. 
    api_response = api_instance.list_client_incomes(authorization, client_id, x_api_key, accept=accept, filter=filter, prefer=prefer, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_client_incomes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| The client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| The returned list of questions can be filtered using one or more of the following supported fields and operators:                * &#x60;id&#x60; (&#x60;in&#x60;)  * &#x60;employment.id&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;)  * &#x60;frequency&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;, &#x60;ne&#x60;)                Usage examples:  * &#x60;filter&#x3D;id in (1,2)&#x60;  * &#x60;filter&#x3D;employment.id eq 22 and id in (1,2)&#x60;  * &#x60;filter&#x3D;frequency eq &#x27;Single&#x27; or frequency in (&#x27;Single&#x27;,&#x27;Monthly&#x27;)&#x60;.                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). | [optional] 
 **prefer** | **str**| Used to indicate which format the income categories are returned in. Valid options are: &#x27;x-iflo-apiversion&#x3D;1&#x27; or &#x27;x-iflo-apiversion&#x3D;2&#x27;. If not specified the default is &#x27;x-iflo-apiversion&#x3D;1&#x27; | [optional] 
 **skip** | **int**| Optional. Number of records to skip. Must be greater than or equal to zero. Defaults to zero if not specified. | [optional] [default to 0]
 **top** | **int**| Optional. The number of records to retrieve (max 500). Defaults to 100 if not specified. | [optional] [default to 100]

### Return type

[**IncomeCollection**](IncomeCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_plan_contributions**
> ContributionCollection list_client_plan_contributions(authorization, client_id, plan_id, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)

Returns list of contributions for a given client and plan. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
plan_id = 56 # int | Plan identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | The results can be filtered using one or more of the supported fields and operators.               For details on how to filter and sort data (using the query language) please see [QueryLang](docs/ApiQueryLang).                             The supported fields and operators are:                             * `appliesTo`(`eq`)               * `contributionType` (`eq`, `ne`, `in`)               * `id` (`eq`, `in`)               * `isCurrent` (`eq`)               * `startsOn` (`eq`, `gt`, `lt`,`ge`, `le`)               * `stopsOn` (`eq`, `ne`, `gt`, `lt`,`ge`, `le`)                             Note. By default contributions without a stopson date are returned when using the stopson filter. To filter these records the `eq` and `ne` operators accept null as the parameter                     and can be used to filter for contributions where the stopson date has not been set.                     e.g. filter=stopsOn eq null. (optional)
order_by = 'order_by_example' # str | The results can be ordered by the following fields:                             * `Id`               * `contributionType`               * `isCurrent`               * `startsOn`               * `stopsOn`                             By default the results are ordered by Id. (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
tenant_id = 56 # int | Tenant Identifier. (optional)
top = 100 # int | The number of records to retrieve (default 25, max 100) (optional) (default to 100)

try:
    # Returns list of contributions for a given client and plan. 
    api_response = api_instance.list_client_plan_contributions(authorization, client_id, plan_id, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_client_plan_contributions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **plan_id** | **int**| Plan identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| The results can be filtered using one or more of the supported fields and operators.               For details on how to filter and sort data (using the query language) please see [QueryLang](docs/ApiQueryLang).                             The supported fields and operators are:                             * &#x60;appliesTo&#x60;(&#x60;eq&#x60;)               * &#x60;contributionType&#x60; (&#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;in&#x60;)               * &#x60;id&#x60; (&#x60;eq&#x60;, &#x60;in&#x60;)               * &#x60;isCurrent&#x60; (&#x60;eq&#x60;)               * &#x60;startsOn&#x60; (&#x60;eq&#x60;, &#x60;gt&#x60;, &#x60;lt&#x60;,&#x60;ge&#x60;, &#x60;le&#x60;)               * &#x60;stopsOn&#x60; (&#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;gt&#x60;, &#x60;lt&#x60;,&#x60;ge&#x60;, &#x60;le&#x60;)                             Note. By default contributions without a stopson date are returned when using the stopson filter. To filter these records the &#x60;eq&#x60; and &#x60;ne&#x60; operators accept null as the parameter                     and can be used to filter for contributions where the stopson date has not been set.                     e.g. filter&#x3D;stopsOn eq null. | [optional] 
 **order_by** | **str**| The results can be ordered by the following fields:                             * &#x60;Id&#x60;               * &#x60;contributionType&#x60;               * &#x60;isCurrent&#x60;               * &#x60;startsOn&#x60;               * &#x60;stopsOn&#x60;                             By default the results are ordered by Id. | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **tenant_id** | **int**| Tenant Identifier. | [optional] 
 **top** | **int**| The number of records to retrieve (default 25, max 100) | [optional] [default to 100]

### Return type

[**ContributionCollection**](ContributionCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_plan_fees**
> FeeCollection list_client_plan_fees(authorization, client_id, plan_id, x_api_key, accept=accept, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of fees for a given client and plan. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
plan_id = 56 # int | Plan identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
tenant_id = 56 # int | Tenant identifier. (optional)
top = 100 # int | The number of records to retrieve (default 25, max 100). (optional) (default to 100)

try:
    # Returns a list of fees for a given client and plan. 
    api_response = api_instance.list_client_plan_fees(authorization, client_id, plan_id, x_api_key, accept=accept, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_client_plan_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **plan_id** | **int**| Plan identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **tenant_id** | **int**| Tenant identifier. | [optional] 
 **top** | **int**| The number of records to retrieve (default 25, max 100). | [optional] [default to 100]

### Return type

[**FeeCollection**](FeeCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_plan_transactions**
> TransactionCollection list_client_plan_transactions(authorization, client_id, plan_id, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of transactions for a client plan.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id - the id of the client.
plan_id = 56 # int | Plan Id - the id of the plan.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:  * `id` (eq,ne,gt,ge,lt,le,in)  * `source` (eq)  * `debitCreditIndicator` (eq)  * `type` (eq, in)  * `transactionDate` (le,lt,gt,ge,eq)  * `category1` (eq,ne)  * `category2` (eq,ne)  * `description` (eq,startswith)  * `gross` (eq,ne,gt,ge,lt,le,in)  * `unitPrice` (eq,ne,gt,ge,lt,le,in)  * `externalReference` (eq,ne,startswith,in) (optional)
order_by = 'order_by_example' # str | By default the list will be ordered desc by Id.  However it can be changed using one or more supported fields below.  Supported fields:  * `transactionDate`  * `category1`  * `category2`  * `description`  * `gross`                Supported directions asc, desc. (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
tenant_id = 56 # int | Tenant Id (optional)
top = 100 # int | The number of records to retrieve (default 100, max 500). (optional) (default to 100)

try:
    # Returns a list of transactions for a client plan.
    api_response = api_instance.list_client_plan_transactions(authorization, client_id, plan_id, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_client_plan_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id - the id of the client. | 
 **plan_id** | **int**| Plan Id - the id of the plan. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:  * &#x60;id&#x60; (eq,ne,gt,ge,lt,le,in)  * &#x60;source&#x60; (eq)  * &#x60;debitCreditIndicator&#x60; (eq)  * &#x60;type&#x60; (eq, in)  * &#x60;transactionDate&#x60; (le,lt,gt,ge,eq)  * &#x60;category1&#x60; (eq,ne)  * &#x60;category2&#x60; (eq,ne)  * &#x60;description&#x60; (eq,startswith)  * &#x60;gross&#x60; (eq,ne,gt,ge,lt,le,in)  * &#x60;unitPrice&#x60; (eq,ne,gt,ge,lt,le,in)  * &#x60;externalReference&#x60; (eq,ne,startswith,in) | [optional] 
 **order_by** | **str**| By default the list will be ordered desc by Id.  However it can be changed using one or more supported fields below.  Supported fields:  * &#x60;transactionDate&#x60;  * &#x60;category1&#x60;  * &#x60;category2&#x60;  * &#x60;description&#x60;  * &#x60;gross&#x60;                Supported directions asc, desc. | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **tenant_id** | **int**| Tenant Id | [optional] 
 **top** | **int**| The number of records to retrieve (default 100, max 500). | [optional] [default to 100]

### Return type

[**TransactionCollection**](TransactionCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_plan_withdrawals**
> WithdrawalCollection list_client_plan_withdrawals(authorization, client_id, plan_id, x_api_key, accept=accept, skip=skip, top=top)

Returns a list of withdrawal for a given client and plan. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
plan_id = 56 # int | Plan identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
top = 100 # int | The number of records to retrieve (default 25, max 100) (optional) (default to 100)

try:
    # Returns a list of withdrawal for a given client and plan. 
    api_response = api_instance.list_client_plan_withdrawals(authorization, client_id, plan_id, x_api_key, accept=accept, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_client_plan_withdrawals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **plan_id** | **int**| Plan identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **top** | **int**| The number of records to retrieve (default 25, max 100) | [optional] [default to 100]

### Return type

[**WithdrawalCollection**](WithdrawalCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_quote_results**
> QuoteResultCollection list_client_quote_results(authorization, client_id, quote_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of client quote results.

This endpoint provides the ability to identify all of client's quote and illustration results.  Be aware that this API will only allow a maximum resulting page size of 500.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported Filters:  * `id` (`eq`, `ne`, `in`, `gt`, `ge`, `lt`, `le`)                See[QueryLang] (docs/ApiQueryLang) for further usage details. (optional)
orderby = 'orderby_example' # str | Supported Sort Properties:  * `id` (`asc` or `desc`)                Default: `id` `desc`. (optional)
skip = 0 # int | The number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
top = 25 # int | The number of records to retrieve (default: 25, max: 500). (optional) (default to 25)

try:
    # Returns a list of client quote results.
    api_response = api_instance.list_client_quote_results(authorization, client_id, quote_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_client_quote_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported Filters:  * &#x60;id&#x60; (&#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;in&#x60;, &#x60;gt&#x60;, &#x60;ge&#x60;, &#x60;lt&#x60;, &#x60;le&#x60;)                See[QueryLang] (docs/ApiQueryLang) for further usage details. | [optional] 
 **orderby** | **str**| Supported Sort Properties:  * &#x60;id&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)                Default: &#x60;id&#x60; &#x60;desc&#x60;. | [optional] 
 **skip** | **int**| The number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **top** | **int**| The number of records to retrieve (default: 25, max: 500). | [optional] [default to 25]

### Return type

[**QuoteResultCollection**](QuoteResultCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_quotes**
> QuotesCollection list_client_quotes(authorization, client_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of quotes.

This endpoint allows an API user to identify all of a client's quotes and illustrations.  Be aware that this API will only allow a maximum resulting page size of 500.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported Filters:  * `id` (`in`),  * `appName` (`startswith`),  * `customReference` (`startswith`),  * `reference` (`startswith`),  * `serviceCase.id` (`eq`, `in`)                See[QueryLang] (docs/ApiQueryLang) for further usage details. (optional)
orderby = 'orderby_example' # str | Supported Sort Properties:  * `id` (`asc` or `desc`),  * `appName` (`asc` or `desc`),  * `customReference` (`asc` or `desc`),  * `reference` (`asc` or `desc`),  * `status` (`asc` or `desc`),  * `productGroup` (`asc` or `desc`),  * `createdAt` (`asc` or `desc`)                Default: `id` `desc`. (optional)
skip = 0 # int | The number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
top = 25 # int | The number of records to retrieve (default: 25, max: 500). (optional) (default to 25)

try:
    # Returns a list of quotes.
    api_response = api_instance.list_client_quotes(authorization, client_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_client_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported Filters:  * &#x60;id&#x60; (&#x60;in&#x60;),  * &#x60;appName&#x60; (&#x60;startswith&#x60;),  * &#x60;customReference&#x60; (&#x60;startswith&#x60;),  * &#x60;reference&#x60; (&#x60;startswith&#x60;),  * &#x60;serviceCase.id&#x60; (&#x60;eq&#x60;, &#x60;in&#x60;)                See[QueryLang] (docs/ApiQueryLang) for further usage details. | [optional] 
 **orderby** | **str**| Supported Sort Properties:  * &#x60;id&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;),  * &#x60;appName&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;),  * &#x60;customReference&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;),  * &#x60;reference&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;),  * &#x60;status&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;),  * &#x60;productGroup&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;),  * &#x60;createdAt&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)                Default: &#x60;id&#x60; &#x60;desc&#x60;. | [optional] 
 **skip** | **int**| The number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **top** | **int**| The number of records to retrieve (default: 25, max: 500). | [optional] [default to 25]

### Return type

[**QuotesCollection**](QuotesCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_transactions**
> TransactionCollection list_client_transactions(authorization, client_id, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of transactions for a client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id - the id of the client.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:  * `id` (eq,ne,gt,ge,lt,le,in)  * `source` (eq)  * `plan.id` (eq,in)  * `debitCreditIndicator` (eq)  * `type` (eq, in)  * `transactionDate` (le,lt,gt,ge,eq)  * `category1` (eq,ne)  * `category2` (eq,ne)  * `description` (eq,startswith)  * `gross` (eq,ne,gt,ge,lt,le,in)  * `unitPrice` (eq,ne,gt,ge,lt,le,in)  * `externalReference` (eq,ne,startswith,in) (optional)
order_by = 'order_by_example' # str | By default the list will be ordered desc by Id.  However it can be changed using one or more supported fields below.  Supported fields:  * `transactionDate`  * `category1`  * `category2`  * `description`  * `gross`                Supported directions asc, desc. (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
tenant_id = 56 # int | Tenant Id (optional)
top = 100 # int | The number of records to retrieve (default 100, max 500). (optional) (default to 100)

try:
    # Returns a list of transactions for a client.
    api_response = api_instance.list_client_transactions(authorization, client_id, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_client_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id - the id of the client. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:  * &#x60;id&#x60; (eq,ne,gt,ge,lt,le,in)  * &#x60;source&#x60; (eq)  * &#x60;plan.id&#x60; (eq,in)  * &#x60;debitCreditIndicator&#x60; (eq)  * &#x60;type&#x60; (eq, in)  * &#x60;transactionDate&#x60; (le,lt,gt,ge,eq)  * &#x60;category1&#x60; (eq,ne)  * &#x60;category2&#x60; (eq,ne)  * &#x60;description&#x60; (eq,startswith)  * &#x60;gross&#x60; (eq,ne,gt,ge,lt,le,in)  * &#x60;unitPrice&#x60; (eq,ne,gt,ge,lt,le,in)  * &#x60;externalReference&#x60; (eq,ne,startswith,in) | [optional] 
 **order_by** | **str**| By default the list will be ordered desc by Id.  However it can be changed using one or more supported fields below.  Supported fields:  * &#x60;transactionDate&#x60;  * &#x60;category1&#x60;  * &#x60;category2&#x60;  * &#x60;description&#x60;  * &#x60;gross&#x60;                Supported directions asc, desc. | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **tenant_id** | **int**| Tenant Id | [optional] 
 **top** | **int**| The number of records to retrieve (default 100, max 500). | [optional] [default to 100]

### Return type

[**TransactionCollection**](TransactionCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dpa_policies**
> DPAPolicyCollection list_dpa_policies(authorization, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of DPA policies.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported filters options:  *  `name (in)`  *  `partyType (eq)`                Valid values for party type are 'Person', 'Corporate', 'Trust' or 'Default'                See [QueryLang](docs/ApiQueryLang) for further details of how to use the filtering and sorting parameters. (optional)
orderby = 'orderby_example' # str | Supported sorting options:  *  `name`  *  `partyType'  *  `createdat (optional)
skip = 0 # int | The number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
top = 100 # int | The number of records to retrieve. (optional) (default to 100)

try:
    # Returns a list of DPA policies.
    api_response = api_instance.list_dpa_policies(authorization, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_dpa_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported filters options:  *  &#x60;name (in)&#x60;  *  &#x60;partyType (eq)&#x60;                Valid values for party type are &#x27;Person&#x27;, &#x27;Corporate&#x27;, &#x27;Trust&#x27; or &#x27;Default&#x27;                See [QueryLang](docs/ApiQueryLang) for further details of how to use the filtering and sorting parameters. | [optional] 
 **orderby** | **str**| Supported sorting options:  *  &#x60;name&#x60;  *  &#x60;partyType&#x27;  *  &#x60;createdat | [optional] 
 **skip** | **int**| The number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **top** | **int**| The number of records to retrieve. | [optional] [default to 100]

### Return type

[**DPAPolicyCollection**](DPAPolicyCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_income_statement_items**
> IncomeStatementItemCollection list_income_statement_items(authorization, income_statement_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of items for a given income statement.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
income_statement_id = 56 # int | Income statement identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:   * __id__ ( in, eq, ne, gt, ge, lt, le )   * __type__ ( in, eq )   * __isAnalysed__ ( eq, ne )    Usage example: `isAnalysed eq false and type in ('OngFee', 'Lvl')` (optional)
orderby = 'orderby_example' # str | By default the list will be ordered desc by Id.    However it can be changed using one or more supported fields below.  Supported fields:   * __id__   (asc,desc)  * __type__ (asc,desc)  * __isAnalysed__ (asc,desc)    Usage example: `orderby=type asc` (optional)
skip = 0 # int | Index from which the results will start. (optional) (default to 0)
top = 100 # int | Number of records to retrieve (optional) (default to 100)

try:
    # Returns a list of items for a given income statement.
    api_response = api_instance.list_income_statement_items(authorization, income_statement_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_income_statement_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **income_statement_id** | **int**| Income statement identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:   * __id__ ( in, eq, ne, gt, ge, lt, le )   * __type__ ( in, eq )   * __isAnalysed__ ( eq, ne )    Usage example: &#x60;isAnalysed eq false and type in (&#x27;OngFee&#x27;, &#x27;Lvl&#x27;)&#x60; | [optional] 
 **orderby** | **str**| By default the list will be ordered desc by Id.    However it can be changed using one or more supported fields below.  Supported fields:   * __id__   (asc,desc)  * __type__ (asc,desc)  * __isAnalysed__ (asc,desc)    Usage example: &#x60;orderby&#x3D;type asc&#x60; | [optional] 
 **skip** | **int**| Index from which the results will start. | [optional] [default to 0]
 **top** | **int**| Number of records to retrieve | [optional] [default to 100]

### Return type

[**IncomeStatementItemCollection**](IncomeStatementItemCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_income_statements**
> IncomeStatementCollection list_income_statements(authorization, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of income statements.

If called with  [Tenant Client Credentials Flow](/docs/Authentication#TCCFlow) and firm_data.incomestatement then it will return income statements for the authenticated client(app) and tenant.  If you add the additional app_data scope then you will receive all your apps data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:   * __id__ ( in, eq, ne, gt, ge, lt, le )   * __date__ ( eq, ne, gt, ge, lt, le )   * __isMatched__ ( eq, ne )   * __reference__ ( eq, in, startswith )    Usage example: `isMatched eq true and date gt '2019-01-01T00:00:00.000'` (optional)
orderby = 'orderby_example' # str | By default the list will be ordered desc by Id.    However it can be changed using one or more supported fields below.  Supported fields:   * __id__  * __date__  * __reference__    Usage example: `orderby=date asc` (optional)
skip = 0 # int | Index from which the results will start. (optional) (default to 0)
top = 100 # int | Number of records to retrieve (optional) (default to 100)

try:
    # Returns a list of income statements.
    api_response = api_instance.list_income_statements(authorization, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_income_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:   * __id__ ( in, eq, ne, gt, ge, lt, le )   * __date__ ( eq, ne, gt, ge, lt, le )   * __isMatched__ ( eq, ne )   * __reference__ ( eq, in, startswith )    Usage example: &#x60;isMatched eq true and date gt &#x27;2019-01-01T00:00:00.000&#x27;&#x60; | [optional] 
 **orderby** | **str**| By default the list will be ordered desc by Id.    However it can be changed using one or more supported fields below.  Supported fields:   * __id__  * __date__  * __reference__    Usage example: &#x60;orderby&#x3D;date asc&#x60; | [optional] 
 **skip** | **int**| Index from which the results will start. | [optional] [default to 0]
 **top** | **int**| Number of records to retrieve | [optional] [default to 100]

### Return type

[**IncomeStatementCollection**](IncomeStatementCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_installed_app_group_settings**
> InstalledAppGroupSettingCollection list_installed_app_group_settings(app_id, authorization, tenant_id, x_api_key, accept=accept, skip=skip, top=top, x_iflo_decrypt=x_iflo_decrypt)

Returns a list of group settings for a given installed app

Give Apps the ability to define and capture their own dynamic group settings data using JSON schema definitions. For more detail and usage refer to [AppSettingsExtension](https://developer.gb.intelliflo.net/docs/ExtensionReference#iflo:store:AppSettingsExtension)  When called with [Authorisation Code flow](https://developer.gb.intelliflo.net/docs/Authentication#CodeFlow) then this will return the first instance of group settings in the upward lineage of the tenants group hierarchy. If called with [Tenant Client Credentials flow](https://developer.gb.intelliflo.net/docs/Authentication#TCCFlow) then it will return all group settings for a tenant. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
authorization = 'authorization_example' # str | 
tenant_id = 56 # int | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int |  (optional) (default to 0)
top = 100 # int |  (optional) (default to 100)
x_iflo_decrypt = false # bool |  (optional) (default to false)

try:
    # Returns a list of group settings for a given installed app
    api_response = api_instance.list_installed_app_group_settings(app_id, authorization, tenant_id, x_api_key, accept=accept, skip=skip, top=top, x_iflo_decrypt=x_iflo_decrypt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_installed_app_group_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **authorization** | **str**|  | 
 **tenant_id** | **int**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **top** | **int**|  | [optional] [default to 100]
 **x_iflo_decrypt** | **bool**|  | [optional] [default to false]

### Return type

[**InstalledAppGroupSettingCollection**](InstalledAppGroupSettingCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_installed_app_user_settings**
> InstalledAppGroupSettingCollection list_installed_app_user_settings(app_id, authorization, tenant_id, x_api_key, accept=accept, skip=skip, top=top, x_iflo_decrypt=x_iflo_decrypt)

Returns a lists of user settings for a given installed app

Give Apps the ability to define and capture their own dynamic user settings data using JSON schema definitions. For more detail and usage refer to [AppSettingsExtension](https://developer.gb.intelliflo.net/docs/ExtensionReference#iflo:store:AppSettingsExtension)  When called with [Authorization Code flow](https://developer.gb.intelliflo.net/docs/Authentication#CodeFlow) this will return the current users settings only. If it is called with [Tenant Client Credentials flow](https://developer.gb.intelliflo.net/docs/Authentication#TCCFlow) then it will return all user settings for a tenant. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
authorization = 'authorization_example' # str | 
tenant_id = 56 # int | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int |  (optional) (default to 0)
top = 100 # int |  (optional) (default to 100)
x_iflo_decrypt = false # bool |  (optional) (default to false)

try:
    # Returns a lists of user settings for a given installed app
    api_response = api_instance.list_installed_app_user_settings(app_id, authorization, tenant_id, x_api_key, accept=accept, skip=skip, top=top, x_iflo_decrypt=x_iflo_decrypt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_installed_app_user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **authorization** | **str**|  | 
 **tenant_id** | **int**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **top** | **int**|  | [optional] [default to 100]
 **x_iflo_decrypt** | **bool**|  | [optional] [default to false]

### Return type

[**InstalledAppGroupSettingCollection**](InstalledAppGroupSettingCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_installed_apps**
> AppCollection list_installed_apps(authorization, x_api_key, accept=accept, skip=skip, tenant_id=tenant_id, top=top, user_id=user_id)

Returns a list of installed apps

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int |  (optional) (default to 0)
tenant_id = 56 # int |  (optional)
top = 100 # int |  (optional) (default to 100)
user_id = 56 # int |  (optional)

try:
    # Returns a list of installed apps
    api_response = api_instance.list_installed_apps(authorization, x_api_key, accept=accept, skip=skip, tenant_id=tenant_id, top=top, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_installed_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **tenant_id** | **int**|  | [optional] 
 **top** | **int**|  | [optional] [default to 100]
 **user_id** | **int**|  | [optional] 

### Return type

[**AppCollection**](AppCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lifecycles**
> LifecycleDocumentCollection list_lifecycles(authorization, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, top=top)

Returns a list of lifecycles.

This endpoint provides the ability to identify the plan lifecycles that have been set for a tenant.  The `filter` parameter allows the results to be filtered.  Please see the parameters for more details.  Be aware that this API will only allow a maximum resulting page size of 500.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported fields and operators:              id (in): e.g. filter=id in (1, 3),              name (eq, startswith): e.g. filter=name eq 'Pre-Existing' and name startswith 'Pre%' (optional)
order_by = 'order_by_example' # str | Supported fields: id, name. Supported directions: asc, desc: orderBy=name desc (optional)
skip = 0 # int | Number of records to skip: skip=1 (optional) (default to 0)
top = 100 # int | Number of records to get: top=11 (optional) (default to 100)

try:
    # Returns a list of lifecycles.
    api_response = api_instance.list_lifecycles(authorization, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_lifecycles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported fields and operators:              id (in): e.g. filter&#x3D;id in (1, 3),              name (eq, startswith): e.g. filter&#x3D;name eq &#x27;Pre-Existing&#x27; and name startswith &#x27;Pre%&#x27; | [optional] 
 **order_by** | **str**| Supported fields: id, name. Supported directions: asc, desc: orderBy&#x3D;name desc | [optional] 
 **skip** | **int**| Number of records to skip: skip&#x3D;1 | [optional] [default to 0]
 **top** | **int**| Number of records to get: top&#x3D;11 | [optional] [default to 100]

### Return type

[**LifecycleDocumentCollection**](LifecycleDocumentCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_plantype_lifecycles**
> LifecycleDocumentCollection list_plantype_lifecycles(authorization, name, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, top=top)

Retrieves a list of lifecycles associated with the specified planType

A lifecycle represents the many stages that a plan can pass through.  The `filter` parameter allows the results to be filtered.  Please see the parameters for more details.  Be aware that this API will only allow a maximum resulting page size of 500.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
name = 'name_example' # str | Plan type name
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported fields and operators:              id (in): e.g. filter=id in (1, 3)              name (eq, startswith): e.g. filter=name eq 'Pre-Existing' and name startswith 'Pre' (optional)
order_by = 'order_by_example' # str | Supported fields: id, name. Supported directions: asc, desc: orderBy=name desc (optional)
skip = 0 # int | Number of records to skip: skip=1 (optional) (default to 0)
top = 100 # int | Number of records to get: top=11 (optional) (default to 100)

try:
    # Retrieves a list of lifecycles associated with the specified planType
    api_response = api_instance.list_plantype_lifecycles(authorization, name, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_plantype_lifecycles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**| Plan type name | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported fields and operators:              id (in): e.g. filter&#x3D;id in (1, 3)              name (eq, startswith): e.g. filter&#x3D;name eq &#x27;Pre-Existing&#x27; and name startswith &#x27;Pre&#x27; | [optional] 
 **order_by** | **str**| Supported fields: id, name. Supported directions: asc, desc: orderBy&#x3D;name desc | [optional] 
 **skip** | **int**| Number of records to skip: skip&#x3D;1 | [optional] [default to 0]
 **top** | **int**| Number of records to get: top&#x3D;11 | [optional] [default to 100]

### Return type

[**LifecycleDocumentCollection**](LifecycleDocumentCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_valuation_batch_results**
> ValuationBatchResultCollection list_valuation_batch_results(authorization, batch_id, tenant_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top, x_iflo_exclude_holdings=x_iflo_exclude_holdings)

Returns the results for a single valuationbatch.

Use this endpoint to view the results of a valuationbatch  * Results will not be available after the valuationbatch is `expired`  * It will have items grouped in `holdings` by `policyNumber` and `portalReference`  * It will have a `matched_plan` indicating if the item has matched to a plan or not  * when `matched_plan = true`      * It will have a `matched_plan_href` to navigate to the plan  * when `matched_plan = true and is_imported = true`      * Holdings will have a `matched_holding_href` to navigate to the holding  * Note that if no fund price is supplied and the fund cannot be matched to a feed fund or equity    then the valuation for plan will not be imported  Use GET valuations/batches to get the batch id and to see the status of the batch.  You can use the optional header x-iflo-exclude-holdings=true to exclude the holdings detail from the response.  This is advisable when fetching the results of large batches.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
batch_id = 56 # int | batch id
tenant_id = 56 # int | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Results can be filtered using one or more supported fields and operators below.              For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).              Supported fields (operators) are              `PolicyNumber` ( `in`, `eq`, `ne`, `startswith` ),              `PortalReference` ( `in`, `eq`, `ne`, `startswith` ),              `Matched_Plan` ( `eq`, `ne` )              `Is_Imported` ( `eq`, `ne` )              Usage example: `filter=matched_plan eq false` (optional)
orderby = 'orderby_example' # str | By default the results will be ordered asc by PolicyNumber.              However it can be changed using one or more supported fields below.              `PolicyNumber`, `PortalReference`, `matched_plan`              Usage example: `orderby=PortalReference desc` (optional)
skip = 56 # int | Number of records to skip. Must be greater than or equal to zero (optional)
top = 56 # int | Number of records to retrieve (default 100, max 500) (optional)
x_iflo_exclude_holdings = false # bool |  (optional) (default to false)

try:
    # Returns the results for a single valuationbatch.
    api_response = api_instance.list_valuation_batch_results(authorization, batch_id, tenant_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top, x_iflo_exclude_holdings=x_iflo_exclude_holdings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_valuation_batch_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **batch_id** | **int**| batch id | 
 **tenant_id** | **int**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Results can be filtered using one or more supported fields and operators below.              For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).              Supported fields (operators) are              &#x60;PolicyNumber&#x60; ( &#x60;in&#x60;, &#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;startswith&#x60; ),              &#x60;PortalReference&#x60; ( &#x60;in&#x60;, &#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;startswith&#x60; ),              &#x60;Matched_Plan&#x60; ( &#x60;eq&#x60;, &#x60;ne&#x60; )              &#x60;Is_Imported&#x60; ( &#x60;eq&#x60;, &#x60;ne&#x60; )              Usage example: &#x60;filter&#x3D;matched_plan eq false&#x60; | [optional] 
 **orderby** | **str**| By default the results will be ordered asc by PolicyNumber.              However it can be changed using one or more supported fields below.              &#x60;PolicyNumber&#x60;, &#x60;PortalReference&#x60;, &#x60;matched_plan&#x60;              Usage example: &#x60;orderby&#x3D;PortalReference desc&#x60; | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] 
 **top** | **int**| Number of records to retrieve (default 100, max 500) | [optional] 
 **x_iflo_exclude_holdings** | **bool**|  | [optional] [default to false]

### Return type

[**ValuationBatchResultCollection**](ValuationBatchResultCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_valuation_batches**
> ValuationBatchCollection list_valuation_batches(authorization, tenant_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of valuationbatch

Use this endpoint to view the statuses of multiple valuationbatches.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
tenant_id = 56 # int | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | List can be filtered using one or more supported fields and operators below.              For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).              Supported fields (operators) are              `Id` (`in`,`eq`,`ne`,`gt`,`ge`,`lt`,`le`),              `State` (`in`,`eq`,`ne`),              `CreatedAt` (`in`,`eq`,`ne`,`gt`,`ge`,`lt`,`le`),              `ProductProvider.Id` (`in`,`eq`,`ne`,`gt`,`ge`,`lt`,`le`),              `CreatedBy.Name` (`in`,`eq`,`ne`,`startswith`)              Usage example: `filter=state eq 'failed' ` (optional)
orderby = 'orderby_example' # str | By default the list will be ordered desc by Id.              However it can be changed using one or more supported fields below.              `Id`, `CreatedAt`, `ProductProvider.Id`, `CreatedBy.Name`              Usage example: `orderby=CreatedAt asc` (optional)
skip = 56 # int | Number of records to skip. Must be greater than or equal to zero (optional)
top = 56 # int | Number of records to retrieve (default 100, max 500) (optional)

try:
    # Returns a list of valuationbatch
    api_response = api_instance.list_valuation_batches(authorization, tenant_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->list_valuation_batches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **tenant_id** | **int**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| List can be filtered using one or more supported fields and operators below.              For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).              Supported fields (operators) are              &#x60;Id&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;,&#x60;gt&#x60;,&#x60;ge&#x60;,&#x60;lt&#x60;,&#x60;le&#x60;),              &#x60;State&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;),              &#x60;CreatedAt&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;,&#x60;gt&#x60;,&#x60;ge&#x60;,&#x60;lt&#x60;,&#x60;le&#x60;),              &#x60;ProductProvider.Id&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;,&#x60;gt&#x60;,&#x60;ge&#x60;,&#x60;lt&#x60;,&#x60;le&#x60;),              &#x60;CreatedBy.Name&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;,&#x60;startswith&#x60;)              Usage example: &#x60;filter&#x3D;state eq &#x27;failed&#x27; &#x60; | [optional] 
 **orderby** | **str**| By default the list will be ordered desc by Id.              However it can be changed using one or more supported fields below.              &#x60;Id&#x60;, &#x60;CreatedAt&#x60;, &#x60;ProductProvider.Id&#x60;, &#x60;CreatedBy.Name&#x60;              Usage example: &#x60;orderby&#x3D;CreatedAt asc&#x60; | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] 
 **top** | **int**| Number of records to retrieve (default 100, max 500) | [optional] 

### Return type

[**ValuationBatchCollection**](ValuationBatchCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_dpa_policy**
> DPAPolicy patch_dpa_policy(body, authorization, x_api_key, policy_id, accept=accept)

Updates an existing DPA policy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = [swagger_client.Operation()] # list[Operation] | A Json Patch document containing details of modifications to be made to the DPA policy.
Only the following paths may be modified:
* `/clientCanAccept`
            
For a simple example a request contains the following JSON:
            
{
    "op": "replace",
    "path": "/clientCanAccept",
    "value": "True"
}
            
would result in the clientCanAccept value for the targeted resource being set to 'True'.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
policy_id = 56 # int | DPA policy Identifier.
accept = 'accept_example' # str |  (optional)

try:
    # Updates an existing DPA policy.
    api_response = api_instance.patch_dpa_policy(body, authorization, x_api_key, policy_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->patch_dpa_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Operation]**](Operation.md)| A Json Patch document containing details of modifications to be made to the DPA policy.
Only the following paths may be modified:
* &#x60;/clientCanAccept&#x60;
            
For a simple example a request contains the following JSON:
            
{
    &quot;op&quot;: &quot;replace&quot;,
    &quot;path&quot;: &quot;/clientCanAccept&quot;,
    &quot;value&quot;: &quot;True&quot;
}
            
would result in the clientCanAccept value for the targeted resource being set to &#x27;True&#x27;. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **policy_id** | **int**| DPA policy Identifier. | 
 **accept** | **str**|  | [optional] 

### Return type

[**DPAPolicy**](DPAPolicy.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_client_quote_status**
> Quote set_client_quote_status(body, authorization, x_api_key, client_id, quote_id, status, accept=accept)

Sets a new status for the client quote.

This endpoint allows an API user to create a new status for the quote or illustration.  This will replace the current status value.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.Quote() # Quote | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
status = 'status_example' # str | New quote status. Supported values are Initiated, Submitted, Failed, Expired and Complete.
accept = 'accept_example' # str |  (optional)

try:
    # Sets a new status for the client quote.
    api_response = api_instance.set_client_quote_status(body, authorization, x_api_key, client_id, quote_id, status, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->set_client_quote_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Quote**](Quote.md)|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **status** | **str**| New quote status. Supported values are Initiated, Submitted, Failed, Expired and Complete. | 
 **accept** | **str**|  | [optional] 

### Return type

[**Quote**](Quote.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_dependant**
> Dependant update_client_dependant(body, authorization, x_api_key, client_id, dependant_id, accept=accept)

Updates a dependant for a given client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.Dependant() # Dependant | Dependant document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier
dependant_id = 56 # int | Dependant identifier
accept = 'accept_example' # str |  (optional)

try:
    # Updates a dependant for a given client.
    api_response = api_instance.update_client_dependant(body, authorization, x_api_key, client_id, dependant_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->update_client_dependant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dependant**](Dependant.md)| Dependant document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **dependant_id** | **int**| Dependant identifier | 
 **accept** | **str**|  | [optional] 

### Return type

[**Dependant**](Dependant.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_expenditure**
> Expenditure update_client_expenditure(body, authorization, x_api_key, client_id, expenditure_id, accept=accept, prefer=prefer)

Updates a client's expenditure record.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.Expenditure() # Expenditure | The updated details for the expenditure.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | The client identifier. The special value \"me\" can be used to indicate the authenticated user.
expenditure_id = 56 # int | The identifier for the expenditure record to update.
accept = 'accept_example' # str |  (optional)
prefer = 'prefer_example' # str | Used to indicate which format the expenditure categories are returned in. Valid options are: 'x-iflo-apiversion=1' or 'x-iflo-apiversion=2'. If not specified the default is 'x-iflo-apiversion=1' (optional)

try:
    # Updates a client's expenditure record.
    api_response = api_instance.update_client_expenditure(body, authorization, x_api_key, client_id, expenditure_id, accept=accept, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->update_client_expenditure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Expenditure**](Expenditure.md)| The updated details for the expenditure. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| The client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **expenditure_id** | **int**| The identifier for the expenditure record to update. | 
 **accept** | **str**|  | [optional] 
 **prefer** | **str**| Used to indicate which format the expenditure categories are returned in. Valid options are: &#x27;x-iflo-apiversion&#x3D;1&#x27; or &#x27;x-iflo-apiversion&#x3D;2&#x27;. If not specified the default is &#x27;x-iflo-apiversion&#x3D;1&#x27; | [optional] 

### Return type

[**Expenditure**](Expenditure.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_fee**
> FeeDocument update_client_fee(body, authorization, x_api_key, client_id, fee_id, accept=accept, tenant_id=tenant_id)

Updates a fee for a given client and fee. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.FeeDocument() # FeeDocument | Fee.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier.
fee_id = 56 # int | Fee identifier.
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier. (optional)

try:
    # Updates a fee for a given client and fee. 
    api_response = api_instance.update_client_fee(body, authorization, x_api_key, client_id, fee_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->update_client_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeeDocument**](FeeDocument.md)| Fee. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **fee_id** | **int**| Fee identifier. | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier. | [optional] 

### Return type

[**FeeDocument**](FeeDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_income**
> Income update_client_income(body, authorization, x_api_key, client_id, income_id, accept=accept, prefer=prefer)

Updates a client's income record.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.Income() # Income | The updated income record.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | The client identifier. The special value \"me\" can be used to indicate the authenticated user.
income_id = 56 # int | The identifier for the income record.
accept = 'accept_example' # str |  (optional)
prefer = 'prefer_example' # str | Used to indicate which format the income categories are returned in. Valid options are: 'x-iflo-apiversion=1' or 'x-iflo-apiversion=2'. If not specified the default is 'x-iflo-apiversion=1' (optional)

try:
    # Updates a client's income record.
    api_response = api_instance.update_client_income(body, authorization, x_api_key, client_id, income_id, accept=accept, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->update_client_income: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Income**](Income.md)| The updated income record. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| The client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **income_id** | **int**| The identifier for the income record. | 
 **accept** | **str**|  | [optional] 
 **prefer** | **str**| Used to indicate which format the income categories are returned in. Valid options are: &#x27;x-iflo-apiversion&#x3D;1&#x27; or &#x27;x-iflo-apiversion&#x3D;2&#x27;. If not specified the default is &#x27;x-iflo-apiversion&#x3D;1&#x27; | [optional] 

### Return type

[**Income**](Income.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_marketing_preferences**
> ClientMarketingPreferences update_client_marketing_preferences(body, authorization, x_api_key, client_id, accept=accept)

Updates client's marketing preferences.

Use this endpoint to updates a client's marketing preferences broken down by medium where appropriate.  A successful response (200) will return updated client's  marketing preferences document.  If a client has not yet provided their preferences and/or consent, new preferences will be created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClientMarketingPreferences() # ClientMarketingPreferences | Client Marketing Preferences document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier. The special value 'me' can be used to indicate the authenticated user.
accept = 'accept_example' # str |  (optional)

try:
    # Updates client's marketing preferences.
    api_response = api_instance.update_client_marketing_preferences(body, authorization, x_api_key, client_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->update_client_marketing_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientMarketingPreferences**](ClientMarketingPreferences.md)| Client Marketing Preferences document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **accept** | **str**|  | [optional] 

### Return type

[**ClientMarketingPreferences**](ClientMarketingPreferences.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_plan**
> BasePlan update_client_plan(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)

Updates a plan for a given client. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.BasePlan() # BasePlan | Plan
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client Id - The special value \"me\" can be used to indicate the authenticated user.
plan_id = 56 # int | PlanId
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Updates a plan for a given client. 
    api_response = api_instance.update_client_plan(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->update_client_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BasePlan**](BasePlan.md)| Plan | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client Id - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| PlanId | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

[**BasePlan**](BasePlan.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_plan_transaction**
> Transaction update_client_plan_transaction(body, authorization, x_api_key, client_id, plan_id, transaction_id, accept=accept, tenant_id=tenant_id)

Updates a client plan transaction.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = [swagger_client.Operation()] # list[Operation] | A Json Patch document containing details of modifications to be made to the client plan transaction resource.
Only the following paths may be modified:
* `/category1`
* `/category1Code`
* `/category2`
* `/category2Code1`
* `/description`
* `/unitPrice`
* `/unitNumber`
* `/transactionDate`
            
For a simple example a request contains the following JSON:
            
{
    "op": "replace",
    "path": "/category1",
    "value": "New Category 1"
}
            
would result in the category1 value for the targeted resource being set to 'New Category 1'.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client Id
plan_id = 56 # int | Plan Id
transaction_id = 789 # int | Transaction Id
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Updates a client plan transaction.
    api_response = api_instance.update_client_plan_transaction(body, authorization, x_api_key, client_id, plan_id, transaction_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->update_client_plan_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Operation]**](Operation.md)| A Json Patch document containing details of modifications to be made to the client plan transaction resource.
Only the following paths may be modified:
* &#x60;/category1&#x60;
* &#x60;/category1Code&#x60;
* &#x60;/category2&#x60;
* &#x60;/category2Code1&#x60;
* &#x60;/description&#x60;
* &#x60;/unitPrice&#x60;
* &#x60;/unitNumber&#x60;
* &#x60;/transactionDate&#x60;
            
For a simple example a request contains the following JSON:
            
{
    &quot;op&quot;: &quot;replace&quot;,
    &quot;path&quot;: &quot;/category1&quot;,
    &quot;value&quot;: &quot;New Category 1&quot;
}
            
would result in the category1 value for the targeted resource being set to &#x27;New Category 1&#x27;. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client Id | 
 **plan_id** | **int**| Plan Id | 
 **transaction_id** | **int**| Transaction Id | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_quote_result_product_benefits**
> ProductBenefitFeatures update_client_quote_result_product_benefits(body, authorization, x_api_key, client_id, quote_id, quote_result_id, accept=accept)

This endpoint allows an API user to update product details of a specific quote result or illustration result for a client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductBenefitFeatures() # ProductBenefitFeatures | Request document with product benefit features
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
quote_result_id = 56 # int | Quote result identifier.
accept = 'accept_example' # str |  (optional)

try:
    # This endpoint allows an API user to update product details of a specific quote result or illustration result for a client.
    api_response = api_instance.update_client_quote_result_product_benefits(body, authorization, x_api_key, client_id, quote_id, quote_result_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->update_client_quote_result_product_benefits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductBenefitFeatures**](ProductBenefitFeatures.md)| Request document with product benefit features | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **quote_result_id** | **int**| Quote result identifier. | 
 **accept** | **str**|  | [optional] 

### Return type

[**ProductBenefitFeatures**](ProductBenefitFeatures.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dpa_policy**
> DPAPolicy update_dpa_policy(body, authorization, x_api_key, policy_id, accept=accept)

Updates an existing DPA policy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.DPAPolicy() # DPAPolicy | A DPA policy document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
policy_id = 56 # int | The DPA policy Identifier.
accept = 'accept_example' # str |  (optional)

try:
    # Updates an existing DPA policy.
    api_response = api_instance.update_dpa_policy(body, authorization, x_api_key, policy_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->update_dpa_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DPAPolicy**](DPAPolicy.md)| A DPA policy document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **policy_id** | **int**| The DPA policy Identifier. | 
 **accept** | **str**|  | [optional] 

### Return type

[**DPAPolicy**](DPAPolicy.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_income_statement**
> IncomeStatement update_income_statement(body, authorization, x_api_key, income_statement_id, accept=accept)

Updates an income statement.

You can only edit the income statement if it is not matched and none of the items are analysed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.IncomeStatement() # IncomeStatement | Income statement document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
income_statement_id = 56 # int | Income statement identifier
accept = 'accept_example' # str |  (optional)

try:
    # Updates an income statement.
    api_response = api_instance.update_income_statement(body, authorization, x_api_key, income_statement_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->update_income_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IncomeStatement**](IncomeStatement.md)| Income statement document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **income_statement_id** | **int**| Income statement identifier | 
 **accept** | **str**|  | [optional] 

### Return type

[**IncomeStatement**](IncomeStatement.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_income_statement_item**
> IncomeStatementItem update_income_statement_item(body, authorization, x_api_key, income_statement_id, income_statement_item_id, accept=accept)

Updates an income statement item for a given income statement.

You cannot edit any properties if the item is analysed.  You can edit policy and client if the item is not analysed and the statement is matched.  You can edit policy, client and gross amount if the item is not analysed and the statement is not matched.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.IncomeStatementItem() # IncomeStatementItem | Income statement item document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
income_statement_id = 56 # int | Income statement identifier
income_statement_item_id = 56 # int | Income statement item identifier
accept = 'accept_example' # str |  (optional)

try:
    # Updates an income statement item for a given income statement.
    api_response = api_instance.update_income_statement_item(body, authorization, x_api_key, income_statement_id, income_statement_item_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->update_income_statement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IncomeStatementItem**](IncomeStatementItem.md)| Income statement item document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **income_statement_id** | **int**| Income statement identifier | 
 **income_statement_item_id** | **int**| Income statement item identifier | 
 **accept** | **str**|  | [optional] 

### Return type

[**IncomeStatementItem**](IncomeStatementItem.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_installed_app_group_settings**
> AppSettingsDocument update_installed_app_group_settings(body, authorization, x_api_key, app_id, group_id, accept=accept, tenant_id=tenant_id)

Updates group settings for a given installed app and group

Give Apps the ability to define and capture their own dynamic group settings data using JSON schema definitions. For more detail and usage refer to [AppSettingsExtension](https://developer.gb.intelliflo.net/docs/ExtensionReference#iflo:store:AppSettingsExtension)  When called with [Authorisation Code flow](https://developer.gb.intelliflo.net/docs/Authentication#CodeFlow) then this will save the specific group settings for the group.     

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppSettingsDocument() # AppSettingsDocument | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
app_id = 'app_id_example' # str | 
group_id = 'group_id_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int |  (optional)

try:
    # Updates group settings for a given installed app and group
    api_response = api_instance.update_installed_app_group_settings(body, authorization, x_api_key, app_id, group_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->update_installed_app_group_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppSettingsDocument**](AppSettingsDocument.md)|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **app_id** | **str**|  | 
 **group_id** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**|  | [optional] 

### Return type

[**AppSettingsDocument**](AppSettingsDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_installed_app_user_settings**
> AppSettingsDocument update_installed_app_user_settings(body, authorization, x_api_key, app_id, user_id, accept=accept, tenant_id=tenant_id)

Updates user settings for a given installed app and user

Give Apps the ability to define and capture their own dynamic user settings data using JSON schema definitions. For more detail and usage refer to [AppSettingsExtension](https://developer.gb.intelliflo.net/docs/ExtensionReference#iflo:store:AppSettingsExtension)  When called with [Authorization Code flow](https://developer.gb.intelliflo.net/docs/Authentication#CodeFlow) then this will save the settings for the current user. If it is called with [Tenant Client Credentials flow](https://developer.gb.intelliflo.net/docs/Authentication#TCCFlow) then it will save the settings for the requested user within a tenant. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppSettingsDocument() # AppSettingsDocument | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
app_id = 'app_id_example' # str | 
user_id = 'user_id_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int |  (optional)

try:
    # Updates user settings for a given installed app and user
    api_response = api_instance.update_installed_app_user_settings(body, authorization, x_api_key, app_id, user_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->update_installed_app_user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppSettingsDocument**](AppSettingsDocument.md)|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **app_id** | **str**|  | 
 **user_id** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**|  | [optional] 

### Return type

[**AppSettingsDocument**](AppSettingsDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lead_marketing_preferences**
> LeadMarketingPreferences update_lead_marketing_preferences(body, authorization, x_api_key, lead_id, accept=accept)

Updates lead's marketing preferences.

Use this endpoint to updates a lead's marketing preferences broken down by medium where appropriate.  A successful response (200) will return updated client's  marketing preferences document.  If a lead has not yet provided their preferences and/or consent, new preferences will be created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2-authorization-code
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-implicit
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2-password
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BetaApi(swagger_client.ApiClient(configuration))
body = swagger_client.LeadMarketingPreferences() # LeadMarketingPreferences | Lead Marketing Preferences document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
lead_id = 56 # int | Lead identifier. The special value 'me' can be used to indicate the authenticated user.
accept = 'accept_example' # str |  (optional)

try:
    # Updates lead's marketing preferences.
    api_response = api_instance.update_lead_marketing_preferences(body, authorization, x_api_key, lead_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BetaApi->update_lead_marketing_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LeadMarketingPreferences**](LeadMarketingPreferences.md)| Lead Marketing Preferences document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **lead_id** | **int**| Lead identifier. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **accept** | **str**|  | [optional] 

### Return type

[**LeadMarketingPreferences**](LeadMarketingPreferences.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

