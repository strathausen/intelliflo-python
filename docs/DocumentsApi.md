# swagger_client.DocumentsApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_document**](DocumentsApi.md#create_client_document) | **POST** /clients/{clientId}/documents | Creates a document for a given client. 
[**get_client_document**](DocumentsApi.md#get_client_document) | **GET** /clients/{clientId}/documents/{documentId} | Returns a document for a given client and document. 
[**list_client_documents**](DocumentsApi.md#list_client_documents) | **GET** /clients/{clientId}/documents | Returns a list of documents for a given client. 
[**update_client_document**](DocumentsApi.md#update_client_document) | **PUT** /clients/{clientId}/documents/{documentId} | Updates a document for a given client and document. 

# **create_client_document**
> Document create_client_document(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)

Creates a document for a given client. 

Use this endpoint to create a client document metadata record. A successful response (201), will return a `x-iflo-object-location` response header that will contain a pre-authenticated and signed hyperlink value. Use this hyperlink to PUT the associated object content.  *Note:*    * No other headers are required for the object upload, a simple PUT on the hyperlink is all that is required. * The object hyperlink is signed with an expiry of 15 minutes, so you have 15 minutes to initiate the upload before the link will expire.     #### **Properties**  The following reserved fields are supported for properties object, they provide additional functionality:  * `_category.name`               *   Sets document category * `_subCategory.name`            *   Sets document sub category * `_fileType.name`      *   Sets file Type * `_status.name`      *   Sets document status  Custom properties are supported.   #### **Tags**  Tags are useful for categorizing and filtering documents.  * Maximum 5 tags per document * Maximum 65 characters per tag * Tags must not contain spaces * Tags must not contain any special characters   #### **Example**   ~~~~javascript {     \"title\":\"A new document\",     \"description\":\"A shiny new document\",     \"properties\":{         \"_fileType.name\": \"Bank Statement\",         \"_subCategory.name\": \"Third Party\",         \"_category.name\": \"Financials\"         \"_status.name\": \"Production\"         \"CustomProperty1\": \"Some Value\"         \"CustomProperty2\": \"Some Value\"     },     \"object\":{         \"original_filename\":\"foo.txt\"     } ,     \"tags\" : {         \"tag1\", \"tag2\"     }     \"linked_entities\":[         {              \"id\" : 123,              \"type\" : \"Plan\"         }   ] } ~~~~ 

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Document() # Document | Client document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier. The special value \"me\" can be used to indicate the authenticated user.
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Creates a document for a given client. 
    api_response = api_instance.create_client_document(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->create_client_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Document**](Document.md)| Client document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_document**
> Document get_client_document(authorization, client_id, document_id, x_api_key, accept=accept, tenant_id=tenant_id)

Returns a document for a given client and document. 

Use this endpoint to retrieve a client's document metadata. A successful response (200), will also return a `x-iflo-object-location` response header that will contain a pre-authenticated and signed hyperlink value. Use this hyperlink to download (GET) the associated object content. *Note:*   * No other headers are required for the object download, a simple GET on the hyperlink is all that is required. * The object hyperlink is signed with an expiry of 15 minutes, so you have 15 minutes to initiate the download before the link will expire. * This link will also work directly in a browser by pasting the link into the location bar. 

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier. The special value \"me\" can be used to indicate the authenticated user.
document_id = 56 # int | Document identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Returns a document for a given client and document. 
    api_response = api_instance.get_client_document(authorization, client_id, document_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_client_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **document_id** | **int**| Document identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_documents**
> DocumentCollection list_client_documents(authorization, client_id, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)

Returns a list of documents for a given client. 

 To filter by tags, append the following to the query string.  `..?filter=tag in ('tag1','tag2' )`  

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier. The special value \"me\" can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Used to filter documents. Supported fields: id(in, eq, gt, lt), createdat(gt, lt), tag(in), linked_entities.type(in),              linked_entities.id(in, eq), properties._status.name(eq), properties._clientDocumentId(eq), properties._isEsignatureDocument(eq),              properties._category.name(eq), properties._subCategory.name(eq), properties._fileType.name(eq)...              Sample: filter=tag in ('private22', 'tag1') (optional)
order_by = 'order_by_example' # str | Supported fields: id, createdat, title. Supported directions: asc, desc. Sample: orderBy=name desc (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero (optional) (default to 0)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)
top = 100 # int | The number of records to retrieve (default 25, max 100) (optional) (default to 100)

try:
    # Returns a list of documents for a given client. 
    api_response = api_instance.list_client_documents(authorization, client_id, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, tenant_id=tenant_id, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->list_client_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Used to filter documents. Supported fields: id(in, eq, gt, lt), createdat(gt, lt), tag(in), linked_entities.type(in),              linked_entities.id(in, eq), properties._status.name(eq), properties._clientDocumentId(eq), properties._isEsignatureDocument(eq),              properties._category.name(eq), properties._subCategory.name(eq), properties._fileType.name(eq)...              Sample: filter&#x3D;tag in (&#x27;private22&#x27;, &#x27;tag1&#x27;) | [optional] 
 **order_by** | **str**| Supported fields: id, createdat, title. Supported directions: asc, desc. Sample: orderBy&#x3D;name desc | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero | [optional] [default to 0]
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 
 **top** | **int**| The number of records to retrieve (default 25, max 100) | [optional] [default to 100]

### Return type

[**DocumentCollection**](DocumentCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_document**
> Document update_client_document(body, authorization, x_api_key, client_id, document_id, accept=accept, tenant_id=tenant_id)

Updates a document for a given client and document. 

Use this endpoint to update a client's document metadata. A successful response (200), will return a `x-iflo-object-location` response header that will contain a pre-authenticated and signed hyperlink value. Use this hyperlink to PUT the associated object content. *Note:*   * No other headers are required for the object upload, a simple PUT on the hyperlink is all that is required. Form data is not supported for this request. * The object hyperlink is signed with an expiry of 15 minutes, so you have 15 minutes to initiate the upload before the link will expire.    #### **Tags**  When updating tags:  * Only tags listed will be saved. Any tags not listed will be removed. * Specifying an empty body will remove all existing tags * Omitting the \"tags\" property will be preserve existing tags.  To delete a tag, perform update, removing the unwanted tag from the list.   

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
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Document() # Document | Client document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier. The special value \"me\" can be used to indicate the authenticated user.
document_id = 56 # int | Document identifier.
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Updates a document for a given client and document. 
    api_response = api_instance.update_client_document(body, authorization, x_api_key, client_id, document_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->update_client_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Document**](Document.md)| Client document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **document_id** | **int**| Document identifier. | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

