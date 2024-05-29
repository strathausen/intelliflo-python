# swagger_client.FundpricesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_fund_prices**](FundpricesApi.md#list_fund_prices) | **GET** /funds/{fundId}/prices | Returns a list of fund prices for a given fund. 

# **list_fund_prices**
> FundPriceCollection list_fund_prices(authorization, fund_id, x_api_key, accept=accept, filter=filter, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of fund prices for a given fund. 

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
api_instance = swagger_client.FundpricesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
fund_id = 'fund_id_example' # str | Fund identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported operator(s): `lt`, `le`, `gt`, `gt` and `eq`. Available Field(s) `date` (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
tenant_id = 56 # int | Tenant identifier (optional)
top = 100 # int | The number of records to retrieve (default 100, max 1100) (optional) (default to 100)

try:
    # Returns a list of fund prices for a given fund. 
    api_response = api_instance.list_fund_prices(authorization, fund_id, x_api_key, accept=accept, filter=filter, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundpricesApi->list_fund_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **fund_id** | **str**| Fund identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported operator(s): &#x60;lt&#x60;, &#x60;le&#x60;, &#x60;gt&#x60;, &#x60;gt&#x60; and &#x60;eq&#x60;. Available Field(s) &#x60;date&#x60; | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **tenant_id** | **int**| Tenant identifier | [optional] 
 **top** | **int**| The number of records to retrieve (default 100, max 1100) | [optional] [default to 100]

### Return type

[**FundPriceCollection**](FundPriceCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

