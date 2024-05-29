# swagger_client.LeadsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lead**](LeadsApi.md#create_lead) | **POST** /leads | Create a lead. 
[**delete_lead**](LeadsApi.md#delete_lead) | **DELETE** /leads/{leadId} | Deletes a given lead. 
[**get_lead**](LeadsApi.md#get_lead) | **GET** /leads/{leadId} | Returns a given lead. 
[**lead_exists**](LeadsApi.md#lead_exists) | **HEAD** /leads/{leadId} | Check if the lead exists. 
[**list_leads**](LeadsApi.md#list_leads) | **GET** /leads | Returns a list of leads. 
[**update_lead**](LeadsApi.md#update_lead) | **PUT** /leads/{leadId} | Updates a given lead. 

# **create_lead**
> Lead create_lead(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)

Create a lead. 

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
api_instance = swagger_client.LeadsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Lead() # Lead | Lead document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Create a lead. 
    api_response = api_instance.create_lead(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeadsApi->create_lead: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Lead**](Lead.md)| Lead document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**Lead**](Lead.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lead**
> delete_lead(authorization, lead_id, x_api_key, accept=accept, tenant_id=tenant_id)

Deletes a given lead. 

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
api_instance = swagger_client.LeadsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
lead_id = 56 # int | Lead identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Deletes a given lead. 
    api_instance.delete_lead(authorization, lead_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling LeadsApi->delete_lead: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **lead_id** | **int**| Lead identifier. | 
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

# **get_lead**
> Lead get_lead(authorization, lead_id, x_api_key, accept=accept, tenant_id=tenant_id)

Returns a given lead. 

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
api_instance = swagger_client.LeadsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
lead_id = 56 # int | Lead identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int |  (optional)

try:
    # Returns a given lead. 
    api_response = api_instance.get_lead(authorization, lead_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeadsApi->get_lead: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **lead_id** | **int**| Lead identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**|  | [optional] 

### Return type

[**Lead**](Lead.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lead_exists**
> lead_exists(authorization, lead_id, x_api_key, accept=accept, tenant_id=tenant_id)

Check if the lead exists. 

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
api_instance = swagger_client.LeadsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
lead_id = 56 # int | Lead identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Check if the lead exists. 
    api_instance.lead_exists(authorization, lead_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling LeadsApi->lead_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **lead_id** | **int**| Lead identifier. | 
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

# **list_leads**
> LeadCollection list_leads(authorization, x_api_key, accept=accept, filter=filter, skip=skip, top=top)

Returns a list of leads. 

Get a list of leads. Some specific filtering is optionally supported. The following fields are supports for equals (`eq`): * `person.firstName`,  * `person.lastName`,  * `corporate.name`,  * `trust.name`,  * `currentAdviser.id`  The following fields are supports for `startswith`:  * `person.firstName`,  * `person.lastName`,  * `corporate.name`,  * `trust.name`  The following field is supported for `in`: * `tag`, * `currentAdviser.id`  *Example* `top=5&amp;Skip=22&amp;filter= person.firstName eq 'john' and person.lastName startswith 'j' and tag in ('tag1', 'tag2', 'tag3')` 

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
api_instance = swagger_client.LeadsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | The list of Leads returned can be filtered using one or more of the supported fields and operators.  The supported fields and operators are:    * `id` (`in`)  * `corporate.name` (`eq`, `startswith`)  * `currentAdviser.id` (`eq`, `in`)  * `person.firstName` (`eq`, `startswith`)  * `person.lastName` (`eq`, `startswith`)  * `trust.name` (`eq`, `startswith`)  * `tag` (`in`)                Example filters:      filter= person.firstName eq 'john' and person.lastName startswith 'j'      filter= id in '(987,7654,126)' and tag in ('tag1', 'tag2', 'tag3')      top=5&Skip=22&filter= person.firstName eq 'john' and person.lastName startswith 'j' and tag in ('tag1', 'tag2', 'tag3')                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). (optional)
skip = 0 # int | Optional. The number of records to skip. If not specified it defaults to 0. (optional) (default to 0)
top = 100 # int | Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. (optional) (default to 100)

try:
    # Returns a list of leads. 
    api_response = api_instance.list_leads(authorization, x_api_key, accept=accept, filter=filter, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeadsApi->list_leads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| The list of Leads returned can be filtered using one or more of the supported fields and operators.  The supported fields and operators are:    * &#x60;id&#x60; (&#x60;in&#x60;)  * &#x60;corporate.name&#x60; (&#x60;eq&#x60;, &#x60;startswith&#x60;)  * &#x60;currentAdviser.id&#x60; (&#x60;eq&#x60;, &#x60;in&#x60;)  * &#x60;person.firstName&#x60; (&#x60;eq&#x60;, &#x60;startswith&#x60;)  * &#x60;person.lastName&#x60; (&#x60;eq&#x60;, &#x60;startswith&#x60;)  * &#x60;trust.name&#x60; (&#x60;eq&#x60;, &#x60;startswith&#x60;)  * &#x60;tag&#x60; (&#x60;in&#x60;)                Example filters:      filter&#x3D; person.firstName eq &#x27;john&#x27; and person.lastName startswith &#x27;j&#x27;      filter&#x3D; id in &#x27;(987,7654,126)&#x27; and tag in (&#x27;tag1&#x27;, &#x27;tag2&#x27;, &#x27;tag3&#x27;)      top&#x3D;5&amp;Skip&#x3D;22&amp;filter&#x3D; person.firstName eq &#x27;john&#x27; and person.lastName startswith &#x27;j&#x27; and tag in (&#x27;tag1&#x27;, &#x27;tag2&#x27;, &#x27;tag3&#x27;)                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). | [optional] 
 **skip** | **int**| Optional. The number of records to skip. If not specified it defaults to 0. | [optional] [default to 0]
 **top** | **int**| Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. | [optional] [default to 100]

### Return type

[**LeadCollection**](LeadCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lead**
> Lead update_lead(body, authorization, x_api_key, lead_id, accept=accept, tenant_id=tenant_id)

Updates a given lead. 

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
api_instance = swagger_client.LeadsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Lead() # Lead | Lead document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
lead_id = 56 # int | Lead identifier.
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Updates a given lead. 
    api_response = api_instance.update_lead(body, authorization, x_api_key, lead_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeadsApi->update_lead: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Lead**](Lead.md)| Lead document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **lead_id** | **int**| Lead identifier. | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**Lead**](Lead.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

