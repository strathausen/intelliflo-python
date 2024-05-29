# swagger_client.ValuationsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset_valuations**](ValuationsApi.md#create_asset_valuations) | **POST** /clients/{clientId}/assets/{assetId}/valuations | Creates a valuation on a given client and asset. 
[**create_plan_valuations**](ValuationsApi.md#create_plan_valuations) | **POST** /clients/{clientId}/plans/{planId}/valuations | Creates a valuation for a given client and plan. 
[**delete_client_asset_valuation**](ValuationsApi.md#delete_client_asset_valuation) | **DELETE** /clients/{clientId}/assets/{assetId}/valuations/{valuationId} | Deletes an association on a valuation for a given client, asset and valuation. 
[**get_client_asset_valuation**](ValuationsApi.md#get_client_asset_valuation) | **GET** /clients/{clientId}/assets/{assetId}/valuations/{valuationId} | Returns an association on a valuation for a given client, asset and valuation. 
[**get_client_plan_valuation**](ValuationsApi.md#get_client_plan_valuation) | **GET** /clients/{clientId}/plans/{planId}/valuations/{valuationId} | Returns a valuation on a given client, plan and valuation. 
[**list_client_asset_valuations**](ValuationsApi.md#list_client_asset_valuations) | **GET** /clients/{clientId}/assets/{assetId}/valuations | Returns a list of valuations on a given client and asset. 
[**list_client_plan_valuations**](ValuationsApi.md#list_client_plan_valuations) | **GET** /clients/{clientId}/plans/{planId}/valuations | Returns a list of valuations for a given client and plan. 
[**update_client_asset_valuation**](ValuationsApi.md#update_client_asset_valuation) | **PUT** /clients/{clientId}/assets/{assetId}/valuations/{valuationId} | Updates or creates an association on a valuation for a given client, asset and valuation. 
[**update_client_plan_valuation**](ValuationsApi.md#update_client_plan_valuation) | **PUT** /clients/{clientId}/plans/{planId}/valuations/{valuationId} | Updates a valuation on a given client, plan and valuation. 

# **create_asset_valuations**
> AssetValuation create_asset_valuations(body, authorization, x_api_key, asset_id, client_id, accept=accept, tenant_id=tenant_id)

Creates a valuation on a given client and asset. 

All valuations are based on asset.Currency which is read-only within these endpoints. For example; if you POST or PUT value.Currency = EUR value.Amount = 100 whilst the asset.Currency is set to GBP then we will return value.Currency = GBP value.Amount = 100.00. 

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
api_instance = swagger_client.ValuationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AssetValuation() # AssetValuation | The asset document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
asset_id = 56 # int | Asset identifier.
client_id = 56 # int | Client identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | The tenant identifier. (optional)

try:
    # Creates a valuation on a given client and asset. 
    api_response = api_instance.create_asset_valuations(body, authorization, x_api_key, asset_id, client_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValuationsApi->create_asset_valuations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetValuation**](AssetValuation.md)| The asset document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **asset_id** | **int**| Asset identifier. | 
 **client_id** | **int**| Client identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| The tenant identifier. | [optional] 

### Return type

[**AssetValuation**](AssetValuation.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_plan_valuations**
> PlanValuation create_plan_valuations(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)

Creates a valuation for a given client and plan. 

All valuations are based on plan.Currency which is inherited from the parent plan and is read-only within these endpoints. For example; if you POST or PUT value.Currency = EUR value.Amount = 100 whilst the plan.Currency is set to GBP then we will return value.Currency = GBP value.Amount = 100.00. 

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
api_instance = swagger_client.ValuationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PlanValuation() # PlanValuation | Valuation
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client Id - The special value \"me\" can be used to indicate the authenticated user.
plan_id = 56 # int | Plan Id
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int |  (optional)

try:
    # Creates a valuation for a given client and plan. 
    api_response = api_instance.create_plan_valuations(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValuationsApi->create_plan_valuations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlanValuation**](PlanValuation.md)| Valuation | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client Id - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| Plan Id | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**|  | [optional] 

### Return type

[**PlanValuation**](PlanValuation.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_asset_valuation**
> delete_client_asset_valuation(asset_id, authorization, client_id, valuation_id, x_api_key, accept=accept, tenant_id=tenant_id)

Deletes an association on a valuation for a given client, asset and valuation. 

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
api_instance = swagger_client.ValuationsApi(swagger_client.ApiClient(configuration))
asset_id = 56 # int | The asset identifier.
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client identifier.
valuation_id = 56 # int | The valuation identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | The tenant identifier. (optional)

try:
    # Deletes an association on a valuation for a given client, asset and valuation. 
    api_instance.delete_client_asset_valuation(asset_id, authorization, client_id, valuation_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling ValuationsApi->delete_client_asset_valuation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The asset identifier. | 
 **authorization** | **str**|  | 
 **client_id** | **int**| The client identifier. | 
 **valuation_id** | **int**| The valuation identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| The tenant identifier. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_asset_valuation**
> AssetValuation get_client_asset_valuation(asset_id, authorization, client_id, valuation_id, x_api_key, accept=accept)

Returns an association on a valuation for a given client, asset and valuation. 

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
api_instance = swagger_client.ValuationsApi(swagger_client.ApiClient(configuration))
asset_id = 56 # int | The asset identifier.
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client identifier.
valuation_id = 56 # int | The valuation identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns an association on a valuation for a given client, asset and valuation. 
    api_response = api_instance.get_client_asset_valuation(asset_id, authorization, client_id, valuation_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValuationsApi->get_client_asset_valuation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The asset identifier. | 
 **authorization** | **str**|  | 
 **client_id** | **int**| The client identifier. | 
 **valuation_id** | **int**| The valuation identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**AssetValuation**](AssetValuation.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_plan_valuation**
> PlanValuation get_client_plan_valuation(authorization, client_id, plan_id, valuation_id, x_api_key, accept=accept, tenant_id=tenant_id)

Returns a valuation on a given client, plan and valuation. 

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
api_instance = swagger_client.ValuationsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id
plan_id = 56 # int | Plan Id
valuation_id = 789 # int | Valuation Id
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, optionally included (optional)

try:
    # Returns a valuation on a given client, plan and valuation. 
    api_response = api_instance.get_client_plan_valuation(authorization, client_id, plan_id, valuation_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValuationsApi->get_client_plan_valuation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id | 
 **plan_id** | **int**| Plan Id | 
 **valuation_id** | **int**| Valuation Id | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, optionally included | [optional] 

### Return type

[**PlanValuation**](PlanValuation.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_asset_valuations**
> AssetValuationCollection list_client_asset_valuations(asset_id, authorization, client_id, x_api_key, accept=accept, order_by=order_by, skip=skip, top=top)

Returns a list of valuations on a given client and asset. 

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
api_instance = swagger_client.ValuationsApi(swagger_client.ApiClient(configuration))
asset_id = 56 # int | Asset identifier.
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
order_by = 'order_by_example' # str | You can sort on Valuation date(ValueOn) and Amount(Value): e.g. orderby=ValueOn desc, orderby=Value asc (optional)
skip = 0 # int | The skip. (optional) (default to 0)
top = 100 # int | The top. (optional) (default to 100)

try:
    # Returns a list of valuations on a given client and asset. 
    api_response = api_instance.list_client_asset_valuations(asset_id, authorization, client_id, x_api_key, accept=accept, order_by=order_by, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValuationsApi->list_client_asset_valuations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| Asset identifier. | 
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **order_by** | **str**| You can sort on Valuation date(ValueOn) and Amount(Value): e.g. orderby&#x3D;ValueOn desc, orderby&#x3D;Value asc | [optional] 
 **skip** | **int**| The skip. | [optional] [default to 0]
 **top** | **int**| The top. | [optional] [default to 100]

### Return type

[**AssetValuationCollection**](AssetValuationCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_plan_valuations**
> ValuationCollection list_client_plan_valuations(authorization, client_id, plan_id, x_api_key, accept=accept, filter=filter, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of valuations for a given client and plan. 

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
api_instance = swagger_client.ValuationsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client Id
plan_id = 56 # int | Plan Id
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported fields and operators:               * valuedOn (gt, ge, lt, le). (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
tenant_id = 56 # int | Tenant identifier, optionally included (optional)
top = 100 # int | The number of records to retrieve (default 100, max 500) (optional) (default to 100)

try:
    # Returns a list of valuations for a given client and plan. 
    api_response = api_instance.list_client_plan_valuations(authorization, client_id, plan_id, x_api_key, accept=accept, filter=filter, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValuationsApi->list_client_plan_valuations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client Id | 
 **plan_id** | **int**| Plan Id | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported fields and operators:               * valuedOn (gt, ge, lt, le). | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **tenant_id** | **int**| Tenant identifier, optionally included | [optional] 
 **top** | **int**| The number of records to retrieve (default 100, max 500) | [optional] [default to 100]

### Return type

[**ValuationCollection**](ValuationCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_asset_valuation**
> AssetValuation update_client_asset_valuation(body, authorization, x_api_key, asset_id, client_id, valuation_id, accept=accept, tenant_id=tenant_id)

Updates or creates an association on a valuation for a given client, asset and valuation. 

All valuations are based on asset.Currency which is read-only within these endpoints. For example; if you POST or PUT value.Currency = EUR value.Amount = 100 whilst the asset.Currency is set to GBP then we will return value.Currency = GBP value.Amount = 100.00. 

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
api_instance = swagger_client.ValuationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AssetValuation() # AssetValuation | The asset valuation document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
asset_id = 56 # int | The asset identifier.
client_id = 56 # int | The client identifier.
valuation_id = 56 # int | The asset valuation identifier.
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | The tenant identifier. (optional)

try:
    # Updates or creates an association on a valuation for a given client, asset and valuation. 
    api_response = api_instance.update_client_asset_valuation(body, authorization, x_api_key, asset_id, client_id, valuation_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValuationsApi->update_client_asset_valuation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetValuation**](AssetValuation.md)| The asset valuation document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **asset_id** | **int**| The asset identifier. | 
 **client_id** | **int**| The client identifier. | 
 **valuation_id** | **int**| The asset valuation identifier. | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| The tenant identifier. | [optional] 

### Return type

[**AssetValuation**](AssetValuation.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_plan_valuation**
> PlanValuation update_client_plan_valuation(body, authorization, x_api_key, client_id, plan_id, valuation_id, accept=accept, tenant_id=tenant_id)

Updates a valuation on a given client, plan and valuation. 

All valuations are based on plan.Currency which is inherited from the parent plan and is read-only within these endpoints. For example; if you POST or PUT value.Currency = EUR value.Amount = 100 whilst the plan.Currency is set to GBP then we will return value.Currency = GBP value.Amount = 100.00. 

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
api_instance = swagger_client.ValuationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PlanValuation() # PlanValuation | Valuation
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client Id - The special value \"me\" can be used to indicate the authenticated user.
plan_id = 56 # int | Plan Id
valuation_id = 789 # int | ValuationId
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | TenantId (optional)

try:
    # Updates a valuation on a given client, plan and valuation. 
    api_response = api_instance.update_client_plan_valuation(body, authorization, x_api_key, client_id, plan_id, valuation_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValuationsApi->update_client_plan_valuation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlanValuation**](PlanValuation.md)| Valuation | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client Id - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| Plan Id | 
 **valuation_id** | **int**| ValuationId | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| TenantId | [optional] 

### Return type

[**PlanValuation**](PlanValuation.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

