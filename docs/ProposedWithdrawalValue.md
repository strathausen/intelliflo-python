# ProposedWithdrawalValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**starts_on** | **datetime** | Date when the withdrawal started. | [optional] 
**stops_on** | **datetime** | Date when the withdrawal ended. | [optional] 
**value** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**previous_value** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**frequency** | **str** | Frequency type. When withdrawal is not of type Regular with frequency type None, then default value will be used instead. | [default to 'Single']
**type** | **str** | Withdrawal type for the withdrawal. | 
**is_full_withdrawal** | **bool** | Determines whether withdrawal is full or partial. | [optional] 
**percentage** | **float** | Percentage of withdrawal. Should be between 0 to 100. | [optional] [default to 0.0]
**previous_percentage** | **float** | Previous percentage of withdrawal. | [optional] 
**withdrawal_reference** | [**WithdrawalReference**](WithdrawalReference.md) |  | [optional] 
**is_stop_existing_withdrawal** | **bool** | Determines whether current regular withdrawal/income should be stopped. | [optional] 
**escalation** | [**EscalationValue**](EscalationValue.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

