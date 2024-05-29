# swagger_client.ContributionsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_plan_contributions**](ContributionsApi.md#create_plan_contributions) | **POST** /clients/{clientId}/plans/{planId}/contributions | Creates a contribution for a given client and plan. 
[**delete_client_plan_contribution**](ContributionsApi.md#delete_client_plan_contribution) | **DELETE** /clients/{clientId}/plans/{planId}/contributions/{contributionId} | Deletes a contribution for a given plan. 
[**get_client_plan_contribution**](ContributionsApi.md#get_client_plan_contribution) | **GET** /clients/{clientId}/plans/{planId}/contributions/{contributionId} | Returns a contribution for a given client and plan. 
[**list_client_plan_contributions**](ContributionsApi.md#list_client_plan_contributions) | **GET** /clients/{clientId}/plans/{planId}/contributions | Returns list of contributions for a given client and plan. 
[**update_client_plan_contribution**](ContributionsApi.md#update_client_plan_contribution) | **PUT** /clients/{clientId}/plans/{planId}/contributions/{contributionId} | Updates a contribution for a given client and plan. 

# **create_plan_contributions**
> Contribution create_plan_contributions(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)

Creates a contribution for a given client and plan. 

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
api_instance = swagger_client.ContributionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Contribution() # Contribution | Resource Document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client Identifier
plan_id = 56 # int | Plan identifier of the plan where this contribution belongs
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Identifier. (optional)

try:
    # Creates a contribution for a given client and plan. 
    api_response = api_instance.create_plan_contributions(body, authorization, x_api_key, client_id, plan_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContributionsApi->create_plan_contributions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Contribution**](Contribution.md)| Resource Document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client Identifier | 
 **plan_id** | **int**| Plan identifier of the plan where this contribution belongs | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Identifier. | [optional] 

### Return type

[**Contribution**](Contribution.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_plan_contribution**
> delete_client_plan_contribution(authorization, client_id, contribution_id, plan_id, x_api_key, accept=accept)

Deletes a contribution for a given plan. 

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
api_instance = swagger_client.ContributionsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
contribution_id = 56 # int | Contribution identifier
plan_id = 56 # int | Plan identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes a contribution for a given plan. 
    api_instance.delete_client_plan_contribution(authorization, client_id, contribution_id, plan_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling ContributionsApi->delete_client_plan_contribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **contribution_id** | **int**| Contribution identifier | 
 **plan_id** | **int**| Plan identifier | 
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

# **get_client_plan_contribution**
> Contribution get_client_plan_contribution(authorization, client_id, contribution_id, plan_id, x_api_key, accept=accept)

Returns a contribution for a given client and plan. 

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
api_instance = swagger_client.ContributionsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier - The special value \"me\" can be used to indicate the authenticated user.
contribution_id = 56 # int | Contribution identifier
plan_id = 56 # int | Plan identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a contribution for a given client and plan. 
    api_response = api_instance.get_client_plan_contribution(authorization, client_id, contribution_id, plan_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContributionsApi->get_client_plan_contribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier - The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **contribution_id** | **int**| Contribution identifier | 
 **plan_id** | **int**| Plan identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Contribution**](Contribution.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_plan_contributions**
> ContributionCollection list_client_plan_contributions(authorization, client_id, plan_id, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)

Returns list of contributions for a given client and plan. 

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
api_instance = swagger_client.ContributionsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
plan_id = 56 # int | Plan identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | The results can be filtered using one or more of the supported fields and operators.               For details on how to filter and sort data (using the query language) please see [QueryLang](docs/ApiQueryLang).                             The supported fields and operators are:                             * `appliesTo`(`eq`)               * `contributionType` (`eq`, `ne`, `in`)               * `id` (`eq`, `in`)               * `isCurrent` (`eq`)               * `startsOn` (`eq`, `gt`, `lt`,`ge`, `le`)               * `stopsOn` (`eq`, `ne`, `gt`, `lt`,`ge`, `le`)                             Note. By default contributions without a stopson date are returned when using the stopson filter. To filter these records the `eq` and `ne` operators accept null as the parameter                     and can be used to filter for contributions where the stopson date has not been set.                     e.g. filter=stopsOn eq null. (optional)
order_by = 'order_by_example' # str | The results can be ordered by the following fields:                             * `Id`               * `contributionType`               * `isCurrent`               * `startsOn`               * `stopsOn`                             By default the results are ordered by Id. (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
tenant_id = 56 # int | Tenant Identifier. (optional)
top = 100 # int | The number of records to retrieve (default 25, max 100) (optional) (default to 100)

try:
    # Returns list of contributions for a given client and plan. 
    api_response = api_instance.list_client_plan_contributions(authorization, client_id, plan_id, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContributionsApi->list_client_plan_contributions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **plan_id** | **int**| Plan identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| The results can be filtered using one or more of the supported fields and operators.               For details on how to filter and sort data (using the query language) please see [QueryLang](docs/ApiQueryLang).                             The supported fields and operators are:                             * &#x60;appliesTo&#x60;(&#x60;eq&#x60;)               * &#x60;contributionType&#x60; (&#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;in&#x60;)               * &#x60;id&#x60; (&#x60;eq&#x60;, &#x60;in&#x60;)               * &#x60;isCurrent&#x60; (&#x60;eq&#x60;)               * &#x60;startsOn&#x60; (&#x60;eq&#x60;, &#x60;gt&#x60;, &#x60;lt&#x60;,&#x60;ge&#x60;, &#x60;le&#x60;)               * &#x60;stopsOn&#x60; (&#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;gt&#x60;, &#x60;lt&#x60;,&#x60;ge&#x60;, &#x60;le&#x60;)                             Note. By default contributions without a stopson date are returned when using the stopson filter. To filter these records the &#x60;eq&#x60; and &#x60;ne&#x60; operators accept null as the parameter                     and can be used to filter for contributions where the stopson date has not been set.                     e.g. filter&#x3D;stopsOn eq null. | [optional] 
 **order_by** | **str**| The results can be ordered by the following fields:                             * &#x60;Id&#x60;               * &#x60;contributionType&#x60;               * &#x60;isCurrent&#x60;               * &#x60;startsOn&#x60;               * &#x60;stopsOn&#x60;                             By default the results are ordered by Id. | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **tenant_id** | **int**| Tenant Identifier. | [optional] 
 **top** | **int**| The number of records to retrieve (default 25, max 100) | [optional] [default to 100]

### Return type

[**ContributionCollection**](ContributionCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_plan_contribution**
> Contribution update_client_plan_contribution(body, authorization, x_api_key, client_id, contribution_id, plan_id, accept=accept)

Updates a contribution for a given client and plan. 

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
api_instance = swagger_client.ContributionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateContribution() # UpdateContribution | Resource document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier.
contribution_id = 56 # int | Identifier of the contribution which will be updated.
plan_id = 56 # int | Identifier of the plan where this resource belongs.
accept = 'accept_example' # str |  (optional)

try:
    # Updates a contribution for a given client and plan. 
    api_response = api_instance.update_client_plan_contribution(body, authorization, x_api_key, client_id, contribution_id, plan_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContributionsApi->update_client_plan_contribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateContribution**](UpdateContribution.md)| Resource document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **contribution_id** | **int**| Identifier of the contribution which will be updated. | 
 **plan_id** | **int**| Identifier of the plan where this resource belongs. | 
 **accept** | **str**|  | [optional] 

### Return type

[**Contribution**](Contribution.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

