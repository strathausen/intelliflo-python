# NewBusinessPersonalProtectionProposal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**premiums** | [**list[ProposedContributionValue]**](ProposedContributionValue.md) | Contributions for the new business plan. | [optional] 
**life_cover** | [**LifeCoverValue**](LifeCoverValue.md) |  | [optional] 
**critical_illness_cover** | [**InsuranceCoverValue**](InsuranceCoverValue.md) |  | [optional] 
**income_cover** | [**InsuranceCoverValue**](InsuranceCoverValue.md) |  | [optional] 
**expense_cover** | [**InsuranceCoverValue**](InsuranceCoverValue.md) |  | [optional] 
**severity_cover** | [**SeverityCoverValue**](SeverityCoverValue.md) |  | [optional] 
**benefits_payable** | [**BenefitsPayableValue**](BenefitsPayableValue.md) |  | [optional] 
**protection_payout_type** | **str** | Income protection definition | [optional] [default to 'Indemnity']
**in_trust** | **bool** | In trust flag. | [optional] 
**in_trust_to_whom** | **str** | Name of the trust beneficiary. | [optional] 
**premium_loading** | **str** | The premiums loading associated with the disclosure of increased risk. | [optional] 
**exclusions_notes** | **str** | Summary of any applicable exclusions. | [optional] 
**renewal_on** | **datetime** | Policy renewal date. | [optional] 
**owner2_percent_of_sum_assured** | **float** | The percentage of the Sum Assured which is allocated to the policy co-owner. | [optional] 
**benefit_options** | **list[str]** | Benefit Options | [optional] 
**benefit_summary_notes** | **str** | Summary of the Benefits associated with this policy. | [optional] 
**index_type** | **str** | Index type defines whether the amount of cover will change over time and, if it does, what governs that change. | [optional] 
**initial_earnings_period** | **str** | Initial earnings period in days(format(ISO-8601) : \&quot;P[n]D\&quot;). | [optional] 
**waiting_period** | **str** | Waiting period in days(format(ISO-8601) : \&quot;P[n]D\&quot;). | [optional] 
**is_rated** | **bool** | Indicates a person with less than average health or who has a high-risk occupation. | [optional] 
**is_premium_waiver_woc** | **bool** | Has the insured taken out premium waiver/Waiver of Contribution insurance to protect their contributions. | [optional] 
**has_original_investment_protection** | **bool** | Product has a guarantee / protection to protect original investment. | [optional] 
**sum_assured** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**premium_percentage_assigned_to_investment** | **float** | The Percentage of Premium assigned to Investment. | [optional] 
**commissions** | [**list[ProposedCommissionValue]**](ProposedCommissionValue.md) | Commission Value. | [optional] 
**new_business_plan** | [**NewBusinessPlanValue**](NewBusinessPlanValue.md) |  | [optional] 
**currency** | **str** | ISO 4217 Currency code for the proposal. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

