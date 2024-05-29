# AtrTemplate2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ATR template unique identifier. | [optional] 
**href** | **str** | ATR template hypermedia link. | [optional] 
**name** | **str** | Name of the ATR template. | 
**group_owner** | [**GroupOwnerReference**](GroupOwnerReference.md) |  | [optional] 
**created_by_app** | [**NamedAppReference**](NamedAppReference.md) |  | [optional] 
**created_by** | [**UserReference**](UserReference.md) |  | [optional] 
**tags** | **list[str]** | List of tags associated with the ATR template. | [optional] 
**is_active** | **bool** | Is ATR template Active? | [optional] [default to False]
**is_answered** | **bool** | Flag indicating whether an ATR questionnaire based upon the template has been completed or not. | [optional] 
**questions** | [**list[AtrTemplateQuestion]**](AtrTemplateQuestion.md) | ATR questions and answer options. | 
**question_groups** | [**dict(str, AtrQuestionGroup)**](AtrQuestionGroup.md) | Question Groups associated with the ATR template.  This can be used to determine if a client&#x27;s answers contain contradictory statements by comparing groups of answers together.  Only one of QuestionGroups of InconsistentAnswers can be specified. | [optional] 
**inconsistent_answers** | [**list[AtrAnswerContradictions]**](AtrAnswerContradictions.md) | A list of questions and any associated contradictory questions and answers.  This can be used to determine if a client&#x27;s answers contain contradictory statements by comparing answers to individual questions.  Only one of QuestionGroups of InconsistentAnswers can be specified. | [optional] 
**risk_profiles** | [**dict(str, AtrRiskProfile)**](AtrRiskProfile.md) | Risk Profiles associated with the ATR template. | [optional] 
**created_at** | **datetime** | Template Created on. | [optional] 
**asset_model** | [**AssetModel**](AssetModel.md) |  | [optional] 
**updated_at** | **datetime** | Template Last Updated on | [optional] 
**app_template** | [**AtrAppTemplateRef**](AtrAppTemplateRef.md) |  | [optional] 
**retake_interval** | **int** | ATR Template Expiration Configuration (in Months) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

