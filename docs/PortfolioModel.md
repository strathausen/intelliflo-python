# PortfolioModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**funds** | [**list[PortfolioModelFundRef]**](PortfolioModelFundRef.md) | A list of funds associated with the portfolio model. | [optional] 
**created_at** | **datetime** | The date when the portfolio model was created. | [optional] 
**created_by_app** | [**NamedAppRef**](NamedAppRef.md) |  | [optional] 
**created_by** | [**NamedUserRef**](NamedUserRef.md) |  | [optional] 
**current_group_name** | **str** | The group name if model applicable to group | [optional] 
**allow_rebalance** | **bool** | Is rebalance allowed for the portfolio model? | [optional] 
**is_invested** | **bool** |  | [optional] 
**tags** | **list[str]** | Descriptive tags applied to a model which can be used for custom searches/filters  e.g. &#x27;ReducedCost&#x27;, &#x27;Outperform&#x27;, &#x27;ESG&#x27; | [optional] 
**expected_return** | **str** | The expected return for the model | [optional] 
**expected_risk** | **str** | The expected risk for the model | [optional] 
**investment_amount_upper** | **float** | The maximum investment amount required/permitted for the model | [optional] 
**investment_amount_lower** | **float** | The minimum investment amount required/permitted for the model | [optional] 
**status** | **str** | The status of model portfolio | [optional] 
**version** | **int** | The version of portfolio | [optional] 
**reference** | **str** | The additional reference the Adviser Pro tool uses for models alongside the model code | [optional] 
**is_locked** | **bool** | Indicates either the model is editable or not for any user except of the owner | [optional] 
**asset_model** | **str** | The Asset Model associated with the portfolio model | [optional] 
**benchmark** | [**BenchmarkRef**](BenchmarkRef.md) |  | [optional] 
**is_latest_version** | **bool** | Indicates whether this version of the model is last or not | [optional] 
**description** | **str** | The description of the portfolio model. | [optional] 
**risk_reference** | **str** | The RiskReference associated with the portfolio model | [optional] 
**investment_objective** | **list[str]** | Investement Objective Attribute | [optional] 
**investment_management_style** | **str** | Investment Management Style Attribute | [optional] 
**tax_qualified** | **str** | Tax Qualified Attribute | [optional] 
**esg** | **list[str]** | Esg Attribute | [optional] 
**is_externally_managed** | **bool** | Indicating whether this instance is externally managed. | [optional] 
**is_imps** | **bool** | Indicating whether this instance is imps. | [optional] 
**model_risk_profile** | [**ModelRiskProfile**](ModelRiskProfile.md) |  | [optional] 
**provider** | **str** | The portfolio model provider. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

