# NewBusinessPlanValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_name** | **str** | Product name for the new business plan. | [optional] 
**external_reference** | **str** | External reference for the new business plan | [optional] 
**bundle_reference** | **str** | Reference for the Recommendation proposal created from a bundled group. | [optional] 
**provider** | [**ProductProviderRef2**](ProductProviderRef2.md) |  | 
**plan_type** | [**PlanTypeReference**](PlanTypeReference.md) |  | 
**selling_adviser** | [**AdviserRef**](AdviserRef.md) |  | 
**life_cycle** | [**NamedLifecycleRef**](NamedLifecycleRef.md) |  | 
**is_advice_off_panel** | **bool** | Is the Adviser recommending a product which is outside of their regulated sphere?  This would be considered \&quot;Off-panel\&quot; advice. Only assignable on POST. | [optional] [default to False]
**commission_rate** | **str** | Commission rate for top up plan. | [optional] 
**split_template** | [**SplitTemplateValue**](SplitTemplateValue.md) |  | [optional] 
**fees** | [**list[FeeRef]**](FeeRef.md) | List of fees for the Top up plan. | [optional] 
**wrap** | [**WrapPlanValue**](WrapPlanValue.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

