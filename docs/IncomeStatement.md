# IncomeStatement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Income statement identifier. | [optional] 
**href** | **str** | Income statement reference. | [optional] 
**reference** | **str** | Income statement reference. EDI Number | [optional] 
**statement_date** | **datetime** | The statement date. | 
**is_matched** | **bool** | Indicates that the statement amount equals the sum of the statement item amounts. | [optional] 
**amount** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**provider** | [**MatchProviderRef**](MatchProviderRef.md) |  | 
**group** | [**GroupRef**](GroupRef.md) |  | 
**created_at** | **datetime** | UTC datetime for when the statement was created. | [optional] 
**created_app** | [**NamedAppRef**](NamedAppRef.md) |  | [optional] 
**created_by** | [**NamedUserRef**](NamedUserRef.md) |  | [optional] 
**requires_approval** | **bool** | Indicates if the statement will go into an import queue and needs explicit approval before being processed, defaults to false. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

