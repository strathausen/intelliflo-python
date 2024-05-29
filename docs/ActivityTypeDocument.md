# ActivityTypeDocument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the activity type. | [optional] 
**href** | **str** | The hypertext reference to the activity type. | [optional] 
**name** | **str** | The name of the activity type. | 
**description** | **str** | The description of the activity type. | [optional] 
**activity_event_type** | **str** | The event type for the activity type. | [optional] 
**is_client_related** | **bool** | Flag indicating if the activity type is client related. | [optional] 
**is_plan_related** | **bool** | Flag indicating if the activity type is plan related. | [optional] 
**is_fee_related** | **bool** | Flag indicating if the activity type is fee related. | [optional] 
**is_retainer_related** | **bool** | Flag indicating if the activity type is retainer related. | [optional] 
**is_opportunity_related** | **bool** | Flag indicating if the activity type is opportunity related. | [optional] 
**is_adviser_related** | **bool** | Flag indicating if the activity type is advisor related. | [optional] 
**is_mandatory_outcome** | **bool** | Flag indicating if the activity outcome is mandatory. | [optional] [default to False]
**is_archived** | **bool** | Flag indicating if activity type is archived. | [optional] 
**is_deletable** | **bool** | Flag indicating if the activity type can be deleted or not. if activity type is used in any of the tasks or appointments then we cannot delete the activity type. | [optional] 
**is_hidden** | **bool** | Flag is indicating if the activity type is hidden for the user based on user group. | [optional] 
**category** | [**NamedActivityCategoryReference**](NamedActivityCategoryReference.md) |  | [optional] 
**group** | [**NamedGroupReference**](NamedGroupReference.md) |  | [optional] 
**include_subgroups** | **bool** | The flag indicating whether to provide access of activity type to sub groups or not. | [optional] 
**priority** | [**NamedPriorityReference**](NamedPriorityReference.md) |  | [optional] 
**task_billing_rate** | **float** | The task billing rate of the activity type. | [optional] 
**estimated_time** | [**ActivityEstimatedTime**](ActivityEstimatedTime.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

