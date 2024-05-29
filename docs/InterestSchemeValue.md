# InterestSchemeValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **float** | The Lender&#x27;s standard product rate. | [optional] 
**type** | **str** | Type of interest rate product. | [optional] [default to 'null']
**collar_rate** | **float** | Represents the interest rate below which a Lender&#x27;s variable interest rate will not drop. | [optional] 
**base_rate** | **str** | The interest rate the Bank of England charges other banks and lenders that wish to borrow money. | [optional] [default to 'null']
**scheme_rate** | **float** | A special rate that overrides the standard rate until the scheme ends. | [optional] 
**scheme_ends_on** | **datetime** | The date on which the scheme rate reverts to the standard rate. | [optional] 
**rate_apr** | **float** | Interest Rate APR. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

