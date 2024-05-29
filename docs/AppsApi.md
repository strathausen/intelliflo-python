# swagger_client.AppsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exist_installed_app**](AppsApi.md#exist_installed_app) | **HEAD** /installed_apps/{appId} | Checks if an installed app exists
[**get_installed_app**](AppsApi.md#get_installed_app) | **GET** /installed_apps/{appId} | Returns an installed app
[**get_installed_app_group_settings**](AppsApi.md#get_installed_app_group_settings) | **GET** /installed_apps/{appId}/group_settings/{groupId} | Returns group settings for a given installed app and group
[**get_installed_app_user_settings**](AppsApi.md#get_installed_app_user_settings) | **GET** /installed_apps/{appId}/user_settings/{userId} | Returns user settings for a given installed app and user
[**list_installed_app_group_settings**](AppsApi.md#list_installed_app_group_settings) | **GET** /installed_apps/{appId}/group_settings | Returns a list of group settings for a given installed app
[**list_installed_app_user_settings**](AppsApi.md#list_installed_app_user_settings) | **GET** /installed_apps/{appId}/user_settings | Returns a lists of user settings for a given installed app
[**list_installed_apps**](AppsApi.md#list_installed_apps) | **GET** /installed_apps | Returns a list of installed apps
[**update_installed_app_group_settings**](AppsApi.md#update_installed_app_group_settings) | **PUT** /installed_apps/{appId}/group_settings/{groupId} | Updates group settings for a given installed app and group
[**update_installed_app_user_settings**](AppsApi.md#update_installed_app_user_settings) | **PUT** /installed_apps/{appId}/user_settings/{userId} | Updates user settings for a given installed app and user

# **exist_installed_app**
> exist_installed_app(app_id, authorization, x_api_key, accept=accept)

Checks if an installed app exists

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Checks if an installed app exists
    api_instance.exist_installed_app(app_id, authorization, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling AppsApi->exist_installed_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **authorization** | **str**|  | 
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

# **get_installed_app**
> App get_installed_app(app_id, authorization, x_api_key, accept=accept)

Returns an installed app

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns an installed app
    api_response = api_instance.get_installed_app(app_id, authorization, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->get_installed_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**App**](App.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installed_app_group_settings**
> AppSettingsDocument get_installed_app_group_settings(app_id, authorization, group_id, tenant_id, x_api_key, accept=accept, x_iflo_decrypt=x_iflo_decrypt)

Returns group settings for a given installed app and group

Give Apps the ability to define and capture their own dynamic group settings data using JSON schema definitions. For more detail and usage refer to [AppSettingsExtension](https://developer.gb.intelliflo.net/docs/ExtensionReference#iflo:store:AppSettingsExtension)  When called with this will return the specific group settings for the group. This endpoint will not traverse the hierarchy to find the first instance. 

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
authorization = 'authorization_example' # str | 
group_id = 'group_id_example' # str | 
tenant_id = 56 # int | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
x_iflo_decrypt = false # bool |  (optional) (default to false)

try:
    # Returns group settings for a given installed app and group
    api_response = api_instance.get_installed_app_group_settings(app_id, authorization, group_id, tenant_id, x_api_key, accept=accept, x_iflo_decrypt=x_iflo_decrypt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->get_installed_app_group_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **authorization** | **str**|  | 
 **group_id** | **str**|  | 
 **tenant_id** | **int**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **x_iflo_decrypt** | **bool**|  | [optional] [default to false]

### Return type

[**AppSettingsDocument**](AppSettingsDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installed_app_user_settings**
> AppSettingsDocument get_installed_app_user_settings(app_id, authorization, tenant_id, user_id, x_api_key, accept=accept, x_iflo_decrypt=x_iflo_decrypt)

Returns user settings for a given installed app and user

Give Apps the ability to define and capture their own dynamic user settings data using JSON schema definitions. For more detail and usage refer to [AppSettingsExtension](https://developer.gb.intelliflo.net/docs/ExtensionReference#iflo:store:AppSettingsExtension)  When called with [Authorization Code flow](https://developer.gb.intelliflo.net/docs/Authentication#CodeFlow) then this will allow the retrieval of the current users settings only. If called with [Tenant Client Credentials flow](https://developer.gb.intelliflo.net/docs/Authentication#TCCFlow) then it will return the user settings for the requested user within a tenant. 

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
authorization = 'authorization_example' # str | 
tenant_id = 56 # int | 
user_id = 'user_id_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
x_iflo_decrypt = false # bool |  (optional) (default to false)

try:
    # Returns user settings for a given installed app and user
    api_response = api_instance.get_installed_app_user_settings(app_id, authorization, tenant_id, user_id, x_api_key, accept=accept, x_iflo_decrypt=x_iflo_decrypt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->get_installed_app_user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **authorization** | **str**|  | 
 **tenant_id** | **int**|  | 
 **user_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **x_iflo_decrypt** | **bool**|  | [optional] [default to false]

### Return type

[**AppSettingsDocument**](AppSettingsDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_installed_app_group_settings**
> InstalledAppGroupSettingCollection list_installed_app_group_settings(app_id, authorization, tenant_id, x_api_key, accept=accept, skip=skip, top=top, x_iflo_decrypt=x_iflo_decrypt)

Returns a list of group settings for a given installed app

Give Apps the ability to define and capture their own dynamic group settings data using JSON schema definitions. For more detail and usage refer to [AppSettingsExtension](https://developer.gb.intelliflo.net/docs/ExtensionReference#iflo:store:AppSettingsExtension)  When called with [Authorisation Code flow](https://developer.gb.intelliflo.net/docs/Authentication#CodeFlow) then this will return the first instance of group settings in the upward lineage of the tenants group hierarchy. If called with [Tenant Client Credentials flow](https://developer.gb.intelliflo.net/docs/Authentication#TCCFlow) then it will return all group settings for a tenant. 

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
authorization = 'authorization_example' # str | 
tenant_id = 56 # int | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int |  (optional) (default to 0)
top = 100 # int |  (optional) (default to 100)
x_iflo_decrypt = false # bool |  (optional) (default to false)

try:
    # Returns a list of group settings for a given installed app
    api_response = api_instance.list_installed_app_group_settings(app_id, authorization, tenant_id, x_api_key, accept=accept, skip=skip, top=top, x_iflo_decrypt=x_iflo_decrypt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->list_installed_app_group_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **authorization** | **str**|  | 
 **tenant_id** | **int**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **top** | **int**|  | [optional] [default to 100]
 **x_iflo_decrypt** | **bool**|  | [optional] [default to false]

### Return type

[**InstalledAppGroupSettingCollection**](InstalledAppGroupSettingCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_installed_app_user_settings**
> InstalledAppGroupSettingCollection list_installed_app_user_settings(app_id, authorization, tenant_id, x_api_key, accept=accept, skip=skip, top=top, x_iflo_decrypt=x_iflo_decrypt)

Returns a lists of user settings for a given installed app

Give Apps the ability to define and capture their own dynamic user settings data using JSON schema definitions. For more detail and usage refer to [AppSettingsExtension](https://developer.gb.intelliflo.net/docs/ExtensionReference#iflo:store:AppSettingsExtension)  When called with [Authorization Code flow](https://developer.gb.intelliflo.net/docs/Authentication#CodeFlow) this will return the current users settings only. If it is called with [Tenant Client Credentials flow](https://developer.gb.intelliflo.net/docs/Authentication#TCCFlow) then it will return all user settings for a tenant. 

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))
app_id = 'app_id_example' # str | 
authorization = 'authorization_example' # str | 
tenant_id = 56 # int | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int |  (optional) (default to 0)
top = 100 # int |  (optional) (default to 100)
x_iflo_decrypt = false # bool |  (optional) (default to false)

try:
    # Returns a lists of user settings for a given installed app
    api_response = api_instance.list_installed_app_user_settings(app_id, authorization, tenant_id, x_api_key, accept=accept, skip=skip, top=top, x_iflo_decrypt=x_iflo_decrypt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->list_installed_app_user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **authorization** | **str**|  | 
 **tenant_id** | **int**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **top** | **int**|  | [optional] [default to 100]
 **x_iflo_decrypt** | **bool**|  | [optional] [default to false]

### Return type

[**InstalledAppGroupSettingCollection**](InstalledAppGroupSettingCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_installed_apps**
> AppCollection list_installed_apps(authorization, x_api_key, accept=accept, skip=skip, tenant_id=tenant_id, top=top, user_id=user_id)

Returns a list of installed apps

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int |  (optional) (default to 0)
tenant_id = 56 # int |  (optional)
top = 100 # int |  (optional) (default to 100)
user_id = 56 # int |  (optional)

try:
    # Returns a list of installed apps
    api_response = api_instance.list_installed_apps(authorization, x_api_key, accept=accept, skip=skip, tenant_id=tenant_id, top=top, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->list_installed_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **tenant_id** | **int**|  | [optional] 
 **top** | **int**|  | [optional] [default to 100]
 **user_id** | **int**|  | [optional] 

### Return type

[**AppCollection**](AppCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_installed_app_group_settings**
> AppSettingsDocument update_installed_app_group_settings(body, authorization, x_api_key, app_id, group_id, accept=accept, tenant_id=tenant_id)

Updates group settings for a given installed app and group

Give Apps the ability to define and capture their own dynamic group settings data using JSON schema definitions. For more detail and usage refer to [AppSettingsExtension](https://developer.gb.intelliflo.net/docs/ExtensionReference#iflo:store:AppSettingsExtension)  When called with [Authorisation Code flow](https://developer.gb.intelliflo.net/docs/Authentication#CodeFlow) then this will save the specific group settings for the group.     

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppSettingsDocument() # AppSettingsDocument | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
app_id = 'app_id_example' # str | 
group_id = 'group_id_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int |  (optional)

try:
    # Updates group settings for a given installed app and group
    api_response = api_instance.update_installed_app_group_settings(body, authorization, x_api_key, app_id, group_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->update_installed_app_group_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppSettingsDocument**](AppSettingsDocument.md)|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **app_id** | **str**|  | 
 **group_id** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**|  | [optional] 

### Return type

[**AppSettingsDocument**](AppSettingsDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_installed_app_user_settings**
> AppSettingsDocument update_installed_app_user_settings(body, authorization, x_api_key, app_id, user_id, accept=accept, tenant_id=tenant_id)

Updates user settings for a given installed app and user

Give Apps the ability to define and capture their own dynamic user settings data using JSON schema definitions. For more detail and usage refer to [AppSettingsExtension](https://developer.gb.intelliflo.net/docs/ExtensionReference#iflo:store:AppSettingsExtension)  When called with [Authorization Code flow](https://developer.gb.intelliflo.net/docs/Authentication#CodeFlow) then this will save the settings for the current user. If it is called with [Tenant Client Credentials flow](https://developer.gb.intelliflo.net/docs/Authentication#TCCFlow) then it will save the settings for the requested user within a tenant. 

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppSettingsDocument() # AppSettingsDocument | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
app_id = 'app_id_example' # str | 
user_id = 'user_id_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int |  (optional)

try:
    # Updates user settings for a given installed app and user
    api_response = api_instance.update_installed_app_user_settings(body, authorization, x_api_key, app_id, user_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->update_installed_app_user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppSettingsDocument**](AppSettingsDocument.md)|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **app_id** | **str**|  | 
 **user_id** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**|  | [optional] 

### Return type

[**AppSettingsDocument**](AppSettingsDocument.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

