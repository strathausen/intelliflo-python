# AtrQuestion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **str** | Free text answer for questions of type &#x27;Text&#x27;. | [optional] 
**answers** | [**list[AtrAnswerValueV2]**](AtrAnswerValueV2.md) | ATR question&#x27;s answers options, only required if the QuestionType is &#x27;SingleChoice&#x27;. | [optional] 
**id** | **str** | ATR question identifier. | 
**text** | **str** | ATR question text. | 
**question_type** | **str** | ATR question type (ex.: single choice, text). | 
**question_group** | **str** | ATR question&#x27;s risk group. Only applicable if QuestionGroups are being used as a means to identify inconsistencies in a client&#x27;s answers.  If InconsistentAnswers are used rather than QuestionGroups this should not be populated. | [optional] 
**tool_tip** | **str** | Question help text. Available as tooltip in external applications such as PFP. | [optional] 
**sub_text1** | **str** | Help text placed underneath the question. Available in external applications such as PFP. | [optional] 
**sub_text2** | **str** | Help text placed underneath the question. Available in external applications such as PFP. | [optional] 
**category** | **str** | ATR question category. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

