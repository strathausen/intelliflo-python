# Expenditure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**description** | **str** | Description of expenditure. | [optional] [default to 'null']
**category** | **str** | Type of expenditure. | 
**net** | [**CurrencyValue**](CurrencyValue.md) |  | 
**frequency** | **str** | Frequency of expenditure. | [optional] [default to 'Monthly']
**contribution_href** | **str** | Read only link to contribution. | [optional] 
**starts_on** | **datetime** | Start date of expenditure. | [optional] 
**ends_on** | **datetime** | End date of expenditure. | [optional] 
**owners** | [**list[ClientRef]**](ClientRef.md) | List Of Owners for expenditure. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

