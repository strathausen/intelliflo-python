# swagger_client.IncomesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_income**](IncomesApi.md#create_client_income) | **POST** /clients/{clientId}/incomes | Creates an income record for a client.
[**delete_client_income**](IncomesApi.md#delete_client_income) | **DELETE** /clients/{clientId}/incomes/{incomeId} | Deletes a client&#x27;s income record.
[**get_client_income**](IncomesApi.md#get_client_income) | **GET** /clients/{clientId}/incomes/{incomeId} | Returns the income for a given client and income. 
[**list_client_incomes**](IncomesApi.md#list_client_incomes) | **GET** /clients/{clientId}/incomes | Returns a list of incomes for a given client. 
[**update_client_income**](IncomesApi.md#update_client_income) | **PUT** /clients/{clientId}/incomes/{incomeId} | Updates a client&#x27;s income record.

# **create_client_income**
> Income create_client_income(body, authorization, x_api_key, client_id, accept=accept, prefer=prefer)

Creates an income record for a client.

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
api_instance = swagger_client.IncomesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateIncome() # CreateIncome | The created income record.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | The client identifier. The special value \"me\" can be used to indicate the authenticated user.
accept = 'accept_example' # str |  (optional)
prefer = 'prefer_example' # str | Used to indicate which format the income categories are returned in. Valid options are: 'x-iflo-apiversion=1' or 'x-iflo-apiversion=2'. If not specified the default is 'x-iflo-apiversion=1' (optional)

try:
    # Creates an income record for a client.
    api_response = api_instance.create_client_income(body, authorization, x_api_key, client_id, accept=accept, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomesApi->create_client_income: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateIncome**](CreateIncome.md)| The created income record. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| The client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **accept** | **str**|  | [optional] 
 **prefer** | **str**| Used to indicate which format the income categories are returned in. Valid options are: &#x27;x-iflo-apiversion&#x3D;1&#x27; or &#x27;x-iflo-apiversion&#x3D;2&#x27;. If not specified the default is &#x27;x-iflo-apiversion&#x3D;1&#x27; | [optional] 

### Return type

[**Income**](Income.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_income**
> delete_client_income(authorization, client_id, income_id, x_api_key, accept=accept)

Deletes a client's income record.

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
api_instance = swagger_client.IncomesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client identifier. The special value \"me\" can be used to indicate the authenticated user.
income_id = 56 # int | The identifier for the income record.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes a client's income record.
    api_instance.delete_client_income(authorization, client_id, income_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling IncomesApi->delete_client_income: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| The client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **income_id** | **int**| The identifier for the income record. | 
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

# **get_client_income**
> Income get_client_income(authorization, client_id, income_id, x_api_key, accept=accept, prefer=prefer)

Returns the income for a given client and income. 

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
api_instance = swagger_client.IncomesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client identifier. The special value \"me\" can be used to indicate the authenticated user.
income_id = 56 # int | The identifier for the income record.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
prefer = 'prefer_example' # str | Used to indicate which format the income categories are returned in. Valid options are: 'x-iflo-apiversion=1' or 'x-iflo-apiversion=2'. If not specified the default is 'x-iflo-apiversion=1' (optional)

try:
    # Returns the income for a given client and income. 
    api_response = api_instance.get_client_income(authorization, client_id, income_id, x_api_key, accept=accept, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomesApi->get_client_income: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| The client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **income_id** | **int**| The identifier for the income record. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **prefer** | **str**| Used to indicate which format the income categories are returned in. Valid options are: &#x27;x-iflo-apiversion&#x3D;1&#x27; or &#x27;x-iflo-apiversion&#x3D;2&#x27;. If not specified the default is &#x27;x-iflo-apiversion&#x3D;1&#x27; | [optional] 

### Return type

[**Income**](Income.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_incomes**
> IncomeCollection list_client_incomes(authorization, client_id, x_api_key, accept=accept, filter=filter, prefer=prefer, skip=skip, top=top)

Returns a list of incomes for a given client. 

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
api_instance = swagger_client.IncomesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client identifier. The special value \"me\" can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | The returned list of questions can be filtered using one or more of the following supported fields and operators:                * `id` (`in`)  * `employment.id` (`in`, `eq`)  * `frequency` (`in`, `eq`, `ne`)                Usage examples:  * `filter=id in (1,2)`  * `filter=employment.id eq 22 and id in (1,2)`  * `filter=frequency eq 'Single' or frequency in ('Single','Monthly')`.                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). (optional)
prefer = 'prefer_example' # str | Used to indicate which format the income categories are returned in. Valid options are: 'x-iflo-apiversion=1' or 'x-iflo-apiversion=2'. If not specified the default is 'x-iflo-apiversion=1' (optional)
skip = 0 # int | Optional. Number of records to skip. Must be greater than or equal to zero. Defaults to zero if not specified. (optional) (default to 0)
top = 100 # int | Optional. The number of records to retrieve (max 500). Defaults to 100 if not specified. (optional) (default to 100)

try:
    # Returns a list of incomes for a given client. 
    api_response = api_instance.list_client_incomes(authorization, client_id, x_api_key, accept=accept, filter=filter, prefer=prefer, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomesApi->list_client_incomes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| The client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| The returned list of questions can be filtered using one or more of the following supported fields and operators:                * &#x60;id&#x60; (&#x60;in&#x60;)  * &#x60;employment.id&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;)  * &#x60;frequency&#x60; (&#x60;in&#x60;, &#x60;eq&#x60;, &#x60;ne&#x60;)                Usage examples:  * &#x60;filter&#x3D;id in (1,2)&#x60;  * &#x60;filter&#x3D;employment.id eq 22 and id in (1,2)&#x60;  * &#x60;filter&#x3D;frequency eq &#x27;Single&#x27; or frequency in (&#x27;Single&#x27;,&#x27;Monthly&#x27;)&#x60;.                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). | [optional] 
 **prefer** | **str**| Used to indicate which format the income categories are returned in. Valid options are: &#x27;x-iflo-apiversion&#x3D;1&#x27; or &#x27;x-iflo-apiversion&#x3D;2&#x27;. If not specified the default is &#x27;x-iflo-apiversion&#x3D;1&#x27; | [optional] 
 **skip** | **int**| Optional. Number of records to skip. Must be greater than or equal to zero. Defaults to zero if not specified. | [optional] [default to 0]
 **top** | **int**| Optional. The number of records to retrieve (max 500). Defaults to 100 if not specified. | [optional] [default to 100]

### Return type

[**IncomeCollection**](IncomeCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_income**
> Income update_client_income(body, authorization, x_api_key, client_id, income_id, accept=accept, prefer=prefer)

Updates a client's income record.

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
api_instance = swagger_client.IncomesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Income() # Income | The updated income record.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | The client identifier. The special value \"me\" can be used to indicate the authenticated user.
income_id = 56 # int | The identifier for the income record.
accept = 'accept_example' # str |  (optional)
prefer = 'prefer_example' # str | Used to indicate which format the income categories are returned in. Valid options are: 'x-iflo-apiversion=1' or 'x-iflo-apiversion=2'. If not specified the default is 'x-iflo-apiversion=1' (optional)

try:
    # Updates a client's income record.
    api_response = api_instance.update_client_income(body, authorization, x_api_key, client_id, income_id, accept=accept, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomesApi->update_client_income: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Income**](Income.md)| The updated income record. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| The client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **income_id** | **int**| The identifier for the income record. | 
 **accept** | **str**|  | [optional] 
 **prefer** | **str**| Used to indicate which format the income categories are returned in. Valid options are: &#x27;x-iflo-apiversion&#x3D;1&#x27; or &#x27;x-iflo-apiversion&#x3D;2&#x27;. If not specified the default is &#x27;x-iflo-apiversion&#x3D;1&#x27; | [optional] 

### Return type

[**Income**](Income.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

