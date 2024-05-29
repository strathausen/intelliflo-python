# NewBusinessEquityReleaseProposal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_monthly_cost** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**proc_fee** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**equity_release_type** | **str** | Type of equity release product. | [optional] 
**ownership_sold** | **float** | Percentage of ownership sold. | [optional] 
**equity** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**property_valuation** | [**MortgagedPropertyValuationValue2**](MortgagedPropertyValuationValue2.md) |  | [optional] 
**lumpsum** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**repayment_method** | **str** | Repayment method type. | [optional] 
**monthly_income** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**loan_value** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**loan_to_value** | **float** | Loan to value percentage. Calculated as: (loanAmount / propertyvaluation.value) * 100. | [optional] 
**term** | [**MortgageTermValue**](MortgageTermValue.md) |  | [optional] 
**interest_only_repayment** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**capital_repayment** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**interest** | [**InterestSchemeValue**](InterestSchemeValue.md) |  | [optional] 
**redemption_penalty** | [**MortgageRedemptionValue3**](MortgageRedemptionValue3.md) |  | [optional] 
**property_address** | [**PropertyAddressRef**](PropertyAddressRef.md) |  | [optional] 
**additional_owners** | [**list[NamedClientReference]**](NamedClientReference.md) | Additional owners (Maximum 2). | [optional] 
**total_fees** | [**list[LenderFeeValue2]**](LenderFeeValue2.md) | Collection of lender specific fees. | [optional] 
**new_business_plan** | [**NewBusinessPlanValue**](NewBusinessPlanValue.md) |  | [optional] 
**currency** | **str** | ISO 4217 Currency code for the proposal. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

