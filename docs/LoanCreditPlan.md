# LoanCreditPlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_loan_value** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**loan_type** | **str** | Type of loan repayment. | [optional] [default to 'null']
**rate_type** | **str** | Type of interest rate product. | [optional] [default to 'null']
**protection_type** | **str** | Protection type. | [optional] [default to 'null']
**redemption_notes** | **str** | Terms of redemption. | [optional] [default to 'null']
**loan_term** | **str** | Loan term in ISO-8601 and restricted to months between 0 to 1200. | [optional] 
**credit_limit** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**interest_rate** | **float** |  | [optional] 
**is_to_be_consolidated** | **bool** | Consolidate | [optional] 
**is_liability_to_be_repaid** | **bool** | Whether liability is to be repaid? | [optional] [default to False]
**liability_repayment_description** | **str** | How will liability be repaid? | [optional] [default to 'null']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

