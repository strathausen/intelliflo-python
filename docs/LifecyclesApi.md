# swagger_client.LifecyclesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lifecycle**](LifecyclesApi.md#get_lifecycle) | **GET** /lifecycles/{lifecycleId} | Returns a lifecycle.
[**list_lifecycle_statuses**](LifecyclesApi.md#list_lifecycle_statuses) | **GET** /lifecycles/statuses | Returns a list of available lifecycle statuses
[**list_lifecycle_transitions**](LifecyclesApi.md#list_lifecycle_transitions) | **GET** /lifecycles/{lifecycleId}/transitions | Returns a list of transitions for a given lifecycle.
[**list_lifecycles**](LifecyclesApi.md#list_lifecycles) | **GET** /lifecycles | Returns a list of lifecycles.
[**list_plantype_lifecycles**](LifecyclesApi.md#list_plantype_lifecycles) | **GET** /plantypes/{name}/lifecycles | Retrieves a list of lifecycles associated with the specified planType

# **get_lifecycle**
> Lifecycle get_lifecycle(authorization, lifecycle_id, x_api_key, accept=accept)

Returns a lifecycle.

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
api_instance = swagger_client.LifecyclesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
lifecycle_id = 56 # int | Lifecycle identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a lifecycle.
    api_response = api_instance.get_lifecycle(authorization, lifecycle_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->get_lifecycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **lifecycle_id** | **int**| Lifecycle identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Lifecycle**](Lifecycle.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lifecycle_statuses**
> LifecycleStatusCollection list_lifecycle_statuses(authorization, x_api_key, accept=accept, filter=filter, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of available lifecycle statuses

This endpoint allows an API user to identify the plan statuses used by a tenant.  The `filter` parameter allows the results to be filtered.  Please see the parameters for more details.  Be aware that this API will only allow a maximum resulting page size of 500.

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
api_instance = swagger_client.LifecyclesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | QueryLang filter.                             Properties and operators supported:                             * `Name` ( in, eq, ne, startsWith )               * `SystemName` ( in, eq, ne, startsWith )                             See [QueryLang](docs/ApiQueryLang) for further usage details (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
tenant_id = 56 # int | Tenant identifier (optional)
top = 100 # int | The number of records to retrieve (default 25, max 100) (optional) (default to 100)

try:
    # Returns a list of available lifecycle statuses
    api_response = api_instance.list_lifecycle_statuses(authorization, x_api_key, accept=accept, filter=filter, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->list_lifecycle_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| QueryLang filter.                             Properties and operators supported:                             * &#x60;Name&#x60; ( in, eq, ne, startsWith )               * &#x60;SystemName&#x60; ( in, eq, ne, startsWith )                             See [QueryLang](docs/ApiQueryLang) for further usage details | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **tenant_id** | **int**| Tenant identifier | [optional] 
 **top** | **int**| The number of records to retrieve (default 25, max 100) | [optional] [default to 100]

### Return type

[**LifecycleStatusCollection**](LifecycleStatusCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lifecycle_transitions**
> LifecycleTransitionValueCollection list_lifecycle_transitions(authorization, lifecycle_id, x_api_key, accept=accept, filter=filter)

Returns a list of transitions for a given lifecycle.

This endpoint provides the ability to identify the valid transitions of a plan from one state to another.  These state transition rules are set per tenant.  Calling this API is a necessary pre-requisite before attempting to set the status of a plan.  The `filter` parameter allows the results to be filtered.  Please see the parameters for more details.

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
api_instance = swagger_client.LifecyclesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
lifecycle_id = 56 # int | Lifecycle identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Used to filter transitions.                             Properties and operators supported:                             * `state` (`eq`, `in`, `ne`)                             Examples:                             * `filter=state eq 'In force'`               * `filter=state in ('Submitted to Provider', 'In force')`               * `filter=state ne 'Submitted to Provider'` (optional)

try:
    # Returns a list of transitions for a given lifecycle.
    api_response = api_instance.list_lifecycle_transitions(authorization, lifecycle_id, x_api_key, accept=accept, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->list_lifecycle_transitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **lifecycle_id** | **int**| Lifecycle identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Used to filter transitions.                             Properties and operators supported:                             * &#x60;state&#x60; (&#x60;eq&#x60;, &#x60;in&#x60;, &#x60;ne&#x60;)                             Examples:                             * &#x60;filter&#x3D;state eq &#x27;In force&#x27;&#x60;               * &#x60;filter&#x3D;state in (&#x27;Submitted to Provider&#x27;, &#x27;In force&#x27;)&#x60;               * &#x60;filter&#x3D;state ne &#x27;Submitted to Provider&#x27;&#x60; | [optional] 

### Return type

[**LifecycleTransitionValueCollection**](LifecycleTransitionValueCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lifecycles**
> LifecycleDocumentCollection list_lifecycles(authorization, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, top=top)

Returns a list of lifecycles.

This endpoint provides the ability to identify the plan lifecycles that have been set for a tenant.  The `filter` parameter allows the results to be filtered.  Please see the parameters for more details.  Be aware that this API will only allow a maximum resulting page size of 500.

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
api_instance = swagger_client.LifecyclesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported fields and operators:              id (in): e.g. filter=id in (1, 3),              name (eq, startswith): e.g. filter=name eq 'Pre-Existing' and name startswith 'Pre%' (optional)
order_by = 'order_by_example' # str | Supported fields: id, name. Supported directions: asc, desc: orderBy=name desc (optional)
skip = 0 # int | Number of records to skip: skip=1 (optional) (default to 0)
top = 100 # int | Number of records to get: top=11 (optional) (default to 100)

try:
    # Returns a list of lifecycles.
    api_response = api_instance.list_lifecycles(authorization, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->list_lifecycles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported fields and operators:              id (in): e.g. filter&#x3D;id in (1, 3),              name (eq, startswith): e.g. filter&#x3D;name eq &#x27;Pre-Existing&#x27; and name startswith &#x27;Pre%&#x27; | [optional] 
 **order_by** | **str**| Supported fields: id, name. Supported directions: asc, desc: orderBy&#x3D;name desc | [optional] 
 **skip** | **int**| Number of records to skip: skip&#x3D;1 | [optional] [default to 0]
 **top** | **int**| Number of records to get: top&#x3D;11 | [optional] [default to 100]

### Return type

[**LifecycleDocumentCollection**](LifecycleDocumentCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_plantype_lifecycles**
> LifecycleDocumentCollection list_plantype_lifecycles(authorization, name, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, top=top)

Retrieves a list of lifecycles associated with the specified planType

A lifecycle represents the many stages that a plan can pass through.  The `filter` parameter allows the results to be filtered.  Please see the parameters for more details.  Be aware that this API will only allow a maximum resulting page size of 500.

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
api_instance = swagger_client.LifecyclesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
name = 'name_example' # str | Plan type name
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported fields and operators:              id (in): e.g. filter=id in (1, 3)              name (eq, startswith): e.g. filter=name eq 'Pre-Existing' and name startswith 'Pre' (optional)
order_by = 'order_by_example' # str | Supported fields: id, name. Supported directions: asc, desc: orderBy=name desc (optional)
skip = 0 # int | Number of records to skip: skip=1 (optional) (default to 0)
top = 100 # int | Number of records to get: top=11 (optional) (default to 100)

try:
    # Retrieves a list of lifecycles associated with the specified planType
    api_response = api_instance.list_plantype_lifecycles(authorization, name, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LifecyclesApi->list_plantype_lifecycles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **name** | **str**| Plan type name | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported fields and operators:              id (in): e.g. filter&#x3D;id in (1, 3)              name (eq, startswith): e.g. filter&#x3D;name eq &#x27;Pre-Existing&#x27; and name startswith &#x27;Pre&#x27; | [optional] 
 **order_by** | **str**| Supported fields: id, name. Supported directions: asc, desc: orderBy&#x3D;name desc | [optional] 
 **skip** | **int**| Number of records to skip: skip&#x3D;1 | [optional] [default to 0]
 **top** | **int**| Number of records to get: top&#x3D;11 | [optional] [default to 100]

### Return type

[**LifecycleDocumentCollection**](LifecycleDocumentCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

