# swagger_client.AdvisersApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adviser_exists**](AdvisersApi.md#adviser_exists) | **HEAD** /advisers/{adviserId} | Checks if the adviser exists. 
[**get_adviser**](AdvisersApi.md#get_adviser) | **GET** /advisers/{adviserId} | Returns an adviser for a given adviser. 
[**list_advisers**](AdvisersApi.md#list_advisers) | **GET** /advisers | Returns a list of advisers. 

# **adviser_exists**
> adviser_exists(adviser_id, authorization, x_api_key, accept=accept)

Checks if the adviser exists. 

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
api_instance = swagger_client.AdvisersApi(swagger_client.ApiClient(configuration))
adviser_id = 56 # int | Adviser identifier.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Checks if the adviser exists. 
    api_instance.adviser_exists(adviser_id, authorization, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling AdvisersApi->adviser_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adviser_id** | **int**| Adviser identifier. | 
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

# **get_adviser**
> Adviser get_adviser(adviser_id, authorization, x_api_key, accept=accept)

Returns an adviser for a given adviser. 

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
api_instance = swagger_client.AdvisersApi(swagger_client.ApiClient(configuration))
adviser_id = 56 # int | Adviser identifier
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns an adviser for a given adviser. 
    api_response = api_instance.get_adviser(adviser_id, authorization, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvisersApi->get_adviser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adviser_id** | **int**| Adviser identifier | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Adviser**](Adviser.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_advisers**
> AdviserCollection list_advisers(authorization, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of advisers. 

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
api_instance = swagger_client.AdvisersApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | The list of Advisers returned can be filtered using one or more of the supported fields and operators.  The supported fields and operators are:    * `externalRef1` (`eq`)  * `externalRef2` (`eq`)  * `fcaRefNo` (`eq`)  * `group.id` (`eq`, `in`)  * `group.name` (`eq`, `startswith`)  * `id` (`eq`, `in`)  * `person.firstName` (`eq`, `startswith`)  * `person.lastName` (`eq`, `startswith`)  * `userId` (`eq`, `in`)                Example filters:      filter= person.firstName eq 'john' and person.lastName startswith 'j'      filter= id in (987,7654,126)        For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). (optional)
orderby = 'orderby_example' # str | The list of Advisers returned can be sorted on the following fields:    * `id` (`asc` or `desc`)  * `person.firstName` (`asc` or `desc`)  * `person.lastName` (`asc` or `desc`)  * `externalRef1` (`asc` or `desc`)  * `externalRef2` (`asc` or `desc`)                Example orderBy:      orderBy=person.lastname desc        By default the list of Advisers are ordered by Id in descending order. (optional)
skip = 0 # int | Optional. The number of records to skip. If not specified it defaults to 0. (optional) (default to 0)
top = 100 # int | Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. (optional) (default to 100)

try:
    # Returns a list of advisers. 
    api_response = api_instance.list_advisers(authorization, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvisersApi->list_advisers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| The list of Advisers returned can be filtered using one or more of the supported fields and operators.  The supported fields and operators are:    * &#x60;externalRef1&#x60; (&#x60;eq&#x60;)  * &#x60;externalRef2&#x60; (&#x60;eq&#x60;)  * &#x60;fcaRefNo&#x60; (&#x60;eq&#x60;)  * &#x60;group.id&#x60; (&#x60;eq&#x60;, &#x60;in&#x60;)  * &#x60;group.name&#x60; (&#x60;eq&#x60;, &#x60;startswith&#x60;)  * &#x60;id&#x60; (&#x60;eq&#x60;, &#x60;in&#x60;)  * &#x60;person.firstName&#x60; (&#x60;eq&#x60;, &#x60;startswith&#x60;)  * &#x60;person.lastName&#x60; (&#x60;eq&#x60;, &#x60;startswith&#x60;)  * &#x60;userId&#x60; (&#x60;eq&#x60;, &#x60;in&#x60;)                Example filters:      filter&#x3D; person.firstName eq &#x27;john&#x27; and person.lastName startswith &#x27;j&#x27;      filter&#x3D; id in (987,7654,126)        For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). | [optional] 
 **orderby** | **str**| The list of Advisers returned can be sorted on the following fields:    * &#x60;id&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;person.firstName&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;person.lastName&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;externalRef1&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;externalRef2&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)                Example orderBy:      orderBy&#x3D;person.lastname desc        By default the list of Advisers are ordered by Id in descending order. | [optional] 
 **skip** | **int**| Optional. The number of records to skip. If not specified it defaults to 0. | [optional] [default to 0]
 **top** | **int**| Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. | [optional] [default to 100]

### Return type

[**AdviserCollection**](AdviserCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

