# swagger_client.PlantypesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_plantypes**](PlantypesApi.md#list_plantypes) | **GET** /plantypes | Returns a list of plan types.

# **list_plantypes**
> PlanTypeCollection list_plantypes(authorization, x_api_key, accept=accept, filter=filter, plan_purpose=plan_purpose, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of plan types.

This will return an unfiltered collection of PlanTypes. This collection can be narrowed by specifying the allowed query parameters.

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
api_instance = swagger_client.PlantypesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supports filtering:  * `id` ( in, eq ) e.g. filter=id in (123, 1234) or filter=id eq 123  * `portfolioCategory` ( in ) e.g. filter=portfolioCategory in ('investments','pensions')  * `isArchived`  ( eq ) e.g. filter=isArchived eq false  * `regionCode` ( eq ) e.g. filter=regionCode eq 'GB'  * `programId` ( in, eq ) e.g. filter=programId in (1, 2) or filter=programId eq 1  * `isWrapper` ( eq ) e.g. filter=isWrapper eq true                See [QueryLang](docs/ApiQueryLang) for further usage details. (optional)
plan_purpose = 'plan_purpose_example' # str | Filters PlanTypes by the given Plan Purpose.                Example: `/plantypes?planPurpose=Buy%20To%20Let` (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
tenant_id = 56 # int | Tenant Id (optional)
top = 100 # int | The number of records to retrieve (default 100, max 500) (optional) (default to 100)

try:
    # Returns a list of plan types.
    api_response = api_instance.list_plantypes(authorization, x_api_key, accept=accept, filter=filter, plan_purpose=plan_purpose, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlantypesApi->list_plantypes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supports filtering:  * &#x60;id&#x60; ( in, eq ) e.g. filter&#x3D;id in (123, 1234) or filter&#x3D;id eq 123  * &#x60;portfolioCategory&#x60; ( in ) e.g. filter&#x3D;portfolioCategory in (&#x27;investments&#x27;,&#x27;pensions&#x27;)  * &#x60;isArchived&#x60;  ( eq ) e.g. filter&#x3D;isArchived eq false  * &#x60;regionCode&#x60; ( eq ) e.g. filter&#x3D;regionCode eq &#x27;GB&#x27;  * &#x60;programId&#x60; ( in, eq ) e.g. filter&#x3D;programId in (1, 2) or filter&#x3D;programId eq 1  * &#x60;isWrapper&#x60; ( eq ) e.g. filter&#x3D;isWrapper eq true                See [QueryLang](docs/ApiQueryLang) for further usage details. | [optional] 
 **plan_purpose** | **str**| Filters PlanTypes by the given Plan Purpose.                Example: &#x60;/plantypes?planPurpose&#x3D;Buy%20To%20Let&#x60; | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **tenant_id** | **int**| Tenant Id | [optional] 
 **top** | **int**| The number of records to retrieve (default 100, max 500) | [optional] [default to 100]

### Return type

[**PlanTypeCollection**](PlanTypeCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

