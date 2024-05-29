# swagger_client.DocumentfoldersApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document_folder**](DocumentfoldersApi.md#create_document_folder) | **POST** /clients/{clientId}/documentfolders | Creates a new document folder.
[**get_document_folder**](DocumentfoldersApi.md#get_document_folder) | **GET** /clients/{clientId}/documentfolders/{documentFolderId} | Gets a single document folder.
[**list_document_folders**](DocumentfoldersApi.md#list_document_folders) | **GET** /clients/{clientId}/documentfolders | Returns a list of document folders.

# **create_document_folder**
> DocumentFolder create_document_folder(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)

Creates a new document folder.

Allows an API consumer to create a new document folder.

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
api_instance = swagger_client.DocumentfoldersApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentFolder() # DocumentFolder | Document folder.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier.
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant (optional)

try:
    # Creates a new document folder.
    api_response = api_instance.create_document_folder(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentfoldersApi->create_document_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentFolder**](DocumentFolder.md)| Document folder. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant | [optional] 

### Return type

[**DocumentFolder**](DocumentFolder.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_folder**
> DocumentFolder get_document_folder(authorization, client_id, document_folder_id, x_api_key, accept=accept)

Gets a single document folder.

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
api_instance = swagger_client.DocumentfoldersApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
document_folder_id = 56 # int | Document folder identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Gets a single document folder.
    api_response = api_instance.get_document_folder(authorization, client_id, document_folder_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentfoldersApi->get_document_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **document_folder_id** | **int**| Document folder identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**DocumentFolder**](DocumentFolder.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_document_folders**
> DocumentFolderCollection list_document_folders(authorization, client_id, x_api_key, accept=accept, filter=filter, skip=skip, top=top)

Returns a list of document folders.

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
api_instance = swagger_client.DocumentfoldersApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | List can be filtered using one or more supported fields and operators below.  Supported fields (operators) are:                * `id` (`in`)  * `Name` (`startswith`,`eq`)                See [QueryLang](docs/ApiQueryLang) for further usage details. (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
top = 100 # int | The number of records to retrieve (default 100) (optional) (default to 100)

try:
    # Returns a list of document folders.
    api_response = api_instance.list_document_folders(authorization, client_id, x_api_key, accept=accept, filter=filter, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentfoldersApi->list_document_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| List can be filtered using one or more supported fields and operators below.  Supported fields (operators) are:                * &#x60;id&#x60; (&#x60;in&#x60;)  * &#x60;Name&#x60; (&#x60;startswith&#x60;,&#x60;eq&#x60;)                See [QueryLang](docs/ApiQueryLang) for further usage details. | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **top** | **int**| The number of records to retrieve (default 100) | [optional] [default to 100]

### Return type

[**DocumentFolderCollection**](DocumentFolderCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

