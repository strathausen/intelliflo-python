# HubBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hub_mode** | **str** | The literal string subscribe or unsubscribe, depending on the goal of the request. | 
**hub_topic** | **str** | The topic URL that the subscriber wishes to subscribe to or unsubscribe from. | 
**hub_callback** | **str** | The callback url where content distribution notifications should be delivered. | 
**hub_lease_seconds** | **int** | Number of seconds to have the subscription active, given as a positive decimal integer. | [optional] 
**hub_secret** | **str** | A cryptographically random unique secret string that will be used to compute an HMAC digest for authorized content distribution. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

