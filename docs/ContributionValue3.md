# ContributionValue3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**starts_on** | **datetime** | Date when the contribution started. | 
**stops_on** | **datetime** | Date when the contribution ended. | [optional] 
**value** | [**CurrencyValue**](CurrencyValue.md) |  | 
**frequency** | **str** | Frequency type. Defaults to Single when the type of withdrawal is not set to Regular and frequency is set to None. | [default to 'Single']
**type** | **str** | Contribution type. | 
**contributor_type** | **str** | Contributor type. If not set will default to Self. | [optional] [default to 'Self']
**escalation** | [**EscalationValue**](EscalationValue.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

