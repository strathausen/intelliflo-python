# Transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Transaction Id | [optional] 
**href** | **str** | Href of the Transaction | [optional] 
**parent_href** | **str** |  | [optional] 
**plan** | [**MatchPlanRef**](MatchPlanRef.md) |  | 
**holding** | [**HoldingRef**](HoldingRef.md) |  | [optional] 
**transaction_date** | **datetime** | Transaction date | 
**source** | **str** | Source - Plan|Fund | 
**type** | **str** | Entry Type - Income|Expense|Transfer In|Transfer Out | [optional] 
**debit_credit_indicator** | **str** | Debit Credit indicator DR|CR | [optional] 
**unit_price** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**cost** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**gross** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**unit_number** | **float** | Unit number, required for fund transactions, defaults to 1 for banking transactions | [optional] 
**description** | **str** | Transaction description | [optional] 
**category1** | **str** | Category 1 | [optional] 
**category1_code** | **str** | Category 1 Value | [optional] 
**category2** | **str** | Category 2 | [optional] 
**category2_code** | **str** | Category 2 Code | [optional] 
**payment_from** | **str** | Payment From | [optional] 
**payment_to** | **str** | Payment to | [optional] 
**frequency** | **str** | Transaction Frequency | [optional] 
**external_reference** | **str** | External Reference | [optional] 
**is_restricted_to_owner** | **bool** | Is Restricted transaction - default to false | [optional] 
**created_by_user** | [**UserRef2**](UserRef2.md) |  | [optional] 
**created_by_app** | [**NamedAppRef**](NamedAppRef.md) |  | [optional] 
**created_at** | **datetime** | Will hold the UTC timestamp for when the transaction was created | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

