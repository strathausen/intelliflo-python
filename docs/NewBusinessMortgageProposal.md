# NewBusinessMortgageProposal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_monthly_cost** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**true_cost** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**repayment_method** | **str** | Repayment method type. | [optional] 
**proc_fee** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**value** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**interest** | [**InterestSchemeValue**](InterestSchemeValue.md) |  | [optional] 
**term** | [**MortgageTermValue**](MortgageTermValue.md) |  | [optional] 
**feature_expiry_date** | **datetime** | Scheme expiry date (e.g. fixed term end date). | [optional] 
**property_valuation** | [**MortgagedPropertyValuationValue2**](MortgagedPropertyValuationValue2.md) |  | [optional] 
**deposit** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**mortgage_number** | **str** | A Provider assigned reference for the purposes of tracking a Mortgage Application until such time as that Application is approved or rejected. | [optional] 
**loan_to_value** | **float** | Loan to value percentage.  Calculated as: (loanAmount / propertyValuation.value) * 100. | [optional] 
**redemption_penalty** | [**MortgageRedemptionValue3**](MortgageRedemptionValue3.md) |  | [optional] 
**is_portable** | **bool** | Is the mortgage portable? | [optional] 
**is_first_time_buyer** | **bool** | Is client a first-time buyer? | [optional] 
**is_consolidated_debt** | **bool** | Is mortgage equity to be used to consolidate debt? | [optional] 
**_property** | [**PropertyValue2**](PropertyValue2.md) |  | [optional] 
**additional_owners** | [**list[NamedClientReference]**](NamedClientReference.md) | Additional owners (Maximum 2). | [optional] 
**property_type** | **str** | Property type. | [optional] 
**capital_repayment** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**rate_period_from_completion_months** | **int** | Number of months remaining before the current rate period ends. | [optional] 
**interest_only_repayment** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**interest_only_repayment_vehicle** | **str** | Interest only repayment vehicle. | [optional] 
**has_guarantor** | **bool** | Is there a mortgage guarantor? | [optional] 
**rate_period_years** | **int** | Rate period (in years). | [optional] 
**reversionary_rate** | **float** | Standard Variable Rate. | [optional] 
**property_address** | [**PropertyAddressRef**](PropertyAddressRef.md) |  | [optional] 
**total_fees** | [**list[LenderFeeValue2]**](LenderFeeValue2.md) | Collection of lender specific fees. | [optional] 
**shared_equity** | [**SharedEquityValue**](SharedEquityValue.md) |  | [optional] 
**new_business_plan** | [**NewBusinessPlanValue**](NewBusinessPlanValue.md) |  | [optional] 
**currency** | **str** | ISO 4217 Currency code for the proposal. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

