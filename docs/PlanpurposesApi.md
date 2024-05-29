# swagger_client.PlanpurposesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_planpurposes**](PlanpurposesApi.md#list_planpurposes) | **GET** /planpurposes | Returns a list of plan purposes for a specific tenant. 

# **list_planpurposes**
> PlanPurposeCollection list_planpurposes(authorization, x_api_key, accept=accept, plan_type=plan_type, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of plan purposes for a specific tenant. 

This will return an unfiltered collection of Plan Purpose resources that have been configured for the [Tenant](/apis?tags=tenants).  This collection can be narrowed by specifying a [PlanType](/apis?tags=plantypes) as an optional query parameter. *Example:* `/planpurposes?planType=Cash%20Account` 

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
api_instance = swagger_client.PlanpurposesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
plan_type = 'plan_type_example' # str | Narrows the scope of the returned collection to only those associated with the given planType (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
tenant_id = 56 # int | Tenant identifier (optional)
top = 100 # int | The number of records to retrieve (default 25, max 100) (optional) (default to 100)

try:
    # Returns a list of plan purposes for a specific tenant. 
    api_response = api_instance.list_planpurposes(authorization, x_api_key, accept=accept, plan_type=plan_type, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlanpurposesApi->list_planpurposes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **plan_type** | **str**| Narrows the scope of the returned collection to only those associated with the given planType | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **tenant_id** | **int**| Tenant identifier | [optional] 
 **top** | **int**| The number of records to retrieve (default 25, max 100) | [optional] [default to 100]

### Return type

[**PlanPurposeCollection**](PlanPurposeCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

