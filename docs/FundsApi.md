# swagger_client.FundsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fund**](FundsApi.md#create_fund) | **POST** /funds | Creates a non-feed fund. 
[**get_fund**](FundsApi.md#get_fund) | **GET** /funds/{fundId} | Returns a fund/equity for a given fundId/equityId. 
[**list_funds**](FundsApi.md#list_funds) | **GET** /funds | Returns a list of funds (feed and non-feed funds) and equities. 
[**update_fund**](FundsApi.md#update_fund) | **PUT** /funds/{fundId} | Updates a non-feed fund for a given fund. 

# **create_fund**
> Fund create_fund(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)

Creates a non-feed fund. 

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
api_instance = swagger_client.FundsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Fund() # Fund | Fund request
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier (optional)

try:
    # Creates a non-feed fund. 
    api_response = api_instance.create_fund(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsApi->create_fund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Fund**](Fund.md)| Fund request | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier | [optional] 

### Return type

[**Fund**](Fund.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fund**
> Fund get_fund(authorization, fund_id, x_api_key, accept=accept, tenant_id=tenant_id)

Returns a fund/equity for a given fundId/equityId. 

**Note:** Use of the this API is subject to specific terms of use.   The data obtained from this API may be used to drive UI applications where the users are licensed Intelligent Office users or customers thereof. Valid use cases fall within the production of print or other media as part of the normal course of financial services business.  The data from this API may **not** be extracted in bulk or redistributed for any purposes other than those stated above. Please be aware that any consumers that operate outside of these terms may have access to these endpoints removed or restricted. If in doubt, please contact us to discuss your use case and we can advise further. 

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
api_instance = swagger_client.FundsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
fund_id = 'fund_id_example' # str | Fund identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier (optional)

try:
    # Returns a fund/equity for a given fundId/equityId. 
    api_response = api_instance.get_fund(authorization, fund_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsApi->get_fund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **fund_id** | **str**| Fund identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier | [optional] 

### Return type

[**Fund**](Fund.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_funds**
> FundCollection list_funds(authorization, x_api_key, accept=accept, filter=filter, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of funds (feed and non-feed funds) and equities. 

**Note:** Use of the this API is subject to specific terms of use.   The data obtained from this API may be used to drive UI applications where the users are licensed Intelligent Office users or customers thereof. Valid use cases fall within the production of print or other media as part of the normal course of financial services business.  The data from this API may **not** be extracted in bulk or redistributed for any purposes other than those stated above. Please be aware that any consumers that operate outside of these terms may have access to these endpoints removed or restricted. If in doubt, please contact us to discuss your use case and we can advise further. 

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
api_instance = swagger_client.FundsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported operator(s): `eq`, `ne`, `in` and `startswith`. Available field(s): `source`, `name`, `type`, `sector`, `provider`, `codes.sedol`,  `codes.isin`, `codes.mex`, `codes.citi`, `codes.epic` and `isClosed` (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
tenant_id = 56 # int | Tenant identifier (optional)
top = 100 # int | The number of records to retrieve (default 100, max 500) (optional) (default to 100)

try:
    # Returns a list of funds (feed and non-feed funds) and equities. 
    api_response = api_instance.list_funds(authorization, x_api_key, accept=accept, filter=filter, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsApi->list_funds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported operator(s): &#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;in&#x60; and &#x60;startswith&#x60;. Available field(s): &#x60;source&#x60;, &#x60;name&#x60;, &#x60;type&#x60;, &#x60;sector&#x60;, &#x60;provider&#x60;, &#x60;codes.sedol&#x60;,  &#x60;codes.isin&#x60;, &#x60;codes.mex&#x60;, &#x60;codes.citi&#x60;, &#x60;codes.epic&#x60; and &#x60;isClosed&#x60; | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **tenant_id** | **int**| Tenant identifier | [optional] 
 **top** | **int**| The number of records to retrieve (default 100, max 500) | [optional] [default to 100]

### Return type

[**FundCollection**](FundCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fund**
> Fund update_fund(body, authorization, x_api_key, fund_id, accept=accept, tenant_id=tenant_id)

Updates a non-feed fund for a given fund. 

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
api_instance = swagger_client.FundsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateFund() # UpdateFund | Fund request
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
fund_id = 'fund_id_example' # str | Fund identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier (optional)

try:
    # Updates a non-feed fund for a given fund. 
    api_response = api_instance.update_fund(body, authorization, x_api_key, fund_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundsApi->update_fund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateFund**](UpdateFund.md)| Fund request | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **fund_id** | **str**| Fund identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier | [optional] 

### Return type

[**Fund**](Fund.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

