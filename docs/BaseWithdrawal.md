# BaseWithdrawal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Withdrawal identifier. | [optional] 
**href** | **str** | Withdrawal reference. | [optional] 
**plan** | [**PlanProviderRef**](PlanProviderRef.md) |  | [optional] 
**value** | [**CurrencyValue**](CurrencyValue.md) |  | 
**frequency** | **str** | Frequency type. | [default to 'Single']
**percentage** | **float** | Percentage value, used for percentage based types only as PercentageOfInvestment or PercentageOfFund. | [optional] 
**starts_on** | **datetime** | The date when the withdrawal started. | 
**stops_on** | **datetime** | The date when the withdrawal will stop. Needed for Regular withdrawal types only. | [optional] 
**note** | **str** | Represents additional details about this resource. | [optional] 
**escalation** | [**EscalationValue**](EscalationValue.md) |  | [optional] 
**contribution** | [**ContributionRef**](ContributionRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

