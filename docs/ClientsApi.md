# swagger_client.ClientsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_exists**](ClientsApi.md#client_exists) | **HEAD** /clients/{clientId} | Checks the client exists. 
[**create_client**](ClientsApi.md#create_client) | **POST** /clients | Creates a client. 
[**delete_client**](ClientsApi.md#delete_client) | **DELETE** /clients/{clientId} | Deletes a given client. 
[**get_client**](ClientsApi.md#get_client) | **GET** /clients/{clientId} | Returns a clients for a given client. 
[**list_client_segments**](ClientsApi.md#list_client_segments) | **GET** /clients/client_segments | Retrieves a list of the available clients&#x27; segments.
[**list_clients**](ClientsApi.md#list_clients) | **GET** /clients | Returns a list of clients. 
[**update_client**](ClientsApi.md#update_client) | **PUT** /clients/{clientId} | Updates a client for a given client. 

# **client_exists**
> client_exists(authorization, client_id, x_api_key, accept=accept)

Checks the client exists. 

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
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.The special value \"me\" can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Checks the client exists. 
    api_instance.client_exists(authorization, client_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling ClientsApi->client_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier.The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
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

# **create_client**
> Client create_client(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)

Creates a client. 

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
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Client() # Client | Client document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Creates a client. 
    api_response = api_instance.create_client(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->create_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Client**](Client.md)| Client document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**Client**](Client.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client**
> delete_client(authorization, client_id, x_api_key, accept=accept, tenant_id=tenant_id)

Deletes a given client. 

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
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.The special value \"me\" can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Deletes a given client. 
    api_instance.delete_client(authorization, client_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling ClientsApi->delete_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier.The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client**
> Client get_client(authorization, client_id, x_api_key, accept=accept, tenant_id=tenant_id)

Returns a clients for a given client. 

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
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Returns a clients for a given client. 
    api_response = api_instance.get_client(authorization, client_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->get_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**Client**](Client.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_segments**
> ClientSegmentCollection list_client_segments(authorization, x_api_key, accept=accept, filter=filter)

Retrieves a list of the available clients' segments.

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
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | The list of client segments associated for a Client. These can be filtered using one or more of the supported fields and operators.  The supported fields and operators are:                * `isarchived` ('eq')                Example filters:      filter=isarchived eq true                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). (optional)

try:
    # Retrieves a list of the available clients' segments.
    api_response = api_instance.list_client_segments(authorization, x_api_key, accept=accept, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->list_client_segments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| The list of client segments associated for a Client. These can be filtered using one or more of the supported fields and operators.  The supported fields and operators are:                * &#x60;isarchived&#x60; (&#x27;eq&#x27;)                Example filters:      filter&#x3D;isarchived eq true                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). | [optional] 

### Return type

[**ClientSegmentCollection**](ClientSegmentCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clients**
> ClientCollection list_clients(authorization, x_api_key, accept=accept, filter=filter, skip=skip, top=top)

Returns a list of clients. 

Get a list of clients. Some specific filtering is optionally supported.  The following fields are supports for equals (`eq`): * `person.dateOfBirth`,  * `person.firstName`,  * `person.lastName`,  * `corporate.name`,  * `trust.name`,  * `currentAdviser.id`,  * `externalReference`,  * `secondaryReference`, * `person.niNumber`  The following fields are supports for `startswith`: * `person.firstName`,  * `person.lastName`,  * `corporate.name`,  * `trust.name`,  * `externalReference`,  * `secondaryReference`, * `person.niNumber`  The following fields are supported for `in`: * `id`, * `tag`, * `person.niNumber`, * `currentAdviser.id`,   *Examples:* `top=5&amp;Skip=22&amp;filter= person.firstName eq 'john' and person.lastName startswith 'j' and id in '(987,654,126) and tag in ('tag1', 'tag2', 'tag3')` 

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
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | The list of Clients returned can be filtered using one or more of the supported fields and operators.  The supported fields and operators are:    * `id` (`in`)  * `corporate.name` (`eq`, `startswith`)  * `currentAdviser.id` (`eq`, `in`)  * `group.id` (`eq`, `in`)  * `person.dateOfBirth` (`eq`)  * `person.firstName` (`eq`, `startswith`)  * `person.lastName` (`eq`, `startswith`)  * `person.niNumber` (`eq`, `startswith`, `in`)  * `externalReference` (`eq`, `startswith`)  * `secondaryReference` (`eq`, `startswith`)  * `trust.name` (`eq`, `startswith`)  * `tag` (`in`)                Example filters:      filter= person.firstName eq 'john' and person.lastName startswith 'j'      filter= id in (987,7654,126) and tag in ('tag1', 'tag2', 'tag3')      filter= person.dateOfBirth eq 1995-09-01                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). (optional)
skip = 0 # int | Optional. The number of records to skip. If not specified it defaults to 0. (optional) (default to 0)
top = 100 # int | Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. (optional) (default to 100)

try:
    # Returns a list of clients. 
    api_response = api_instance.list_clients(authorization, x_api_key, accept=accept, filter=filter, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->list_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| The list of Clients returned can be filtered using one or more of the supported fields and operators.  The supported fields and operators are:    * &#x60;id&#x60; (&#x60;in&#x60;)  * &#x60;corporate.name&#x60; (&#x60;eq&#x60;, &#x60;startswith&#x60;)  * &#x60;currentAdviser.id&#x60; (&#x60;eq&#x60;, &#x60;in&#x60;)  * &#x60;group.id&#x60; (&#x60;eq&#x60;, &#x60;in&#x60;)  * &#x60;person.dateOfBirth&#x60; (&#x60;eq&#x60;)  * &#x60;person.firstName&#x60; (&#x60;eq&#x60;, &#x60;startswith&#x60;)  * &#x60;person.lastName&#x60; (&#x60;eq&#x60;, &#x60;startswith&#x60;)  * &#x60;person.niNumber&#x60; (&#x60;eq&#x60;, &#x60;startswith&#x60;, &#x60;in&#x60;)  * &#x60;externalReference&#x60; (&#x60;eq&#x60;, &#x60;startswith&#x60;)  * &#x60;secondaryReference&#x60; (&#x60;eq&#x60;, &#x60;startswith&#x60;)  * &#x60;trust.name&#x60; (&#x60;eq&#x60;, &#x60;startswith&#x60;)  * &#x60;tag&#x60; (&#x60;in&#x60;)                Example filters:      filter&#x3D; person.firstName eq &#x27;john&#x27; and person.lastName startswith &#x27;j&#x27;      filter&#x3D; id in (987,7654,126) and tag in (&#x27;tag1&#x27;, &#x27;tag2&#x27;, &#x27;tag3&#x27;)      filter&#x3D; person.dateOfBirth eq 1995-09-01                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). | [optional] 
 **skip** | **int**| Optional. The number of records to skip. If not specified it defaults to 0. | [optional] [default to 0]
 **top** | **int**| Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. | [optional] [default to 100]

### Return type

[**ClientCollection**](ClientCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client**
> Client update_client(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)

Updates a client for a given client. 

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
api_instance = swagger_client.ClientsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Client() # Client | Client document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier. The special value \"me\" can be used to indicate the authenticated user.
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Updates a client for a given client. 
    api_response = api_instance.update_client(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->update_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Client**](Client.md)| Client document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**Client**](Client.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

