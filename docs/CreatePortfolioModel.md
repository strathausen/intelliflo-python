# CreatePortfolioModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the portfolio model. | [optional] 
**funds** | [**list[CreatePortfolioModelFundRef]**](CreatePortfolioModelFundRef.md) | A list of funds associated with the portfolio model. | [optional] 
**tags** | **list[str]** | Descriptive tags applied to a model which can be used for custom searches/filters e.g.  &#x27;ReducedCost&#x27;, &#x27;Outperform&#x27;, &#x27;ESG&#x27; | [optional] 
**expected_return** | **str** | The expected return for the model | [optional] 
**expected_risk** | **str** | The expected risk for the model | [optional] 
**investment_amount_upper** | **float** | The maximum investment amount required/permitted for the model | [optional] 
**investment_amount_lower** | **float** | The minimum investment amount required/permitted for the model | [optional] 
**status** | **str** | The status of model portfolio | [optional] 
**version** | **int** | The version of portfolio | [optional] 
**reference** | **str** | The additional reference the Adviser Pro tool uses for models alongside the model code | [optional] 
**benchmark** | [**BenchmarkRef**](BenchmarkRef.md) |  | [optional] 
**is_locked** | **bool** | Indicates either the model is editable or not for any user except of the owner | [optional] 
**risk_reference** | **str** | The RiskReference associated with the portfolio model | [optional] 
**investment_objective** | **list[str]** | Investement Objective Attribute | [optional] 
**investment_management_style** | **str** | Investment Management Style Attribute | [optional] 
**tax_qualified** | **str** | Tax Qualified Attribute | [optional] 
**esg** | **list[str]** | Esg Attribute | [optional] 
**is_externally_managed** | **bool** | Gets or sets a value indicating whether this instance is externally managed. | [optional] 
**model_risk_profile** | [**ModelRiskProfile**](ModelRiskProfile.md) |  | [optional] 
**provider** | **str** | The portfolio model provider. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

