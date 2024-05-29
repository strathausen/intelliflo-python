# swagger_client.LivesassuredApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_client_plans_lives_assured**](LivesassuredApi.md#list_client_plans_lives_assured) | **GET** /clients/{clientId}/plans/{planId}/livesassured | Returns a list of Lives Assured for the plan.
[**update_client_plans_lives_assured**](LivesassuredApi.md#update_client_plans_lives_assured) | **PUT** /clients/{clientId}/plans/{planId}/livesassured | Creates or updates the list of Lives Assured for the plan. A maximum of 6 lives assured can be added.

# **list_client_plans_lives_assured**
> LifeAssuredCollection list_client_plans_lives_assured(authorization, client_id, plan_id, x_api_key, accept=accept, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of Lives Assured for the plan.

Returns a list of Lives Assured for the plan.  'Life assured' refers to the client or person whose life has been covered by a life assurance policy.  Each life assured can either be a reference to an existing iO client, or details of a separate person (including first name, last name and date of birth).  ###### **Notes**  * The life assured `type` can be `Client` or `Other`.  * For a `type` of `Client`, the resource will contain the `id` and a read-only `href` for the client.  * For a `type` of `Other`, the resource can contain the `title`, `firstName`, `lastName`, `dateOfBirth`, and `gender` of the person.  * `permanentTotalDisabilityCover` can be returned for both types.

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
api_instance = swagger_client.LivesassuredApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id
plan_id = 56 # int | Plan Id
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int | Number of records to skip (optional) (default to 0)
tenant_id = 56 # int | Tenant Id (optional)
top = 100 # int | Number of records to retrieve (optional) (default to 100)

try:
    # Returns a list of Lives Assured for the plan.
    api_response = api_instance.list_client_plans_lives_assured(authorization, client_id, plan_id, x_api_key, accept=accept, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LivesassuredApi->list_client_plans_lives_assured: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id | 
 **plan_id** | **int**| Plan Id | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**| Number of records to skip | [optional] [default to 0]
 **tenant_id** | **int**| Tenant Id | [optional] 
 **top** | **int**| Number of records to retrieve | [optional] [default to 100]

### Return type

[**LifeAssuredCollection**](LifeAssuredCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_plans_lives_assured**
> LifeAssuredCollection update_client_plans_lives_assured(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)

Creates or updates the list of Lives Assured for the plan. A maximum of 6 lives assured can be added.

Creates or updates the list of Lives Assured for the plan.  'Life assured' refers to the client or person whose life has been covered by a life assurance policy.  A maximum of 6 lives assured can be added.  Each life assured can either be a reference to an existing iO client, or details of a separate person (including first name, last name and date of birth).  ###### **Notes**  * The life assured `type` is required and can be `Client` or `Other`.  * For a `type` of `Client`:    * `id` (for the client) is required.    * `permanentTotalDisabilityCover` may be included.    * Any other fields e.g. `firstName` will be ignored.    * `href` is read-only.  * For a `type` of `Other`:    * `firstName`, `lastName` and `dateOfBirth` are required.    * `permanentTotalDisabilityCover`, `title` and `gender` may be included.    * `id`, if included, will be ignored.

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
api_instance = swagger_client.LivesassuredApi(swagger_client.ApiClient(configuration))
body = swagger_client.LifeAssuredCollection() # LifeAssuredCollection | List of Lives Assured. A maximum of 6 lives assured can be added.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client Id
plan_id = 56 # int | Plan Id
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Creates or updates the list of Lives Assured for the plan. A maximum of 6 lives assured can be added.
    api_response = api_instance.update_client_plans_lives_assured(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LivesassuredApi->update_client_plans_lives_assured: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LifeAssuredCollection**](LifeAssuredCollection.md)| List of Lives Assured. A maximum of 6 lives assured can be added. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client Id | 
 **plan_id** | **int**| Plan Id | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

[**LifeAssuredCollection**](LifeAssuredCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

