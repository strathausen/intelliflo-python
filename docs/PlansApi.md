# swagger_client.PlansApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_opportunity_plan**](PlansApi.md#create_client_opportunity_plan) | **POST** /clients/{clientId}/opportunities/{opportunityId}/plans/{planId} | Updates an opportunity with a plan for a given client, opportunity and plan. 
[**create_client_plans**](PlansApi.md#create_client_plans) | **POST** /clients/{clientId}/plans | Creates a plan for a given client. 
[**create_client_servicecase_plan**](PlansApi.md#create_client_servicecase_plan) | **POST** /clients/{clientId}/servicecases/{serviceCaseId}/plans/{planId} | Creates an association with a service on a plan for a given client, service and plan. 
[**create_topup_plan**](PlansApi.md#create_topup_plan) | **POST** /clients/{clientId}/plans/{planId} | Creates a plan for a given client. 
[**delete_client_opportunity_plan**](PlansApi.md#delete_client_opportunity_plan) | **DELETE** /clients/{clientId}/opportunities/{opportunityId}/plans/{planId} | Deletes an opportunity from a plan for a given client, opportunity and plan. 
[**delete_client_plan**](PlansApi.md#delete_client_plan) | **DELETE** /clients/{clientId}/plans/{planId} | Deletes the client plan by the given client id and plan id.
[**delete_client_servicecase_plan**](PlansApi.md#delete_client_servicecase_plan) | **DELETE** /clients/{clientId}/servicecases/{serviceCaseId}/plans/{planId} | Deletes an association on a service with a plan for a given client, service and plan. 
[**exists_client_plan**](PlansApi.md#exists_client_plan) | **HEAD** /clients/{clientId}/plans/{planId} | Checks a plan exists for a given client and plan. 
[**get_client_plan**](PlansApi.md#get_client_plan) | **GET** /clients/{clientId}/plans/{planId} | Returns a plan for a given client and plan. 
[**get_plan**](PlansApi.md#get_plan) | **GET** /plans/{planId} | Get a Plan
[**list_client_plans**](PlansApi.md#list_client_plans) | **GET** /clients/{clientId}/plans | Returns a list of plans for a given client. 
[**patch_client_plan**](PlansApi.md#patch_client_plan) | **PATCH** /clients/{clientId}/plans/{planId} | Patch update a client plan for given client id and plan id.
[**plan_exists**](PlansApi.md#plan_exists) | **HEAD** /plans/{planId} | Check that plan available for the user
[**update_client_plan**](PlansApi.md#update_client_plan) | **PUT** /clients/{clientId}/plans/{planId} | Updates a plan for a given client. 

# **create_client_opportunity_plan**
> create_client_opportunity_plan(authorization, client_id, opportunity_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)

Updates an opportunity with a plan for a given client, opportunity and plan. 

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
api_instance = swagger_client.PlansApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
opportunity_id = 56 # int | Opportunity identifier
plan_id = 56 # int | Plan identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Updates an opportunity with a plan for a given client, opportunity and plan. 
    api_instance.create_client_opportunity_plan(authorization, client_id, opportunity_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling PlansApi->create_client_opportunity_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **opportunity_id** | **int**| Opportunity identifier | 
 **plan_id** | **int**| Plan identifier | 
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

# **create_client_plans**
> BasePlan create_client_plans(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)

Creates a plan for a given client. 

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
api_instance = swagger_client.PlansApi(swagger_client.ApiClient(configuration))
body = swagger_client.BasePlan() # BasePlan | Plan
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client Id - The special value \"me\" can be used to indicate the authenticated user.
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Creates a plan for a given client. 
    api_response = api_instance.create_client_plans(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->create_client_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BasePlan**](BasePlan.md)| Plan | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client Id - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

[**BasePlan**](BasePlan.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_servicecase_plan**
> create_client_servicecase_plan(authorization, client_id, plan_id, service_case_id, x_api_key, accept=accept, tenant_id=tenant_id)

Creates an association with a service on a plan for a given client, service and plan. 

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
api_instance = swagger_client.PlansApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
plan_id = 56 # int | Plan identifier
service_case_id = 56 # int | Service Case identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Creates an association with a service on a plan for a given client, service and plan. 
    api_instance.create_client_servicecase_plan(authorization, client_id, plan_id, service_case_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling PlansApi->create_client_servicecase_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **plan_id** | **int**| Plan identifier | 
 **service_case_id** | **int**| Service Case identifier | 
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

# **create_topup_plan**
> BasePlan create_topup_plan(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)

Creates a plan for a given client. 

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
api_instance = swagger_client.PlansApi(swagger_client.ApiClient(configuration))
body = swagger_client.BasePlan() # BasePlan | Plan
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client Id - The special value \"me\" can be used to indicate the authenticated user.
plan_id = 56 # int | PlanId
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Creates a plan for a given client. 
    api_response = api_instance.create_topup_plan(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->create_topup_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BasePlan**](BasePlan.md)| Plan | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client Id - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| PlanId | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

[**BasePlan**](BasePlan.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_opportunity_plan**
> delete_client_opportunity_plan(authorization, client_id, opportunity_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)

Deletes an opportunity from a plan for a given client, opportunity and plan. 

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
api_instance = swagger_client.PlansApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
opportunity_id = 56 # int | Opportunity identifier
plan_id = 56 # int | Plan identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Deletes an opportunity from a plan for a given client, opportunity and plan. 
    api_instance.delete_client_opportunity_plan(authorization, client_id, opportunity_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling PlansApi->delete_client_opportunity_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **opportunity_id** | **int**| Opportunity identifier | 
 **plan_id** | **int**| Plan identifier | 
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

# **delete_client_plan**
> delete_client_plan(authorization, client_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)

Deletes the client plan by the given client id and plan id.

This operation performs a soft deletion of a clients plan. Only the user that created the plan is allowed to delete it, i.e. if the plan was created  by an adviser within IO it can't be deleted by an app unless the app identifies itself as the adviser who created the plan (authorization code flow).

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
api_instance = swagger_client.PlansApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id - The special value \"me\" can be used to indicate the authenticated user.
plan_id = 56 # int | The plan identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | The tenant identifier. (optional)

try:
    # Deletes the client plan by the given client id and plan id.
    api_instance.delete_client_plan(authorization, client_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling PlansApi->delete_client_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| The plan identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| The tenant identifier. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_servicecase_plan**
> delete_client_servicecase_plan(authorization, client_id, plan_id, service_case_id, x_api_key, accept=accept, tenant_id=tenant_id)

Deletes an association on a service with a plan for a given client, service and plan. 

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
api_instance = swagger_client.PlansApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
plan_id = 56 # int | Plan identifier
service_case_id = 56 # int | Service case identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Deletes an association on a service with a plan for a given client, service and plan. 
    api_instance.delete_client_servicecase_plan(authorization, client_id, plan_id, service_case_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling PlansApi->delete_client_servicecase_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **plan_id** | **int**| Plan identifier | 
 **service_case_id** | **int**| Service case identifier | 
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

# **exists_client_plan**
> exists_client_plan(authorization, client_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)

Checks a plan exists for a given client and plan. 

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
api_instance = swagger_client.PlansApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id - The special value \"me\" can be used to indicate the authenticated user.
plan_id = 56 # int | Plan Id
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Checks a plan exists for a given client and plan. 
    api_instance.exists_client_plan(authorization, client_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling PlansApi->exists_client_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| Plan Id | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_plan**
> BasePlan get_client_plan(authorization, client_id, plan_id, x_api_key, accept=accept, prefer=prefer, tenant_id=tenant_id)

Returns a plan for a given client and plan. 

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
api_instance = swagger_client.PlansApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id - The special value \"me\" can be used to indicate the authenticated user.
plan_id = 56 # int | Plan Id
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
prefer = 'prefer_example' # str | Used to indicate preferred behaviours, by the client. Options: include=fundProposal (optional)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Returns a plan for a given client and plan. 
    api_response = api_instance.get_client_plan(authorization, client_id, plan_id, x_api_key, accept=accept, prefer=prefer, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->get_client_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| Plan Id | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **prefer** | **str**| Used to indicate preferred behaviours, by the client. Options: include&#x3D;fundProposal | [optional] 
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

[**BasePlan**](BasePlan.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plan**
> BasePlan get_plan(authorization, plan_id, x_api_key, accept=accept, permission_type=permission_type, prefer=prefer, tenant_id=tenant_id)

Get a Plan

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
api_instance = swagger_client.PlansApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
plan_id = 56 # int | Plan Id
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
permission_type = 'ReadWrite' # str | Permission type: Read or ReadWrite              * `When read, it will return all plans that the client can read (IncludeInPfp). When readwrite, it will return only plans that the client can modify(owner)` (optional) (default to ReadWrite)
prefer = 'prefer_example' # str | Used to indicate preferred behaviours, by the client. Options: include=fundProposal (optional)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Get a Plan
    api_response = api_instance.get_plan(authorization, plan_id, x_api_key, accept=accept, permission_type=permission_type, prefer=prefer, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->get_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **plan_id** | **int**| Plan Id | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **permission_type** | **str**| Permission type: Read or ReadWrite              * &#x60;When read, it will return all plans that the client can read (IncludeInPfp). When readwrite, it will return only plans that the client can modify(owner)&#x60; | [optional] [default to ReadWrite]
 **prefer** | **str**| Used to indicate preferred behaviours, by the client. Options: include&#x3D;fundProposal | [optional] 
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

[**BasePlan**](BasePlan.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_plans**
> PlanCollection list_client_plans(authorization, client_id, x_api_key, accept=accept, filter=filter, prefer=prefer, skip=skip, tenant_id=tenant_id, top=top, type_of=type_of)

Returns a list of plans for a given client. 

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
api_instance = swagger_client.PlansApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id - The special value \"me\" can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | List can be filtered using one or more supported fields and operators below.                Supported fields (operators) are:  * `Id` (`in`)  * `ProductProvider.Id` (`in`,`eq`,`ne`)  * `ProductProvider.Name` (`in`,`eq`,`ne`,`startswith`)  * `PlanType.Name` (`in`,`eq`,`ne`)  * `PlanType.PortfolioCategory` (`in`,`eq`) `valid values are: [investments, currentaccounts, savings, pensions, property, protection, creditcards, mortgages, loans]`  * `CurrentStatus` (`in`,`eq`,`ne`)  * `SystemStatus` (`in`,`ne`)  * `QuoteResult.Id` (`in`,`eq`,`ne`)  * `Parent.Id` (`in`,`eq`)  * `tags` (`startswith`,`in`,`eq`)  * `IsProviderManaged` (`eq`)  * `ProviderCodes.Code1` (`in`, `eq`)  * `ProviderCodes.Code2` (`in`, `eq`)  * `ProviderCodes.Code3` (`in`, `eq`)  * `CratedAt` (`gt`, `lt`)  * `Program.Id` (`in`,`eq`)                Usage examples:  * `filter=id in (1,2)`  * `filter=currentstatus eq 'in force'`  * `filter=tag eq 'tagName'  * `filter=tag in ('tag1', 'tag2')  * `filter=tag startswith 'tagName'  * `filter=createdAt gt yyyy-MM-dd`  * `filter=createdAt lt yyyy-MM-dd`                See [QueryLang](docs/ApiQueryLang) for further usage details. (optional)
prefer = 'prefer_example' # str | Used to indicate preferred behaviours, by the client. Options: include=fundProposal (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
tenant_id = 56 # int | Tenant Id (optional)
top = 100 # int | The number of records to retrieve (default 25, max 100) (optional) (default to 100)
type_of = 'type_of_example' # str | Filters by discriminator (abstract or concrete), e.g 'AssetPlan', will return plans that inherit from AssetPlan. (optional)

try:
    # Returns a list of plans for a given client. 
    api_response = api_instance.list_client_plans(authorization, client_id, x_api_key, accept=accept, filter=filter, prefer=prefer, skip=skip, tenant_id=tenant_id, top=top, type_of=type_of)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->list_client_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| List can be filtered using one or more supported fields and operators below.                Supported fields (operators) are:  * &#x60;Id&#x60; (&#x60;in&#x60;)  * &#x60;ProductProvider.Id&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;)  * &#x60;ProductProvider.Name&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;,&#x60;startswith&#x60;)  * &#x60;PlanType.Name&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;)  * &#x60;PlanType.PortfolioCategory&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;) &#x60;valid values are: [investments, currentaccounts, savings, pensions, property, protection, creditcards, mortgages, loans]&#x60;  * &#x60;CurrentStatus&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;)  * &#x60;SystemStatus&#x60; (&#x60;in&#x60;,&#x60;ne&#x60;)  * &#x60;QuoteResult.Id&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;)  * &#x60;Parent.Id&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;)  * &#x60;tags&#x60; (&#x60;startswith&#x60;,&#x60;in&#x60;,&#x60;eq&#x60;)  * &#x60;IsProviderManaged&#x60; (&#x60;eq&#x60;)  * &#x60;ProviderCodes.Code1&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;)  * &#x60;ProviderCodes.Code2&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;)  * &#x60;ProviderCodes.Code3&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;)  * &#x60;CratedAt&#x60; (&#x60;gt&#x60;, &#x60;lt&#x60;)  * &#x60;Program.Id&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;)                Usage examples:  * &#x60;filter&#x3D;id in (1,2)&#x60;  * &#x60;filter&#x3D;currentstatus eq &#x27;in force&#x27;&#x60;  * &#x60;filter&#x3D;tag eq &#x27;tagName&#x27;  * &#x60;filter&#x3D;tag in (&#x27;tag1&#x27;, &#x27;tag2&#x27;)  * &#x60;filter&#x3D;tag startswith &#x27;tagName&#x27;  * &#x60;filter&#x3D;createdAt gt yyyy-MM-dd&#x60;  * &#x60;filter&#x3D;createdAt lt yyyy-MM-dd&#x60;                See [QueryLang](docs/ApiQueryLang) for further usage details. | [optional] 
 **prefer** | **str**| Used to indicate preferred behaviours, by the client. Options: include&#x3D;fundProposal | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **tenant_id** | **int**| Tenant Id | [optional] 
 **top** | **int**| The number of records to retrieve (default 25, max 100) | [optional] [default to 100]
 **type_of** | **str**| Filters by discriminator (abstract or concrete), e.g &#x27;AssetPlan&#x27;, will return plans that inherit from AssetPlan. | [optional] 

### Return type

[**PlanCollection**](PlanCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_client_plan**
> BasePlan patch_client_plan(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)

Patch update a client plan for given client id and plan id.

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
api_instance = swagger_client.PlansApi(swagger_client.ApiClient(configuration))
body = [swagger_client.Operation()] # list[Operation] | A Json Patch document containing details of modifications to be made to the client plan resource.
Properties which cannot be updated on PUT, cannot be updated using patch
            
For a simple example a request contains the following JSON:
            
[{
    "op": "replace",
    "path": "/policyNumber",
    "value": "new policy number"
},
{
    "op": "add",
    "path": "/tags/-",
    "value": "tag2"
},
{
    "op": "remove",
    "path": "/parent"
}]
            
This would result in the following updates to the plan:
            
* The value of the policyNumber property would be updated to 'new policy number' text.
* A new tag 'tag2' would be added to the existing list of tags.
* The value of the parent property would be removed.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | The client identifier.
plan_id = 56 # int | The plan identifier.
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Patch update a client plan for given client id and plan id.
    api_response = api_instance.patch_client_plan(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->patch_client_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Operation]**](Operation.md)| A Json Patch document containing details of modifications to be made to the client plan resource.
Properties which cannot be updated on PUT, cannot be updated using patch
            
For a simple example a request contains the following JSON:
            
[{
    &quot;op&quot;: &quot;replace&quot;,
    &quot;path&quot;: &quot;/policyNumber&quot;,
    &quot;value&quot;: &quot;new policy number&quot;
},
{
    &quot;op&quot;: &quot;add&quot;,
    &quot;path&quot;: &quot;/tags/-&quot;,
    &quot;value&quot;: &quot;tag2&quot;
},
{
    &quot;op&quot;: &quot;remove&quot;,
    &quot;path&quot;: &quot;/parent&quot;
}]
            
This would result in the following updates to the plan:
            
* The value of the policyNumber property would be updated to &#x27;new policy number&#x27; text.
* A new tag &#x27;tag2&#x27; would be added to the existing list of tags.
* The value of the parent property would be removed. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| The client identifier. | 
 **plan_id** | **int**| The plan identifier. | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

[**BasePlan**](BasePlan.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plan_exists**
> plan_exists(authorization, plan_id, x_api_key, accept=accept, permission_type=permission_type, tenant_id=tenant_id)

Check that plan available for the user

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
api_instance = swagger_client.PlansApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
plan_id = 56 # int | Plan Id
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
permission_type = 'ReadWrite' # str | Permission Type (optional) (default to ReadWrite)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Check that plan available for the user
    api_instance.plan_exists(authorization, plan_id, x_api_key, accept=accept, permission_type=permission_type, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling PlansApi->plan_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **plan_id** | **int**| Plan Id | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **permission_type** | **str**| Permission Type | [optional] [default to ReadWrite]
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_plan**
> BasePlan update_client_plan(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)

Updates a plan for a given client. 

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
api_instance = swagger_client.PlansApi(swagger_client.ApiClient(configuration))
body = swagger_client.BasePlan() # BasePlan | Plan
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client Id - The special value \"me\" can be used to indicate the authenticated user.
plan_id = 56 # int | PlanId
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Updates a plan for a given client. 
    api_response = api_instance.update_client_plan(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlansApi->update_client_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BasePlan**](BasePlan.md)| Plan | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client Id - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| PlanId | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

[**BasePlan**](BasePlan.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

