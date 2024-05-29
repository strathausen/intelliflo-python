# swagger_client.WithdrawalsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_plan_withdrawals**](WithdrawalsApi.md#create_plan_withdrawals) | **POST** /clients/{clientId}/plans/{planId}/withdrawals | Creates a withdrawal for a given client and plan. 
[**delete_client_plan_withdrawal**](WithdrawalsApi.md#delete_client_plan_withdrawal) | **DELETE** /clients/{clientId}/plans/{planId}/withdrawals/{withdrawalId} | Deletes a withdrawal for a given client, plan and withdrawal. 
[**get_client_plan_withdrawal**](WithdrawalsApi.md#get_client_plan_withdrawal) | **GET** /clients/{clientId}/plans/{planId}/withdrawals/{withdrawalId} | Returns a withdrawal for a given client, plan and withdrawal. 
[**list_client_plan_withdrawals**](WithdrawalsApi.md#list_client_plan_withdrawals) | **GET** /clients/{clientId}/plans/{planId}/withdrawals | Returns a list of withdrawal for a given client and plan. 
[**update_client_plan_withdrawal**](WithdrawalsApi.md#update_client_plan_withdrawal) | **PUT** /clients/{clientId}/plans/{planId}/withdrawals/{withdrawalId} | Updates a withdrawal for a given client, plan and withdrawal. 

# **create_plan_withdrawals**
> Withdrawal create_plan_withdrawals(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)

Creates a withdrawal for a given client and plan. 

Option \"None\" is being deprecated, use at your own risk.  frequencyType \"none\" will be set to \"single\" if used together with withdrawalType \"regular\". All other usage of \"none\" will result in http 400.

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
api_instance = swagger_client.WithdrawalsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Withdrawal() # Withdrawal | Withdrawal document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client Identifier
plan_id = 56 # int | Plan Identifier for the plan where this resource will be created.
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Identifer. (optional)

try:
    # Creates a withdrawal for a given client and plan. 
    api_response = api_instance.create_plan_withdrawals(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WithdrawalsApi->create_plan_withdrawals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Withdrawal**](Withdrawal.md)| Withdrawal document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client Identifier | 
 **plan_id** | **int**| Plan Identifier for the plan where this resource will be created. | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Identifer. | [optional] 

### Return type

[**Withdrawal**](Withdrawal.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_plan_withdrawal**
> delete_client_plan_withdrawal(authorization, client_id, plan_id, withdrawal_id, x_api_key, accept=accept)

Deletes a withdrawal for a given client, plan and withdrawal. 

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
api_instance = swagger_client.WithdrawalsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
plan_id = 56 # int | Plan identifier
withdrawal_id = 56 # int | withdrawal identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes a withdrawal for a given client, plan and withdrawal. 
    api_instance.delete_client_plan_withdrawal(authorization, client_id, plan_id, withdrawal_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling WithdrawalsApi->delete_client_plan_withdrawal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **plan_id** | **int**| Plan identifier | 
 **withdrawal_id** | **int**| withdrawal identifier | 
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

# **get_client_plan_withdrawal**
> Withdrawal get_client_plan_withdrawal(authorization, client_id, plan_id, withdrawal_id, x_api_key, accept=accept)

Returns a withdrawal for a given client, plan and withdrawal. 

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
api_instance = swagger_client.WithdrawalsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value \"me\" can be used to indicate the authenticated user.
plan_id = 56 # int | Plan identifier
withdrawal_id = 56 # int | Withdrawal identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a withdrawal for a given client, plan and withdrawal. 
    api_response = api_instance.get_client_plan_withdrawal(authorization, client_id, plan_id, withdrawal_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WithdrawalsApi->get_client_plan_withdrawal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| Plan identifier | 
 **withdrawal_id** | **int**| Withdrawal identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Withdrawal**](Withdrawal.md)

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
api_instance = swagger_client.WithdrawalsApi(swagger_client.ApiClient(configuration))
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
    print("Exception when calling WithdrawalsApi->list_client_plan_withdrawals: %s\n" % e)
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

# **update_client_plan_withdrawal**
> Withdrawal update_client_plan_withdrawal(body, authorization, x_api_key, client_id, plan_id, withdrawal_id, accept=accept)

Updates a withdrawal for a given client, plan and withdrawal. 

Option \"None\" is being deprecated, use at your own risk.  frequencyType \"none\" will be set to \"single\" if used together with withdrawalType \"regular\". All other usage of \"none\" will result in http 400.

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
api_instance = swagger_client.WithdrawalsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateWithdrawal() # UpdateWithdrawal | Withdrawal document with requested changes.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier
plan_id = 56 # int | Plan identifier for the plan where this resource belongs to.
withdrawal_id = 56 # int | Withdrawal Identifier.
accept = 'accept_example' # str |  (optional)

try:
    # Updates a withdrawal for a given client, plan and withdrawal. 
    api_response = api_instance.update_client_plan_withdrawal(body, authorization, x_api_key, client_id, plan_id, withdrawal_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WithdrawalsApi->update_client_plan_withdrawal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWithdrawal**](UpdateWithdrawal.md)| Withdrawal document with requested changes. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **plan_id** | **int**| Plan identifier for the plan where this resource belongs to. | 
 **withdrawal_id** | **int**| Withdrawal Identifier. | 
 **accept** | **str**|  | [optional] 

### Return type

[**Withdrawal**](Withdrawal.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

