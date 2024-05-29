# swagger_client.ExpendituresApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_expenditure**](ExpendituresApi.md#create_client_expenditure) | **POST** /clients/{clientId}/expenditures | Creates an expenditure record for a client.
[**delete_client_expenditure**](ExpendituresApi.md#delete_client_expenditure) | **DELETE** /clients/{clientId}/expenditures/{expenditureId} | Deletes a client&#x27;s expenditure record.
[**get_client_expenditure**](ExpendituresApi.md#get_client_expenditure) | **GET** /clients/{clientId}/expenditures/{expenditureId} | Retrieves a client&#x27;s expenditure record.
[**list_client_expenditures**](ExpendituresApi.md#list_client_expenditures) | **GET** /clients/{clientId}/expenditures | Returns a list of expenditure records for a client. The returned list may be filtered.
[**update_client_expenditure**](ExpendituresApi.md#update_client_expenditure) | **PUT** /clients/{clientId}/expenditures/{expenditureId} | Updates a client&#x27;s expenditure record.

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
api_instance = swagger_client.ExpendituresApi(swagger_client.ApiClient(configuration))
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
    print("Exception when calling ExpendituresApi->create_client_expenditure: %s\n" % e)
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
api_instance = swagger_client.ExpendituresApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client identifier. The special value \"me\" can be used to indicate the authenticated user.
expenditure_id = 56 # int | The identifier of the expenditure record.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes a client's expenditure record.
    api_instance.delete_client_expenditure(authorization, client_id, expenditure_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling ExpendituresApi->delete_client_expenditure: %s\n" % e)
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
api_instance = swagger_client.ExpendituresApi(swagger_client.ApiClient(configuration))
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
    print("Exception when calling ExpendituresApi->get_client_expenditure: %s\n" % e)
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
api_instance = swagger_client.ExpendituresApi(swagger_client.ApiClient(configuration))
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
    print("Exception when calling ExpendituresApi->list_client_expenditures: %s\n" % e)
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
api_instance = swagger_client.ExpendituresApi(swagger_client.ApiClient(configuration))
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
    print("Exception when calling ExpendituresApi->update_client_expenditure: %s\n" % e)
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

