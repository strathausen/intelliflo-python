# PlanValuation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Valuation unique identifier. | [optional] 
**href** | **str** | Valuation hypermedia link. | [optional] 
**value** | [**CurrencyValue**](CurrencyValue.md) |  | 
**valued_on** | **datetime** | Valuation date. | [optional] 
**created_at** | **datetime** | Date and time the valuation was created. | [optional] 
**surrender_transfer_value** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**type** | **str** | Plan valuation type.  Editable on POST. Only &#x60;Manual&#x60; and &#x60;UnderlyingFundValues&#x60; values are allowed upon creation.  If nothing is specified, &#x60;Manual&#x60; will be used. | [optional] [default to 'Manual']
**plan** | [**PlanPolicyRef**](PlanPolicyRef.md) |  | [optional] 
**updated_by** | [**UserRef2**](UserRef2.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

