# ProviderModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | An unique Identifier for this Portfolio Model | [optional] 
**provider_name** | **str** | The Portfolio Model Provider | [optional] 
**href** | **str** | Resource Uri for this Portfolio Model | [optional] 
**code** | **str** | A Unique code to identify this Portfolio Model | 
**name** | **str** | The Name of the this Portfolio Model | 
**description** | **str** | Short Description of this Portfolio Model | 
**change_description** | **str** | Short commentary on what has changed in this version of the Portfolio Model | [optional] 
**market_commentary_rss_href** | **str** | The Url for the Market Commentary RSS feed for this Portfolio Model | [optional] 
**is_active** | **bool** | Indicates that this is the latest version of the Portfolio Model | [optional] 
**funds** | [**list[ModelFundValue]**](ModelFundValue.md) | The list of recommended Fund allocations for this model. | 
**atrs** | [**list[ModelAtrValue]**](ModelAtrValue.md) | The list of ATRs that this model is suitable for | 
**created_at** | **datetime** | Indicates when this version of the Portfolio Model was created. | [optional] 
**created_by_app** | [**NamedAppRef**](NamedAppRef.md) |  | [optional] 
**reference** | **str** | The additional reference the Adviser Pro tool uses for models alongside the model code | [optional] 
**expected_return** | **str** | The expected return for the model | [optional] 
**expected_risk** | **str** | The expected risk for the model | [optional] 
**investment_amount_upper** | **float** | The maximum investment amount required/permitted for the model | [optional] 
**investment_amount_lower** | **float** | The minimum investment amount required/permitted for the model | [optional] 
**benchmark_name** | **str** | The Benchmark associated with the portfolio model | [optional] 
**allow_rebalance** | **bool** | Allow iMPS rebalance activity | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

