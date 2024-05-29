# swagger_client.UnmatchedplansApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_unmatched_plans**](UnmatchedplansApi.md#list_unmatched_plans) | **GET** /plans/unmatched | Gets a Collection of unmatched Plans.

# **list_unmatched_plans**
> UnmatchedPlanDocumentCollection list_unmatched_plans(authorization, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)

Gets a Collection of unmatched Plans.

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
api_instance = swagger_client.UnmatchedplansApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | List can be filtered using one or more supported fields and operators below.                Supported fields (operators) are:  * `id` (`in`)  * `productName` (`in`,`eq`)  * `planType.name` (`in`,`eq`,`ne`)  * `policyNumber` (`in`,`eq`)  * `owner.name` (`eq`,`startswith`)  * `sellingAdviser.name` (`eq`,`startswith`)                Usage examples:  * `filter=id in (123, 134)`  * `filter=type eq 'Product Name'`  * `filter=planType.name in ('Type1', 'Type2')`  * `filter=owner.name startswith 'Peter'`  * `filter=sellingAdviser.name startswith 'John'`                See [QueryLang](docs/ApiQueryLang) for further usage details. (optional)
order_by = 'order_by_example' # str | The results can be ordered by the following fields:                * `policyNumber`  * `planType.name`  * `productName`  * `sellingAdviser.name` (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
tenant_id = 56 # int | The Tenant identifier. Can only be used under system reach. (optional)
top = 100 # int | The number of records to retrieve (default 25, max 100). (optional) (default to 100)

try:
    # Gets a Collection of unmatched Plans.
    api_response = api_instance.list_unmatched_plans(authorization, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnmatchedplansApi->list_unmatched_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| List can be filtered using one or more supported fields and operators below.                Supported fields (operators) are:  * &#x60;id&#x60; (&#x60;in&#x60;)  * &#x60;productName&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;)  * &#x60;planType.name&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;)  * &#x60;policyNumber&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;)  * &#x60;owner.name&#x60; (&#x60;eq&#x60;,&#x60;startswith&#x60;)  * &#x60;sellingAdviser.name&#x60; (&#x60;eq&#x60;,&#x60;startswith&#x60;)                Usage examples:  * &#x60;filter&#x3D;id in (123, 134)&#x60;  * &#x60;filter&#x3D;type eq &#x27;Product Name&#x27;&#x60;  * &#x60;filter&#x3D;planType.name in (&#x27;Type1&#x27;, &#x27;Type2&#x27;)&#x60;  * &#x60;filter&#x3D;owner.name startswith &#x27;Peter&#x27;&#x60;  * &#x60;filter&#x3D;sellingAdviser.name startswith &#x27;John&#x27;&#x60;                See [QueryLang](docs/ApiQueryLang) for further usage details. | [optional] 
 **order_by** | **str**| The results can be ordered by the following fields:                * &#x60;policyNumber&#x60;  * &#x60;planType.name&#x60;  * &#x60;productName&#x60;  * &#x60;sellingAdviser.name&#x60; | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **tenant_id** | **int**| The Tenant identifier. Can only be used under system reach. | [optional] 
 **top** | **int**| The number of records to retrieve (default 25, max 100). | [optional] [default to 100]

### Return type

[**UnmatchedPlanDocumentCollection**](UnmatchedPlanDocumentCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-client-credentials](../README.md#oauth2-client-credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

