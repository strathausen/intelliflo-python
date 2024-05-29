# swagger_client.HoldingsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_plan_holdings**](HoldingsApi.md#create_plan_holdings) | **POST** /clients/{clientId}/plans/{planId}/holdings | Creates fund holdings for a given client and plan. 
[**get_client_plan_holding**](HoldingsApi.md#get_client_plan_holding) | **GET** /clients/{clientId}/plans/{planId}/holdings/{holdingId} | Returns a fund holding for a given client, plan and holding. 
[**list_client_plan_holdings**](HoldingsApi.md#list_client_plan_holdings) | **GET** /clients/{clientId}/plans/{planId}/holdings | Returns a list of fund holdings for a given client and plan. 
[**update_client_plan_holding**](HoldingsApi.md#update_client_plan_holding) | **PUT** /clients/{clientId}/plans/{planId}/holdings/{holdingId} | Updates a fund holding for a given client, plan and holding. 

# **create_plan_holdings**
> GetPlanHolding create_plan_holdings(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)

Creates fund holdings for a given client and plan. 

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
api_instance = swagger_client.HoldingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PostPlanHolding() # PostPlanHolding | Plan holding request
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier
plan_id = 56 # int | Plan identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier (optional)

try:
    # Creates fund holdings for a given client and plan. 
    api_response = api_instance.create_plan_holdings(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HoldingsApi->create_plan_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostPlanHolding**](PostPlanHolding.md)| Plan holding request | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **plan_id** | **int**| Plan identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier | [optional] 

### Return type

[**GetPlanHolding**](GetPlanHolding.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_plan_holding**
> GetPlanHolding get_client_plan_holding(authorization, client_id, holding_id, plan_id, x_api_key, accept=accept, prefer=prefer, tenant_id=tenant_id)

Returns a fund holding for a given client, plan and holding. 

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
api_instance = swagger_client.HoldingsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value \"me\" can be used to indicate the authenticated user.
holding_id = 56 # int | Fund Holding identifier
plan_id = 56 # int | Plan identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
prefer = 'prefer_example' # str | Used to indicate preferred behaviour, by the client. Options: include=fundDetails (optional)
tenant_id = 56 # int | Tenant identifier (optional)

try:
    # Returns a fund holding for a given client, plan and holding. 
    api_response = api_instance.get_client_plan_holding(authorization, client_id, holding_id, plan_id, x_api_key, accept=accept, prefer=prefer, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HoldingsApi->get_client_plan_holding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **holding_id** | **int**| Fund Holding identifier | 
 **plan_id** | **int**| Plan identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **prefer** | **str**| Used to indicate preferred behaviour, by the client. Options: include&#x3D;fundDetails | [optional] 
 **tenant_id** | **int**| Tenant identifier | [optional] 

### Return type

[**GetPlanHolding**](GetPlanHolding.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_plan_holdings**
> PlanHoldingCollection list_client_plan_holdings(authorization, client_id, plan_id, x_api_key, accept=accept, filter=filter, order_by=order_by, prefer=prefer, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of fund holdings for a given client and plan. 

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
api_instance = swagger_client.HoldingsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
plan_id = 56 # int | Plan identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | List can be filtered using one or more supported fields and operators below.              For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).              Supported fields (operators) are              `Id` (`in`,`eq`,`ne`,`gt`,`ge`,`lt`,`le`),              `UnitsHolding` (`ne`) (optional)
order_by = 'order_by_example' # str | By default the list will be ordered desc by Id.              However it can be changed using one or more supported fields below.              `Id`              Usage example: `orderby=Id asc` (optional)
prefer = 'prefer_example' # str | Used to indicate preferred behaviour, by the client. Options: include=fundDetails (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
tenant_id = 56 # int | Tenant identifier (optional)
top = 100 # int | The number of records to retrieve (default 25, max 100) (optional) (default to 100)

try:
    # Returns a list of fund holdings for a given client and plan. 
    api_response = api_instance.list_client_plan_holdings(authorization, client_id, plan_id, x_api_key, accept=accept, filter=filter, order_by=order_by, prefer=prefer, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HoldingsApi->list_client_plan_holdings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **plan_id** | **int**| Plan identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| List can be filtered using one or more supported fields and operators below.              For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).              Supported fields (operators) are              &#x60;Id&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;,&#x60;gt&#x60;,&#x60;ge&#x60;,&#x60;lt&#x60;,&#x60;le&#x60;),              &#x60;UnitsHolding&#x60; (&#x60;ne&#x60;) | [optional] 
 **order_by** | **str**| By default the list will be ordered desc by Id.              However it can be changed using one or more supported fields below.              &#x60;Id&#x60;              Usage example: &#x60;orderby&#x3D;Id asc&#x60; | [optional] 
 **prefer** | **str**| Used to indicate preferred behaviour, by the client. Options: include&#x3D;fundDetails | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **tenant_id** | **int**| Tenant identifier | [optional] 
 **top** | **int**| The number of records to retrieve (default 25, max 100) | [optional] [default to 100]

### Return type

[**PlanHoldingCollection**](PlanHoldingCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_plan_holding**
> GetPlanHolding update_client_plan_holding(body, authorization, x_api_key, client_id, holding_id, plan_id, accept=accept, tenant_id=tenant_id)

Updates a fund holding for a given client, plan and holding. 

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
api_instance = swagger_client.HoldingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PostPlanHolding() # PostPlanHolding | Plan holding request
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier
holding_id = 56 # int | Holding identifier
plan_id = 56 # int | Plan identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier (optional)

try:
    # Updates a fund holding for a given client, plan and holding. 
    api_response = api_instance.update_client_plan_holding(body, authorization, x_api_key, client_id, holding_id, plan_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HoldingsApi->update_client_plan_holding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostPlanHolding**](PostPlanHolding.md)| Plan holding request | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **holding_id** | **int**| Holding identifier | 
 **plan_id** | **int**| Plan identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier | [optional] 

### Return type

[**GetPlanHolding**](GetPlanHolding.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

