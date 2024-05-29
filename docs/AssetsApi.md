# swagger_client.AssetsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_assets**](AssetsApi.md#create_client_assets) | **POST** /clients/{clientId}/assets | Creates the asset for a given client. 
[**delete_client_asset**](AssetsApi.md#delete_client_asset) | **DELETE** /clients/{clientId}/assets/{assetId} | Deletes the asset for a given client and asset. 
[**get_client_asset**](AssetsApi.md#get_client_asset) | **GET** /clients/{clientId}/assets/{assetId} | Returns the asset for a given client and asset. 
[**list_client_assets**](AssetsApi.md#list_client_assets) | **GET** /clients/{clientId}/assets | Returns a list of assets for the given client. 
[**update_client_asset**](AssetsApi.md#update_client_asset) | **PUT** /clients/{clientId}/assets/{assetId} | Updates the asset for a given client and asset. 

# **create_client_assets**
> Asset create_client_assets(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)

Creates the asset for a given client. 

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
api_instance = swagger_client.AssetsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Asset() # Asset | The asset document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | The tenant identifier. (optional)

try:
    # Creates the asset for a given client. 
    api_response = api_instance.create_client_assets(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->create_client_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Asset**](Asset.md)| The asset document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| The tenant identifier. | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_asset**
> delete_client_asset(asset_id, authorization, client_id, x_api_key, accept=accept, tenant_id=tenant_id)

Deletes the asset for a given client and asset. 

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
api_instance = swagger_client.AssetsApi(swagger_client.ApiClient(configuration))
asset_id = 56 # int | The asset identifier.
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | The tenant identifier. (optional)

try:
    # Deletes the asset for a given client and asset. 
    api_instance.delete_client_asset(asset_id, authorization, client_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling AssetsApi->delete_client_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The asset identifier. | 
 **authorization** | **str**|  | 
 **client_id** | **int**| The client identifier. | 
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

# **get_client_asset**
> Asset get_client_asset(asset_id, authorization, client_id, x_api_key, accept=accept)

Returns the asset for a given client and asset. 

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
api_instance = swagger_client.AssetsApi(swagger_client.ApiClient(configuration))
asset_id = 56 # int | The asset identifier.
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns the asset for a given client and asset. 
    api_response = api_instance.get_client_asset(asset_id, authorization, client_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_client_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The asset identifier. | 
 **authorization** | **str**|  | 
 **client_id** | **int**| The client identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_assets**
> AssetCollection list_client_assets(authorization, client_id, x_api_key, accept=accept, filter=filter, order_by=order_by, portfolio_type=portfolio_type, skip=skip, top=top)

Returns a list of assets for the given client. 

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
api_instance = swagger_client.AssetsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supports filtering:                             Properties and operators supported:                             * Asset `id` ( in ) e.g. filter=id in (1,2,3)               * `plan.id`  ( in, eq, ne ) e.g. filter=plan.id in (1,2,3), filter=plan.id eq null, filter=plan.id ne null               * `assetType`( in, eq, ne ) e.g. filter=assetType in ('Type1','Type2') (optional)
order_by = 'order_by_example' # str | Supports sorting:                             Properties and operators supported:                             * Asset `id` e.g. orderby=id asc               * `plan.id` e.g. orderby=plan.id desc                             Sort direction 'asc' or 'desc'. If not specified, then the resources will be ordered in ascending order by default. (optional)
portfolio_type = 'portfolio_type_example' # str | Supports filtering by PortfolioType:               `Single` - Returns assets solely owned by the client.               `Joint` - Returns assets where the client is a joint owner.               `FamilyWealth` - Returns assets owned by the relations of the client where client is not the asset's owner.                             Operators supported:                             * PortfolioType `value` ( in, eq ) e.g. portfolioType=value in ('Single','Joint','FamilyWealth'), portfolioType=value eq 'Joint'               If not specified, then the resources will be filtered by 'Single' and 'Joint' by default. (optional)
skip = 0 # int | Number of records to skip: skip=1 (optional) (default to 0)
top = 100 # int | Number of records to get: top=11 (optional) (default to 100)

try:
    # Returns a list of assets for the given client. 
    api_response = api_instance.list_client_assets(authorization, client_id, x_api_key, accept=accept, filter=filter, order_by=order_by, portfolio_type=portfolio_type, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->list_client_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supports filtering:                             Properties and operators supported:                             * Asset &#x60;id&#x60; ( in ) e.g. filter&#x3D;id in (1,2,3)               * &#x60;plan.id&#x60;  ( in, eq, ne ) e.g. filter&#x3D;plan.id in (1,2,3), filter&#x3D;plan.id eq null, filter&#x3D;plan.id ne null               * &#x60;assetType&#x60;( in, eq, ne ) e.g. filter&#x3D;assetType in (&#x27;Type1&#x27;,&#x27;Type2&#x27;) | [optional] 
 **order_by** | **str**| Supports sorting:                             Properties and operators supported:                             * Asset &#x60;id&#x60; e.g. orderby&#x3D;id asc               * &#x60;plan.id&#x60; e.g. orderby&#x3D;plan.id desc                             Sort direction &#x27;asc&#x27; or &#x27;desc&#x27;. If not specified, then the resources will be ordered in ascending order by default. | [optional] 
 **portfolio_type** | **str**| Supports filtering by PortfolioType:               &#x60;Single&#x60; - Returns assets solely owned by the client.               &#x60;Joint&#x60; - Returns assets where the client is a joint owner.               &#x60;FamilyWealth&#x60; - Returns assets owned by the relations of the client where client is not the asset&#x27;s owner.                             Operators supported:                             * PortfolioType &#x60;value&#x60; ( in, eq ) e.g. portfolioType&#x3D;value in (&#x27;Single&#x27;,&#x27;Joint&#x27;,&#x27;FamilyWealth&#x27;), portfolioType&#x3D;value eq &#x27;Joint&#x27;               If not specified, then the resources will be filtered by &#x27;Single&#x27; and &#x27;Joint&#x27; by default. | [optional] 
 **skip** | **int**| Number of records to skip: skip&#x3D;1 | [optional] [default to 0]
 **top** | **int**| Number of records to get: top&#x3D;11 | [optional] [default to 100]

### Return type

[**AssetCollection**](AssetCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_asset**
> Asset update_client_asset(body, authorization, x_api_key, asset_id, client_id, accept=accept, tenant_id=tenant_id)

Updates the asset for a given client and asset. 

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
api_instance = swagger_client.AssetsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Asset() # Asset | The asset document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
asset_id = 56 # int | The asset identifier.
client_id = 56 # int | The client identifier.
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | The tenant identifier. (optional)

try:
    # Updates the asset for a given client and asset. 
    api_response = api_instance.update_client_asset(body, authorization, x_api_key, asset_id, client_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->update_client_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Asset**](Asset.md)| The asset document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **asset_id** | **int**| The asset identifier. | 
 **client_id** | **int**| The client identifier. | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| The tenant identifier. | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

