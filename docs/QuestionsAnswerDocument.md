# QuestionsAnswerDocument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier for the questions answer. | [optional] 
**text** | **str** | The text of the question. | [optional] 
**order** | **int** | The order of the question in a list of questions. | [optional] 
**answer** | **str** | The answer to the question. The answer(s) to questions that can potentially have multiple answers (type &#x27;select&#x27;, &#x27;dropdown&#x27; or &#x27;checkbox&#x27;) are held in the options field. | [optional] 
**notes** | **str** | Supplementary notes related to the answer. | [optional] 
**options** | [**list[QuestionAnswerOption]**](QuestionAnswerOption.md) | The answer(s) to questions of type &#x27;select&#x27;, &#x27;dropdown&#x27; or &#x27;checkbox&#x27;. | [optional] 
**is_archived** | **bool** | Flag indicating whether the question relating to the answer has been archived or not. | [optional] 
**tags** | **list[str]** | A list of tags associated with the question. Tags are free text and are used to group a series of questions together. | [optional] 
**attributes** | **dict(str, str)** | Question related attributes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

