# ActivityOutcomeDocument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the activity outcome. | [optional] 
**href** | **str** | The hypertext reference to the activity outcome. | [optional] 
**name** | **str** | The name of the activity outcome. | 
**activity_type** | [**NamedActivityTypeReference**](NamedActivityTypeReference.md) |  | [optional] 
**group** | [**NamedGroupReference**](NamedGroupReference.md) |  | [optional] 
**is_deletable** | **bool** | Flag indicating if the activity outcome can be deleted or not. if activity outcome is used in any of the tasks or appointments then we cannot delete the activity outcome. | [optional] [default to False]
**is_archived** | **bool** | Flag indicating if the activity outcome is archived or not. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

