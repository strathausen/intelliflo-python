# AtrInstalledTemplate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the 3rd party provider template . | [optional] 
**href** | **str** | ATR app template hypermedia link. | [optional] 
**is_accepted** | **bool** | Accept ATR template from the provider apps they have installed. | [optional] 
**name** | **str** | the name of the ATR template. | 
**created_by_app** | [**NamedAppReference**](NamedAppReference.md) |  | [optional] 
**questions** | [**list[AtrTemplateQuestion]**](AtrTemplateQuestion.md) | ATR questions and answer options. | 
**question_groups** | [**dict(str, AtrQuestionGroup)**](AtrQuestionGroup.md) | Question Groups associated with the ATR template. This can be used to determine if a client&#x27;s answers contain contradictory statements by comparing groups of answers together.  Only one of QuestionGroups of InconsistentAnswers can be specified. | [optional] 
**inconsistent_answers** | [**list[AtrAnswerContradictions]**](AtrAnswerContradictions.md) | A list of questions and any associated contradictory questions and answers. This can be used to determine if a client&#x27;s answers contain contradictory statements  by comparing answers to individual questions. Only one of QuestionGroups of InconsistentAnswers can be specified. | [optional] 
**risk_profiles** | [**dict(str, AtrRiskProfile)**](AtrRiskProfile.md) | Risk Profiles associated with the ATR template.  The risk profile code has a maximum length of 7 and should meet the match the regex&#x3D;^[A-Z]{3}-[%.,+0-z]{1,3}$]. | 
**asset_model** | [**AssetModel**](AssetModel.md) |  | [optional] 
**created_at** | **datetime** | Template created on. | [optional] 
**updated_at** | **datetime** | Template last updated on. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

