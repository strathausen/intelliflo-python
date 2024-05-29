# swagger_client.WebhooksApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /hub/webhooks | Creates or updates an existing webhook subscription.
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /hub/webhooks/{id} | Deletes a specific webhook subscription by id (Unsubscribe).
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /hub/webhooks/{id} | Returns a specific webhook subscription by id.
[**list_webhooks**](WebhooksApi.md#list_webhooks) | **GET** /hub/webhooks | Returns the list of webhook subscriptions.
[**subscribe_unsubscribe_web_sub**](WebhooksApi.md#subscribe_unsubscribe_web_sub) | **POST** /hub | A WebSub compliant endpoint which creates or updates an existing webhook subscription.

# **create_webhook**
> Webhook create_webhook(body, authorization, x_api_key, accept=accept)

Creates or updates an existing webhook subscription.

This will create or update a webhook subscription, see [Events](/apis/events) for supported events.

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
# Configure OAuth2 access token for authorization: oauth2-client-credentials
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
body = swagger_client.WebhookCreate() # WebhookCreate | Resource Document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Creates or updates an existing webhook subscription.
    api_response = api_instance.create_webhook(body, authorization, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookCreate**](WebhookCreate.md)| Resource Document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-client-credentials](../README.md#oauth2-client-credentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> delete_webhook(id, authorization, x_api_key, accept=accept)

Deletes a specific webhook subscription by id (Unsubscribe).

This will delete a specific webhook subscription by id.

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
# Configure OAuth2 access token for authorization: oauth2-client-credentials
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Subscription identifier.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes a specific webhook subscription by id (Unsubscribe).
    api_instance.delete_webhook(id, authorization, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subscription identifier. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-client-credentials](../README.md#oauth2-client-credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> Webhook get_webhook(id, authorization, x_api_key, accept=accept)

Returns a specific webhook subscription by id.

This will return a specific webhook subscription by id.

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
# Configure OAuth2 access token for authorization: oauth2-client-credentials
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Subscription identifier.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a specific webhook subscription by id.
    api_response = api_instance.get_webhook(id, authorization, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subscription identifier. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-client-credentials](../README.md#oauth2-client-credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhooks**
> WebhookCollection list_webhooks(authorization, x_api_key, accept=accept)

Returns the list of webhook subscriptions.

This will return a list of webhook subscriptions.

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
# Configure OAuth2 access token for authorization: oauth2-client-credentials
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns the list of webhook subscriptions.
    api_response = api_instance.list_webhooks(authorization, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->list_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**WebhookCollection**](WebhookCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-client-credentials](../README.md#oauth2-client-credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_unsubscribe_web_sub**
> subscribe_unsubscribe_web_sub(hub_mode, hub_topic, hub_callback, hub_lease_seconds, hub_secret, authorization, x_api_key, accept=accept)

A WebSub compliant endpoint which creates or updates an existing webhook subscription.

This endpoint is a [WebSub](https://www.w3.org/TR/websub/#subscriber-sends-subscription-request) compliant hub for managing subscriptions to event topics, see [Events](/apis/events) for supported events.  This request MUST have a Content-Type header of `application/x-www-form-urlencoded` and use the described parameters in the body as described below.

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
# Configure OAuth2 access token for authorization: oauth2-client-credentials
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
hub_mode = 'hub_mode_example' # str | 
hub_topic = 'hub_topic_example' # str | 
hub_callback = 'hub_callback_example' # str | 
hub_lease_seconds = 56 # int | 
hub_secret = 'hub_secret_example' # str | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # A WebSub compliant endpoint which creates or updates an existing webhook subscription.
    api_instance.subscribe_unsubscribe_web_sub(hub_mode, hub_topic, hub_callback, hub_lease_seconds, hub_secret, authorization, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling WebhooksApi->subscribe_unsubscribe_web_sub: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hub_mode** | **str**|  | 
 **hub_topic** | **str**|  | 
 **hub_callback** | **str**|  | 
 **hub_lease_seconds** | **int**|  | 
 **hub_secret** | **str**|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-client-credentials](../README.md#oauth2-client-credentials)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

