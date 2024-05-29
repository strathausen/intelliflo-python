# swagger_client.QuotesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_client_quote_applicant**](QuotesApi.md#add_client_quote_applicant) | **POST** /clients/{clientId}/quotes/{quoteId} | Adds a secondary client owner to a given quote.
[**client_quote_exists**](QuotesApi.md#client_quote_exists) | **HEAD** /clients/{clientId}/quotes/{quoteId} | Checks that a quote exists for a given client.
[**client_quote_results_exists**](QuotesApi.md#client_quote_results_exists) | **HEAD** /clients/{clientId}/quotes/{quoteId}/results/{quoteResultId} | Checks that a quote result exists for a client quote.
[**create_client_quote**](QuotesApi.md#create_client_quote) | **POST** /clients/{clientId}/quotes | Creates a new client quote.
[**create_client_quote_result**](QuotesApi.md#create_client_quote_result) | **POST** /clients/{clientId}/quotes/{quoteId}/results | Creates a new client quote result.
[**get_client_quote**](QuotesApi.md#get_client_quote) | **GET** /clients/{clientId}/quotes/{quoteId} | Returns a client quote.
[**get_client_quote_result**](QuotesApi.md#get_client_quote_result) | **GET** /clients/{clientId}/quotes/{quoteId}/results/{quoteResultId} | Returns a client quote result.
[**get_client_quote_result_product_benefits**](QuotesApi.md#get_client_quote_result_product_benefits) | **GET** /clients/{clientId}/quotes/{quoteId}/results/{quoteResultId}/benefits | This endpoint allows an API user to retrieve product details of a specific quote result or illustration result for a client.
[**list_client_quote_results**](QuotesApi.md#list_client_quote_results) | **GET** /clients/{clientId}/quotes/{quoteId}/results | Returns a list of client quote results.
[**list_client_quotes**](QuotesApi.md#list_client_quotes) | **GET** /clients/{clientId}/quotes | Returns a list of quotes.
[**set_client_quote_status**](QuotesApi.md#set_client_quote_status) | **POST** /clients/{clientId}/quotes/{quoteId}/status/{status} | Sets a new status for the client quote.
[**update_client_quote_result_product_benefits**](QuotesApi.md#update_client_quote_result_product_benefits) | **PUT** /clients/{clientId}/quotes/{quoteId}/results/{quoteResultId}/benefits | This endpoint allows an API user to update product details of a specific quote result or illustration result for a client.

# **add_client_quote_applicant**
> Quote add_client_quote_applicant(authorization, client_id, quote_id, x_api_key, accept=accept)

Adds a secondary client owner to a given quote.

This endpoint allows an API user to add a secondary owner for the quote or illustration.

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Adds a secondary client owner to a given quote.
    api_response = api_instance.add_client_quote_applicant(authorization, client_id, quote_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->add_client_quote_applicant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Quote**](Quote.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_quote_exists**
> client_quote_exists(authorization, client_id, quote_id, x_api_key, accept=accept)

Checks that a quote exists for a given client.

This endpoint allows an API user to check if a specific quote or illustration exists for a client.

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Checks that a quote exists for a given client.
    api_instance.client_quote_exists(authorization, client_id, quote_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling QuotesApi->client_quote_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
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

# **client_quote_results_exists**
> client_quote_results_exists(authorization, client_id, quote_id, quote_result_id, x_api_key, accept=accept)

Checks that a quote result exists for a client quote.

This endpoint allows an API user to check if the results for a quote or illustration for a client exists.

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
quote_result_id = 56 # int | Quote result identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Checks that a quote result exists for a client quote.
    api_instance.client_quote_results_exists(authorization, client_id, quote_id, quote_result_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling QuotesApi->client_quote_results_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **quote_result_id** | **int**| Quote result identifier. | 
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

# **create_client_quote**
> Quote create_client_quote(body, authorization, x_api_key, client_id, accept=accept)

Creates a new client quote.

This endpoint allows an API user to create a quote or illustration for a client using the document in the body of this request.

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Quote() # Quote | Request document with quote details.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
accept = 'accept_example' # str |  (optional)

try:
    # Creates a new client quote.
    api_response = api_instance.create_client_quote(body, authorization, x_api_key, client_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->create_client_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Quote**](Quote.md)| Request document with quote details. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **accept** | **str**|  | [optional] 

### Return type

[**Quote**](Quote.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_quote_result**
> QuoteResult create_client_quote_result(body, authorization, x_api_key, client_id, quote_id, accept=accept)

Creates a new client quote result.

This endpoint allows an API user to create the results for a quote or illustration using the document supplied in the body of the request.

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
body = swagger_client.QuoteResult() # QuoteResult | Request document with quote result details.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
accept = 'accept_example' # str |  (optional)

try:
    # Creates a new client quote result.
    api_response = api_instance.create_client_quote_result(body, authorization, x_api_key, client_id, quote_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->create_client_quote_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuoteResult**](QuoteResult.md)| Request document with quote result details. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **accept** | **str**|  | [optional] 

### Return type

[**QuoteResult**](QuoteResult.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_quote**
> Quote get_client_quote(authorization, client_id, quote_id, x_api_key, accept=accept)

Returns a client quote.

This endpoint allows an API user to retrieve a specific quote or illustration for a client.

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a client quote.
    api_response = api_instance.get_client_quote(authorization, client_id, quote_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->get_client_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Quote**](Quote.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_quote_result**
> QuoteResult get_client_quote_result(authorization, client_id, quote_id, quote_result_id, x_api_key, accept=accept)

Returns a client quote result.

This endpoint allows an API user to retrieve a specific quote result or illustration result for a client.

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
quote_result_id = 56 # int | Quote result identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a client quote result.
    api_response = api_instance.get_client_quote_result(authorization, client_id, quote_id, quote_result_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->get_client_quote_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **quote_result_id** | **int**| Quote result identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**QuoteResult**](QuoteResult.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_quote_result_product_benefits**
> ProductBenefitFeatures get_client_quote_result_product_benefits(authorization, client_id, quote_id, quote_result_id, x_api_key, accept=accept)

This endpoint allows an API user to retrieve product details of a specific quote result or illustration result for a client.

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
quote_result_id = 56 # int | Quote result identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # This endpoint allows an API user to retrieve product details of a specific quote result or illustration result for a client.
    api_response = api_instance.get_client_quote_result_product_benefits(authorization, client_id, quote_id, quote_result_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->get_client_quote_result_product_benefits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **quote_result_id** | **int**| Quote result identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**ProductBenefitFeatures**](ProductBenefitFeatures.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_quote_results**
> QuoteResultCollection list_client_quote_results(authorization, client_id, quote_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of client quote results.

This endpoint provides the ability to identify all of client's quote and illustration results.  Be aware that this API will only allow a maximum resulting page size of 500.

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported Filters:  * `id` (`eq`, `ne`, `in`, `gt`, `ge`, `lt`, `le`)                See[QueryLang] (docs/ApiQueryLang) for further usage details. (optional)
orderby = 'orderby_example' # str | Supported Sort Properties:  * `id` (`asc` or `desc`)                Default: `id` `desc`. (optional)
skip = 0 # int | The number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
top = 25 # int | The number of records to retrieve (default: 25, max: 500). (optional) (default to 25)

try:
    # Returns a list of client quote results.
    api_response = api_instance.list_client_quote_results(authorization, client_id, quote_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->list_client_quote_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported Filters:  * &#x60;id&#x60; (&#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;in&#x60;, &#x60;gt&#x60;, &#x60;ge&#x60;, &#x60;lt&#x60;, &#x60;le&#x60;)                See[QueryLang] (docs/ApiQueryLang) for further usage details. | [optional] 
 **orderby** | **str**| Supported Sort Properties:  * &#x60;id&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)                Default: &#x60;id&#x60; &#x60;desc&#x60;. | [optional] 
 **skip** | **int**| The number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **top** | **int**| The number of records to retrieve (default: 25, max: 500). | [optional] [default to 25]

### Return type

[**QuoteResultCollection**](QuoteResultCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_quotes**
> QuotesCollection list_client_quotes(authorization, client_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of quotes.

This endpoint allows an API user to identify all of a client's quotes and illustrations.  Be aware that this API will only allow a maximum resulting page size of 500.

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported Filters:  * `id` (`in`),  * `appName` (`startswith`),  * `customReference` (`startswith`),  * `reference` (`startswith`),  * `serviceCase.id` (`eq`, `in`)                See[QueryLang] (docs/ApiQueryLang) for further usage details. (optional)
orderby = 'orderby_example' # str | Supported Sort Properties:  * `id` (`asc` or `desc`),  * `appName` (`asc` or `desc`),  * `customReference` (`asc` or `desc`),  * `reference` (`asc` or `desc`),  * `status` (`asc` or `desc`),  * `productGroup` (`asc` or `desc`),  * `createdAt` (`asc` or `desc`)                Default: `id` `desc`. (optional)
skip = 0 # int | The number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
top = 25 # int | The number of records to retrieve (default: 25, max: 500). (optional) (default to 25)

try:
    # Returns a list of quotes.
    api_response = api_instance.list_client_quotes(authorization, client_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->list_client_quotes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported Filters:  * &#x60;id&#x60; (&#x60;in&#x60;),  * &#x60;appName&#x60; (&#x60;startswith&#x60;),  * &#x60;customReference&#x60; (&#x60;startswith&#x60;),  * &#x60;reference&#x60; (&#x60;startswith&#x60;),  * &#x60;serviceCase.id&#x60; (&#x60;eq&#x60;, &#x60;in&#x60;)                See[QueryLang] (docs/ApiQueryLang) for further usage details. | [optional] 
 **orderby** | **str**| Supported Sort Properties:  * &#x60;id&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;),  * &#x60;appName&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;),  * &#x60;customReference&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;),  * &#x60;reference&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;),  * &#x60;status&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;),  * &#x60;productGroup&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;),  * &#x60;createdAt&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)                Default: &#x60;id&#x60; &#x60;desc&#x60;. | [optional] 
 **skip** | **int**| The number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **top** | **int**| The number of records to retrieve (default: 25, max: 500). | [optional] [default to 25]

### Return type

[**QuotesCollection**](QuotesCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_client_quote_status**
> Quote set_client_quote_status(body, authorization, x_api_key, client_id, quote_id, status, accept=accept)

Sets a new status for the client quote.

This endpoint allows an API user to create a new status for the quote or illustration.  This will replace the current status value.

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Quote() # Quote | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
status = 'status_example' # str | New quote status. Supported values are Initiated, Submitted, Failed, Expired and Complete.
accept = 'accept_example' # str |  (optional)

try:
    # Sets a new status for the client quote.
    api_response = api_instance.set_client_quote_status(body, authorization, x_api_key, client_id, quote_id, status, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->set_client_quote_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Quote**](Quote.md)|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **status** | **str**| New quote status. Supported values are Initiated, Submitted, Failed, Expired and Complete. | 
 **accept** | **str**|  | [optional] 

### Return type

[**Quote**](Quote.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_quote_result_product_benefits**
> ProductBenefitFeatures update_client_quote_result_product_benefits(body, authorization, x_api_key, client_id, quote_id, quote_result_id, accept=accept)

This endpoint allows an API user to update product details of a specific quote result or illustration result for a client.

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductBenefitFeatures() # ProductBenefitFeatures | Request document with product benefit features
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier - The special value `me` can be used to indicate the authenticated user.
quote_id = 56 # int | Quote identifier.
quote_result_id = 56 # int | Quote result identifier.
accept = 'accept_example' # str |  (optional)

try:
    # This endpoint allows an API user to update product details of a specific quote result or illustration result for a client.
    api_response = api_instance.update_client_quote_result_product_benefits(body, authorization, x_api_key, client_id, quote_id, quote_result_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->update_client_quote_result_product_benefits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductBenefitFeatures**](ProductBenefitFeatures.md)| Request document with product benefit features | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value &#x60;me&#x60; can be used to indicate the authenticated user. | 
 **quote_id** | **int**| Quote identifier. | 
 **quote_result_id** | **int**| Quote result identifier. | 
 **accept** | **str**|  | [optional] 

### Return type

[**ProductBenefitFeatures**](ProductBenefitFeatures.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

