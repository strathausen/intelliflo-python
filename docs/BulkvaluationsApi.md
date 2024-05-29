# swagger_client.BulkvaluationsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_valuation_batch**](BulkvaluationsApi.md#delete_valuation_batch) | **DELETE** /valuations/batches/{batchId} | Deletes an existing valuationbatch and undo any related valuations and transactions
[**enqueue_valuation_batch**](BulkvaluationsApi.md#enqueue_valuation_batch) | **POST** /valuations/batches | Creates a new valuationbatch and enqueues it for importing
[**get_valuation_batch**](BulkvaluationsApi.md#get_valuation_batch) | **GET** /valuations/batches/{batchId} | Returns a single valuationbatch
[**list_valuation_batch_results**](BulkvaluationsApi.md#list_valuation_batch_results) | **GET** /valuations/batches/{batchId}/results | Returns the results for a single valuationbatch.
[**list_valuation_batches**](BulkvaluationsApi.md#list_valuation_batches) | **GET** /valuations/batches | Returns a list of valuationbatch

# **delete_valuation_batch**
> delete_valuation_batch(authorization, batch_id, x_api_key, accept=accept)

Deletes an existing valuationbatch and undo any related valuations and transactions

Use this endpoint to undo any valuations and transactions.                * Only valuationbatches in `completed` state can be undone.  * This is **NOT** meant as a regular use case, instead should only be used when incorrect data was sent in a previous batch.  * Any such incorrect data must be undone within 3 months of creating the valuationbatch or it will be `expired` and then it can no longer be undone.  * If you need to undo the batch, make sure you have spoken to the tenant first so they can take appropriate actions if they have already used the incorrect data when advising a client.

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
api_instance = swagger_client.BulkvaluationsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
batch_id = 56 # int | Batch Id
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes an existing valuationbatch and undo any related valuations and transactions
    api_instance.delete_valuation_batch(authorization, batch_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling BulkvaluationsApi->delete_valuation_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **batch_id** | **int**| Batch Id | 
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

# **enqueue_valuation_batch**
> ValuationBatch enqueue_valuation_batch(body, authorization, x_api_key, x_iflo_product_provider_id, tenant_id, accept=accept, x_iflo_planmatch_includeportalreference=x_iflo_planmatch_includeportalreference, x_iflo_planmatch_normalised=x_iflo_planmatch_normalised)

Creates a new valuationbatch and enqueues it for importing

Use this endpoint to upload large batches of valuation data.    ### Request Headers  In addition to standard headers like `Authorization` and `x-api-key` there are some additional `headers` required for bulk valuation.  Please see **Request Headers** section below for details.    ### Request Body  * Header must be provided in the first line separated with `single tab` and must be as below.  `PolicyNumber    PortalReference CodeType    Code    Name    Units   UnitsDate   UnitPrice   CurrencyCode`  * Data must be of the product provider  and/or of any its linked product providers.  * Maximum size supported per batch is 10 MB.  * Data can be split in multiple batches, but ensure single policy's holdings are NOT split between batches.  * Any duplicate holdings for a single policy must be merged.  * Unit price can be omitted if the fund can be matched to a feed fund or equity or an existing manual fund.    #### Details of schema    | Field Name     | Type  |Description |  |:-----------------|:-------------------|:---------|  | PolicyNumber    | string(255) | **Required**.  Unique number to identify the plan |  | PortalReference | string(255) | **Optional**.  Any additional provider reference|  | CodeType        | string(15) | **Required**.  Allowed values are ` 'ISIN','SEDOL','CITI','MEX','EPIC','ProviderCode','APIR','TICKER' depending on region.`|  | Code | string(50) | **Required**.|  | Name | string(255) | **Required**.|  | Units | decimal(18,4) | **Required**.|  | UnitsDate | string(10) | **Required**.  Must be in ISO 8601 Date format (` 'YYYY-MM-DD' `) |  | UnitPrice | decimal(18,4) | **Optional**.|  | CurrencyCode | string(3) | **Required**. Must be the three letter ISO 4217 alphabetic code, We also support `GBX` |  ### Example   Note: A full list of regional URL's are available [here](docs/URLs).  ```curl  $YOUR_API_KEY='your Intelliflo API access key'  $YOUR_AUTHENTICATION_TOKEN='your JSON Web Token'  $PRODUCT_PROVIDER_ID='correct product provider id - double check if you are not sure'  curl -X POST \\    https://api.intelliflo.com/v2/valuations/batches \\    -H 'Authorization: $YOUR_AUTHENTICATION_TOKEN' \\    -H 'x-api-key: $YOUR_API_KEY' \\    -H 'Content-Type: text/tab-separated-values' \\    -H 'x-iflo-productProviderId: $PRODUCT_PROVIDER_ID' \\    -d '  PolicyNumber PortalReference CodeType Code Name Units UnitsDate UnitPrice CurrencyCode  isa01  isin IE00BGJWXV08 Metzler Cap 100 2019-02-28 85 GBP  isa01  Epic 0JGD ISHARES GLOBAL 50 2019-02-26 77.00 EUR  isa01  ProviderCode Cash Cash 75 2019-02-26 1 GBX  '  ```

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
api_instance = swagger_client.BulkvaluationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppId() # AppId | 
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
x_iflo_product_provider_id = 56 # int | Id of the Product Provider  You can list the available product providers using the [ProductProviders API](/apis?tags=productproviders#ListProductproviders)
tenant_id = 56 # int | 
accept = 'accept_example' # str |  (optional)
x_iflo_planmatch_includeportalreference = true # bool | Determines whether to include the portal reference in matching algorithm.  Default is `false` and plans will be matched only on `PolicyNumber`.  By providing `true` in here plans will be matched on `PolicyNumber`  and `PortalReference`.  You may want to consider this when `PolicyNumber` is not unique to the product provider. (optional)
x_iflo_planmatch_normalised = true # bool | Determines whether to sanitize the field values in the matching algorithm.  Default is `false` and will be an exact (but not case sensitive) match on the matching fields.  By providing `true` in here we will remove any spaces and any leading zeroes in IO before matching.  In such case ensure the batch has them already removed in the matching fields. (optional)

try:
    # Creates a new valuationbatch and enqueues it for importing
    api_response = api_instance.enqueue_valuation_batch(body, authorization, x_api_key, x_iflo_product_provider_id, tenant_id, accept=accept, x_iflo_planmatch_includeportalreference=x_iflo_planmatch_includeportalreference, x_iflo_planmatch_normalised=x_iflo_planmatch_normalised)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkvaluationsApi->enqueue_valuation_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppId**](AppId.md)|  | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_iflo_product_provider_id** | **int**| Id of the Product Provider  You can list the available product providers using the [ProductProviders API](/apis?tags&#x3D;productproviders#ListProductproviders) | 
 **tenant_id** | **int**|  | 
 **accept** | **str**|  | [optional] 
 **x_iflo_planmatch_includeportalreference** | **bool**| Determines whether to include the portal reference in matching algorithm.  Default is &#x60;false&#x60; and plans will be matched only on &#x60;PolicyNumber&#x60;.  By providing &#x60;true&#x60; in here plans will be matched on &#x60;PolicyNumber&#x60;  and &#x60;PortalReference&#x60;.  You may want to consider this when &#x60;PolicyNumber&#x60; is not unique to the product provider. | [optional] 
 **x_iflo_planmatch_normalised** | **bool**| Determines whether to sanitize the field values in the matching algorithm.  Default is &#x60;false&#x60; and will be an exact (but not case sensitive) match on the matching fields.  By providing &#x60;true&#x60; in here we will remove any spaces and any leading zeroes in IO before matching.  In such case ensure the batch has them already removed in the matching fields. | [optional] 

### Return type

[**ValuationBatch**](ValuationBatch.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: text/tab-separated-values, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_valuation_batch**
> ValuationBatch get_valuation_batch(authorization, batch_id, tenant_id, x_api_key, accept=accept)

Returns a single valuationbatch

Use this endpoint to view the status of a batch.                Batch can have one of the following status  * Queued  * InProgress  * Failed  * Completed  * DeleteInProgress  * DeleteFailed  * Expired (When a batch is older than 3 months batch data will be removed and the batch state will be set to `Expired` by system)

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
api_instance = swagger_client.BulkvaluationsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
batch_id = 56 # int | batch id
tenant_id = 56 # int | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a single valuationbatch
    api_response = api_instance.get_valuation_batch(authorization, batch_id, tenant_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkvaluationsApi->get_valuation_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **batch_id** | **int**| batch id | 
 **tenant_id** | **int**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**ValuationBatch**](ValuationBatch.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_valuation_batch_results**
> ValuationBatchResultCollection list_valuation_batch_results(authorization, batch_id, tenant_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top, x_iflo_exclude_holdings=x_iflo_exclude_holdings)

Returns the results for a single valuationbatch.

Use this endpoint to view the results of a valuationbatch  * Results will not be available after the valuationbatch is `expired`  * It will have items grouped in `holdings` by `policyNumber` and `portalReference`  * It will have a `matched_plan` indicating if the item has matched to a plan or not  * when `matched_plan = true`      * It will have a `matched_plan_href` to navigate to the plan  * when `matched_plan = true and is_imported = true`      * Holdings will have a `matched_holding_href` to navigate to the holding  * Note that if no fund price is supplied and the fund cannot be matched to a feed fund or equity    then the valuation for plan will not be imported  Use GET valuations/batches to get the batch id and to see the status of the batch.  You can use the optional header x-iflo-exclude-holdings=true to exclude the holdings detail from the response.  This is advisable when fetching the results of large batches.

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
api_instance = swagger_client.BulkvaluationsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
batch_id = 56 # int | batch id
tenant_id = 56 # int | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Results can be filtered using one or more supported fields and operators below.              For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).              Supported fields (operators) are              `PolicyNumber` ( `in`, `eq`, `ne`, `startswith` ),              `PortalReference` ( `in`, `eq`, `ne`, `startswith` ),              `Matched_Plan` ( `eq`, `ne` )              `Is_Imported` ( `eq`, `ne` )              Usage example: `filter=matched_plan eq false` (optional)
orderby = 'orderby_example' # str | By default the results will be ordered asc by PolicyNumber.              However it can be changed using one or more supported fields below.              `PolicyNumber`, `PortalReference`, `matched_plan`              Usage example: `orderby=PortalReference desc` (optional)
skip = 56 # int | Number of records to skip. Must be greater than or equal to zero (optional)
top = 56 # int | Number of records to retrieve (default 100, max 500) (optional)
x_iflo_exclude_holdings = false # bool |  (optional) (default to false)

try:
    # Returns the results for a single valuationbatch.
    api_response = api_instance.list_valuation_batch_results(authorization, batch_id, tenant_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top, x_iflo_exclude_holdings=x_iflo_exclude_holdings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkvaluationsApi->list_valuation_batch_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **batch_id** | **int**| batch id | 
 **tenant_id** | **int**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Results can be filtered using one or more supported fields and operators below.              For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).              Supported fields (operators) are              &#x60;PolicyNumber&#x60; ( &#x60;in&#x60;, &#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;startswith&#x60; ),              &#x60;PortalReference&#x60; ( &#x60;in&#x60;, &#x60;eq&#x60;, &#x60;ne&#x60;, &#x60;startswith&#x60; ),              &#x60;Matched_Plan&#x60; ( &#x60;eq&#x60;, &#x60;ne&#x60; )              &#x60;Is_Imported&#x60; ( &#x60;eq&#x60;, &#x60;ne&#x60; )              Usage example: &#x60;filter&#x3D;matched_plan eq false&#x60; | [optional] 
 **orderby** | **str**| By default the results will be ordered asc by PolicyNumber.              However it can be changed using one or more supported fields below.              &#x60;PolicyNumber&#x60;, &#x60;PortalReference&#x60;, &#x60;matched_plan&#x60;              Usage example: &#x60;orderby&#x3D;PortalReference desc&#x60; | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] 
 **top** | **int**| Number of records to retrieve (default 100, max 500) | [optional] 
 **x_iflo_exclude_holdings** | **bool**|  | [optional] [default to false]

### Return type

[**ValuationBatchResultCollection**](ValuationBatchResultCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_valuation_batches**
> ValuationBatchCollection list_valuation_batches(authorization, tenant_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of valuationbatch

Use this endpoint to view the statuses of multiple valuationbatches.

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
api_instance = swagger_client.BulkvaluationsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
tenant_id = 56 # int | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | List can be filtered using one or more supported fields and operators below.              For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).              Supported fields (operators) are              `Id` (`in`,`eq`,`ne`,`gt`,`ge`,`lt`,`le`),              `State` (`in`,`eq`,`ne`),              `CreatedAt` (`in`,`eq`,`ne`,`gt`,`ge`,`lt`,`le`),              `ProductProvider.Id` (`in`,`eq`,`ne`,`gt`,`ge`,`lt`,`le`),              `CreatedBy.Name` (`in`,`eq`,`ne`,`startswith`)              Usage example: `filter=state eq 'failed' ` (optional)
orderby = 'orderby_example' # str | By default the list will be ordered desc by Id.              However it can be changed using one or more supported fields below.              `Id`, `CreatedAt`, `ProductProvider.Id`, `CreatedBy.Name`              Usage example: `orderby=CreatedAt asc` (optional)
skip = 56 # int | Number of records to skip. Must be greater than or equal to zero (optional)
top = 56 # int | Number of records to retrieve (default 100, max 500) (optional)

try:
    # Returns a list of valuationbatch
    api_response = api_instance.list_valuation_batches(authorization, tenant_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkvaluationsApi->list_valuation_batches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **tenant_id** | **int**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| List can be filtered using one or more supported fields and operators below.              For details on how to use the query language please see [QueryLang](docs/ApiQueryLang).              Supported fields (operators) are              &#x60;Id&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;,&#x60;gt&#x60;,&#x60;ge&#x60;,&#x60;lt&#x60;,&#x60;le&#x60;),              &#x60;State&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;),              &#x60;CreatedAt&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;,&#x60;gt&#x60;,&#x60;ge&#x60;,&#x60;lt&#x60;,&#x60;le&#x60;),              &#x60;ProductProvider.Id&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;,&#x60;gt&#x60;,&#x60;ge&#x60;,&#x60;lt&#x60;,&#x60;le&#x60;),              &#x60;CreatedBy.Name&#x60; (&#x60;in&#x60;,&#x60;eq&#x60;,&#x60;ne&#x60;,&#x60;startswith&#x60;)              Usage example: &#x60;filter&#x3D;state eq &#x27;failed&#x27; &#x60; | [optional] 
 **orderby** | **str**| By default the list will be ordered desc by Id.              However it can be changed using one or more supported fields below.              &#x60;Id&#x60;, &#x60;CreatedAt&#x60;, &#x60;ProductProvider.Id&#x60;, &#x60;CreatedBy.Name&#x60;              Usage example: &#x60;orderby&#x3D;CreatedAt asc&#x60; | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] 
 **top** | **int**| Number of records to retrieve (default 100, max 500) | [optional] 

### Return type

[**ValuationBatchCollection**](ValuationBatchCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

