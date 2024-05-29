# UnmatchedPlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The UnMatched Plan Identifier. | [optional] 
**href** | **str** | The Plan Reference. | [optional] 
**plan_type** | [**PlanTypeShortReference**](PlanTypeShortReference.md) |  | 
**owners** | [**list[NamedOwnerRef]**](NamedOwnerRef.md) | Each plan can have one or more owners. The Client could be purchasing the product on behalf of someone else. | [optional] 
**address** | [**AddressValueRef**](AddressValueRef.md) |  | [optional] 
**policy_number** | **str** | Unique reference number to the Client&#x27;s Plan as issued by the Platform Provider. | [optional] [default to 'null']
**product_name** | **str** | Optional name which would usually be the market name of the product. | [optional] [default to 'null']
**selling_adviser** | [**NamedAdviserRef**](NamedAdviserRef.md) |  | 
**product_provider** | [**NamedProductProviderRef**](NamedProductProviderRef.md) |  | 
**provider_codes** | [**ProviderCodesValue**](ProviderCodesValue.md) |  | [optional] 
**group** | [**GroupRef**](GroupRef.md) |  | [optional] 
**created_at** | **datetime** | Created Date. | [optional] 
**changed_at** | **datetime** | Last Updated Date. | [optional] 
**sort_code** | **str** | Sort code/routing number/branch code are domestic bank codes used to route money transfers between financial institutions. | [optional] [default to 'null']
**program_id** | **int** | The program identifier. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

