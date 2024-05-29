# swagger_client.MarketingpreferencesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_marketing_preferences**](MarketingpreferencesApi.md#get_client_marketing_preferences) | **GET** /clients/{clientId}/marketing_preferences | Returns client&#x27;s current marketing preferences.
[**get_lead_marketing_preferences**](MarketingpreferencesApi.md#get_lead_marketing_preferences) | **GET** /leads/{leadId}/marketing_preferences | Returns lead&#x27;s current marketing preferences.
[**update_client_marketing_preferences**](MarketingpreferencesApi.md#update_client_marketing_preferences) | **PUT** /clients/{clientId}/marketing_preferences | Updates client&#x27;s marketing preferences.
[**update_lead_marketing_preferences**](MarketingpreferencesApi.md#update_lead_marketing_preferences) | **PUT** /leads/{leadId}/marketing_preferences | Updates lead&#x27;s marketing preferences.

# **get_client_marketing_preferences**
> ClientMarketingPreferences get_client_marketing_preferences(authorization, client_id, x_api_key, accept=accept)

Returns client's current marketing preferences.

Use this endpoint to return  a client's marketing preferences broken down by medium where appropriate.  A successful response (200) will return client's  marketing preferences document.  If a client has not yet provided their preferences and/or consent, the returned preferences will be defaulted to a suitable privacy configuration.  The returned configuration should be adhered to regardless of whether consent has been given yet or not.

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
api_instance = swagger_client.MarketingpreferencesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier. The special value 'me' can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns client's current marketing preferences.
    api_response = api_instance.get_client_marketing_preferences(authorization, client_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketingpreferencesApi->get_client_marketing_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**ClientMarketingPreferences**](ClientMarketingPreferences.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lead_marketing_preferences**
> LeadMarketingPreferences get_lead_marketing_preferences(authorization, lead_id, x_api_key, accept=accept)

Returns lead's current marketing preferences.

Use this endpoint to return  a lead's marketing preferences broken down by medium where appropriate.  A successful response (200) will return lead's  marketing preferences document.  If a lead has not yet provided their preferences and/or consent, the returned preferences will be defaulted to a suitable privacy configuration.  The returned configuration should be adhered to regardless of whether consent has been given yet or not.

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
api_instance = swagger_client.MarketingpreferencesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
lead_id = 56 # int | Lead identifier. The special value 'me' can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns lead's current marketing preferences.
    api_response = api_instance.get_lead_marketing_preferences(authorization, lead_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketingpreferencesApi->get_lead_marketing_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **lead_id** | **int**| Lead identifier. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**LeadMarketingPreferences**](LeadMarketingPreferences.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_marketing_preferences**
> ClientMarketingPreferences update_client_marketing_preferences(body, authorization, x_api_key, client_id, accept=accept)

Updates client's marketing preferences.

Use this endpoint to updates a client's marketing preferences broken down by medium where appropriate.  A successful response (200) will return updated client's  marketing preferences document.  If a client has not yet provided their preferences and/or consent, new preferences will be created.

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
api_instance = swagger_client.MarketingpreferencesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClientMarketingPreferences() # ClientMarketingPreferences | Client Marketing Preferences document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier. The special value 'me' can be used to indicate the authenticated user.
accept = 'accept_example' # str |  (optional)

try:
    # Updates client's marketing preferences.
    api_response = api_instance.update_client_marketing_preferences(body, authorization, x_api_key, client_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketingpreferencesApi->update_client_marketing_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientMarketingPreferences**](ClientMarketingPreferences.md)| Client Marketing Preferences document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **accept** | **str**|  | [optional] 

### Return type

[**ClientMarketingPreferences**](ClientMarketingPreferences.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lead_marketing_preferences**
> LeadMarketingPreferences update_lead_marketing_preferences(body, authorization, x_api_key, lead_id, accept=accept)

Updates lead's marketing preferences.

Use this endpoint to updates a lead's marketing preferences broken down by medium where appropriate.  A successful response (200) will return updated client's  marketing preferences document.  If a lead has not yet provided their preferences and/or consent, new preferences will be created.

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
api_instance = swagger_client.MarketingpreferencesApi(swagger_client.ApiClient(configuration))
body = swagger_client.LeadMarketingPreferences() # LeadMarketingPreferences | Lead Marketing Preferences document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
lead_id = 56 # int | Lead identifier. The special value 'me' can be used to indicate the authenticated user.
accept = 'accept_example' # str |  (optional)

try:
    # Updates lead's marketing preferences.
    api_response = api_instance.update_lead_marketing_preferences(body, authorization, x_api_key, lead_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketingpreferencesApi->update_lead_marketing_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LeadMarketingPreferences**](LeadMarketingPreferences.md)| Lead Marketing Preferences document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **lead_id** | **int**| Lead identifier. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **accept** | **str**|  | [optional] 

### Return type

[**LeadMarketingPreferences**](LeadMarketingPreferences.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

