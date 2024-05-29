# BaseContribution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Contribution identifier. | [optional] 
**href** | **str** | Reference to the actual contribution. | [optional] 
**plan** | [**PlanProviderRef**](PlanProviderRef.md) |  | [optional] 
**value** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**frequency** | **str** | Frequency type. When contribution is not of type Regular with frequency type None, then default value will be used instead. | [default to 'Single']
**contributor_type** | **str** | Contributor type. | 
**starts_on** | **datetime** | The date when the contribution started. | 
**stops_on** | **datetime** | The date when the contribution will stop. Needed by contributions of type Regular. | [optional] 
**is_current** | **bool** | Defines if the contribution is current or not. | [optional] [default to False]
**note** | **str** | Represents additional details about this resource. | [optional] [default to 'null']
**escalation** | [**EscalationValue**](EscalationValue.md) |  | [optional] 
**withdrawal** | [**WithdrawalRef**](WithdrawalRef.md) |  | [optional] 
**percentage** | **float** | Contribution percentage. | [optional] 
**employment** | [**EmploymentRef**](EmploymentRef.md) |  | [optional] 
**applies_to** | **str** |  | [optional] [default to 'null']
**tax_basis** | **str** | Tax Basis on proposed contribution. | [optional] [default to 'null']
**transfer_type** | **str** | Transfer type applicable for the Contribution of type transfer. | [optional] [default to 'null']
**is_full_transfer** | **bool** | Determines whether transfer is full or partial. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

