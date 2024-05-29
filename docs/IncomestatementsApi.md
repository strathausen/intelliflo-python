# swagger_client.IncomestatementsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_income_statement**](IncomestatementsApi.md#create_income_statement) | **POST** /incomestatements | Creates a new income statement.
[**create_income_statement_items**](IncomestatementsApi.md#create_income_statement_items) | **POST** /incomestatements/{incomeStatementId}/items | Creates income statement items for an income statement.
[**delete_income_statement**](IncomestatementsApi.md#delete_income_statement) | **DELETE** /incomestatements/{incomeStatementId} | Deletes an existing income statement.
[**get_income_statement**](IncomestatementsApi.md#get_income_statement) | **GET** /incomestatements/{incomeStatementId} | Returns an income statement.
[**get_income_statement_item**](IncomestatementsApi.md#get_income_statement_item) | **GET** /incomestatements/{incomeStatementId}/items/{incomeStatementItemId} | Returns a given item for a given income statement.
[**list_income_statement_items**](IncomestatementsApi.md#list_income_statement_items) | **GET** /incomestatements/{incomeStatementId}/items | Returns a list of items for a given income statement.
[**list_income_statements**](IncomestatementsApi.md#list_income_statements) | **GET** /incomestatements | Returns a list of income statements.
[**update_income_statement**](IncomestatementsApi.md#update_income_statement) | **PUT** /incomestatements/{incomeStatementId} | Updates an income statement.
[**update_income_statement_item**](IncomestatementsApi.md#update_income_statement_item) | **PUT** /incomestatements/{incomeStatementId}/items/{incomeStatementItemId} | Updates an income statement item for a given income statement.

# **create_income_statement**
> IncomeStatement create_income_statement(body, authorization, x_api_key, accept=accept)

Creates a new income statement.

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
api_instance = swagger_client.IncomestatementsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IncomeStatement() # IncomeStatement | Income statement document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Creates a new income statement.
    api_response = api_instance.create_income_statement(body, authorization, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomestatementsApi->create_income_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IncomeStatement**](IncomeStatement.md)| Income statement document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**IncomeStatement**](IncomeStatement.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_income_statement_items**
> create_income_statement_items(body, authorization, x_api_key, income_statement_id, accept=accept)

Creates income statement items for an income statement.

Add income statement items to an existing income statement.  There is a limit of 10000 items per post, however you can make multiple posts.  You cannot post if the statement is matched or any of the items are analysed.

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
api_instance = swagger_client.IncomestatementsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IncomeStatementItemBatch() # IncomeStatementItemBatch | A batch of income statement items
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
income_statement_id = 56 # int | Income statement identifier
accept = 'accept_example' # str |  (optional)

try:
    # Creates income statement items for an income statement.
    api_instance.create_income_statement_items(body, authorization, x_api_key, income_statement_id, accept=accept)
except ApiException as e:
    print("Exception when calling IncomestatementsApi->create_income_statement_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IncomeStatementItemBatch**](IncomeStatementItemBatch.md)| A batch of income statement items | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **income_statement_id** | **int**| Income statement identifier | 
 **accept** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_income_statement**
> delete_income_statement(authorization, income_statement_id, x_api_key, accept=accept)

Deletes an existing income statement.

You can only delete an income statement if it is not matched and none of the items are analysed.  This will delete the income statement and the associated items.

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
api_instance = swagger_client.IncomestatementsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
income_statement_id = 56 # int | Income statement identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes an existing income statement.
    api_instance.delete_income_statement(authorization, income_statement_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling IncomestatementsApi->delete_income_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **income_statement_id** | **int**| Income statement identifier | 
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

# **get_income_statement**
> IncomeStatement get_income_statement(authorization, income_statement_id, x_api_key, accept=accept)

Returns an income statement.

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
api_instance = swagger_client.IncomestatementsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
income_statement_id = 56 # int | Income statement identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns an income statement.
    api_response = api_instance.get_income_statement(authorization, income_statement_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomestatementsApi->get_income_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **income_statement_id** | **int**| Income statement identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**IncomeStatement**](IncomeStatement.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_income_statement_item**
> IncomeStatementItem get_income_statement_item(authorization, income_statement_id, income_statement_item_id, x_api_key, accept=accept)

Returns a given item for a given income statement.

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
api_instance = swagger_client.IncomestatementsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
income_statement_id = 56 # int | Income statement identifier
income_statement_item_id = 56 # int | Income statement item identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a given item for a given income statement.
    api_response = api_instance.get_income_statement_item(authorization, income_statement_id, income_statement_item_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomestatementsApi->get_income_statement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **income_statement_id** | **int**| Income statement identifier | 
 **income_statement_item_id** | **int**| Income statement item identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**IncomeStatementItem**](IncomeStatementItem.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_income_statement_items**
> IncomeStatementItemCollection list_income_statement_items(authorization, income_statement_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of items for a given income statement.

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
api_instance = swagger_client.IncomestatementsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
income_statement_id = 56 # int | Income statement identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:   * __id__ ( in, eq, ne, gt, ge, lt, le )   * __type__ ( in, eq )   * __isAnalysed__ ( eq, ne )    Usage example: `isAnalysed eq false and type in ('OngFee', 'Lvl')` (optional)
orderby = 'orderby_example' # str | By default the list will be ordered desc by Id.    However it can be changed using one or more supported fields below.  Supported fields:   * __id__   (asc,desc)  * __type__ (asc,desc)  * __isAnalysed__ (asc,desc)    Usage example: `orderby=type asc` (optional)
skip = 0 # int | Index from which the results will start. (optional) (default to 0)
top = 100 # int | Number of records to retrieve (optional) (default to 100)

try:
    # Returns a list of items for a given income statement.
    api_response = api_instance.list_income_statement_items(authorization, income_statement_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomestatementsApi->list_income_statement_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **income_statement_id** | **int**| Income statement identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:   * __id__ ( in, eq, ne, gt, ge, lt, le )   * __type__ ( in, eq )   * __isAnalysed__ ( eq, ne )    Usage example: &#x60;isAnalysed eq false and type in (&#x27;OngFee&#x27;, &#x27;Lvl&#x27;)&#x60; | [optional] 
 **orderby** | **str**| By default the list will be ordered desc by Id.    However it can be changed using one or more supported fields below.  Supported fields:   * __id__   (asc,desc)  * __type__ (asc,desc)  * __isAnalysed__ (asc,desc)    Usage example: &#x60;orderby&#x3D;type asc&#x60; | [optional] 
 **skip** | **int**| Index from which the results will start. | [optional] [default to 0]
 **top** | **int**| Number of records to retrieve | [optional] [default to 100]

### Return type

[**IncomeStatementItemCollection**](IncomeStatementItemCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_income_statements**
> IncomeStatementCollection list_income_statements(authorization, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of income statements.

If called with  [Tenant Client Credentials Flow](/docs/Authentication#TCCFlow) and firm_data.incomestatement then it will return income statements for the authenticated client(app) and tenant.  If you add the additional app_data scope then you will receive all your apps data.

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
api_instance = swagger_client.IncomestatementsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:   * __id__ ( in, eq, ne, gt, ge, lt, le )   * __date__ ( eq, ne, gt, ge, lt, le )   * __isMatched__ ( eq, ne )   * __reference__ ( eq, in, startswith )    Usage example: `isMatched eq true and date gt '2019-01-01T00:00:00.000'` (optional)
orderby = 'orderby_example' # str | By default the list will be ordered desc by Id.    However it can be changed using one or more supported fields below.  Supported fields:   * __id__  * __date__  * __reference__    Usage example: `orderby=date asc` (optional)
skip = 0 # int | Index from which the results will start. (optional) (default to 0)
top = 100 # int | Number of records to retrieve (optional) (default to 100)

try:
    # Returns a list of income statements.
    api_response = api_instance.list_income_statements(authorization, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomestatementsApi->list_income_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:   * __id__ ( in, eq, ne, gt, ge, lt, le )   * __date__ ( eq, ne, gt, ge, lt, le )   * __isMatched__ ( eq, ne )   * __reference__ ( eq, in, startswith )    Usage example: &#x60;isMatched eq true and date gt &#x27;2019-01-01T00:00:00.000&#x27;&#x60; | [optional] 
 **orderby** | **str**| By default the list will be ordered desc by Id.    However it can be changed using one or more supported fields below.  Supported fields:   * __id__  * __date__  * __reference__    Usage example: &#x60;orderby&#x3D;date asc&#x60; | [optional] 
 **skip** | **int**| Index from which the results will start. | [optional] [default to 0]
 **top** | **int**| Number of records to retrieve | [optional] [default to 100]

### Return type

[**IncomeStatementCollection**](IncomeStatementCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_income_statement**
> IncomeStatement update_income_statement(body, authorization, x_api_key, income_statement_id, accept=accept)

Updates an income statement.

You can only edit the income statement if it is not matched and none of the items are analysed.

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
api_instance = swagger_client.IncomestatementsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IncomeStatement() # IncomeStatement | Income statement document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
income_statement_id = 56 # int | Income statement identifier
accept = 'accept_example' # str |  (optional)

try:
    # Updates an income statement.
    api_response = api_instance.update_income_statement(body, authorization, x_api_key, income_statement_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomestatementsApi->update_income_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IncomeStatement**](IncomeStatement.md)| Income statement document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **income_statement_id** | **int**| Income statement identifier | 
 **accept** | **str**|  | [optional] 

### Return type

[**IncomeStatement**](IncomeStatement.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_income_statement_item**
> IncomeStatementItem update_income_statement_item(body, authorization, x_api_key, income_statement_id, income_statement_item_id, accept=accept)

Updates an income statement item for a given income statement.

You cannot edit any properties if the item is analysed.  You can edit policy and client if the item is not analysed and the statement is matched.  You can edit policy, client and gross amount if the item is not analysed and the statement is not matched.

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
api_instance = swagger_client.IncomestatementsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IncomeStatementItem() # IncomeStatementItem | Income statement item document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
income_statement_id = 56 # int | Income statement identifier
income_statement_item_id = 56 # int | Income statement item identifier
accept = 'accept_example' # str |  (optional)

try:
    # Updates an income statement item for a given income statement.
    api_response = api_instance.update_income_statement_item(body, authorization, x_api_key, income_statement_id, income_statement_item_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncomestatementsApi->update_income_statement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IncomeStatementItem**](IncomeStatementItem.md)| Income statement item document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **income_statement_id** | **int**| Income statement identifier | 
 **income_statement_item_id** | **int**| Income statement item identifier | 
 **accept** | **str**|  | [optional] 

### Return type

[**IncomeStatementItem**](IncomeStatementItem.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

