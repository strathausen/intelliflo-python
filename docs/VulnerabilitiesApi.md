# swagger_client.VulnerabilitiesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_vulnerability**](VulnerabilitiesApi.md#get_client_vulnerability) | **GET** /clients/{clientId}/vulnerabilities/{vulnerabilityId} | Get a single client vulnerability.
[**get_client_vulnerability_current**](VulnerabilitiesApi.md#get_client_vulnerability_current) | **GET** /clients/{clientId}/vulnerabilities/current | Get client&#x27;s current vulnerability.
[**list_clients_vulnerabilities**](VulnerabilitiesApi.md#list_clients_vulnerabilities) | **GET** /clients/vulnerabilities/current | Returns a list of current vulnerabilities for clients defined in the filter.
[**update_client_vulnerabilities_current**](VulnerabilitiesApi.md#update_client_vulnerabilities_current) | **PUT** /clients/{clientId}/vulnerabilities/current | Update client&#x27;s current vulnerability.

# **get_client_vulnerability**
> ClientVulnerabilityDocument get_client_vulnerability(authorization, client_id, vulnerability_id, x_api_key, accept=accept, tenant_id=tenant_id)

Get a single client vulnerability.

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
api_instance = swagger_client.VulnerabilitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Identifier
vulnerability_id = 56 # int | Vulnerability Identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Identifier (optional)

try:
    # Get a single client vulnerability.
    api_response = api_instance.get_client_vulnerability(authorization, client_id, vulnerability_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VulnerabilitiesApi->get_client_vulnerability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Identifier | 
 **vulnerability_id** | **int**| Vulnerability Identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Identifier | [optional] 

### Return type

[**ClientVulnerabilityDocument**](ClientVulnerabilityDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_vulnerability_current**
> ClientVulnerabilityDocument get_client_vulnerability_current(authorization, client_id, x_api_key, accept=accept, tenant_id=tenant_id)

Get client's current vulnerability.

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
api_instance = swagger_client.VulnerabilitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Identifier (optional)

try:
    # Get client's current vulnerability.
    api_response = api_instance.get_client_vulnerability_current(authorization, client_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VulnerabilitiesApi->get_client_vulnerability_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Identifier | [optional] 

### Return type

[**ClientVulnerabilityDocument**](ClientVulnerabilityDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clients_vulnerabilities**
> ClientVulnerabilityCollection list_clients_vulnerabilities(authorization, tenant_id, x_api_key, accept=accept, filter=filter, skip=skip, top=top)

Returns a list of current vulnerabilities for clients defined in the filter.

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
api_instance = swagger_client.VulnerabilitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
tenant_id = 56 # int | Tenant identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Vulnerabilities can be filtered using fields and operators below.  Supported fields (operators) are:  * `clientId` (`eq`, `in`)                Example filters:      `filter=clientId eq 12226`      `filter=clientId in (5444,87883,43442)`                See [QueryLang](docs/ApiQueryLang) for further usage details. (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
top = 100 # int | The number of records to retrieve (default 100, max 500) (optional) (default to 100)

try:
    # Returns a list of current vulnerabilities for clients defined in the filter.
    api_response = api_instance.list_clients_vulnerabilities(authorization, tenant_id, x_api_key, accept=accept, filter=filter, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VulnerabilitiesApi->list_clients_vulnerabilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **tenant_id** | **int**| Tenant identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Vulnerabilities can be filtered using fields and operators below.  Supported fields (operators) are:  * &#x60;clientId&#x60; (&#x60;eq&#x60;, &#x60;in&#x60;)                Example filters:      &#x60;filter&#x3D;clientId eq 12226&#x60;      &#x60;filter&#x3D;clientId in (5444,87883,43442)&#x60;                See [QueryLang](docs/ApiQueryLang) for further usage details. | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **top** | **int**| The number of records to retrieve (default 100, max 500) | [optional] [default to 100]

### Return type

[**ClientVulnerabilityCollection**](ClientVulnerabilityCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_vulnerabilities_current**
> ClientVulnerabilityDocument update_client_vulnerabilities_current(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)

Update client's current vulnerability.

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
api_instance = swagger_client.VulnerabilitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClientVulnerabilityDocument() # ClientVulnerabilityDocument | Vulnerability document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client Identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Identifier (optional)

try:
    # Update client's current vulnerability.
    api_response = api_instance.update_client_vulnerabilities_current(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VulnerabilitiesApi->update_client_vulnerabilities_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientVulnerabilityDocument**](ClientVulnerabilityDocument.md)| Vulnerability document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client Identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Identifier | [optional] 

### Return type

[**ClientVulnerabilityDocument**](ClientVulnerabilityDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

