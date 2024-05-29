# swagger_client.ProductprovidersApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_productprovider**](ProductprovidersApi.md#get_productprovider) | **GET** /productproviders/{productProviderId} | Returns a product provider. 
[**list_productproviders**](ProductprovidersApi.md#list_productproviders) | **GET** /productproviders | Returns a list of product providers. 

# **get_productprovider**
> ProductProvider get_productprovider(authorization, product_provider_id, x_api_key, accept=accept)

Returns a product provider. 

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
api_instance = swagger_client.ProductprovidersApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
product_provider_id = 56 # int | ProductProvider identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a product provider. 
    api_response = api_instance.get_productprovider(authorization, product_provider_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductprovidersApi->get_productprovider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **product_provider_id** | **int**| ProductProvider identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**ProductProvider**](ProductProvider.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_productproviders**
> ProductProviderCollection list_productproviders(authorization, x_api_key, accept=accept, filter=filter, skip=skip, top=top)

Returns a list of product providers. 

Gets a list of ProductProvider. Some specific filtering is optionally supported:   The following fields are supports for `startswith`:  * `name`  *Example*  `top=5&amp;Skip=1&amp;filter= name startswith '21'` 

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
api_instance = swagger_client.ProductprovidersApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)
skip = 0 # int |  (optional) (default to 0)
top = 100 # int |  (optional) (default to 100)

try:
    # Returns a list of product providers. 
    api_response = api_instance.list_productproviders(authorization, x_api_key, accept=accept, filter=filter, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductprovidersApi->list_productproviders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **top** | **int**|  | [optional] [default to 100]

### Return type

[**ProductProviderCollection**](ProductProviderCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

