# swagger_client.TimeentriesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_time_entries**](TimeentriesApi.md#list_time_entries) | **GET** /time_entries | Returns a list of time entries. 

# **list_time_entries**
> TimeEntryCollection2 list_time_entries(authorization, x_api_key, accept=accept, filter=filter, skip=skip, top=top)

Returns a list of time entries. 

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

# create an instance of the API class
api_instance = swagger_client.TimeentriesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported Filters:  * `startedAt` (`ge`)  * `endedAt` (`le`)  * `createdAt` (`ge`)                Usage Examples:  * `?filter= startedAt ge 2023-09-21T00:00:00Z and endedAt le 2025-01-01T00:00:00Z`.  * `?filter= createdAt ge 2023-09-21T00:00:00Z.                See [QueryLang](docs/ApiQueryLang) for further usage details. (optional)
skip = 0 # int | The number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
top = 100 # int | The number of records to retrieve (default: 100, max: 500). (optional) (default to 100)

try:
    # Returns a list of time entries. 
    api_response = api_instance.list_time_entries(authorization, x_api_key, accept=accept, filter=filter, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeentriesApi->list_time_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported Filters:  * &#x60;startedAt&#x60; (&#x60;ge&#x60;)  * &#x60;endedAt&#x60; (&#x60;le&#x60;)  * &#x60;createdAt&#x60; (&#x60;ge&#x60;)                Usage Examples:  * &#x60;?filter&#x3D; startedAt ge 2023-09-21T00:00:00Z and endedAt le 2025-01-01T00:00:00Z&#x60;.  * &#x60;?filter&#x3D; createdAt ge 2023-09-21T00:00:00Z.                See [QueryLang](docs/ApiQueryLang) for further usage details. | [optional] 
 **skip** | **int**| The number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **top** | **int**| The number of records to retrieve (default: 100, max: 500). | [optional] [default to 100]

### Return type

[**TimeEntryCollection2**](TimeEntryCollection2.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

