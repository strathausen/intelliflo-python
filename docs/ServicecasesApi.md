# swagger_client.ServicecasesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_servicecases**](ServicecasesApi.md#create_client_servicecases) | **POST** /clients/{clientId}/servicecases | Creates a service case for a given client. 
[**get_client_servicecase**](ServicecasesApi.md#get_client_servicecase) | **GET** /clients/{clientId}/servicecases/{serviceCaseId} | Returns a service case for a given client and service case. 
[**list_client_servicecases**](ServicecasesApi.md#list_client_servicecases) | **GET** /clients/{clientId}/servicecases | Returns a list of service cases for a given client. 
[**update_client_servicecase**](ServicecasesApi.md#update_client_servicecase) | **PUT** /clients/{clientId}/servicecases/{serviceCaseId} | Updates a service case for a given client and service case. 

# **create_client_servicecases**
> ServiceCase create_client_servicecases(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)

Creates a service case for a given client. 

Allows an API consumer to create a new service case.

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
api_instance = swagger_client.ServicecasesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceCase() # ServiceCase | Service case document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Creates a service case for a given client. 
    api_response = api_instance.create_client_servicecases(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicecasesApi->create_client_servicecases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceCase**](ServiceCase.md)| Service case document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**ServiceCase**](ServiceCase.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_servicecase**
> ServiceCase get_client_servicecase(authorization, client_id, service_case_id, x_api_key, accept=accept)

Returns a service case for a given client and service case. 

Allows an API consumer to get a service case by Id.

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
api_instance = swagger_client.ServicecasesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
service_case_id = 56 # int | ServiceCase identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a service case for a given client and service case. 
    api_response = api_instance.get_client_servicecase(authorization, client_id, service_case_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicecasesApi->get_client_servicecase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **service_case_id** | **int**| ServiceCase identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**ServiceCase**](ServiceCase.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_servicecases**
> ServiceCaseCollection list_client_servicecases(authorization, client_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of service cases for a given client. 

Allows an API consumer to get all service cases.

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
api_instance = swagger_client.ServicecasesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | List can be filtered using one or more supported fields and operators below.  Supported fields (operators) are:  * `client.id` (`eq`, `in`)  * `jointclient.id` (`eq`,`in`) e.g. ?filter= jointclient.id in (1,555666913,111)  * `documentBinder.id` (`eq`, `in`) e.g. ?filter= documentBinder.id eq 1  * `startedAt` (`eq`)  * `adviser.id` (`eq`, `in')  * `documentBinder.name` (`startswith`)  * `status` (`startswith`)  * `adviser.name` (`startswith`)  * `description` (`startswith`) e.g. ?filter= description startswith 'Equity Release'  * `id` (`eq`, `in`)  * `plan.id` (`eq`, `in`)  * `isCompleted` (`eq`)    See [QueryLang](docs/ApiQueryLang) for further usage details. (optional)
orderby = 'orderby_example' # str | Supported Sort Properties:  * `reference` (`asc` or `desc`)  * `description` (`asc` or `desc`)  * `isJoint` (`asc` or `desc`)  * `status` (`asc` or `desc`)  * `adviser.name` (`asc` or `desc`)  * `documentBinder.name` (`asc` or `desc`)  * `id` (`asc` or `desc`)  Default `reference` `desc`. (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
top = 100 # int | The number of records to retrieve (default 25, max 100) (optional) (default to 100)

try:
    # Returns a list of service cases for a given client. 
    api_response = api_instance.list_client_servicecases(authorization, client_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicecasesApi->list_client_servicecases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| List can be filtered using one or more supported fields and operators below.  Supported fields (operators) are:  * &#x60;client.id&#x60; (&#x60;eq&#x60;, &#x60;in&#x60;)  * &#x60;jointclient.id&#x60; (&#x60;eq&#x60;,&#x60;in&#x60;) e.g. ?filter&#x3D; jointclient.id in (1,555666913,111)  * &#x60;documentBinder.id&#x60; (&#x60;eq&#x60;, &#x60;in&#x60;) e.g. ?filter&#x3D; documentBinder.id eq 1  * &#x60;startedAt&#x60; (&#x60;eq&#x60;)  * &#x60;adviser.id&#x60; (&#x60;eq&#x60;, &#x60;in&#x27;)  * &#x60;documentBinder.name&#x60; (&#x60;startswith&#x60;)  * &#x60;status&#x60; (&#x60;startswith&#x60;)  * &#x60;adviser.name&#x60; (&#x60;startswith&#x60;)  * &#x60;description&#x60; (&#x60;startswith&#x60;) e.g. ?filter&#x3D; description startswith &#x27;Equity Release&#x27;  * &#x60;id&#x60; (&#x60;eq&#x60;, &#x60;in&#x60;)  * &#x60;plan.id&#x60; (&#x60;eq&#x60;, &#x60;in&#x60;)  * &#x60;isCompleted&#x60; (&#x60;eq&#x60;)    See [QueryLang](docs/ApiQueryLang) for further usage details. | [optional] 
 **orderby** | **str**| Supported Sort Properties:  * &#x60;reference&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;description&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;isJoint&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;status&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;adviser.name&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;documentBinder.name&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;id&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  Default &#x60;reference&#x60; &#x60;desc&#x60;. | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **top** | **int**| The number of records to retrieve (default 25, max 100) | [optional] [default to 100]

### Return type

[**ServiceCaseCollection**](ServiceCaseCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_servicecase**
> ServiceCase update_client_servicecase(body, authorization, x_api_key, client_id, service_case_id, accept=accept, tenant_id=tenant_id)

Updates a service case for a given client and service case. 

Allows an API consumer to update a given service case.

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
api_instance = swagger_client.ServicecasesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceCase() # ServiceCase | Service case document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier
service_case_id = 56 # int | Service case id
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Updates a service case for a given client and service case. 
    api_response = api_instance.update_client_servicecase(body, authorization, x_api_key, client_id, service_case_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicecasesApi->update_client_servicecase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceCase**](ServiceCase.md)| Service case document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **service_case_id** | **int**| Service case id | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**ServiceCase**](ServiceCase.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

