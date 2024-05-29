# swagger_client.TransactionsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_create_client_transactions**](TransactionsApi.md#batch_create_client_transactions) | **POST** /clients/{clientId}/transactions | Creates a batch of transactions for different plans for a particular client.
[**batch_create_transactions**](TransactionsApi.md#batch_create_transactions) | **POST** /transactions | Creates a batch of transactions for different plans.
[**client_plan_transaction_exists**](TransactionsApi.md#client_plan_transaction_exists) | **HEAD** /clients/{clientId}/plans/{planId}/transactions/{transactionId} | Check to see if a transaction exists.
[**get_client_plan_transaction**](TransactionsApi.md#get_client_plan_transaction) | **GET** /clients/{clientId}/plans/{planId}/transactions/{transactionId} | Gets a single transaction by id.
[**list_client_plan_transactions**](TransactionsApi.md#list_client_plan_transactions) | **GET** /clients/{clientId}/plans/{planId}/transactions | Returns a list of transactions for a client plan.
[**list_client_transactions**](TransactionsApi.md#list_client_transactions) | **GET** /clients/{clientId}/transactions | Returns a list of transactions for a client.
[**update_client_plan_transaction**](TransactionsApi.md#update_client_plan_transaction) | **PATCH** /clients/{clientId}/plans/{planId}/transactions/{transactionId} | Updates a client plan transaction.

# **batch_create_client_transactions**
> TransactionBatchResponse batch_create_client_transactions(body, authorization, x_api_key, client_id, accept=accept, x_iflo_batch_ignore_error=x_iflo_batch_ignore_error, tenant_id=tenant_id)

Creates a batch of transactions for different plans for a particular client.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransactionBatch() # TransactionBatch | A collection of transactions.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client Id
accept = 'accept_example' # str |  (optional)
x_iflo_batch_ignore_error = false # bool | You can choose to set \"x-iflo-ignore-error=true\" when posting a batch of transactions.              This processes the entire batch and skip any row containing transaction we cannot match against the plan or underlying holding. (optional) (default to false)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Creates a batch of transactions for different plans for a particular client.
    api_response = api_instance.batch_create_client_transactions(body, authorization, x_api_key, client_id, accept=accept, x_iflo_batch_ignore_error=x_iflo_batch_ignore_error, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->batch_create_client_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionBatch**](TransactionBatch.md)| A collection of transactions. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client Id | 
 **accept** | **str**|  | [optional] 
 **x_iflo_batch_ignore_error** | **bool**| You can choose to set \&quot;x-iflo-ignore-error&#x3D;true\&quot; when posting a batch of transactions.              This processes the entire batch and skip any row containing transaction we cannot match against the plan or underlying holding. | [optional] [default to false]
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

[**TransactionBatchResponse**](TransactionBatchResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_create_transactions**
> TransactionBatchResponse batch_create_transactions(body, authorization, x_api_key, accept=accept, x_iflo_batch_ignore_error=x_iflo_batch_ignore_error, tenant_id=tenant_id)

Creates a batch of transactions for different plans.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransactionBatch() # TransactionBatch | A collection of transactions.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
x_iflo_batch_ignore_error = false # bool | You can choose to set \"x-iflo-ignore-error=true\" when posting a batch of transactions.              This processes the entire batch and skip any row containing transaction we cannot match against the plan or underlying holding. (optional) (default to false)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Creates a batch of transactions for different plans.
    api_response = api_instance.batch_create_transactions(body, authorization, x_api_key, accept=accept, x_iflo_batch_ignore_error=x_iflo_batch_ignore_error, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->batch_create_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionBatch**](TransactionBatch.md)| A collection of transactions. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **x_iflo_batch_ignore_error** | **bool**| You can choose to set \&quot;x-iflo-ignore-error&#x3D;true\&quot; when posting a batch of transactions.              This processes the entire batch and skip any row containing transaction we cannot match against the plan or underlying holding. | [optional] [default to false]
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

[**TransactionBatchResponse**](TransactionBatchResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_plan_transaction_exists**
> client_plan_transaction_exists(authorization, client_id, plan_id, transaction_id, x_api_key, accept=accept, tenant_id=tenant_id)

Check to see if a transaction exists.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id - the special value \\\"me\\\" can be used to indicate the authenticated user.
plan_id = 56 # int | Plan Id - the id of the plan.
transaction_id = 789 # int | Transaction Id - the id of the transaction.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Check to see if a transaction exists.
    api_instance.client_plan_transaction_exists(authorization, client_id, plan_id, transaction_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling TransactionsApi->client_plan_transaction_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id - the special value \\\&quot;me\\\&quot; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| Plan Id - the id of the plan. | 
 **transaction_id** | **int**| Transaction Id - the id of the transaction. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_plan_transaction**
> Transaction get_client_plan_transaction(authorization, client_id, plan_id, transaction_id, x_api_key, accept=accept, tenant_id=tenant_id)

Gets a single transaction by id.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id - the special value \\\"me\\\" can be used to indicate the authenticated user.
plan_id = 56 # int | Plan Id - the id of the plan.
transaction_id = 789 # int | Transaction Id - the id of the transaction.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Gets a single transaction by id.
    api_response = api_instance.get_client_plan_transaction(authorization, client_id, plan_id, transaction_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_client_plan_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id - the special value \\\&quot;me\\\&quot; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| Plan Id - the id of the plan. | 
 **transaction_id** | **int**| Transaction Id - the id of the transaction. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_plan_transactions**
> TransactionCollection list_client_plan_transactions(authorization, client_id, plan_id, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of transactions for a client plan.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id - the id of the client.
plan_id = 56 # int | Plan Id - the id of the plan.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:  * `id` (eq,ne,gt,ge,lt,le,in)  * `source` (eq)  * `debitCreditIndicator` (eq)  * `type` (eq, in)  * `transactionDate` (le,lt,gt,ge,eq)  * `category1` (eq,ne)  * `category2` (eq,ne)  * `description` (eq,startswith)  * `gross` (eq,ne,gt,ge,lt,le,in)  * `unitPrice` (eq,ne,gt,ge,lt,le,in)  * `externalReference` (eq,ne,startswith,in) (optional)
order_by = 'order_by_example' # str | By default the list will be ordered desc by Id.  However it can be changed using one or more supported fields below.  Supported fields:  * `transactionDate`  * `category1`  * `category2`  * `description`  * `gross`                Supported directions asc, desc. (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
tenant_id = 56 # int | Tenant Id (optional)
top = 100 # int | The number of records to retrieve (default 100, max 500). (optional) (default to 100)

try:
    # Returns a list of transactions for a client plan.
    api_response = api_instance.list_client_plan_transactions(authorization, client_id, plan_id, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->list_client_plan_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id - the id of the client. | 
 **plan_id** | **int**| Plan Id - the id of the plan. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:  * &#x60;id&#x60; (eq,ne,gt,ge,lt,le,in)  * &#x60;source&#x60; (eq)  * &#x60;debitCreditIndicator&#x60; (eq)  * &#x60;type&#x60; (eq, in)  * &#x60;transactionDate&#x60; (le,lt,gt,ge,eq)  * &#x60;category1&#x60; (eq,ne)  * &#x60;category2&#x60; (eq,ne)  * &#x60;description&#x60; (eq,startswith)  * &#x60;gross&#x60; (eq,ne,gt,ge,lt,le,in)  * &#x60;unitPrice&#x60; (eq,ne,gt,ge,lt,le,in)  * &#x60;externalReference&#x60; (eq,ne,startswith,in) | [optional] 
 **order_by** | **str**| By default the list will be ordered desc by Id.  However it can be changed using one or more supported fields below.  Supported fields:  * &#x60;transactionDate&#x60;  * &#x60;category1&#x60;  * &#x60;category2&#x60;  * &#x60;description&#x60;  * &#x60;gross&#x60;                Supported directions asc, desc. | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **tenant_id** | **int**| Tenant Id | [optional] 
 **top** | **int**| The number of records to retrieve (default 100, max 500). | [optional] [default to 100]

### Return type

[**TransactionCollection**](TransactionCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_transactions**
> TransactionCollection list_client_transactions(authorization, client_id, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of transactions for a client.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id - the id of the client.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:  * `id` (eq,ne,gt,ge,lt,le,in)  * `source` (eq)  * `plan.id` (eq,in)  * `debitCreditIndicator` (eq)  * `type` (eq, in)  * `transactionDate` (le,lt,gt,ge,eq)  * `category1` (eq,ne)  * `category2` (eq,ne)  * `description` (eq,startswith)  * `gross` (eq,ne,gt,ge,lt,le,in)  * `unitPrice` (eq,ne,gt,ge,lt,le,in)  * `externalReference` (eq,ne,startswith,in) (optional)
order_by = 'order_by_example' # str | By default the list will be ordered desc by Id.  However it can be changed using one or more supported fields below.  Supported fields:  * `transactionDate`  * `category1`  * `category2`  * `description`  * `gross`                Supported directions asc, desc. (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
tenant_id = 56 # int | Tenant Id (optional)
top = 100 # int | The number of records to retrieve (default 100, max 500). (optional) (default to 100)

try:
    # Returns a list of transactions for a client.
    api_response = api_instance.list_client_transactions(authorization, client_id, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->list_client_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id - the id of the client. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:  * &#x60;id&#x60; (eq,ne,gt,ge,lt,le,in)  * &#x60;source&#x60; (eq)  * &#x60;plan.id&#x60; (eq,in)  * &#x60;debitCreditIndicator&#x60; (eq)  * &#x60;type&#x60; (eq, in)  * &#x60;transactionDate&#x60; (le,lt,gt,ge,eq)  * &#x60;category1&#x60; (eq,ne)  * &#x60;category2&#x60; (eq,ne)  * &#x60;description&#x60; (eq,startswith)  * &#x60;gross&#x60; (eq,ne,gt,ge,lt,le,in)  * &#x60;unitPrice&#x60; (eq,ne,gt,ge,lt,le,in)  * &#x60;externalReference&#x60; (eq,ne,startswith,in) | [optional] 
 **order_by** | **str**| By default the list will be ordered desc by Id.  However it can be changed using one or more supported fields below.  Supported fields:  * &#x60;transactionDate&#x60;  * &#x60;category1&#x60;  * &#x60;category2&#x60;  * &#x60;description&#x60;  * &#x60;gross&#x60;                Supported directions asc, desc. | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **tenant_id** | **int**| Tenant Id | [optional] 
 **top** | **int**| The number of records to retrieve (default 100, max 500). | [optional] [default to 100]

### Return type

[**TransactionCollection**](TransactionCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_plan_transaction**
> Transaction update_client_plan_transaction(body, authorization, x_api_key, client_id, plan_id, transaction_id, accept=accept, tenant_id=tenant_id)

Updates a client plan transaction.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.Operation()] # list[Operation] | A Json Patch document containing details of modifications to be made to the client plan transaction resource.
Only the following paths may be modified:
* `/category1`
* `/category1Code`
* `/category2`
* `/category2Code1`
* `/description`
* `/unitPrice`
* `/unitNumber`
* `/transactionDate`
            
For a simple example a request contains the following JSON:
            
{
    "op": "replace",
    "path": "/category1",
    "value": "New Category 1"
}
            
would result in the category1 value for the targeted resource being set to 'New Category 1'.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client Id
plan_id = 56 # int | Plan Id
transaction_id = 789 # int | Transaction Id
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Id (optional)

try:
    # Updates a client plan transaction.
    api_response = api_instance.update_client_plan_transaction(body, authorization, x_api_key, client_id, plan_id, transaction_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->update_client_plan_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Operation]**](Operation.md)| A Json Patch document containing details of modifications to be made to the client plan transaction resource.
Only the following paths may be modified:
* &#x60;/category1&#x60;
* &#x60;/category1Code&#x60;
* &#x60;/category2&#x60;
* &#x60;/category2Code1&#x60;
* &#x60;/description&#x60;
* &#x60;/unitPrice&#x60;
* &#x60;/unitNumber&#x60;
* &#x60;/transactionDate&#x60;
            
For a simple example a request contains the following JSON:
            
{
    &quot;op&quot;: &quot;replace&quot;,
    &quot;path&quot;: &quot;/category1&quot;,
    &quot;value&quot;: &quot;New Category 1&quot;
}
            
would result in the category1 value for the targeted resource being set to &#x27;New Category 1&#x27;. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client Id | 
 **plan_id** | **int**| Plan Id | 
 **transaction_id** | **int**| Transaction Id | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Id | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

