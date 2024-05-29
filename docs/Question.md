# Question

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the Question. | [optional] 
**href** | **str** |  | [optional] 
**question_type** | **str** | The type of the Question. | 
**subcategory** | [**Subcategory**](Subcategory.md) |  | [optional] 
**is_required** | **bool** | Flag indicating whether the question must be answered or not. | [optional] 
**is_multiple** | **bool** | Flag indicating whether multiple answer options can exist for a given question. This can only be used if the QuestionType is &#x27;select&#x27;, &#x27;dropdown&#x27; or &#x27;checkbox&#x27;. | [optional] 
**text** | **str** | The actual text for the question. | 
**options** | [**list[QuestionOption]**](QuestionOption.md) | The list of potential answers to a question. This is only applicable and required if the QuestionType is &#x27;select&#x27;, &#x27;dropdown&#x27; or &#x27;checkbox&#x27;. | [optional] 
**order** | **int** | The order, within the questions subcategory, in which the questions should be displayed. | 
**tags** | **list[str]** | A list of tags associated with the question. Tags are free text and are used to group a series of questions together. Questions can be filtered by Tag. | [optional] 
**is_archived** | **bool** | Flag indicating whether the question has been archived or not. Archived questions are no longer used/displayed. | [optional] 
**include_notes** | **bool** | Flag indicating whether to display a text box to capture additional text notes alongside the answer input. | [optional] 
**place_holder_text** | **str** | Text to display on the form as placeholder text. | [optional] 
**help_text** | **str** | Text to display on form as help text. | [optional] 
**pattern** | **str** | Regex pattern for input validation. | [optional] 
**error_text** | **str** | The error text to display to the user if the given answer is invalid. | [optional] 
**attributes** | **dict(str, str)** | A list (max 5) of attributes related to a question. Attribute prefixed with &#x27;_&#x27; are reserved system attributes.  The attributes &#x27;_category&#x27; and &#x27;_subcategory&#x27; may be used to categorise questions. | [optional] 
**logic** | [**list[QuestionLogic]**](QuestionLogic.md) | Rules determining if the question is displayed/required etc based on the answers to other related questions.. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

