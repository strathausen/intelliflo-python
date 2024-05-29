# swagger_client.TenantsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tenant**](TenantsApi.md#get_tenant) | **GET** /tenants/{tenantId} | Retrieves the tenant resource specified 

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
api_instance = swagger_client.TenantsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
tenant_id = 56 # int | Tenant identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Retrieves the tenant resource specified 
    api_response = api_instance.get_tenant(authorization, tenant_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->get_tenant: %s\n" % e)
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

