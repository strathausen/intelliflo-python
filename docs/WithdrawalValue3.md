# WithdrawalValue3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**starts_on** | **datetime** | Date when the withdrawal started. | 
**stops_on** | **datetime** | Date when the withdrawal ended. | [optional] 
**value** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**frequency** | **str** | Frequency type. Defaults to Single when the type of withdrawal is not set to Regular and frequency is set to None. | [default to 'Single']
**type** | **str** | Withdrawal type. | 
**percentage** | **float** | Percentage of withdrawal. Should be between 0 to 100. | [optional] [default to 0.0]
**escalation** | [**EscalationValue**](EscalationValue.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

