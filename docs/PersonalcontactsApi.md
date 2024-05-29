# swagger_client.PersonalcontactsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_personal_contact**](PersonalcontactsApi.md#create_personal_contact) | **POST** /clients/{clientId}/personalContacts | Add a new personal contact for a given client
[**delete_personal_contact**](PersonalcontactsApi.md#delete_personal_contact) | **DELETE** /clients/{clientId}/personalContacts/{personalContactId} | Delete an existing personal contact
[**get_personal_contact**](PersonalcontactsApi.md#get_personal_contact) | **GET** /clients/{clientId}/personalContacts/{personalContactId} | Get given personal contact for a given client
[**list_personal_contacts**](PersonalcontactsApi.md#list_personal_contacts) | **GET** /clients/{clientId}/personalContacts | List personal contacts for a given client.
[**patch_personal_contact**](PersonalcontactsApi.md#patch_personal_contact) | **PATCH** /clients/{clientId}/personalContacts/{personalContactId} | Patch an existing personal contact
[**update_personal_contact**](PersonalcontactsApi.md#update_personal_contact) | **PUT** /clients/{clientId}/personalContacts/{personalContactId} | Update an existing personal contact.

# **create_personal_contact**
> PersonalContactDocument create_personal_contact(body, authorization, x_api_key, client_id, accept=accept)

Add a new personal contact for a given client

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
api_instance = swagger_client.PersonalcontactsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PersonalContactDocument() # PersonalContactDocument | Personal Contact document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
accept = 'accept_example' # str |  (optional)

try:
    # Add a new personal contact for a given client
    api_response = api_instance.create_personal_contact(body, authorization, x_api_key, client_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalcontactsApi->create_personal_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PersonalContactDocument**](PersonalContactDocument.md)| Personal Contact document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **accept** | **str**|  | [optional] 

### Return type

[**PersonalContactDocument**](PersonalContactDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_personal_contact**
> delete_personal_contact(authorization, client_id, personal_contact_id, x_api_key, accept=accept)

Delete an existing personal contact

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
api_instance = swagger_client.PersonalcontactsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
personal_contact_id = 56 # int | The identifier for a PersonalContact.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Delete an existing personal contact
    api_instance.delete_personal_contact(authorization, client_id, personal_contact_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling PersonalcontactsApi->delete_personal_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **personal_contact_id** | **int**| The identifier for a PersonalContact. | 
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

# **get_personal_contact**
> PersonalContactDocument get_personal_contact(authorization, client_id, personal_contact_id, x_api_key, accept=accept)

Get given personal contact for a given client

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
api_instance = swagger_client.PersonalcontactsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
personal_contact_id = 56 # int | The identifier for a PersonalContact.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Get given personal contact for a given client
    api_response = api_instance.get_personal_contact(authorization, client_id, personal_contact_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalcontactsApi->get_personal_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **personal_contact_id** | **int**| The identifier for a PersonalContact. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**PersonalContactDocument**](PersonalContactDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_personal_contacts**
> PersonalContactDocumentCollection list_personal_contacts(authorization, client_id, x_api_key, accept=accept, filter=filter, skip=skip, top=top)

List personal contacts for a given client.

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
api_instance = swagger_client.PersonalcontactsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported Filters:  * `id` (`in`, `eq`)  * `tag` (`startswith`, `eq`, `in`,)  * `person.firstName` (`startswith`, `eq`, `in`)  * `person.lastName` (`startswith`, `eq`, `in`)  * `trust.name` (`startswith`, `eq`, `in`)  * `corporate.name` (`startswith`, `eq`, `in`)  * `externalReference` (`eq`)                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). (optional)
skip = 0 # int | Optional. The number of records to skip. If not specified it defaults to 0. (optional) (default to 0)
top = 100 # int | Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. (optional) (default to 100)

try:
    # List personal contacts for a given client.
    api_response = api_instance.list_personal_contacts(authorization, client_id, x_api_key, accept=accept, filter=filter, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalcontactsApi->list_personal_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported Filters:  * &#x60;id&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;)  * &#x60;tag&#x60; (&#x60;startswith&#x60;, &#x60;eq&#x60;, &#x60;in&#x60;,)  * &#x60;person.firstName&#x60; (&#x60;startswith&#x60;, &#x60;eq&#x60;, &#x60;in&#x60;)  * &#x60;person.lastName&#x60; (&#x60;startswith&#x60;, &#x60;eq&#x60;, &#x60;in&#x60;)  * &#x60;trust.name&#x60; (&#x60;startswith&#x60;, &#x60;eq&#x60;, &#x60;in&#x60;)  * &#x60;corporate.name&#x60; (&#x60;startswith&#x60;, &#x60;eq&#x60;, &#x60;in&#x60;)  * &#x60;externalReference&#x60; (&#x60;eq&#x60;)                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). | [optional] 
 **skip** | **int**| Optional. The number of records to skip. If not specified it defaults to 0. | [optional] [default to 0]
 **top** | **int**| Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. | [optional] [default to 100]

### Return type

[**PersonalContactDocumentCollection**](PersonalContactDocumentCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_personal_contact**
> PersonalContactDocument patch_personal_contact(body, authorization, x_api_key, client_id, personal_contact_id, accept=accept)

Patch an existing personal contact

A Json Patch document containing details of modifications to be made to the model resource.  Properties which cannot be updated on PUT, cannot be updated using patch For a simple example a request contains the following  JSON: { \"op\": \"replace\", \"path\": \"/expectedReturn\", \"value\": \"1.234\" }

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
api_instance = swagger_client.PersonalcontactsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.Operation()] # list[Operation] | Personal Contact json patch document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
personal_contact_id = 56 # int | The identifier for a PersonalContact.
accept = 'accept_example' # str |  (optional)

try:
    # Patch an existing personal contact
    api_response = api_instance.patch_personal_contact(body, authorization, x_api_key, client_id, personal_contact_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalcontactsApi->patch_personal_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Operation]**](Operation.md)| Personal Contact json patch document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **personal_contact_id** | **int**| The identifier for a PersonalContact. | 
 **accept** | **str**|  | [optional] 

### Return type

[**PersonalContactDocument**](PersonalContactDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_personal_contact**
> PersonalContactDocument update_personal_contact(body, authorization, x_api_key, client_id, personal_contact_id, accept=accept)

Update an existing personal contact.

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
api_instance = swagger_client.PersonalcontactsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PersonalContactDocument() # PersonalContactDocument | Personal Contact document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
personal_contact_id = 56 # int | The identifier for a PersonalContact.
accept = 'accept_example' # str |  (optional)

try:
    # Update an existing personal contact.
    api_response = api_instance.update_personal_contact(body, authorization, x_api_key, client_id, personal_contact_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalcontactsApi->update_personal_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PersonalContactDocument**](PersonalContactDocument.md)| Personal Contact document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **personal_contact_id** | **int**| The identifier for a PersonalContact. | 
 **accept** | **str**|  | [optional] 

### Return type

[**PersonalContactDocument**](PersonalContactDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

