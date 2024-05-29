# ProposedContributionValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**starts_on** | **datetime** | Date when the contribution started. | 
**stops_on** | **datetime** | Date when the contribution ended. | [optional] 
**value** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**previous_value** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**frequency** | **str** | Frequency type. When contribution is not of type Regular with frequency type None, then default value will be used instead. | [default to 'Single']
**type** | **str** | Contribution type for the contribution. | 
**transfer_type** | **str** | Transfer type applicable for the Contribution of type transfer. | [optional] 
**is_full_transfer** | **bool** | Determines whether transfer is full or partial. | [optional] 
**tax_basis** | **str** | Tax Basis on proposed contributions. | [optional] 
**contributor_type** | **str** | Contributor type for the contribution. Default will be Self if not supplied. | [optional] [default to 'Self']
**escalation** | [**EscalationValue**](EscalationValue.md) |  | [optional] 
**contribution_reference** | [**ContributionReference**](ContributionReference.md) |  | [optional] 
**is_stop_existing_contribution** | **bool** | Determines whether current regular contribution/premium should be stopped. | [optional] 
**transfer_from** | [**NamedPlanReference**](NamedPlanReference.md) |  | [optional] 
**include_in_initial_fees** | **bool** | Determines whether to include Initial Fees or Not. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

