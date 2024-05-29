# GroupProtectionPlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excess** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**sum_assured** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**until_age** | **int** | Income is protected until client reaches age (years). | [optional] 
**term** | **str** | Policy duration in years (format(ISO-8601): \&quot;P[n][Y]\&quot;). | [optional] [default to 'null']
**life_cover_sum_assured** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**owner2_percent_of_sum_assured** | **float** | The percentage of the Sum Assured which is allocated to the policy co-owner. | [optional] 
**critical_illness_term** | **str** | Critical Illness term in years (format(ISO-8601): \&quot;P[n][Y]\&quot;). | [optional] [default to 'null']
**critical_illness_sum_assured** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**benefit_options** | **list[str]** | List of applicable benefits against which payments will be made.  Valid options: ChildrensBenefit, Convertible, Renewable,  TerminalIllness, PaymentProtection. | [optional] 
**benefit_value** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**benefit_frequency** | **str** | How often Benefit payments are made. | [optional] [default to 'null']
**benefit_period** | [**BenefitPeriodValue**](BenefitPeriodValue.md) |  | [optional] 
**deferred_period** | **str** | The period between going off work and your income payments commencing (format(ISO-8601): \&quot;P[n][YMWD]\&quot;). | [optional] [default to 'null']
**qualification_period** | [**QualificationPeriodValue**](QualificationPeriodValue.md) |  | [optional] 
**split_benefit_frequency** | **str** | How often Split Benefit payments are made. | [optional] [default to 'null']
**split_benefit_value** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**split_deferred_period** | **str** | Split deferred period (format(ISO-8601): \&quot;P[n][YMWD]\&quot;). | [optional] [default to 'null']
**benefit_summary_notes** | **str** | Summary of the Benefits associated with this policy. | [optional] [default to 'null']
**additional_cover_amount** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**index_type** | **str** | Index type defines whether the amount of cover will change over time and, if it does, what governs that change. | [optional] [default to 'null']
**initial_earnings_period** | **str** | Initial earnings period in days (format(ISO-8601): \&quot;P[n]D\&quot;). | [optional] [default to 'null']
**waiting_period** | **str** | Waiting period in days (format(ISO-8601): \&quot;P[n]D\&quot;). | [optional] [default to 'null']
**life_cover_payment_basis** | **str** | Under what conditions Life Cover will be paid. | [optional] [default to 'null']
**review_on** | **datetime** | Next policy review date. | [optional] 
**is_rated** | **bool** | Indicates a person with less than average health or who has a high-risk occupation. | [optional] [default to False]
**is_premium_waiver_woc** | **bool** | Has the insured taken out premium waiver/Waiver of Contribution insurance to protect their contributions. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

