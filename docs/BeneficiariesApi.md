# swagger_client.BeneficiariesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_client_plan_beneficiaries**](BeneficiariesApi.md#delete_client_plan_beneficiaries) | **DELETE** /clients/{clientId}/plans/{planId}/beneficiaries | Deletes beneficiary or beneficiaries for a given plan.
[**list_client_plans_beneficiaries**](BeneficiariesApi.md#list_client_plans_beneficiaries) | **GET** /clients/{clientId}/plans/{planId}/beneficiaries | Returns a list of beneficiaries for a given client and plan. 
[**update_client_plans_beneficiaries**](BeneficiariesApi.md#update_client_plans_beneficiaries) | **PUT** /clients/{clientId}/plans/{planId}/beneficiaries | Updates or creates the beneficiary for a given client and plan. 

# **delete_client_plan_beneficiaries**
> delete_client_plan_beneficiaries(authorization, client_id, plan_id, x_api_key, accept=accept)

Deletes beneficiary or beneficiaries for a given plan.

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
api_instance = swagger_client.BeneficiariesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
plan_id = 56 # int | Plan identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes beneficiary or beneficiaries for a given plan.
    api_instance.delete_client_plan_beneficiaries(authorization, client_id, plan_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling BeneficiariesApi->delete_client_plan_beneficiaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **plan_id** | **int**| Plan identifier | 
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

# **list_client_plans_beneficiaries**
> BeneficiaryCollection list_client_plans_beneficiaries(authorization, client_id, plan_id, x_api_key, accept=accept, filter=filter, skip=skip, top=top)

Returns a list of beneficiaries for a given client and plan. 

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
api_instance = swagger_client.BeneficiariesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
plan_id = 56 # int | Plan identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supports filtering by externalReference (eq), e.g.: externalReference eq 'MyRef' (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
top = 100 # int | The number of records to retrieve (default: 100, max: 500) (optional) (default to 100)

try:
    # Returns a list of beneficiaries for a given client and plan. 
    api_response = api_instance.list_client_plans_beneficiaries(authorization, client_id, plan_id, x_api_key, accept=accept, filter=filter, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BeneficiariesApi->list_client_plans_beneficiaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **plan_id** | **int**| Plan identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supports filtering by externalReference (eq), e.g.: externalReference eq &#x27;MyRef&#x27; | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **top** | **int**| The number of records to retrieve (default: 100, max: 500) | [optional] [default to 100]

### Return type

[**BeneficiaryCollection**](BeneficiaryCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_plans_beneficiaries**
> BeneficiaryCollection update_client_plans_beneficiaries(body, authorization, x_api_key, client_id, plan_id, accept=accept)

Updates or creates the beneficiary for a given client and plan. 

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
api_instance = swagger_client.BeneficiariesApi(swagger_client.ApiClient(configuration))
body = swagger_client.BeneficiaryCollection() # BeneficiaryCollection | plan beneficiary collection
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier
plan_id = 56 # int | Plan identifier
accept = 'accept_example' # str |  (optional)

try:
    # Updates or creates the beneficiary for a given client and plan. 
    api_response = api_instance.update_client_plans_beneficiaries(body, authorization, x_api_key, client_id, plan_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BeneficiariesApi->update_client_plans_beneficiaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BeneficiaryCollection**](BeneficiaryCollection.md)| plan beneficiary collection | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **plan_id** | **int**| Plan identifier | 
 **accept** | **str**|  | [optional] 

### Return type

[**BeneficiaryCollection**](BeneficiaryCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

