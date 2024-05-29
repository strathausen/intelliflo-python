# swagger_client.FundholdingtimeseriesApi

All URIs are relative to *https://api.gb.intelliflo.net/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fund_holding_time_series**](FundholdingtimeseriesApi.md#get_fund_holding_time_series) | **GET** /clients/{clientId}/plans/{planId}/holdings/{holdingId}/timeseries | Returns up to three years of fund holding time series for a given client and plan. 

# **get_fund_holding_time_series**
> FundHoldingTimeSeriesCollection get_fund_holding_time_series(client_id, plan_id, holding_id, earliest, accept=accept, authorization=authorization, latest=latest, tenant_id=tenant_id, x_api_key=x_api_key)

Returns up to three years of fund holding time series for a given client and plan. 

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
api_instance = swagger_client.FundholdingtimeseriesApi(swagger_client.ApiClient(configuration))
client_id = 56 # int | Client identifier
plan_id = 56 # int | Plan identifier
holding_id = 56 # int | Fund Holding identifier
earliest = 'earliest_example' # str | Earliest date of the period in yyyy-mm-dd format, can be up to three years in the past
accept = 'accept_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)
latest = 'latest_example' # str | Latest date of the period in yyyy-mm-dd format, if not provided defaults to today (optional)
tenant_id = 56 # int | Tenant identifier (optional)
x_api_key = 'x_api_key_example' # str |  (optional)

try:
    # Returns up to three years of fund holding time series for a given client and plan. 
    api_response = api_instance.get_fund_holding_time_series(client_id, plan_id, holding_id, earliest, accept=accept, authorization=authorization, latest=latest, tenant_id=tenant_id, x_api_key=x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundholdingtimeseriesApi->get_fund_holding_time_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**| Client identifier | 
 **plan_id** | **int**| Plan identifier | 
 **holding_id** | **int**| Fund Holding identifier | 
 **earliest** | **str**| Earliest date of the period in yyyy-mm-dd format, can be up to three years in the past | 
 **accept** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **latest** | **str**| Latest date of the period in yyyy-mm-dd format, if not provided defaults to today | [optional] 
 **tenant_id** | **int**| Tenant identifier | [optional] 
 **x_api_key** | **str**|  | [optional] 

### Return type

[**FundHoldingTimeSeriesCollection**](FundHoldingTimeSeriesCollection.md)

### Authorization

[apiKey](../README.md#apiKey), [oauth2-authorization-code](../README.md#oauth2-authorization-code), [oauth2-implicit](../README.md#oauth2-implicit), [oauth2-password](../README.md#oauth2-password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

