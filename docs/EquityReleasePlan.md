# EquityReleasePlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equity_release_type** | **str** | Type of equity release product. | [optional] [default to 'null']
**ownership_sold** | **float** | Percentage of ownership sold. | [optional] 
**released** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**equity** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**valuation** | [**MortgagedPropertyValuationValue3**](MortgagedPropertyValuationValue3.md) |  | [optional] 
**loan_value** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**lump_sum** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**monthly_income** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**is_to_be_consolidated** | **bool** | Consolidate | [optional] 
**is_liability_to_be_repaid** | **bool** | Whether liability is to be repaid? | [optional] [default to False]
**liability_repayment_description** | **str** | How will liability be repaid? | [optional] [default to 'null']
**repayment_method** | **str** | Repayment method type. | [optional] [default to 'null']
**interest** | [**InterestSchemeValue**](InterestSchemeValue.md) |  | [optional] 
**term** | [**MortgageTermValue**](MortgageTermValue.md) |  | [optional] 
**application_submitted_on** | **datetime** | Date mortgage application submitted. | [optional] 
**loan_to_value** | **float** | Loan to value percentage. | [optional] 
**offer_made_on** | **datetime** | Date mortgage offer made on. | [optional] 
**target_completion_date** | **datetime** | Target completion date. | [optional] 
**completion_date** | **datetime** | Completion date. | [optional] 
**exchange_date** | **datetime** | Exchange date. | [optional] 
**review_on** | **datetime** | Mortgage review date. | [optional] 
**redemption_penalty** | [**MortgageRedemptionValue2**](MortgageRedemptionValue2.md) |  | [optional] 
**additional_owners** | [**list[ClientRef]**](ClientRef.md) | Additional owners (Maximum 2). | [optional] 
**capital_repayment** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**interest_only_repayment** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**asset** | [**AssetReference**](AssetReference.md) |  | [optional] 
**address** | [**AddressRef**](AddressRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

