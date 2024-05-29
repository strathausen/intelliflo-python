# NewBusinessGeneralInsuranceProposal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**premiums** | [**list[ProposedContributionValue]**](ProposedContributionValue.md) | Contributions for the new business plan. | [optional] 
**in_trust** | **bool** | In trust flag. | [optional] 
**in_trust_to_whom** | **str** | Name of the trust beneficiary. | [optional] 
**premium_loading** | **str** | The premiums loading associated with the disclosure of increased risk. | [optional] 
**exclusions_notes** | **str** | Summary of any applicable exclusions. | [optional] 
**term** | **str** | Policy duration in years (ISO-8601: P[n][Y]) | [optional] 
**cover_type** | **str** | Insurance cover type. | [optional] 
**cover_options** | **list[str]** | List of cover options. | [optional] 
**cover_area** | **str** | Geographic area over which the policy is valid. | [optional] 
**is_cover_note_issued** | **bool** | Policy cover notes issued flag. | [optional] 
**excess** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**sum_insured** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**buildings** | [**BuildingContentsInsuranceValue**](BuildingContentsInsuranceValue.md) |  | [optional] 
**contents** | [**BuildingContentsInsuranceValue**](BuildingContentsInsuranceValue.md) |  | [optional] 
**new_business_plan** | [**NewBusinessPlanValue**](NewBusinessPlanValue.md) |  | [optional] 
**currency** | **str** | ISO 4217 Currency code for the proposal. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

