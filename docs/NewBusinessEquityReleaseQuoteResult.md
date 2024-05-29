# NewBusinessEquityReleaseQuoteResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requirement** | [**RequirementRef**](RequirementRef.md) |  | [optional] 
**initial_monthly_cost** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**proc_fee** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**equity_release_type** | **str** | Type of equity release product. | [optional] 
**ownership_sold** | **float** | Percentage of ownership sold. | [optional] 
**released** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**equity** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**valuation** | [**MortgagedPropertyValuationValue4**](MortgagedPropertyValuationValue4.md) |  | [optional] 
**lumpsum** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**repayment_method** | **str** | Repayment method type. | [optional] [default to 'null']
**monthly_income** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**asset** | [**AssetReference**](AssetReference.md) |  | [optional] 
**loan_value** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**loan_to_value** | **float** | Loan to value percentage. | [optional] 
**application_submitted_on** | **datetime** | Date application submitted. | [optional] 
**target_completion_date** | **datetime** | Target completion date. | [optional] 
**completion_date** | **datetime** | Completion date. | [optional] 
**exchange_date** | **datetime** | Exchange date. | [optional] 
**offer_made_on** | **datetime** | Offer issued date. | [optional] 
**review_on** | **datetime** | Review date. | [optional] 
**term** | [**MortgageTermValue**](MortgageTermValue.md) |  | [optional] 
**interest_only_repayment** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**capital_repayment** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**interest** | [**InterestSchemeValue**](InterestSchemeValue.md) |  | [optional] 
**redemption_penalty** | [**MortgageRedemptionValue3**](MortgageRedemptionValue3.md) |  | [optional] 
**property_address** | [**PropertyAddressRef**](PropertyAddressRef.md) |  | [optional] 
**additional_owners** | [**list[PartyRef]**](PartyRef.md) | Additional owners (Maximum 2). | [optional] 
**total_fees** | [**list[LenderFeeValue3]**](LenderFeeValue3.md) | Collection of lender specific fees. | [optional] 
**provider** | [**ProductProviderRef**](ProductProviderRef.md) |  | [optional] 
**plan_type** | [**PlanTypeReference**](PlanTypeReference.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

