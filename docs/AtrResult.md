# AtrResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** | System generated score based on weights. | [optional] 
**notes** | **str** | Any notes associated with the answer. | [optional] 
**has_inconsistency_in_answers** | **bool** | Flag indicating if there is inconsistency found in the client&#x27;s answers. | [optional] 
**inconsistency_notes** | **str** | If HasInconsistencyInAnswers flag returns true, inconsistency notes can be provided. | [optional] 
**generated_risk_profile** | [**AtrGeneratedRiskProfile**](AtrGeneratedRiskProfile.md) |  | [optional] 
**agreed_with_generated_risk_profile** | **bool** | Flag indicating whether or not the client agreed with the generated ATR risk profile. | [optional] 
**chosen_risk_profile_value** | [**AtrChosenRiskProfile**](AtrChosenRiskProfile.md) |  | [optional] 
**completed_at** | **datetime** | ATR result completed date. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

