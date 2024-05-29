# Document

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**title** | **str** | Editable on POST, PUT | [optional] 
**description** | **str** | Editable on POST, PUT | [optional] 
**created_at** | **datetime** |  | [optional] 
**properties** | **dict(str, str)** | Editable on POST, PUT.  Limited to 10 items. Excluding reserved properties. | [optional] 
**linked_entities** | [**list[DocumentLinkedEntityRef]**](DocumentLinkedEntityRef.md) | Editable on POST, PUT  Limited to 2 linked entities (one of the items must be a service case if linked entities more than 1). | [optional] 
**object** | [**ObjectRef**](ObjectRef.md) |  | [optional] 
**owners_href** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**is_private** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

