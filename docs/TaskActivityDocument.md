# TaskActivityDocument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the task. | [optional] 
**href** | **str** | The hypertext reference to the task. | [optional] 
**subject** | **str** | The subject of the task. | [optional] 
**description** | **str** | The description of the task. | [optional] 
**activity_type** | [**NamedActivityCategoryTypeReference**](NamedActivityCategoryTypeReference.md) |  | 
**priority** | [**NamedActivityPriorityReference**](NamedActivityPriorityReference.md) |  | [optional] 
**status** | **str** | The current status of the task. Valid values are: &#x27;NotStarted&#x27;, &#x27;WorkInProgress&#x27;, &#x27;Incomplete&#x27;, &#x27;Complete&#x27;, &#x27;WaitingForResponse&#x27; | [optional] 
**shown_in_diary** | **bool** | Flag indicating if the task should be displayed in user diary. | [optional] [default to False]
**shown_in_portal** | **bool** | Flag indicating if the task  should be displayed in portal. | [optional] [default to False]
**reference** | **str** | A reference of the task. | [optional] 
**completion** | [**TaskActivityCompletion**](TaskActivityCompletion.md) |  | [optional] 
**related_to** | [**list[ActivityRelatedEntity]**](ActivityRelatedEntity.md) | The list of entities the task is related to. | [optional] 
**linked_entity** | [**ActivityLinkedEntity**](ActivityLinkedEntity.md) |  | [optional] 
**assigned_by** | [**NamedUserReference**](NamedUserReference.md) |  | [optional] 
**assigned_to** | [**TaskAssignment**](TaskAssignment.md) |  | [optional] 
**starts_at** | **datetime** | The date the task is scheduled to start. | [optional] 
**due_at** | **datetime** | The date the task is due to be completed. | 
**duration** | [**TaskDurationValue**](TaskDurationValue.md) |  | [optional] 
**billing** | [**TaskBillingValue**](TaskBillingValue.md) |  | [optional] 
**cost** | [**TaskCostValue**](TaskCostValue.md) |  | [optional] 
**recurrence** | [**ActivityRecurrenceValue**](ActivityRecurrenceValue.md) |  | [optional] 
**created_by_app** | [**NamedAppReference**](NamedAppReference.md) |  | [optional] 
**created_by_user** | [**NamedUserReference**](NamedUserReference.md) |  | [optional] 
**created_at** | **datetime** | The date the task was created. | [optional] 
**updated_by_app** | [**NamedAppReference**](NamedAppReference.md) |  | [optional] 
**updated_by_user** | [**NamedUserReference**](NamedUserReference.md) |  | [optional] 
**updated_at** | **datetime** | The date the task was last updated. | [optional] 
**properties** | [**list[ModelProperty]**](ModelProperty.md) | Properties | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

