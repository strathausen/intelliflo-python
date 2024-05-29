# IncomeStatementItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The Income statement item identifier. | [optional] 
**href** | **str** | The income statement item resource. | [optional] 
**income_statement** | [**IncomeStatementRef**](IncomeStatementRef.md) |  | [optional] 
**is_analysed** | **bool** | Indicates whether the item has been analysed. | [optional] 
**type** | **str** | The income type | 
**gross** | [**CurrencyValue**](CurrencyValue.md) |  | 
**net** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**plan** | [**MatchPlanRef**](MatchPlanRef.md) |  | [optional] 
**client** | [**MatchClientRef**](MatchClientRef.md) |  | 
**provider_agency_no** | **str** | The provider agency number. | [optional] 
**created_at** | **datetime** | UTC datetime for when the statement was created. | [optional] 
**created_app** | [**NamedAppRef**](NamedAppRef.md) |  | [optional] 
**created_by** | [**NamedUserRef**](NamedUserRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

