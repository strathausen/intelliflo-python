# swagger_client.ModelsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_portfolio_model**](ModelsApi.md#activate_portfolio_model) | **POST** /models/{modelId}/active | Activates or deactivates a portfolio model.
[**create_draft_portfolio_model**](ModelsApi.md#create_draft_portfolio_model) | **POST** /models/draft | Creates a draft portfolio model.
[**create_model**](ModelsApi.md#create_model) | **POST** /models | Creates a portfolio model.
[**create_provider_model**](ModelsApi.md#create_provider_model) | **POST** /apps/{appId}/models | Creates a new provider model.
[**get_model**](ModelsApi.md#get_model) | **GET** /models/{modelId} | Returns a portfolio model.
[**get_provider_model**](ModelsApi.md#get_provider_model) | **GET** /apps/{appId}/models/{modelId} | Returns a provider model.
[**get_provider_models**](ModelsApi.md#get_provider_models) | **GET** /apps/{appId}/models | Returns a list of provider models.
[**list_models**](ModelsApi.md#list_models) | **GET** /models | Returns a list of portfolio models.
[**patch_model**](ModelsApi.md#patch_model) | **PATCH** /models/{modelId} | Patch update a model.
[**publish_draft_portfolio_model**](ModelsApi.md#publish_draft_portfolio_model) | **POST** /models/draft/{modelId}/publish | Publishes a draft portfolio model.
[**update_draft_portfolio_model**](ModelsApi.md#update_draft_portfolio_model) | **PUT** /models/draft/{modelId} | Put update a draft portfolio model.
[**update_or_create_portfolio_model**](ModelsApi.md#update_or_create_portfolio_model) | **PUT** /models | Updates or creates a portfolio model.

# **activate_portfolio_model**
> PortfolioModel activate_portfolio_model(authorization, model_id, x_api_key, accept=accept, is_active=is_active, tenant_id=tenant_id)

Activates or deactivates a portfolio model.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
model_id = 56 # int | The model identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
is_active = true # bool | Toggle to activate or deactivate model. (optional)
tenant_id = 56 # int | The tenant identifier. (optional)

try:
    # Activates or deactivates a portfolio model.
    api_response = api_instance.activate_portfolio_model(authorization, model_id, x_api_key, accept=accept, is_active=is_active, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->activate_portfolio_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **model_id** | **int**| The model identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **is_active** | **bool**| Toggle to activate or deactivate model. | [optional] 
 **tenant_id** | **int**| The tenant identifier. | [optional] 

### Return type

[**PortfolioModel**](PortfolioModel.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_draft_portfolio_model**
> PortfolioModel create_draft_portfolio_model(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)

Creates a draft portfolio model.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DraftPortfolioModel() # DraftPortfolioModel | The Portfolio Model request.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | The Tenant Identifier. (optional)

try:
    # Creates a draft portfolio model.
    api_response = api_instance.create_draft_portfolio_model(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->create_draft_portfolio_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DraftPortfolioModel**](DraftPortfolioModel.md)| The Portfolio Model request. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| The Tenant Identifier. | [optional] 

### Return type

[**PortfolioModel**](PortfolioModel.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_model**
> PortfolioModel create_model(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)

Creates a portfolio model.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreatePortfolioModel() # CreatePortfolioModel | The Portfolio Model request.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | The Tenant Identifier. (optional)

try:
    # Creates a portfolio model.
    api_response = api_instance.create_model(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->create_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePortfolioModel**](CreatePortfolioModel.md)| The Portfolio Model request. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| The Tenant Identifier. | [optional] 

### Return type

[**PortfolioModel**](PortfolioModel.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_provider_model**
> ProviderModel create_provider_model(body, authorization, x_api_key, app_id, accept=accept)

Creates a new provider model.

Create a new provider model or a new version of an existing model.  To create a new version of an existing model make sure that the model.code is the same.  This will then archive the previous version and the firm can then approve the new version.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProviderModel() # ProviderModel | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
app_id = 'app_id_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Creates a new provider model.
    api_response = api_instance.create_provider_model(body, authorization, x_api_key, app_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->create_provider_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProviderModel**](ProviderModel.md)|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **app_id** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**ProviderModel**](ProviderModel.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> PortfolioModel get_model(authorization, model_id, x_api_key, accept=accept, tenant_id=tenant_id)

Returns a portfolio model.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
model_id = 56 # int | The model identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | The tenant identifier. (optional)

try:
    # Returns a portfolio model.
    api_response = api_instance.get_model(authorization, model_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->get_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **model_id** | **int**| The model identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| The tenant identifier. | [optional] 

### Return type

[**PortfolioModel**](PortfolioModel.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_model**
> ProviderModel get_provider_model(app_id, authorization, model_id, x_api_key, accept=accept)

Returns a provider model.

Gives model providers the ability to view and manage their models.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
authorization = 'authorization_example' # str | 
model_id = 56 # int | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a provider model.
    api_response = api_instance.get_provider_model(app_id, authorization, model_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->get_provider_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **authorization** | **str**|  | 
 **model_id** | **int**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**ProviderModel**](ProviderModel.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider_models**
> ProviderModelCollection get_provider_models(app_id, authorization, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of provider models.

This will only allow a maximum resulting page size of 500.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:   * __id__ ( in, eq, ne, gt, ge, lt, le )   * __isAccepted__ ( in, eq, ne )   * __appId__ (in, eq, ne, startswith )   * __code__ ( in, eq, ne, startswith )   * __name__ ( in, eq, ne, startswith )   * __atr.code__ ( in, eq, startswith )  Usage example: `filter=appId eq 'a13f242' and code startswith 'abc'` (optional)
orderby = 'orderby_example' # str | By default the list will be ordered desc by Id.    However it can be changed using one or more supported fields below.  Supported fields:   * __id__  * __isAccepted__  * __code__  * __name__    Usage example: `orderby=name asc` (optional)
skip = 0 # int | Index from which the results will start. (optional) (default to 0)
top = 100 # int | Number of records to retrieve (optional) (default to 100)

try:
    # Returns a list of provider models.
    api_response = api_instance.get_provider_models(app_id, authorization, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->get_provider_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Results can be filtered using one or more supported fields and operators below.  For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).  Supported fields and operators:   * __id__ ( in, eq, ne, gt, ge, lt, le )   * __isAccepted__ ( in, eq, ne )   * __appId__ (in, eq, ne, startswith )   * __code__ ( in, eq, ne, startswith )   * __name__ ( in, eq, ne, startswith )   * __atr.code__ ( in, eq, startswith )  Usage example: &#x60;filter&#x3D;appId eq &#x27;a13f242&#x27; and code startswith &#x27;abc&#x27;&#x60; | [optional] 
 **orderby** | **str**| By default the list will be ordered desc by Id.    However it can be changed using one or more supported fields below.  Supported fields:   * __id__  * __isAccepted__  * __code__  * __name__    Usage example: &#x60;orderby&#x3D;name asc&#x60; | [optional] 
 **skip** | **int**| Index from which the results will start. | [optional] [default to 0]
 **top** | **int**| Number of records to retrieve | [optional] [default to 100]

### Return type

[**ProviderModelCollection**](ProviderModelCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_models**
> PortfolioModelCollection list_models(authorization, x_api_key, accept=accept, details_only=details_only, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of portfolio models.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
details_only = false # bool | Flag to choose full or short version of Model Portfolio. (optional) (default to false)
filter = 'filter_example' # str | <returns>A list of matching portfolio model documents.</returns>              Results can be filtered using one or more supported fields and operators below.              For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).              Supported fields and operators:              * `id` (eq, ne, in, gt, ge, lt, le)              * `isActive` (eq)              * `provider` (eq, startswith, in)              * `code` (eq, in)              * `createdAt` (le,lt,gt,ge,eq)              * `name` (startswith)              * `groupOwner.id` (eq, in)              * `groupOwner.name` (startswith)              * `currentGroupName` (startswith)              * `allowRebalance` (eq)              * `isInvested` (eq)              * `tags.any` (in)              * `investmentAmountLower` (le, ge)              * `investmentAmountUpper` (le, ge)              * `atr.code` (eq, startswith, in)              * `atr.code.any` (in)              * `status` (eq)              * `version` (eq)              * `allowRebalance` (eq)              * `isLatestVersion` (eq)              * `investmentObjective` (in)              * `investmentManagementStyle` (eq)              * `taxQualified` (eq)              * `esg` (in)              * `riskProfile.Id` (eq, in)              * `isImps` (eq)              * `IsExternallyManaged` (eq)              * `IsDiscretionaryFundManaged` (eq)              * `platformProvider` (startswith) (optional)
order_by = 'order_by_example' # str | By default the list will be ordered desc by Id.  However it can be changed using one or more supported fields below.  Supported fields:  * `id`  * `code`  * `createdAt`  * `name`  * `provider`  * `groupOwner.name`  * `currentGroupName`  * `status`  * `version`  * `IsDiscretionaryFundManaged`  Supported directions asc, desc. (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
tenant_id = 56 # int | The tenant identifier. (optional)
top = 100 # int | The number of records to retrieve (default 25, max 100). (optional) (default to 100)

try:
    # Returns a list of portfolio models.
    api_response = api_instance.list_models(authorization, x_api_key, accept=accept, details_only=details_only, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->list_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **details_only** | **bool**| Flag to choose full or short version of Model Portfolio. | [optional] [default to false]
 **filter** | **str**| &lt;returns&gt;A list of matching portfolio model documents.&lt;/returns&gt;              Results can be filtered using one or more supported fields and operators below.              For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).              Supported fields and operators:              * &#x60;id&#x60; (eq, ne, in, gt, ge, lt, le)              * &#x60;isActive&#x60; (eq)              * &#x60;provider&#x60; (eq, startswith, in)              * &#x60;code&#x60; (eq, in)              * &#x60;createdAt&#x60; (le,lt,gt,ge,eq)              * &#x60;name&#x60; (startswith)              * &#x60;groupOwner.id&#x60; (eq, in)              * &#x60;groupOwner.name&#x60; (startswith)              * &#x60;currentGroupName&#x60; (startswith)              * &#x60;allowRebalance&#x60; (eq)              * &#x60;isInvested&#x60; (eq)              * &#x60;tags.any&#x60; (in)              * &#x60;investmentAmountLower&#x60; (le, ge)              * &#x60;investmentAmountUpper&#x60; (le, ge)              * &#x60;atr.code&#x60; (eq, startswith, in)              * &#x60;atr.code.any&#x60; (in)              * &#x60;status&#x60; (eq)              * &#x60;version&#x60; (eq)              * &#x60;allowRebalance&#x60; (eq)              * &#x60;isLatestVersion&#x60; (eq)              * &#x60;investmentObjective&#x60; (in)              * &#x60;investmentManagementStyle&#x60; (eq)              * &#x60;taxQualified&#x60; (eq)              * &#x60;esg&#x60; (in)              * &#x60;riskProfile.Id&#x60; (eq, in)              * &#x60;isImps&#x60; (eq)              * &#x60;IsExternallyManaged&#x60; (eq)              * &#x60;IsDiscretionaryFundManaged&#x60; (eq)              * &#x60;platformProvider&#x60; (startswith) | [optional] 
 **order_by** | **str**| By default the list will be ordered desc by Id.  However it can be changed using one or more supported fields below.  Supported fields:  * &#x60;id&#x60;  * &#x60;code&#x60;  * &#x60;createdAt&#x60;  * &#x60;name&#x60;  * &#x60;provider&#x60;  * &#x60;groupOwner.name&#x60;  * &#x60;currentGroupName&#x60;  * &#x60;status&#x60;  * &#x60;version&#x60;  * &#x60;IsDiscretionaryFundManaged&#x60;  Supported directions asc, desc. | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **tenant_id** | **int**| The tenant identifier. | [optional] 
 **top** | **int**| The number of records to retrieve (default 25, max 100). | [optional] [default to 100]

### Return type

[**PortfolioModelCollection**](PortfolioModelCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_model**
> PortfolioModel patch_model(body, authorization, x_api_key, tenant_id, model_id, accept=accept)

Patch update a model.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.Operation()] # list[Operation] | A Json Patch document containing details of modifications to be made to the model resource.
Properties which cannot be updated on PUT, cannot be updated using patch
            
For a simple example a request contains the following JSON:
            
{
    "op": "replace",
    "path": "/expectedReturn",
    "value": "1.234"
}
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
tenant_id = 56 # int | The tenant Id
model_id = 56 # int | The model identifier.
accept = 'accept_example' # str |  (optional)

try:
    # Patch update a model.
    api_response = api_instance.patch_model(body, authorization, x_api_key, tenant_id, model_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->patch_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Operation]**](Operation.md)| A Json Patch document containing details of modifications to be made to the model resource.
Properties which cannot be updated on PUT, cannot be updated using patch
            
For a simple example a request contains the following JSON:
            
{
    &quot;op&quot;: &quot;replace&quot;,
    &quot;path&quot;: &quot;/expectedReturn&quot;,
    &quot;value&quot;: &quot;1.234&quot;
} | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **tenant_id** | **int**| The tenant Id | 
 **model_id** | **int**| The model identifier. | 
 **accept** | **str**|  | [optional] 

### Return type

[**PortfolioModel**](PortfolioModel.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_draft_portfolio_model**
> publish_draft_portfolio_model(authorization, model_id, x_api_key, accept=accept, tenant_id=tenant_id)

Publishes a draft portfolio model.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
model_id = 56 # int | The model identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | The tenant identifier. (optional)

try:
    # Publishes a draft portfolio model.
    api_instance.publish_draft_portfolio_model(authorization, model_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling ModelsApi->publish_draft_portfolio_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **model_id** | **int**| The model identifier. | 
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

# **update_draft_portfolio_model**
> PortfolioModel update_draft_portfolio_model(body, authorization, x_api_key, tenant_id, model_id, accept=accept)

Put update a draft portfolio model.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DraftPortfolioModel() # DraftPortfolioModel | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
tenant_id = 56 # int | The tenant Id
model_id = 56 # int | The model identifier.
accept = 'accept_example' # str |  (optional)

try:
    # Put update a draft portfolio model.
    api_response = api_instance.update_draft_portfolio_model(body, authorization, x_api_key, tenant_id, model_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->update_draft_portfolio_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DraftPortfolioModel**](DraftPortfolioModel.md)|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **tenant_id** | **int**| The tenant Id | 
 **model_id** | **int**| The model identifier. | 
 **accept** | **str**|  | [optional] 

### Return type

[**PortfolioModel**](PortfolioModel.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_create_portfolio_model**
> update_or_create_portfolio_model(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)

Updates or creates a portfolio model.

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
api_instance = swagger_client.ModelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.PortfolioModel() # PortfolioModel | The Portfolio Model request.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | The Tenant Identifier. (optional)

try:
    # Updates or creates a portfolio model.
    api_instance.update_or_create_portfolio_model(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling ModelsApi->update_or_create_portfolio_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PortfolioModel**](PortfolioModel.md)| The Portfolio Model request. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| The Tenant Identifier. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

