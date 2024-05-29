# swagger_client.NeedsandprioritiesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_question**](NeedsandprioritiesApi.md#get_question) | **GET** /questions/{questionId} | Retrieves the details of a question.
[**list_questions**](NeedsandprioritiesApi.md#list_questions) | **GET** /questions | Retrieves a list of questions associated with the current tenant. The returned list may be filtered.
[**list_questions_answers**](NeedsandprioritiesApi.md#list_questions_answers) | **GET** /clients/{clientId}/questions | Returns a list of the answers a client has given to a given set of questions. The answers are returned in the order that the related questions should be answered.

# **get_question**
> Question get_question(authorization, question_id, x_api_key, accept=accept, tenant_id=tenant_id)

Retrieves the details of a question.

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
api_instance = swagger_client.NeedsandprioritiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
question_id = 56 # int | The identifier of the question to be retrieved.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Optional. The tenant identifier. This can only be used under system reach. (optional)

try:
    # Retrieves the details of a question.
    api_response = api_instance.get_question(authorization, question_id, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NeedsandprioritiesApi->get_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **question_id** | **int**| The identifier of the question to be retrieved. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Optional. The tenant identifier. This can only be used under system reach. | [optional] 

### Return type

[**Question**](Question.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_questions**
> QuestionCollection list_questions(authorization, x_api_key, accept=accept, filter=filter, skip=skip, top=top)

Retrieves a list of questions associated with the current tenant. The returned list may be filtered.

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
api_instance = swagger_client.NeedsandprioritiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | The list of questions returned can be filtered using one or more of the supported fields and operators.  The supported fields and operators are:    *  `tags.any` (`in`)  *  `isArchived` (`eq`)  *  `attributes._category` (`eq`)  *  `attributes._subcategory` (`eq`)                Example filters:      filter = tags.any in ('tagA','tag2') or attributes._category eq 'General'        For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). (optional)
skip = 0 # int | Optional. The number of records to skip. If not specified it defaults to 0. (optional) (default to 0)
top = 100 # int | Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. (optional) (default to 100)

try:
    # Retrieves a list of questions associated with the current tenant. The returned list may be filtered.
    api_response = api_instance.list_questions(authorization, x_api_key, accept=accept, filter=filter, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NeedsandprioritiesApi->list_questions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| The list of questions returned can be filtered using one or more of the supported fields and operators.  The supported fields and operators are:    *  &#x60;tags.any&#x60; (&#x60;in&#x60;)  *  &#x60;isArchived&#x60; (&#x60;eq&#x60;)  *  &#x60;attributes._category&#x60; (&#x60;eq&#x60;)  *  &#x60;attributes._subcategory&#x60; (&#x60;eq&#x60;)                Example filters:      filter &#x3D; tags.any in (&#x27;tagA&#x27;,&#x27;tag2&#x27;) or attributes._category eq &#x27;General&#x27;        For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). | [optional] 
 **skip** | **int**| Optional. The number of records to skip. If not specified it defaults to 0. | [optional] [default to 0]
 **top** | **int**| Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. | [optional] [default to 100]

### Return type

[**QuestionCollection**](QuestionCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_questions_answers**
> QuestionsAnswerCollection list_questions_answers(authorization, client_id, x_api_key, accept=accept, filter=filter, skip=skip, top=top)

Returns a list of the answers a client has given to a given set of questions. The answers are returned in the order that the related questions should be answered.

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
api_instance = swagger_client.NeedsandprioritiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | The list of answers returned can be filtered using one or more of the supported fields and operators.  The supported fields and operators are:    * `question.tags.any` (`in`)  * `question.attributes._category` (`eq`)  * `question.attributes._subcategory` (`eq`)  * `question.isArchived` (`eq`)                Example filters:      filter = question.isArchived eq true        For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). (optional)
skip = 0 # int | Optional. The number of records to skip. If not specified it defaults to 0. (optional) (default to 0)
top = 100 # int | Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. (optional) (default to 100)

try:
    # Returns a list of the answers a client has given to a given set of questions. The answers are returned in the order that the related questions should be answered.
    api_response = api_instance.list_questions_answers(authorization, client_id, x_api_key, accept=accept, filter=filter, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NeedsandprioritiesApi->list_questions_answers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| The list of answers returned can be filtered using one or more of the supported fields and operators.  The supported fields and operators are:    * &#x60;question.tags.any&#x60; (&#x60;in&#x60;)  * &#x60;question.attributes._category&#x60; (&#x60;eq&#x60;)  * &#x60;question.attributes._subcategory&#x60; (&#x60;eq&#x60;)  * &#x60;question.isArchived&#x60; (&#x60;eq&#x60;)                Example filters:      filter &#x3D; question.isArchived eq true        For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). | [optional] 
 **skip** | **int**| Optional. The number of records to skip. If not specified it defaults to 0. | [optional] [default to 0]
 **top** | **int**| Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. | [optional] [default to 100]

### Return type

[**QuestionsAnswerCollection**](QuestionsAnswerCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

