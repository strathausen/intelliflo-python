# swagger_client.StatusesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_plan_statuses**](StatusesApi.md#create_plan_statuses) | **POST** /clients/{clientId}/plans/{planId}/statuses | Creates status history for a given client and plan. 
[**get_plan_status**](StatusesApi.md#get_plan_status) | **GET** /clients/{clientId}/plans/{planId}/statuses/{planStatusId} | Retrieves a specific history record
[**list_client_plan_statuses**](StatusesApi.md#list_client_plan_statuses) | **GET** /clients/{clientId}/plans/{planId}/statuses | Returns a list of status histories for a given client and plan. 

# **create_plan_statuses**
> PlanStatus create_plan_statuses(body, authorization, x_api_key, client_id, plan_id, accept=accept, ignore_rules=ignore_rules, tenant_id=tenant_id)

Creates status history for a given client and plan. 

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
# Configure OAuth2 access token for authorization: oauth2-client-credentials
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StatusesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PlanStatus() # PlanStatus | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client Id - The special value \"me\" can be used to indicate the authenticated user.
plan_id = 56 # int | Plan Id
accept = 'accept_example' # str |  (optional)
ignore_rules = 'ALL' # str | Supported fields and operators:              ignoreRules=ALL (optional) (default to ALL)
tenant_id = 56 # int |  (optional)

try:
    # Creates status history for a given client and plan. 
    api_response = api_instance.create_plan_statuses(body, authorization, x_api_key, client_id, plan_id, accept=accept, ignore_rules=ignore_rules, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->create_plan_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlanStatus**](PlanStatus.md)|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client Id - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| Plan Id | 
 **accept** | **str**|  | [optional] 
 **ignore_rules** | **str**| Supported fields and operators:              ignoreRules&#x3D;ALL | [optional] [default to ALL]
 **tenant_id** | **int**|  | [optional] 

### Return type

[**PlanStatus**](PlanStatus.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-client-credentials](../README.md#oauth2-client-credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plan_status**
> PlanStatus get_plan_status(authorization, client_id, plan_id, plan_status_id, x_api_key, accept=accept, tenant_id=tenant_id)

Retrieves a specific history record

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
# Configure OAuth2 access token for authorization: oauth2-client-credentials
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StatusesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id
plan_id = 56 # int | Plan Id
plan_status_id = 56 # int | Unique id for the status change
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, optionally included (optional)

try:
    # Retrieves a specific history record
    api_response = api_instance.get_plan_status(authorization, client_id, plan_id, plan_status_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->get_plan_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id | 
 **plan_id** | **int**| Plan Id | 
 **plan_status_id** | **int**| Unique id for the status change | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, optionally included | [optional] 

### Return type

[**PlanStatus**](PlanStatus.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-client-credentials](../README.md#oauth2-client-credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_plan_statuses**
> PlanStatusCollection list_client_plan_statuses(authorization, client_id, plan_id, x_api_key, accept=accept, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of status histories for a given client and plan. 

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
# Configure OAuth2 access token for authorization: oauth2-client-credentials
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StatusesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id
plan_id = 56 # int | Plan Id
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
tenant_id = 56 # int | Tenant identifier, optionally included (optional)
top = 100 # int | The number of records to retrieve (default 25, max 100) (optional) (default to 100)

try:
    # Returns a list of status histories for a given client and plan. 
    api_response = api_instance.list_client_plan_statuses(authorization, client_id, plan_id, x_api_key, accept=accept, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->list_client_plan_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id | 
 **plan_id** | **int**| Plan Id | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **tenant_id** | **int**| Tenant identifier, optionally included | [optional] 
 **top** | **int**| The number of records to retrieve (default 25, max 100) | [optional] [default to 100]

### Return type

[**PlanStatusCollection**](PlanStatusCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-client-credentials](../README.md#oauth2-client-credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

