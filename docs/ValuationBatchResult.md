# ValuationBatchResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**batch_href** | **str** |  | [optional] 
**policy_number** | **str** | Policy Number | [optional] 
**portal_reference** | **str** | Any shared additional reference | [optional] 
**matched_plan** | **bool** | True if a plan have been matched correctly. | [optional] 
**is_imported** | **bool** | True if the holdings for the plan have been imported. | [optional] 
**matched_plan_href** | **str** | Matched plan location | [optional] 
**holdings** | [**list[ValuationBatchHoldingValue]**](ValuationBatchHoldingValue.md) | Holdings grouped by policyNumber | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

