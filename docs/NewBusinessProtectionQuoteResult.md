# NewBusinessProtectionQuoteResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**premiums** | [**list[ContributionValue3]**](ContributionValue3.md) | Premiums for the protection quote result. | [optional] 
**life_cover** | [**LifeCoverValue**](LifeCoverValue.md) |  | [optional] 
**critical_illness_cover** | [**InsuranceCoverValue**](InsuranceCoverValue.md) |  | [optional] 
**income_cover** | [**InsuranceCoverValue**](InsuranceCoverValue.md) |  | [optional] 
**expense_cover** | [**InsuranceCoverValue**](InsuranceCoverValue.md) |  | [optional] 
**severity_cover** | [**SeverityCoverValue**](SeverityCoverValue.md) |  | [optional] 
**benefits_payable** | [**BenefitsPayableValue**](BenefitsPayableValue.md) |  | [optional] 
**index_type** | **str** | Defines how the amount of cover will change over time and, if it does, what governs that change. | [optional] 
**in_trust** | **bool** | In trust flag. | [optional] [default to False]
**in_trust_to_whom** | **str** | Name of the trust beneficiary. | [optional] 
**benefit_options** | **list[str]** | List of applicable benefits against which payments will be made. | [optional] 
**is_rated** | **bool** | A “rated” life insurance policy is a policy that is also often referred to as a “substandard” policy.  A person with less than average health or who has a high-risk occupation may receive a rated or substandard policy. | [optional] 
**is_premium_waiver_woc** | **bool** | Has the insured taken out premium waiver/Waiver of Contribution insurance to protect their contributions should they not be able to work as a result of accident or sickness? | [optional] 
**benefit_summary** | **str** | A textual summary of the Benefits associated with this policy. | [optional] 
**exclusion_notes** | **str** | A textual summary of any applicable exclusions. | [optional] 
**initial_earnings_period** | **str** | Period within which the Provider can seek to clawback commissions if premium payments reduce, vary, stop or are suspended. Should be specified in iso8601 format (\&quot;P[n]D\&quot;). | [optional] 
**waiting_period** | **str** | Waiting period is the time you must wait from when you become unable to work due to illness or injury to the time you become eligible to start receiving payments.  Duration in iso8601 format (\&quot;P[n]D\&quot;). | [optional] 
**premium_loading** | **str** | The premiums loading associated with the disclosure of increased risk. | [optional] 
**owner2_percent_of_sum_assured** | **float** | The percentage of the Sum Assured which is allocated to the policy co-owner. | [optional] 
**sum_assured** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**commissions** | [**list[CommissionValue]**](CommissionValue.md) | Commission Value. | [optional] 
**provider** | [**ProductProviderRef**](ProductProviderRef.md) |  | [optional] 
**plan_type** | [**PlanTypeReference**](PlanTypeReference.md) |  | [optional] 
**protection_payout_type** | **str** | Income Protection Definition. | [optional] [default to 'Indemnity']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

