# swagger_client.ChargesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_plan_charge**](ChargesApi.md#create_client_plan_charge) | **POST** /clients/{clientId}/plans/{planId}/charges | Creates a new charge for a client&#x27;s plan.
[**delete_client_plan_charge**](ChargesApi.md#delete_client_plan_charge) | **DELETE** /clients/{clientId}/plans/{planId}/charges/{chargeId} | Deletes an existing charge for a client&#x27;s plan.
[**get_client_plan_charge**](ChargesApi.md#get_client_plan_charge) | **GET** /clients/{clientId}/plans/{planId}/charges/{chargeId} | Returns a single charge for a client&#x27;s plan.
[**list_client_plan_charges**](ChargesApi.md#list_client_plan_charges) | **GET** /clients/{clientId}/plans/{planId}/charges | Returns a list of charge for a client&#x27;s plan.
[**update_client_plan_charge**](ChargesApi.md#update_client_plan_charge) | **PUT** /clients/{clientId}/plans/{planId}/charges/{chargeId} | Updates an existing charge for a client&#x27;s plan.

# **create_client_plan_charge**
> PlanCharge create_client_plan_charge(body, authorization, x_api_key, client_id, plan_id, accept=accept)

Creates a new charge for a client's plan.

Creates a new charge for a client's plan.

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
api_instance = swagger_client.ChargesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PlanCharge() # PlanCharge | Charge document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier. The special value 'me' can be used to indicate the authenticated user.
plan_id = 56 # int | Plan identifier.
accept = 'accept_example' # str |  (optional)

try:
    # Creates a new charge for a client's plan.
    api_response = api_instance.create_client_plan_charge(body, authorization, x_api_key, client_id, plan_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargesApi->create_client_plan_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlanCharge**](PlanCharge.md)| Charge document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| Plan identifier. | 
 **accept** | **str**|  | [optional] 

### Return type

[**PlanCharge**](PlanCharge.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_plan_charge**
> delete_client_plan_charge(authorization, charge_id, client_id, plan_id, x_api_key, accept=accept)

Deletes an existing charge for a client's plan.

Deletes an existing charge for a client's plan.

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
api_instance = swagger_client.ChargesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
charge_id = 56 # int | Charge Id.
client_id = 56 # int | Client identifier. The special value 'me' can be used to indicate the authenticated user.
plan_id = 56 # int | Plan identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes an existing charge for a client's plan.
    api_instance.delete_client_plan_charge(authorization, charge_id, client_id, plan_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling ChargesApi->delete_client_plan_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **charge_id** | **int**| Charge Id. | 
 **client_id** | **int**| Client identifier. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| Plan identifier. | 
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

# **get_client_plan_charge**
> PlanCharge get_client_plan_charge(authorization, charge_id, client_id, plan_id, x_api_key, accept=accept)

Returns a single charge for a client's plan.

Returns a single charge for a client's plan. A charge is a cost related to a plan/product.                **Notes**:  * Charges are separate to adviser fees.  * Charge types can be One-off Charge, Ongoing Charge, Transaction Cost, Incidental Cost.  * There can be multiple charges recorded against a plan.

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
api_instance = swagger_client.ChargesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
charge_id = 56 # int | Charge identifier.
client_id = 56 # int | Client identifier. The special value 'me' can be used to indicate the authenticated user.
plan_id = 56 # int | Plan identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a single charge for a client's plan.
    api_response = api_instance.get_client_plan_charge(authorization, charge_id, client_id, plan_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargesApi->get_client_plan_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **charge_id** | **int**| Charge identifier. | 
 **client_id** | **int**| Client identifier. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| Plan identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**PlanCharge**](PlanCharge.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_plan_charges**
> PlanChargeCollection list_client_plan_charges(authorization, client_id, plan_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of charge for a client's plan.

Returns a list of charge for a client's plan.                Filtering:  * `chargedOn` can be filtered by equals (`eq`), greater than (`gt`), greater or equal (`ge`), less than (`lt`), less than or equal (`le`).  * `totalAmount` can be filtered by greater than (`gt`), greater or equal (`ge`), less than (`lt`), less than or equal (`le`).  * `id` and `type` can be filtered using `in`.                Multiple filter expressions can be combined using `and` operator.                *Examples:* top=5&skip=22&filter= type in ('OneOffCharge', 'OngoingCharge') and chargedOn ge '2018-01-01' and id in '(987,654,126)'

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
api_instance = swagger_client.ChargesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier. The special value 'me' can be used to indicate the authenticated user.
plan_id = 56 # int | Plan identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Optional. Supported operators: 'and', 'gt', 'ge', 'lt', 'le','eq', 'ne', 'in', 'not', 'or'. Available Fields: 'id', 'type', 'chargedOn', 'totalAmount'. (optional)
orderby = 'orderby_example' # str | Optional. Supported fields: 'id', 'type', 'chargedOn', 'totalAmount'. If 'asc' or 'desc' not specified, then the resources will be ordered in ascending order. e.g: 'orderby=id asc'. (optional)
skip = 0 # int | Number of records to skip. Default value is '0'. Must be greater than or equal to zero. (optional) (default to 0)
top = 100 # int | Number of records to retrieve. Default value is '100'. Must be greater than zero. Max allowed value is '250'. (optional) (default to 100)

try:
    # Returns a list of charge for a client's plan.
    api_response = api_instance.list_client_plan_charges(authorization, client_id, plan_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargesApi->list_client_plan_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| Plan identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Optional. Supported operators: &#x27;and&#x27;, &#x27;gt&#x27;, &#x27;ge&#x27;, &#x27;lt&#x27;, &#x27;le&#x27;,&#x27;eq&#x27;, &#x27;ne&#x27;, &#x27;in&#x27;, &#x27;not&#x27;, &#x27;or&#x27;. Available Fields: &#x27;id&#x27;, &#x27;type&#x27;, &#x27;chargedOn&#x27;, &#x27;totalAmount&#x27;. | [optional] 
 **orderby** | **str**| Optional. Supported fields: &#x27;id&#x27;, &#x27;type&#x27;, &#x27;chargedOn&#x27;, &#x27;totalAmount&#x27;. If &#x27;asc&#x27; or &#x27;desc&#x27; not specified, then the resources will be ordered in ascending order. e.g: &#x27;orderby&#x3D;id asc&#x27;. | [optional] 
 **skip** | **int**| Number of records to skip. Default value is &#x27;0&#x27;. Must be greater than or equal to zero. | [optional] [default to 0]
 **top** | **int**| Number of records to retrieve. Default value is &#x27;100&#x27;. Must be greater than zero. Max allowed value is &#x27;250&#x27;. | [optional] [default to 100]

### Return type

[**PlanChargeCollection**](PlanChargeCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_plan_charge**
> PlanCharge update_client_plan_charge(body, authorization, x_api_key, charge_id, client_id, plan_id, accept=accept)

Updates an existing charge for a client's plan.

Updates an existing charge for a client's plan.

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
api_instance = swagger_client.ChargesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PlanCharge() # PlanCharge | Plan Charge document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
charge_id = 56 # int | Charge Id.
client_id = 56 # int | Client identifier. The special value 'me' can be used to indicate the authenticated user.
plan_id = 56 # int | Plan identifier.
accept = 'accept_example' # str |  (optional)

try:
    # Updates an existing charge for a client's plan.
    api_response = api_instance.update_client_plan_charge(body, authorization, x_api_key, charge_id, client_id, plan_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargesApi->update_client_plan_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlanCharge**](PlanCharge.md)| Plan Charge document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **charge_id** | **int**| Charge Id. | 
 **client_id** | **int**| Client identifier. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **plan_id** | **int**| Plan identifier. | 
 **accept** | **str**|  | [optional] 

### Return type

[**PlanCharge**](PlanCharge.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

