# swagger_client.AddressesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_address**](AddressesApi.md#create_client_address) | **POST** /clients/{clientId}/addresses | Create an address
[**create_lead_address**](AddressesApi.md#create_lead_address) | **POST** /leads/{leadId}/addresses | Creates a new Address for the given Lead.
[**delete_client_address**](AddressesApi.md#delete_client_address) | **DELETE** /clients/{clientId}/addresses/{addressId} | Deletes an existing Address for the given Client.
[**delete_lead_address**](AddressesApi.md#delete_lead_address) | **DELETE** /leads/{leadId}/addresses/{addressId} | Deletes an existing Address for the given Lead.
[**get_adviser_address**](AddressesApi.md#get_adviser_address) | **GET** /advisers/{adviserId}/addresses/{addressId} | Retrieves the Address for the given addressId.
[**get_client_address**](AddressesApi.md#get_client_address) | **GET** /clients/{clientId}/addresses/{addressId} | Get a client&#x27;s address by id.
[**get_lead_address**](AddressesApi.md#get_lead_address) | **GET** /leads/{leadId}/addresses/{addressId} | Retrieves the Address for the given addressId.
[**list_adviser_addresses**](AddressesApi.md#list_adviser_addresses) | **GET** /advisers/{adviserId}/addresses | Returns a paged list of Address (AddressCollection)
[**list_client_addresses**](AddressesApi.md#list_client_addresses) | **GET** /clients/{clientId}/addresses | Returns a list of addresses for a client
[**list_lead_addresses**](AddressesApi.md#list_lead_addresses) | **GET** /leads/{leadId}/addresses | Returns a paged list of Address (AddressCollection)
[**update_client_address**](AddressesApi.md#update_client_address) | **PUT** /clients/{clientId}/addresses/{addressId} | Update an address
[**update_lead_address**](AddressesApi.md#update_lead_address) | **PUT** /leads/{leadId}/addresses/{addressId} | Updates an existing Address for the given Lead.

# **create_client_address**
> Address create_client_address(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)

Create an address

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
api_instance = swagger_client.AddressesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Address() # Address | Address document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Create an address
    api_response = api_instance.create_client_address(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->create_client_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Address**](Address.md)| Address document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**Address**](Address.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_lead_address**
> Address create_lead_address(body, authorization, x_api_key, lead_id, accept=accept, tenant_id=tenant_id)

Creates a new Address for the given Lead.

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
api_instance = swagger_client.AddressesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Address() # Address | Address document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
lead_id = 56 # int | Lead identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Creates a new Address for the given Lead.
    api_response = api_instance.create_lead_address(body, authorization, x_api_key, lead_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->create_lead_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Address**](Address.md)| Address document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **lead_id** | **int**| Lead identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**Address**](Address.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_address**
> delete_client_address(address_id, authorization, client_id, x_api_key, accept=accept, tenant_id=tenant_id)

Deletes an existing Address for the given Client.

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
api_instance = swagger_client.AddressesApi(swagger_client.ApiClient(configuration))
address_id = 56 # int | Address identifier
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Deletes an existing Address for the given Client.
    api_instance.delete_client_address(address_id, authorization, client_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling AddressesApi->delete_client_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **int**| Address identifier | 
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
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

# **delete_lead_address**
> delete_lead_address(address_id, authorization, lead_id, x_api_key, accept=accept, tenant_id=tenant_id)

Deletes an existing Address for the given Lead.

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
api_instance = swagger_client.AddressesApi(swagger_client.ApiClient(configuration))
address_id = 56 # int | Address identifier
authorization = 'authorization_example' # str | 
lead_id = 56 # int | Lead identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Deletes an existing Address for the given Lead.
    api_instance.delete_lead_address(address_id, authorization, lead_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling AddressesApi->delete_lead_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **int**| Address identifier | 
 **authorization** | **str**|  | 
 **lead_id** | **int**| Lead identifier | 
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

# **get_adviser_address**
> Address get_adviser_address(address_id, adviser_id, authorization, x_api_key, accept=accept)

Retrieves the Address for the given addressId.

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
api_instance = swagger_client.AddressesApi(swagger_client.ApiClient(configuration))
address_id = 56 # int | Address identifier
adviser_id = 56 # int | Adviser identifier
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Retrieves the Address for the given addressId.
    api_response = api_instance.get_adviser_address(address_id, adviser_id, authorization, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_adviser_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **int**| Address identifier | 
 **adviser_id** | **int**| Adviser identifier | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Address**](Address.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_address**
> Address get_client_address(address_id, authorization, client_id, x_api_key, accept=accept)

Get a client's address by id.

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
api_instance = swagger_client.AddressesApi(swagger_client.ApiClient(configuration))
address_id = 56 # int | Address identifier
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Get a client's address by id.
    api_response = api_instance.get_client_address(address_id, authorization, client_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_client_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **int**| Address identifier | 
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Address**](Address.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lead_address**
> Address get_lead_address(address_id, authorization, lead_id, x_api_key, accept=accept)

Retrieves the Address for the given addressId.

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
api_instance = swagger_client.AddressesApi(swagger_client.ApiClient(configuration))
address_id = 56 # int | Address identifier
authorization = 'authorization_example' # str | 
lead_id = 56 # int | Lead identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Retrieves the Address for the given addressId.
    api_response = api_instance.get_lead_address(address_id, authorization, lead_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_lead_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **int**| Address identifier | 
 **authorization** | **str**|  | 
 **lead_id** | **int**| Lead identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Address**](Address.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_adviser_addresses**
> AddressCollection list_adviser_addresses(adviser_id, authorization, x_api_key, accept=accept, skip=skip, top=top)

Returns a paged list of Address (AddressCollection)

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
api_instance = swagger_client.AddressesApi(swagger_client.ApiClient(configuration))
adviser_id = 56 # int | Adviser identifier.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int | Optional. The number of records to skip. If not specified it defaults to 0. (optional) (default to 0)
top = 100 # int | Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. (optional) (default to 100)

try:
    # Returns a paged list of Address (AddressCollection)
    api_response = api_instance.list_adviser_addresses(adviser_id, authorization, x_api_key, accept=accept, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->list_adviser_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adviser_id** | **int**| Adviser identifier. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**| Optional. The number of records to skip. If not specified it defaults to 0. | [optional] [default to 0]
 **top** | **int**| Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. | [optional] [default to 100]

### Return type

[**AddressCollection**](AddressCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_addresses**
> AddressCollection list_client_addresses(authorization, client_id, x_api_key, accept=accept, skip=skip, top=top)

Returns a list of addresses for a client

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
api_instance = swagger_client.AddressesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int | Optional. The number of records to skip. If not specified it defaults to 0. (optional) (default to 0)
top = 100 # int | Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. (optional) (default to 100)

try:
    # Returns a list of addresses for a client
    api_response = api_instance.list_client_addresses(authorization, client_id, x_api_key, accept=accept, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->list_client_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**| Optional. The number of records to skip. If not specified it defaults to 0. | [optional] [default to 0]
 **top** | **int**| Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. | [optional] [default to 100]

### Return type

[**AddressCollection**](AddressCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lead_addresses**
> AddressCollection list_lead_addresses(authorization, lead_id, x_api_key, accept=accept, skip=skip, top=top)

Returns a paged list of Address (AddressCollection)

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
api_instance = swagger_client.AddressesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
lead_id = 56 # int | Lead identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int | Optional. The number of records to skip. If not specified it defaults to 0. (optional) (default to 0)
top = 100 # int | Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. (optional) (default to 100)

try:
    # Returns a paged list of Address (AddressCollection)
    api_response = api_instance.list_lead_addresses(authorization, lead_id, x_api_key, accept=accept, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->list_lead_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **lead_id** | **int**| Lead identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**| Optional. The number of records to skip. If not specified it defaults to 0. | [optional] [default to 0]
 **top** | **int**| Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. | [optional] [default to 100]

### Return type

[**AddressCollection**](AddressCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_address**
> Address update_client_address(body, authorization, x_api_key, address_id, client_id, accept=accept, tenant_id=tenant_id)

Update an address

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
api_instance = swagger_client.AddressesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Address() # Address | Address document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
address_id = 56 # int | 
client_id = 56 # int | Client identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Update an address
    api_response = api_instance.update_client_address(body, authorization, x_api_key, address_id, client_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->update_client_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Address**](Address.md)| Address document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **address_id** | **int**|  | 
 **client_id** | **int**| Client identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**Address**](Address.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lead_address**
> Address update_lead_address(body, authorization, x_api_key, address_id, lead_id, accept=accept, tenant_id=tenant_id)

Updates an existing Address for the given Lead.

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
api_instance = swagger_client.AddressesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Address() # Address | Address document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
address_id = 56 # int | Address identifier
lead_id = 56 # int | Lead identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Updates an existing Address for the given Lead.
    api_response = api_instance.update_lead_address(body, authorization, x_api_key, address_id, lead_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->update_lead_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Address**](Address.md)| Address document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **address_id** | **int**| Address identifier | 
 **lead_id** | **int**| Lead identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**Address**](Address.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

