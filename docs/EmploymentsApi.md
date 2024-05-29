# swagger_client.EmploymentsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_employment**](EmploymentsApi.md#create_client_employment) | **POST** /clients/{clientId}/employments | Create an employment for a given client.
[**delete_client_employment**](EmploymentsApi.md#delete_client_employment) | **DELETE** /clients/{clientId}/employments/{employmentId} | Deletes a given employment.
[**get_client_employment**](EmploymentsApi.md#get_client_employment) | **GET** /clients/{clientId}/employments/{employmentId} | Get an employment for a given client.
[**list_client_employments**](EmploymentsApi.md#list_client_employments) | **GET** /clients/{clientId}/employments | Get a list of employments for a given client.
[**update_client_employment**](EmploymentsApi.md#update_client_employment) | **PUT** /clients/{clientId}/employments/{employmentId} | Updates an employment for a given client.

# **create_client_employment**
> Employment create_client_employment(body, authorization, x_api_key, client_id, accept=accept)

Create an employment for a given client.

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
api_instance = swagger_client.EmploymentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateEmployment() # CreateEmployment | Employment document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier
accept = 'accept_example' # str |  (optional)

try:
    # Create an employment for a given client.
    api_response = api_instance.create_client_employment(body, authorization, x_api_key, client_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmploymentsApi->create_client_employment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEmployment**](CreateEmployment.md)| Employment document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **accept** | **str**|  | [optional] 

### Return type

[**Employment**](Employment.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_employment**
> delete_client_employment(authorization, client_id, employment_id, x_api_key, accept=accept)

Deletes a given employment.

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
api_instance = swagger_client.EmploymentsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
employment_id = 56 # int | Employment identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes a given employment.
    api_instance.delete_client_employment(authorization, client_id, employment_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling EmploymentsApi->delete_client_employment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **employment_id** | **int**| Employment identifier | 
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

# **get_client_employment**
> Employment get_client_employment(authorization, client_id, employment_id, x_api_key, accept=accept)

Get an employment for a given client.

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
api_instance = swagger_client.EmploymentsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id - The special value \"me\" can be used to indicate the authenticated user.
employment_id = 56 # int | Employment identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Get an employment for a given client.
    api_response = api_instance.get_client_employment(authorization, client_id, employment_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmploymentsApi->get_client_employment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **employment_id** | **int**| Employment identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Employment**](Employment.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_employments**
> EmploymentCollection list_client_employments(authorization, client_id, x_api_key, accept=accept, filter=filter, skip=skip, top=top)

Get a list of employments for a given client.

Get a list of client's employments. Some specific filtering is optionally supported.  The following field is supported for in  id  Examples: top=5&skip=22&filter= id in '(987,654,126)

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
api_instance = swagger_client.EmploymentsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id - The special value \"me\" can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supports filtering by id (in), e.g.: filter=id in (123, 124) (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
top = 100 # int | The number of records to retrieve (default 100, max 500) (optional) (default to 100)

try:
    # Get a list of employments for a given client.
    api_response = api_instance.list_client_employments(authorization, client_id, x_api_key, accept=accept, filter=filter, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmploymentsApi->list_client_employments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supports filtering by id (in), e.g.: filter&#x3D;id in (123, 124) | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **top** | **int**| The number of records to retrieve (default 100, max 500) | [optional] [default to 100]

### Return type

[**EmploymentCollection**](EmploymentCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_employment**
> Employment update_client_employment(body, authorization, x_api_key, client_id, employment_id, accept=accept)

Updates an employment for a given client.

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
api_instance = swagger_client.EmploymentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Employment() # Employment | Employment document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier
employment_id = 56 # int | Employment identifier
accept = 'accept_example' # str |  (optional)

try:
    # Updates an employment for a given client.
    api_response = api_instance.update_client_employment(body, authorization, x_api_key, client_id, employment_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmploymentsApi->update_client_employment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Employment**](Employment.md)| Employment document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **employment_id** | **int**| Employment identifier | 
 **accept** | **str**|  | [optional] 

### Return type

[**Employment**](Employment.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

