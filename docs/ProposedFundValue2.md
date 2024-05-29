# ProposedFundValue2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percentage** | **float** | The proportion to invest in the fund, ie. Percentage of Holding. | [optional] [default to 0.0]
**percentage_of_regular_contribution** | **float** | The proportion of regular contribution. | [optional] 
**name** | **str** | The name of the fund. | 
**currency** | **str** | The currency of the fund. If this is not supplied then we will assume regional currency  if we find multiple matches for the Fund codes. | [optional] 
**fund_type** | **str** | Indicates whether the validated funds relates to a FeedFund, Equity or Manual Fund. | [optional] 
**codes** | [**RecommendFundCodesValue**](RecommendFundCodesValue.md) |  | [optional] 
**risk_score** | [**RiskScoreValue**](RiskScoreValue.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

