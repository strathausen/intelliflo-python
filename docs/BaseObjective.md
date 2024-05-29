# BaseObjective

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Requirement unique identifier. | [optional] 
**href** | **str** | Hypermedia link to the requirement. | [optional] 
**discriminator** | **str** | Requirements discriminator. | 
**category** | **str** | Category for the requirement. | 
**created_user** | [**ReadOnlyNamedUserRef**](ReadOnlyNamedUserRef.md) |  | [optional] 
**created_on** | **datetime** | Requirement created date. | [optional] 
**applicants** | [**list[NamedCustomerRef]**](NamedCustomerRef.md) | Owners of the requirement. The owner at index 0 is the primary owner. | [optional] 
**summary** | **str** | Summary of the requirement. | [optional] 
**details** | **str** | Additional notes or details of the requirement. | [optional] 
**status** | **str** | Status of the requirement. | [optional] 
**time_horizon** | **str** | Time horizon for the requirement | [optional] 
**linked_opportunities** | [**list[OpportunityRef]**](OpportunityRef.md) | Linked opportunities to the requirement. | [optional] 
**plans** | [**list[PlanRef2]**](PlanRef2.md) | Plan reference linked to the recommendation. | [optional] 
**last_reviewed_at** | **datetime** | Objective last reviewed timestamp. | [optional] 
**properties** | **dict(str, str)** | Editable on POST, PUT.  Limited to 25 items. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

