# swagger_client.OpportunitiesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_campaign_channel**](OpportunitiesApi.md#create_campaign_channel) | **POST** /opportunities/campaignchannels | Creates a new Campaign Channel.
[**create_campaign_type**](OpportunitiesApi.md#create_campaign_type) | **POST** /opportunities/campaigntypes | Creates a new Campaign Type.
[**create_client_opportunity**](OpportunitiesApi.md#create_client_opportunity) | **POST** /clients/{clientId}/opportunities | Creates a new Opportunity for the given client.
[**create_lead_opportunity**](OpportunitiesApi.md#create_lead_opportunity) | **POST** /leads/{leadId}/opportunities | Creates a new Opportunity for the given Lead.
[**create_opportunity_campaign**](OpportunitiesApi.md#create_opportunity_campaign) | **POST** /opportunities/campaigns | Creates a new Opportunity campaign for a tenant.
[**create_opportunity_proposition**](OpportunitiesApi.md#create_opportunity_proposition) | **POST** /opportunities/propositions | Creates a new Opportunity proposition for a tenant.
[**create_opportunity_status**](OpportunitiesApi.md#create_opportunity_status) | **POST** /opportunities/statuses | Creates a new Opportunity Status.
[**create_opportunity_type**](OpportunitiesApi.md#create_opportunity_type) | **POST** /opportunities/types | Creates a new Opportunity Type for a tenant.
[**delete_campaign_channel**](OpportunitiesApi.md#delete_campaign_channel) | **DELETE** /opportunities/campaignchannels/{campaignChannelId} | Deletes Campaign Channel for a given tenant
[**delete_campaign_type**](OpportunitiesApi.md#delete_campaign_type) | **DELETE** /opportunities/campaigntypes/{campaignTypeId} | Deletes Campaign Type for a given tenant
[**delete_opportunity_campaign**](OpportunitiesApi.md#delete_opportunity_campaign) | **DELETE** /opportunities/campaigns/{opportunityCampaignId} | Deletes an Opportunity campaign. Only Opportunity campaigns that are not in use can be deleted.
[**delete_opportunity_proposition**](OpportunitiesApi.md#delete_opportunity_proposition) | **DELETE** /opportunities/propositions/{propositionId} | Deletes an existing Opportunity proposition for a tenant.
[**delete_opportunity_status**](OpportunitiesApi.md#delete_opportunity_status) | **DELETE** /opportunities/statuses/{opportunityStatusId} | Deletes an opportunity status for a given tenant
[**delete_opportunity_type**](OpportunitiesApi.md#delete_opportunity_type) | **DELETE** /opportunities/types/{opportunityTypeId} | Deletes an Opportunity type. Only opportunity types that are not in use can be deleted.
[**get_client_opportunity**](OpportunitiesApi.md#get_client_opportunity) | **GET** /clients/{clientId}/opportunities/{opportunityId} | Returns opportunity documents for a given client and document. 
[**get_lead_opportunity**](OpportunitiesApi.md#get_lead_opportunity) | **GET** /leads/{leadId}/opportunities/{opportunityId} | Returns an opportunity document for a given lead. 
[**get_opportunity_type**](OpportunitiesApi.md#get_opportunity_type) | **GET** /opportunities/types/{opportunityTypeId} | Returns the requested Opportunity type for a tenant.
[**list_campaign_channels**](OpportunitiesApi.md#list_campaign_channels) | **GET** /opportunities/campaignchannels | Returns a list of campaign channel for a given tenant.
[**list_campaign_types**](OpportunitiesApi.md#list_campaign_types) | **GET** /opportunities/campaigntypes | Returns a list of campaign types for a given tenant.
[**list_client_opportunities**](OpportunitiesApi.md#list_client_opportunities) | **GET** /clients/{clientId}/opportunities | Returns list of opportunities for a given client. 
[**list_lead_opportunities**](OpportunitiesApi.md#list_lead_opportunities) | **GET** /leads/{leadId}/opportunities | Returns a list of opportunity documents for a given lead. 
[**list_opportunity_campaigns**](OpportunitiesApi.md#list_opportunity_campaigns) | **GET** /opportunities/campaigns | Returns a list of the Opportunity campaigns for a tenant.
[**list_opportunity_propositions**](OpportunitiesApi.md#list_opportunity_propositions) | **GET** /opportunities/propositions | Returns a list of the opportunity propositions for a tenant.
[**list_opportunity_statuses**](OpportunitiesApi.md#list_opportunity_statuses) | **GET** /opportunities/statuses | Returns a list of opportunity statuses for a given tenant
[**list_opportunity_types**](OpportunitiesApi.md#list_opportunity_types) | **GET** /opportunities/types | Returns a list of the opportunity types for a tenant.
[**update_campaign_channel**](OpportunitiesApi.md#update_campaign_channel) | **PUT** /opportunities/campaignchannels/{campaignChannelId} | Updates an existing Campaign Channel.
[**update_campaign_type**](OpportunitiesApi.md#update_campaign_type) | **PUT** /opportunities/campaigntypes/{campaignTypeId} | Updates an existing Campaign Type.
[**update_client_opportunity**](OpportunitiesApi.md#update_client_opportunity) | **PUT** /clients/{clientId}/opportunities/{opportunityId} | Updates an existing Opportunity for the given client.
[**update_lead_opporunity**](OpportunitiesApi.md#update_lead_opporunity) | **PUT** /leads/{leadId}/opportunities/{opportunityId} | Updates an existing Opportunity for the given Lead.
[**update_opportunity_campaign**](OpportunitiesApi.md#update_opportunity_campaign) | **PUT** /opportunities/campaigns/{opportunityCampaignId} | Updates an Opportunity campaign for a tenant.
[**update_opportunity_proposition**](OpportunitiesApi.md#update_opportunity_proposition) | **PUT** /opportunities/propositions/{propositionId} | Updates an existing Opportunity proposition for a tenant.
[**update_opportunity_status**](OpportunitiesApi.md#update_opportunity_status) | **PUT** /opportunities/statuses/{opportunityStatusId} | Updates an existing Opportunity Status.
[**update_opportunity_type**](OpportunitiesApi.md#update_opportunity_type) | **PUT** /opportunities/types/{opportunityTypeId} | Updates an Opportunity Type for a tenant.

# **create_campaign_channel**
> CampaignChannel create_campaign_channel(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)

Creates a new Campaign Channel.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CampaignChannel() # CampaignChannel | Campaign Channel document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Creates a new Campaign Channel.
    api_response = api_instance.create_campaign_channel(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->create_campaign_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CampaignChannel**](CampaignChannel.md)| Campaign Channel document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**CampaignChannel**](CampaignChannel.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_campaign_type**
> CampaignType create_campaign_type(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)

Creates a new Campaign Type.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CampaignType() # CampaignType | Campaign Type document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Creates a new Campaign Type.
    api_response = api_instance.create_campaign_type(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->create_campaign_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CampaignType**](CampaignType.md)| Campaign Type document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**CampaignType**](CampaignType.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_opportunity**
> Opportunity create_client_opportunity(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)

Creates a new Opportunity for the given client.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Opportunity() # Opportunity | Opportunity document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Creates a new Opportunity for the given client.
    api_response = api_instance.create_client_opportunity(body, authorization, x_api_key, client_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->create_client_opportunity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Opportunity**](Opportunity.md)| Opportunity document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**Opportunity**](Opportunity.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_lead_opportunity**
> Opportunity create_lead_opportunity(body, authorization, x_api_key, lead_id, accept=accept, tenant_id=tenant_id)

Creates a new Opportunity for the given Lead.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Opportunity() # Opportunity | Opportunity document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
lead_id = 56 # int | Lead identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Creates a new Opportunity for the given Lead.
    api_response = api_instance.create_lead_opportunity(body, authorization, x_api_key, lead_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->create_lead_opportunity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Opportunity**](Opportunity.md)| Opportunity document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **lead_id** | **int**| Lead identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**Opportunity**](Opportunity.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_opportunity_campaign**
> OpportunityCampaign create_opportunity_campaign(body, authorization, x_api_key, accept=accept)

Creates a new Opportunity campaign for a tenant.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.OpportunityCampaign() # OpportunityCampaign | Opportunity campaign document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Creates a new Opportunity campaign for a tenant.
    api_response = api_instance.create_opportunity_campaign(body, authorization, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->create_opportunity_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpportunityCampaign**](OpportunityCampaign.md)| Opportunity campaign document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**OpportunityCampaign**](OpportunityCampaign.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_opportunity_proposition**
> OpportunityProposition create_opportunity_proposition(body, authorization, x_api_key, accept=accept)

Creates a new Opportunity proposition for a tenant.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.OpportunityProposition() # OpportunityProposition | Opportunity proposition document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Creates a new Opportunity proposition for a tenant.
    api_response = api_instance.create_opportunity_proposition(body, authorization, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->create_opportunity_proposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpportunityProposition**](OpportunityProposition.md)| Opportunity proposition document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**OpportunityProposition**](OpportunityProposition.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_opportunity_status**
> OpportunityStatus create_opportunity_status(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)

Creates a new Opportunity Status.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.OpportunityStatus() # OpportunityStatus | Opportunity Status document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Creates a new Opportunity Status.
    api_response = api_instance.create_opportunity_status(body, authorization, x_api_key, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->create_opportunity_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpportunityStatus**](OpportunityStatus.md)| Opportunity Status document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**OpportunityStatus**](OpportunityStatus.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_opportunity_type**
> OpportunityType create_opportunity_type(body, authorization, x_api_key, accept=accept)

Creates a new Opportunity Type for a tenant.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.OpportunityType() # OpportunityType | Opportunity type document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Creates a new Opportunity Type for a tenant.
    api_response = api_instance.create_opportunity_type(body, authorization, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->create_opportunity_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpportunityType**](OpportunityType.md)| Opportunity type document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**OpportunityType**](OpportunityType.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign_channel**
> delete_campaign_channel(authorization, campaign_channel_id, x_api_key, accept=accept, tenant_id=tenant_id)

Deletes Campaign Channel for a given tenant

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
campaign_channel_id = 56 # int | Campaign Channel identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Deletes Campaign Channel for a given tenant
    api_instance.delete_campaign_channel(authorization, campaign_channel_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->delete_campaign_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **campaign_channel_id** | **int**| Campaign Channel identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign_type**
> delete_campaign_type(authorization, campaign_type_id, x_api_key, accept=accept, tenant_id=tenant_id)

Deletes Campaign Type for a given tenant

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
campaign_type_id = 56 # int | Campaign Type identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Deletes Campaign Type for a given tenant
    api_instance.delete_campaign_type(authorization, campaign_type_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->delete_campaign_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **campaign_type_id** | **int**| Campaign Type identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_opportunity_campaign**
> delete_opportunity_campaign(authorization, opportunity_campaign_id, x_api_key, accept=accept)

Deletes an Opportunity campaign. Only Opportunity campaigns that are not in use can be deleted.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
opportunity_campaign_id = 56 # int | The identifier for the Opportunity campaign.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes an Opportunity campaign. Only Opportunity campaigns that are not in use can be deleted.
    api_instance.delete_opportunity_campaign(authorization, opportunity_campaign_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->delete_opportunity_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **opportunity_campaign_id** | **int**| The identifier for the Opportunity campaign. | 
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

# **delete_opportunity_proposition**
> delete_opportunity_proposition(authorization, proposition_id, x_api_key, accept=accept)

Deletes an existing Opportunity proposition for a tenant.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
proposition_id = 56 # int | Opportunity proposition identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes an existing Opportunity proposition for a tenant.
    api_instance.delete_opportunity_proposition(authorization, proposition_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->delete_opportunity_proposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **proposition_id** | **int**| Opportunity proposition identifier. | 
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

# **delete_opportunity_status**
> delete_opportunity_status(authorization, opportunity_status_id, x_api_key, accept=accept, tenant_id=tenant_id)

Deletes an opportunity status for a given tenant

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
opportunity_status_id = 56 # int | Opportunity Status identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Deletes an opportunity status for a given tenant
    api_instance.delete_opportunity_status(authorization, opportunity_status_id, x_api_key, accept=accept, tenant_id=tenant_id)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->delete_opportunity_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **opportunity_status_id** | **int**| Opportunity Status identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_opportunity_type**
> delete_opportunity_type(authorization, opportunity_type_id, x_api_key, accept=accept)

Deletes an Opportunity type. Only opportunity types that are not in use can be deleted.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
opportunity_type_id = 56 # int | The identifier for the Opportunity type.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Deletes an Opportunity type. Only opportunity types that are not in use can be deleted.
    api_instance.delete_opportunity_type(authorization, opportunity_type_id, x_api_key, accept=accept)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->delete_opportunity_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **opportunity_type_id** | **int**| The identifier for the Opportunity type. | 
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

# **get_client_opportunity**
> Opportunity get_client_opportunity(authorization, client_id, opportunity_id, x_api_key, accept=accept)

Returns opportunity documents for a given client and document. 

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier
opportunity_id = 56 # int | Opportunity identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns opportunity documents for a given client and document. 
    api_response = api_instance.get_client_opportunity(authorization, client_id, opportunity_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->get_client_opportunity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **opportunity_id** | **int**| Opportunity identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Opportunity**](Opportunity.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lead_opportunity**
> Opportunity get_lead_opportunity(authorization, lead_id, opportunity_id, x_api_key, accept=accept)

Returns an opportunity document for a given lead. 

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
lead_id = 56 # int | Lead identifier
opportunity_id = 56 # int | Opportunity identifier
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns an opportunity document for a given lead. 
    api_response = api_instance.get_lead_opportunity(authorization, lead_id, opportunity_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->get_lead_opportunity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **lead_id** | **int**| Lead identifier | 
 **opportunity_id** | **int**| Opportunity identifier | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**Opportunity**](Opportunity.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_opportunity_type**
> OpportunityType get_opportunity_type(authorization, opportunity_type_id, x_api_key, accept=accept)

Returns the requested Opportunity type for a tenant.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
opportunity_type_id = 56 # int | The identifier for the Opportunity type.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)

try:
    # Returns the requested Opportunity type for a tenant.
    api_response = api_instance.get_opportunity_type(authorization, opportunity_type_id, x_api_key, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->get_opportunity_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **opportunity_type_id** | **int**| The identifier for the Opportunity type. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**OpportunityType**](OpportunityType.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_campaign_channels**
> CampaignChannelCollection list_campaign_channels(authorization, x_api_key, accept=accept, filter=filter)

Returns a list of campaign channel for a given tenant.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Optional. The list can be filtered using one or more of the following supported fields and operators:                * `isArchived` (`eq`)                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). (optional)

try:
    # Returns a list of campaign channel for a given tenant.
    api_response = api_instance.list_campaign_channels(authorization, x_api_key, accept=accept, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->list_campaign_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Optional. The list can be filtered using one or more of the following supported fields and operators:                * &#x60;isArchived&#x60; (&#x60;eq&#x60;)                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). | [optional] 

### Return type

[**CampaignChannelCollection**](CampaignChannelCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_campaign_types**
> CampaignTypeCollection list_campaign_types(authorization, x_api_key, accept=accept, filter=filter)

Returns a list of campaign types for a given tenant.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Optional. The list can be filtered using one or more of the following supported fields and operators:                * `isArchived` (`eq`)                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). (optional)

try:
    # Returns a list of campaign types for a given tenant.
    api_response = api_instance.list_campaign_types(authorization, x_api_key, accept=accept, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->list_campaign_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Optional. The list can be filtered using one or more of the following supported fields and operators:                * &#x60;isArchived&#x60; (&#x60;eq&#x60;)                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). | [optional] 

### Return type

[**CampaignTypeCollection**](CampaignTypeCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_opportunities**
> OpportunityCollection list_client_opportunities(authorization, client_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns list of opportunities for a given client. 

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
client_id = 56 # int | Client identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | The list of client opportunities returned can be filtered using one or more of the supported fields and operators.  The supported fields and operators are:    * `isClosed (`eq`)                Example filters:      filter= isClosed eq true        For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). (optional)
orderby = 'orderby_example' # str | The list of client opportunities returned can be sorted on the following fields:    * `createdOn` (`asc` or `desc`)  * `id` (`asc` or `desc`)  * `isClosed` (`asc` or `desc`)  * `opportunityType.Name` (`asc` or `desc`)  * `reference` (`asc` or `desc`)  * `status.Name` (`asc` or `desc`)        Example orderBy:      orderBy=opportunityType.Name desc        By default the list of client opportunities are ordered by Id in ascending order. (optional)
skip = 0 # int | Optional. The number of records to skip. If not specified it defaults to 0. (optional) (default to 0)
top = 100 # int | Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. (optional) (default to 100)

try:
    # Returns list of opportunities for a given client. 
    api_response = api_instance.list_client_opportunities(authorization, client_id, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->list_client_opportunities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **client_id** | **int**| Client identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| The list of client opportunities returned can be filtered using one or more of the supported fields and operators.  The supported fields and operators are:    * &#x60;isClosed (&#x60;eq&#x60;)                Example filters:      filter&#x3D; isClosed eq true        For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). | [optional] 
 **orderby** | **str**| The list of client opportunities returned can be sorted on the following fields:    * &#x60;createdOn&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;id&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;isClosed&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;opportunityType.Name&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;reference&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;status.Name&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)        Example orderBy:      orderBy&#x3D;opportunityType.Name desc        By default the list of client opportunities are ordered by Id in ascending order. | [optional] 
 **skip** | **int**| Optional. The number of records to skip. If not specified it defaults to 0. | [optional] [default to 0]
 **top** | **int**| Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. | [optional] [default to 100]

### Return type

[**OpportunityCollection**](OpportunityCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lead_opportunities**
> OpportunityCollection list_lead_opportunities(authorization, lead_id, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, top=top)

Returns a list of opportunity documents for a given lead. 

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
lead_id = 56 # int | Lead identifier.
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | The list of Lead opportunities returned can be filtered using one or more of the supported fields and operators.  The supported fields and operators are:    * `isClosed (`eq`)                        For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). (optional)
order_by = 'order_by_example' # str |  (optional)
skip = 0 # int | Optional. The number of records to skip. If not specified it defaults to 0. (optional) (default to 0)
top = 100 # int | Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. (optional) (default to 100)

try:
    # Returns a list of opportunity documents for a given lead. 
    api_response = api_instance.list_lead_opportunities(authorization, lead_id, x_api_key, accept=accept, filter=filter, order_by=order_by, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->list_lead_opportunities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **lead_id** | **int**| Lead identifier. | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| The list of Lead opportunities returned can be filtered using one or more of the supported fields and operators.  The supported fields and operators are:    * &#x60;isClosed (&#x60;eq&#x60;)                        For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). | [optional] 
 **order_by** | **str**|  | [optional] 
 **skip** | **int**| Optional. The number of records to skip. If not specified it defaults to 0. | [optional] [default to 0]
 **top** | **int**| Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. | [optional] [default to 100]

### Return type

[**OpportunityCollection**](OpportunityCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_opportunity_campaigns**
> OpportunityCampaignCollection list_opportunity_campaigns(authorization, x_api_key, accept=accept, filter=filter)

Returns a list of the Opportunity campaigns for a tenant.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported filters options:               * `isArchived (eq)`               * `isOrganisational (eq)`                             See [QueryLang](docs/ApiQueryLang) for further details of how to use the filtering and sorting parameters. (optional)

try:
    # Returns a list of the Opportunity campaigns for a tenant.
    api_response = api_instance.list_opportunity_campaigns(authorization, x_api_key, accept=accept, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->list_opportunity_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported filters options:               * &#x60;isArchived (eq)&#x60;               * &#x60;isOrganisational (eq)&#x60;                             See [QueryLang](docs/ApiQueryLang) for further details of how to use the filtering and sorting parameters. | [optional] 

### Return type

[**OpportunityCampaignCollection**](OpportunityCampaignCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_opportunity_propositions**
> OpportunityPropositionCollection list_opportunity_propositions(authorization, x_api_key, accept=accept, filter=filter)

Returns a list of the opportunity propositions for a tenant.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported Filters:  * `isArchived` (`eq`) (optional)

try:
    # Returns a list of the opportunity propositions for a tenant.
    api_response = api_instance.list_opportunity_propositions(authorization, x_api_key, accept=accept, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->list_opportunity_propositions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported Filters:  * &#x60;isArchived&#x60; (&#x60;eq&#x60;) | [optional] 

### Return type

[**OpportunityPropositionCollection**](OpportunityPropositionCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_opportunity_statuses**
> OpportunityStatusCollection list_opportunity_statuses(authorization, x_api_key, accept=accept, filter=filter, tenant_id=tenant_id)

Returns a list of opportunity statuses for a given tenant

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported Filters:  * `isArchived` (`eq`) (optional)
tenant_id = 56 # int | Tenant identifier (optional)

try:
    # Returns a list of opportunity statuses for a given tenant
    api_response = api_instance.list_opportunity_statuses(authorization, x_api_key, accept=accept, filter=filter, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->list_opportunity_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported Filters:  * &#x60;isArchived&#x60; (&#x60;eq&#x60;) | [optional] 
 **tenant_id** | **int**| Tenant identifier | [optional] 

### Return type

[**OpportunityStatusCollection**](OpportunityStatusCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_opportunity_types**
> OpportunityTypeCollection list_opportunity_types(authorization, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)

Returns a list of the opportunity types for a tenant.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
accept = 'accept_example' # str |  (optional)
filter = 'filter_example' # str | Supported filters options:  * `isArchived (eq)`  * `objectiveType (eq, in)`                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). (optional)
orderby = 'orderby_example' # str | The list of Opportunity types returned can be sorted on the following fields:    * `id` (`asc` or `desc`)  * `name` (`asc` or `desc`)  * `objectiveType` (`asc` or `desc`)  * `isArchived` (`asc` or `desc`)                By default the list of Opportunity types are ordered by Id in ascending order. (optional)
skip = 0 # int | Optional. The number of records to skip. If not specified it defaults to 0. (optional) (default to 0)
top = 100 # int | Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. (optional) (default to 100)

try:
    # Returns a list of the opportunity types for a tenant.
    api_response = api_instance.list_opportunity_types(authorization, x_api_key, accept=accept, filter=filter, orderby=orderby, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->list_opportunity_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **filter** | **str**| Supported filters options:  * &#x60;isArchived (eq)&#x60;  * &#x60;objectiveType (eq, in)&#x60;                For further details of how to use the filter parameter see [QueryLang](docs/ApiQueryLang). | [optional] 
 **orderby** | **str**| The list of Opportunity types returned can be sorted on the following fields:    * &#x60;id&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;name&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;objectiveType&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)  * &#x60;isArchived&#x60; (&#x60;asc&#x60; or &#x60;desc&#x60;)                By default the list of Opportunity types are ordered by Id in ascending order. | [optional] 
 **skip** | **int**| Optional. The number of records to skip. If not specified it defaults to 0. | [optional] [default to 0]
 **top** | **int**| Optional. The number of records to retrieve (the maximum is 500). If not specified it defaults to 100. | [optional] [default to 100]

### Return type

[**OpportunityTypeCollection**](OpportunityTypeCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_channel**
> CampaignChannel update_campaign_channel(body, authorization, x_api_key, campaign_channel_id, accept=accept, tenant_id=tenant_id)

Updates an existing Campaign Channel.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CampaignChannel() # CampaignChannel | Campaign Channel document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
campaign_channel_id = 56 # int | Campaign Channel identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Updates an existing Campaign Channel.
    api_response = api_instance.update_campaign_channel(body, authorization, x_api_key, campaign_channel_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->update_campaign_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CampaignChannel**](CampaignChannel.md)| Campaign Channel document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **campaign_channel_id** | **int**| Campaign Channel identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**CampaignChannel**](CampaignChannel.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_type**
> CampaignType update_campaign_type(body, authorization, x_api_key, campaign_type_id, accept=accept, tenant_id=tenant_id)

Updates an existing Campaign Type.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CampaignType() # CampaignType | Campaign Type document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
campaign_type_id = 56 # int | Campaign Type identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Updates an existing Campaign Type.
    api_response = api_instance.update_campaign_type(body, authorization, x_api_key, campaign_type_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->update_campaign_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CampaignType**](CampaignType.md)| Campaign Type document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **campaign_type_id** | **int**| Campaign Type identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**CampaignType**](CampaignType.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_opportunity**
> Opportunity update_client_opportunity(body, authorization, x_api_key, client_id, opportunity_id, accept=accept, tenant_id=tenant_id)

Updates an existing Opportunity for the given client.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Opportunity() # Opportunity | Opportunity document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
client_id = 56 # int | Client identifier
opportunity_id = 56 # int | Opportunity identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Updates an existing Opportunity for the given client.
    api_response = api_instance.update_client_opportunity(body, authorization, x_api_key, client_id, opportunity_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->update_client_opportunity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Opportunity**](Opportunity.md)| Opportunity document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **client_id** | **int**| Client identifier | 
 **opportunity_id** | **int**| Opportunity identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**Opportunity**](Opportunity.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lead_opporunity**
> Opportunity update_lead_opporunity(body, authorization, x_api_key, lead_id, opportunity_id, accept=accept, tenant_id=tenant_id)

Updates an existing Opportunity for the given Lead.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Opportunity() # Opportunity | Opportunity document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
lead_id = 56 # int | Lead identifier
opportunity_id = 56 # int | Opportunity identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Updates an existing Opportunity for the given Lead.
    api_response = api_instance.update_lead_opporunity(body, authorization, x_api_key, lead_id, opportunity_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->update_lead_opporunity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Opportunity**](Opportunity.md)| Opportunity document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **lead_id** | **int**| Lead identifier | 
 **opportunity_id** | **int**| Opportunity identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**Opportunity**](Opportunity.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_opportunity_campaign**
> OpportunityCampaign update_opportunity_campaign(body, authorization, x_api_key, opportunity_campaign_id, accept=accept)

Updates an Opportunity campaign for a tenant.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.OpportunityCampaign() # OpportunityCampaign | The details to update the Opportunity campaign.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
opportunity_campaign_id = 56 # int | The identifier for the Opportunity campaign.
accept = 'accept_example' # str |  (optional)

try:
    # Updates an Opportunity campaign for a tenant.
    api_response = api_instance.update_opportunity_campaign(body, authorization, x_api_key, opportunity_campaign_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->update_opportunity_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpportunityCampaign**](OpportunityCampaign.md)| The details to update the Opportunity campaign. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **opportunity_campaign_id** | **int**| The identifier for the Opportunity campaign. | 
 **accept** | **str**|  | [optional] 

### Return type

[**OpportunityCampaign**](OpportunityCampaign.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_opportunity_proposition**
> OpportunityProposition update_opportunity_proposition(body, authorization, x_api_key, proposition_id, accept=accept)

Updates an existing Opportunity proposition for a tenant.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.OpportunityProposition() # OpportunityProposition | Opportunity proposition document.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
proposition_id = 56 # int | Opportunity proposition identifier.
accept = 'accept_example' # str |  (optional)

try:
    # Updates an existing Opportunity proposition for a tenant.
    api_response = api_instance.update_opportunity_proposition(body, authorization, x_api_key, proposition_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->update_opportunity_proposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpportunityProposition**](OpportunityProposition.md)| Opportunity proposition document. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **proposition_id** | **int**| Opportunity proposition identifier. | 
 **accept** | **str**|  | [optional] 

### Return type

[**OpportunityProposition**](OpportunityProposition.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_opportunity_status**
> OpportunityStatus update_opportunity_status(body, authorization, x_api_key, opportunity_status_id, accept=accept, tenant_id=tenant_id)

Updates an existing Opportunity Status.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.OpportunityStatus() # OpportunityStatus | Opportunity Status document
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
opportunity_status_id = 56 # int | Opportunity Status identifier
accept = 'accept_example' # str |  (optional)
tenant_id = 56 # int | Tenant Identifier, used to filter by tenant. Only use under system reach (optional)

try:
    # Updates an existing Opportunity Status.
    api_response = api_instance.update_opportunity_status(body, authorization, x_api_key, opportunity_status_id, accept=accept, tenant_id=tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->update_opportunity_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpportunityStatus**](OpportunityStatus.md)| Opportunity Status document | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **opportunity_status_id** | **int**| Opportunity Status identifier | 
 **accept** | **str**|  | [optional] 
 **tenant_id** | **int**| Tenant Identifier, used to filter by tenant. Only use under system reach | [optional] 

### Return type

[**OpportunityStatus**](OpportunityStatus.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_opportunity_type**
> OpportunityType update_opportunity_type(body, authorization, x_api_key, opportunity_type_id, accept=accept)

Updates an Opportunity Type for a tenant.

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
api_instance = swagger_client.OpportunitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.OpportunityType() # OpportunityType | The details to update the opportunity type.
authorization = 'authorization_example' # str | 
x_api_key = 'x_api_key_example' # str | 
opportunity_type_id = 56 # int | The identifier for the Opportunity type.
accept = 'accept_example' # str |  (optional)

try:
    # Updates an Opportunity Type for a tenant.
    api_response = api_instance.update_opportunity_type(body, authorization, x_api_key, opportunity_type_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpportunitiesApi->update_opportunity_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpportunityType**](OpportunityType.md)| The details to update the opportunity type. | 
 **authorization** | **str**|  | 
 **x_api_key** | **str**|  | 
 **opportunity_type_id** | **int**| The identifier for the Opportunity type. | 
 **accept** | **str**|  | [optional] 

### Return type

[**OpportunityType**](OpportunityType.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

