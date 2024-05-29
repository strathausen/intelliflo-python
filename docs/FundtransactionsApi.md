# swagger_client.FundtransactionsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_plan_holding_transaction**](FundtransactionsApi.md#get_client_plan_holding_transaction) | **GET** /clients/{clientId}/plans/{planId}/holdings/{holdingId}/transactions/{transactionId} | Returns a fund holdings transaction for a given client, plan, holding and transaction. 
[**list_client_plan_holding_transactions**](FundtransactionsApi.md#list_client_plan_holding_transactions) | **GET** /clients/{clientId}/plans/{planId}/holdings/{holdingId}/transactions | Returns a list of fund holdings transactions for a given client, plan and holding. 

# **get_client_plan_holding_transaction**
> FundTransaction get_client_plan_holding_transaction(authorization, client_id, holding_id, plan_id, tenant_id, transaction_id, x_api_key, accept=accept)

Returns a fund holdings transaction for a given client, plan, holding and transaction. 

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
api_instance = swagger_client.FundtransactionsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value \"me\" can be used to indicate the authenticated user.
holding_id = 56 # int | Fund Holding identifier
plan_id = 56 # int | Plan identifier
tenant_id = 56 # int | Tenant identifier
transaction_id = 56 # int | Transaction identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a fund holdings transaction for a given client, plan, holding and transaction. 
    api_response = api_instance.get_client_plan_holding_transaction(authorization, client_id, holding_id, plan_id, tenant_id, transaction_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundtransactionsApi->get_client_plan_holding_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **holding_id** | **int**| Fund Holding identifier | 
 **plan_id** | **int**| Plan identifier | 
 **tenant_id** | **int**| Tenant identifier | 
 **transaction_id** | **int**| Transaction identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**FundTransaction**](FundTransaction.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_plan_holding_transactions**
> FundTransactionCollection list_client_plan_holding_transactions(authorization, client_id, holding_id, plan_id, tenant_id, x_api_key, accept=accept, filter=filter, skip=skip, top=top)

Returns a list of fund holdings transactions for a given client, plan and holding. 

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
api_instance = swagger_client.FundtransactionsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
holding_id = 56 # int | Plan holding identifier
plan_id = 56 # int | Plan identifier
tenant_id = 56 # int | Tenant identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported fields and operators: type (in), transactiondate (lt, le, gt, ge): e.g. filter=type in ('sale','purchase') and transactiondate gt 'startDate' (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
top = 100 # int | The number of records to retrieve (default 25, max 100) (optional) (default to 100)

try:
    # Returns a list of fund holdings transactions for a given client, plan and holding. 
    api_response = api_instance.list_client_plan_holding_transactions(authorization, client_id, holding_id, plan_id, tenant_id, x_api_key, accept=accept, filter=filter, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundtransactionsApi->list_client_plan_holding_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **holding_id** | **int**| Plan holding identifier | 
 **plan_id** | **int**| Plan identifier | 
 **tenant_id** | **int**| Tenant identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported fields and operators: type (in), transactiondate (lt, le, gt, ge): e.g. filter&#x3D;type in (&#x27;sale&#x27;,&#x27;purchase&#x27;) and transactiondate gt &#x27;startDate&#x27; | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **top** | **int**| The number of records to retrieve (default 25, max 100) | [optional] [default to 100]

### Return type

[**FundTransactionCollection**](FundTransactionCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

