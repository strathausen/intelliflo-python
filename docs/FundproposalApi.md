# swagger_client.FundproposalApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_client_plan_fundproposal**](FundproposalApi.md#delete_client_plan_fundproposal) | **DELETE** /clients/{clientId}/plans/{planId}/fundproposal | Deletes fund proposals from holdings for a given client and plan. 
[**get_client_plan_fundproposal**](FundproposalApi.md#get_client_plan_fundproposal) | **GET** /clients/{clientId}/plans/{planId}/fundproposal | Returns a fund proposals from holidings for a given client and plan. 
[**update_client_plan_fundproposal**](FundproposalApi.md#update_client_plan_fundproposal) | **PUT** /clients/{clientId}/plans/{planId}/fundproposal | Updates or creates a fund proposal for a given client and plan. 

# **delete_client_plan_fundproposal**
> delete_client_plan_fundproposal(authorization, client_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)

Deletes fund proposals from holdings for a given client and plan. 

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
api_instance = swagger_client.FundproposalApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
plan_id = 56 # int | Plan identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int |  (optional)

try:
    # Deletes fund proposals from holdings for a given client and plan. 
    api_instance.delete_client_plan_fundproposal(authorization, client_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling FundproposalApi->delete_client_plan_fundproposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **plan_id** | **int**| Plan identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_plan_fundproposal**
> FundProposal get_client_plan_fundproposal(authorization, client_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)

Returns a fund proposals from holidings for a given client and plan. 

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
api_instance = swagger_client.FundproposalApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
plan_id = 56 # int | Plan identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int |  (optional)

try:
    # Returns a fund proposals from holidings for a given client and plan. 
    api_response = api_instance.get_client_plan_fundproposal(authorization, client_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundproposalApi->get_client_plan_fundproposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **plan_id** | **int**| Plan identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**|  | [optional] 

### Return type

[**FundProposal**](FundProposal.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_plan_fundproposal**
> FundProposal update_client_plan_fundproposal(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)

Updates or creates a fund proposal for a given client and plan. 

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
api_instance = swagger_client.FundproposalApi(swagger_client.ApiClient(configuration))
body = swagger_client.FundProposal() # FundProposal | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier
plan_id = 56 # int | Plan identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int |  (optional)

try:
    # Updates or creates a fund proposal for a given client and plan. 
    api_response = api_instance.update_client_plan_fundproposal(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundproposalApi->update_client_plan_fundproposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FundProposal**](FundProposal.md)|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **plan_id** | **int**| Plan identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**|  | [optional] 

### Return type

[**FundProposal**](FundProposal.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

