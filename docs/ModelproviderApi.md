# swagger_client.ModelproviderApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_provider_model**](ModelproviderApi.md#create_provider_model) | **POST** /apps/{appId}/models | Creates a new provider model.
[**get_provider_model**](ModelproviderApi.md#get_provider_model) | **GET** /apps/{appId}/models/{modelId} | Returns a provider model.
[**get_provider_models**](ModelproviderApi.md#get_provider_models) | **GET** /apps/{appId}/models | Returns a list of provider models.

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
api_instance = swagger_client.ModelproviderApi(swagger_client.ApiClient(configuration))
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
    print("Exception when calling ModelproviderApi->create_provider_model: %s\n" % e)
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
api_instance = swagger_client.ModelproviderApi(swagger_client.ApiClient(configuration))
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
    print("Exception when calling ModelproviderApi->get_provider_model: %s\n" % e)
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
api_instance = swagger_client.ModelproviderApi(swagger_client.ApiClient(configuration))
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
    print("Exception when calling ModelproviderApi->get_provider_models: %s\n" % e)
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

