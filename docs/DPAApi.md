# swagger_client.DPAApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_dpa_policy_agreement**](DPAApi.md#create_client_dpa_policy_agreement) | **POST** /clients/{clientId}/dpa_agreements | Creates a new DPA policy agreement for a client.
[**create_dpa_policy**](DPAApi.md#create_dpa_policy) | **POST** /dpa_policies | Creates a new DPA policy which will become the current DPA policy when created (see notes on party type above).
[**delete_dpa_policy**](DPAApi.md#delete_dpa_policy) | **DELETE** /dpa_policies/{policyId} | Deletes an existing DPA policy. Only policies that are not associated with client agreements can be deleted.
[**get_client_dpa_policy_agreement**](DPAApi.md#get_client_dpa_policy_agreement) | **GET** /clients/{clientId}/dpa_agreements/{agreementId} | Returns a single DPA policy agreement for a client.
[**get_current_dpa_policy**](DPAApi.md#get_current_dpa_policy) | **GET** /dpa_policies/current | Returns the current default DPA policy (see notes on party type above).
[**get_dpa_policy**](DPAApi.md#get_dpa_policy) | **GET** /dpa_policies/{policyId} | Returns a single DPA policy.
[**list_client_dpa_policy_agreements**](DPAApi.md#list_client_dpa_policy_agreements) | **GET** /clients/{clientId}/dpa_agreements | Returns a list of client&#x27;s DPA policy agreements.
[**list_dpa_policies**](DPAApi.md#list_dpa_policies) | **GET** /dpa_policies | Returns a list of DPA policies.
[**patch_dpa_policy**](DPAApi.md#patch_dpa_policy) | **PATCH** /dpa_policies/{policyId} | Updates an existing DPA policy.
[**update_dpa_policy**](DPAApi.md#update_dpa_policy) | **PUT** /dpa_policies/{policyId} | Updates an existing DPA policy.

# **create_client_dpa_policy_agreement**
> DPAPolicyAgreement create_client_dpa_policy_agreement(body, authorization, x_api_key, client_id, accept=accept)

Creates a new DPA policy agreement for a client.

Creates a new DPA policy agreement for a client. A DPA policy agreement is a client's response to a firm's DPA policy.                **Notes:**  * The firm's existing DPA policy should be specified for an agreement to be created.  * In order to be valid, an agreement should contain 'Yes' answers to all policy statements and the agreement date populated.

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
api_instance = swagger_client.DPAApi(swagger_client.ApiClient(configuration))
body = swagger_client.DPAPolicyAgreement() # DPAPolicyAgreement | DPA policy Agreement document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | The client that agreed to the DPA policy. The special value 'me' can be used to indicate the authenticated user.
accept = 'accept_example' # str |  (optional)

try:
    # Creates a new DPA policy agreement for a client.
    api_response = api_instance.create_client_dpa_policy_agreement(body, authorization, x_api_key, client_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DPAApi->create_client_dpa_policy_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DPAPolicyAgreement**](DPAPolicyAgreement.md)| DPA policy Agreement document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| The client that agreed to the DPA policy. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **accept** | **str**|  | [optional] 

### Return type

[**DPAPolicyAgreement**](DPAPolicyAgreement.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dpa_policy**
> DPAPolicy create_dpa_policy(body, authorization, x_api_key, accept=accept)

Creates a new DPA policy which will become the current DPA policy when created (see notes on party type above).

If a party type is specified the DPA policy will be related to that party type. If no party type is specified it becomes the default DPA policy for the tenant.

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
api_instance = swagger_client.DPAApi(swagger_client.ApiClient(configuration))
body = swagger_client.DPAPolicy() # DPAPolicy | A DPA policy document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Creates a new DPA policy which will become the current DPA policy when created (see notes on party type above).
    api_response = api_instance.create_dpa_policy(body, authorization, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DPAApi->create_dpa_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DPAPolicy**](DPAPolicy.md)| A DPA policy document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**DPAPolicy**](DPAPolicy.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dpa_policy**
> delete_dpa_policy(authorization, policy_id, x_api_key, accept=accept)

Deletes an existing DPA policy. Only policies that are not associated with client agreements can be deleted.

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
api_instance = swagger_client.DPAApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
policy_id = 56 # int | DPA policy Identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes an existing DPA policy. Only policies that are not associated with client agreements can be deleted.
    api_instance.delete_dpa_policy(authorization, policy_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling DPAApi->delete_dpa_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **policy_id** | **int**| DPA policy Identifier. | 
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

# **get_client_dpa_policy_agreement**
> DPAPolicyAgreement get_client_dpa_policy_agreement(agreement_id, authorization, client_id, x_api_key, accept=accept)

Returns a single DPA policy agreement for a client.

Returns a single DPA policy agreement for a client. A DPA policy agreement is a client's response to a firm's DPA policy.                **Notes:**  * DPA policy agreement has a maximum of 5 statements with Yes/No responses and an agreement date.

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
api_instance = swagger_client.DPAApi(swagger_client.ApiClient(configuration))
agreement_id = 56 # int | DPA Policy Agreement identifier. The special value 'current' can be used to indicate the latest agreement.
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client that agreed to the DPA policy. The special value 'me' can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a single DPA policy agreement for a client.
    api_response = api_instance.get_client_dpa_policy_agreement(agreement_id, authorization, client_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DPAApi->get_client_dpa_policy_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agreement_id** | **int**| DPA Policy Agreement identifier. The special value &#x27;current&#x27; can be used to indicate the latest agreement. | 
 **authorization** | **str**|  | 
 **client_id** | **int**| The client that agreed to the DPA policy. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**DPAPolicyAgreement**](DPAPolicyAgreement.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_dpa_policy**
> DPAPolicy get_current_dpa_policy(authorization, x_api_key, accept=accept, prefer=prefer)

Returns the current default DPA policy (see notes on party type above).

To retrieve the current DPA policy for a specific party type rather than the default DPA policy, specify the party type in a preference header. The current DPA policy is most recent active policy.                To specify a preference header add a header named 'prefer'  header to one of the following options:   * partytype=Corporate   * partytype=Persons   * partytype=Trust

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
api_instance = swagger_client.DPAApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
prefer = 'prefer_example' # str | Used to indicate the party type associated with the DPA for the request. Options: PartyType=Person (optional)

try:
    # Returns the current default DPA policy (see notes on party type above).
    api_response = api_instance.get_current_dpa_policy(authorization, x_api_key, accept=accept, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DPAApi->get_current_dpa_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **prefer** | **str**| Used to indicate the party type associated with the DPA for the request. Options: PartyType&#x3D;Person | [optional] 

### Return type

[**DPAPolicy**](DPAPolicy.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dpa_policy**
> DPAPolicy get_dpa_policy(authorization, policy_id, x_api_key, accept=accept)

Returns a single DPA policy.

To retrieve the active DPA policy use  the /dpa_policies/current'endpoint.

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
api_instance = swagger_client.DPAApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
policy_id = 56 # int | The DPA policy identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns a single DPA policy.
    api_response = api_instance.get_dpa_policy(authorization, policy_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DPAApi->get_dpa_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **policy_id** | **int**| The DPA policy identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**DPAPolicy**](DPAPolicy.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_dpa_policy_agreements**
> DPAPolicyAgreementCollection list_client_dpa_policy_agreements(authorization, client_id, x_api_key, accept=accept, skip=skip, top=top)

Returns a list of client's DPA policy agreements.

Returns a list of client's DPA policy agreements.

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
api_instance = swagger_client.DPAApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | The client that agreed to the DPA policy. The special value 'me' can be used to indicate the authenticated user.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
skip = 0 # int | Number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
top = 250 # int | Number of records to retrieve (default '25', max '100'). (optional) (default to 250)

try:
    # Returns a list of client's DPA policy agreements.
    api_response = api_instance.list_client_dpa_policy_agreements(authorization, client_id, x_api_key, accept=accept, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DPAApi->list_client_dpa_policy_agreements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| The client that agreed to the DPA policy. The special value &#x27;me&#x27; can be used to indicate the authenticated user. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **skip** | **int**| Number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **top** | **int**| Number of records to retrieve (default &#x27;25&#x27;, max &#x27;100&#x27;). | [optional] [default to 250]

### Return type

[**DPAPolicyAgreementCollection**](DPAPolicyAgreementCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dpa_policies**
> DPAPolicyCollection list_dpa_policies(authorization, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of DPA policies.

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
api_instance = swagger_client.DPAApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported filters options:  *  `name (in)`  *  `partyType (eq)`                Valid values for party type are 'Person', 'Corporate', 'Trust' or 'Default'                See [QueryLang](docs/ApiQueryLang) for further details of how to use the filtering and sorting parameters. (optional)
orderby = 'orderby_example' # str | Supported sorting options:  *  `name`  *  `partyType'  *  `createdat (optional)
skip = 0 # int | The number of records to skip. Must be greater than or equal to zero. (optional) (default to 0)
top = 100 # int | The number of records to retrieve. (optional) (default to 100)

try:
    # Returns a list of DPA policies.
    api_response = api_instance.list_dpa_policies(authorization, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DPAApi->list_dpa_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported filters options:  *  &#x60;name (in)&#x60;  *  &#x60;partyType (eq)&#x60;                Valid values for party type are &#x27;Person&#x27;, &#x27;Corporate&#x27;, &#x27;Trust&#x27; or &#x27;Default&#x27;                See [QueryLang](docs/ApiQueryLang) for further details of how to use the filtering and sorting parameters. | [optional] 
 **orderby** | **str**| Supported sorting options:  *  &#x60;name&#x60;  *  &#x60;partyType&#x27;  *  &#x60;createdat | [optional] 
 **skip** | **int**| The number of records to skip. Must be greater than or equal to zero. | [optional] [default to 0]
 **top** | **int**| The number of records to retrieve. | [optional] [default to 100]

### Return type

[**DPAPolicyCollection**](DPAPolicyCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_dpa_policy**
> DPAPolicy patch_dpa_policy(body, authorization, x_api_key, policy_id, accept=accept)

Updates an existing DPA policy.

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
api_instance = swagger_client.DPAApi(swagger_client.ApiClient(configuration))
body = [swagger_client.Operation()] # list[Operation] | A Json Patch document containing details of modifications to be made to the DPA policy.
Only the following paths may be modified:
* `/clientCanAccept`
            
For a simple example a request contains the following JSON:
            
{
    "op": "replace",
    "path": "/clientCanAccept",
    "value": "True"
}
            
would result in the clientCanAccept value for the targeted resource being set to 'True'.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
policy_id = 56 # int | DPA policy Identifier.
accept = 'accept_example' # str |  (optional)

try:
    # Updates an existing DPA policy.
    api_response = api_instance.patch_dpa_policy(body, authorization, x_api_key, policy_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DPAApi->patch_dpa_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Operation]**](Operation.md)| A Json Patch document containing details of modifications to be made to the DPA policy.
Only the following paths may be modified:
* &#x60;/clientCanAccept&#x60;
            
For a simple example a request contains the following JSON:
            
{
    &quot;op&quot;: &quot;replace&quot;,
    &quot;path&quot;: &quot;/clientCanAccept&quot;,
    &quot;value&quot;: &quot;True&quot;
}
            
would result in the clientCanAccept value for the targeted resource being set to &#x27;True&#x27;. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **policy_id** | **int**| DPA policy Identifier. | 
 **accept** | **str**|  | [optional] 

### Return type

[**DPAPolicy**](DPAPolicy.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dpa_policy**
> DPAPolicy update_dpa_policy(body, authorization, x_api_key, policy_id, accept=accept)

Updates an existing DPA policy.

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
api_instance = swagger_client.DPAApi(swagger_client.ApiClient(configuration))
body = swagger_client.DPAPolicy() # DPAPolicy | A DPA policy document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
policy_id = 56 # int | The DPA policy Identifier.
accept = 'accept_example' # str |  (optional)

try:
    # Updates an existing DPA policy.
    api_response = api_instance.update_dpa_policy(body, authorization, x_api_key, policy_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DPAApi->update_dpa_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DPAPolicy**](DPAPolicy.md)| A DPA policy document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **policy_id** | **int**| The DPA policy Identifier. | 
 **accept** | **str**|  | [optional] 

### Return type

[**DPAPolicy**](DPAPolicy.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

