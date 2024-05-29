# Asset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique asset resource identifier | [optional] 
**href** | **str** |  | [optional] 
**description** | **str** | Description of the asset | 
**plan** | [**PlanIdRef**](PlanIdRef.md) |  | [optional] 
**asset_type** | **str** | Type (or category) of asset | 
**is_visible_to_client** | **bool** | Information visible to client | [optional] 
**is_loan_amount** | **bool** | If it is a loan amount | [optional] 
**is_investment_property** | **bool** | If it is investment property | [optional] 
**original_value** | [**AssetValuationRef**](AssetValuationRef.md) |  | [optional] 
**current_value** | [**AssetValuationRef**](AssetValuationRef.md) |  | [optional] 
**owner** | **str** | Current selected Owner | [optional] [default to 'null']
**owners** | [**list[ClientOwnershipRef]**](ClientOwnershipRef.md) | Asset Owners | [optional] 
**address** | [**AddressValue2**](AddressValue2.md) |  | [optional] 
**purchased_on** | **datetime** | Purchase date | [optional] 
**valued_on** | **datetime** | Valued on date | [optional] 
**purchase_price** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**income** | [**IncomeIdRef**](IncomeIdRef.md) |  | [optional] 
**is_holding** | **bool** | If it is holding | [optional] 
**currency** | **str** | Asset&#x27;s currency. | [optional] 
**exchange_rate** | [**CurrencyRef**](CurrencyRef.md) |  | [optional] 
**created_by_user** | [**UserRef2**](UserRef2.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

