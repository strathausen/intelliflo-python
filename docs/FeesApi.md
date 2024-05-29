# swagger_client.FeesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_fees**](FeesApi.md#create_client_fees) | **POST** /clients/{clientId}/fees | Creates a fee for a given client. 
[**create_client_plan_fee**](FeesApi.md#create_client_plan_fee) | **POST** /clients/{clientId}/plans/{planId}/fees/{feeId} | Creates an association on a fee with a client and plan. 
[**delete_client_plan_fee**](FeesApi.md#delete_client_plan_fee) | **DELETE** /clients/{clientId}/plans/{planId}/fees/{feeId} | Deletes the association on the fee with a client and plan. 
[**get_client_fee**](FeesApi.md#get_client_fee) | **GET** /clients/{clientId}/fees/{feeId} | Returns a fee for a given client and fee. 
[**get_client_plan_fee**](FeesApi.md#get_client_plan_fee) | **GET** /clients/{clientId}/plans/{planId}/fees/{feeId} | Returns a fee for a given plan. 
[**list_client_fees**](FeesApi.md#list_client_fees) | **GET** /clients/{clientId}/fees | Returns a list of fees for a given client. 
[**list_client_plan_fees**](FeesApi.md#list_client_plan_fees) | **GET** /clients/{clientId}/plans/{planId}/fees | Returns a list of fees for a given client and plan. 
[**update_client_fee**](FeesApi.md#update_client_fee) | **PUT** /clients/{clientId}/fees/{feeId} | Updates a fee for a given client and fee. 

# **create_client_fees**
> FeeDocument create_client_fees(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)

Creates a fee for a given client. 

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
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
body = swagger_client.FeeDocument() # FeeDocument | Fee
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier.
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier. (optional)

try:
    # Creates a fee for a given client. 
    api_response = api_instance.create_client_fees(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->create_client_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeeDocument**](FeeDocument.md)| Fee | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier. | [optional] 

### Return type

[**FeeDocument**](FeeDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_plan_fee**
> FeeDocument create_client_plan_fee(authorization, client_id, fee_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)

Creates an association on a fee with a client and plan. 

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
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
fee_id = 56 # int | Fee identifier.
plan_id = 56 # int | Plan identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier. (optional)

try:
    # Creates an association on a fee with a client and plan. 
    api_response = api_instance.create_client_plan_fee(authorization, client_id, fee_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->create_client_plan_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **fee_id** | **int**| Fee identifier. | 
 **plan_id** | **int**| Plan identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier. | [optional] 

### Return type

[**FeeDocument**](FeeDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_plan_fee**
> delete_client_plan_fee(authorization, client_id, fee_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)

Deletes the association on the fee with a client and plan. 

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
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
fee_id = 56 # int | Fee identifier.
plan_id = 56 # int | Plan identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier. (optional)

try:
    # Deletes the association on the fee with a client and plan. 
    api_instance.delete_client_plan_fee(authorization, client_id, fee_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling FeesApi->delete_client_plan_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **fee_id** | **int**| Fee identifier. | 
 **plan_id** | **int**| Plan identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_fee**
> FeeDocument get_client_fee(authorization, client_id, fee_id, x_api_key, accept=accept, tenant_id=tenant_id)

Returns a fee for a given client and fee. 

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
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
fee_id = 56 # int | Fee identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier. (optional)

try:
    # Returns a fee for a given client and fee. 
    api_response = api_instance.get_client_fee(authorization, client_id, fee_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->get_client_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **fee_id** | **int**| Fee identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier. | [optional] 

### Return type

[**FeeDocument**](FeeDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_plan_fee**
> FeeDocument get_client_plan_fee(authorization, client_id, fee_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)

Returns a fee for a given plan. 

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
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
fee_id = 56 # int | Fee identifier.
plan_id = 56 # int | Plan identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier. (optional)

try:
    # Returns a fee for a given plan. 
    api_response = api_instance.get_client_plan_fee(authorization, client_id, fee_id, plan_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->get_client_plan_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **fee_id** | **int**| Fee identifier. | 
 **plan_id** | **int**| Plan identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier. | [optional] 

### Return type

[**FeeDocument**](FeeDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_fees**
> FeeCollection list_client_fees(authorization, client_id, x_api_key, accept=accept, filter=filter, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of fees for a given client. 

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
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported Filters:  * `id` (`in`, `eq`, `ne`, `gt`, `ge`, `lt`, `le`)    `status` (`in`, `eq`, `ne`, `startswith`)    `feeType.Name` (`in`, `eq`, `ne`, `startswith`)    `feeType.Category` (`in`, `eq`, `ne`)    `feeChargingType.Name` (`eq`)    `clients.id` (`in`)  See[QueryLang] (docs/ApiQueryLang) for further usage details. (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
tenant_id = 56 # int | Tenant Identifier. (optional)
top = 100 # int | The number of records to retrieve (default 100, max 500). (optional) (default to 100)

try:
    # Returns a list of fees for a given client. 
    api_response = api_instance.list_client_fees(authorization, client_id, x_api_key, accept=accept, filter=filter, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->list_client_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported Filters:  * &#x60;id&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;gt&#x60;, &#x60;ge&#x60;, &#x60;lt&#x60;, &#x60;le&#x60;)    &#x60;status&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;startswith&#x60;)    &#x60;feeType.Name&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;startswith&#x60;)    &#x60;feeType.Category&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;, &#x60;ne&#x60;)    &#x60;feeChargingType.Name&#x60; (&#x60;eq&#x60;)    &#x60;clients.id&#x60; (&#x60;in&#x60;)  See[QueryLang] (docs/ApiQueryLang) for further usage details. | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **tenant_id** | **int**| Tenant Identifier. | [optional] 
 **top** | **int**| The number of records to retrieve (default 100, max 500). | [optional] [default to 100]

### Return type

[**FeeCollection**](FeeCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_plan_fees**
> FeeCollection list_client_plan_fees(authorization, client_id, plan_id, x_api_key, accept=accept, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of fees for a given client and plan. 

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
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
plan_id = 56 # int | Plan identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
tenant_id = 56 # int | Tenant identifier. (optional)
top = 100 # int | The number of records to retrieve (default 25, max 100). (optional) (default to 100)

try:
    # Returns a list of fees for a given client and plan. 
    api_response = api_instance.list_client_plan_fees(authorization, client_id, plan_id, x_api_key, accept=accept, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->list_client_plan_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **plan_id** | **int**| Plan identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **tenant_id** | **int**| Tenant identifier. | [optional] 
 **top** | **int**| The number of records to retrieve (default 25, max 100). | [optional] [default to 100]

### Return type

[**FeeCollection**](FeeCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_fee**
> FeeDocument update_client_fee(body, authorization, x_api_key, client_id, fee_id, accept=accept, tenant_id=tenant_id)

Updates a fee for a given client and fee. 

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
api_instance = swagger_client.FeesApi(swagger_client.ApiClient(configuration))
body = swagger_client.FeeDocument() # FeeDocument | Fee.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier.
fee_id = 56 # int | Fee identifier.
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier. (optional)

try:
    # Updates a fee for a given client and fee. 
    api_response = api_instance.update_client_fee(body, authorization, x_api_key, client_id, fee_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->update_client_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeeDocument**](FeeDocument.md)| Fee. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **fee_id** | **int**| Fee identifier. | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier. | [optional] 

### Return type

[**FeeDocument**](FeeDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

