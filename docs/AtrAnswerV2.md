# AtrAnswerV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ATR answer unique identifier. | [optional] 
**href** | **str** | ATR answer hypermedia link. | [optional] 
**clients** | [**list[ClientRef]**](ClientRef.md) | Atr answer client references. | [optional] 
**context** | **str** | Context under which the answers were provided. | 
**status** | **str** | Status of the ATR. When status is set to \&quot;Completed\&quot;, results are generated and question answers cannot be modified. | [optional] [default to 'Draft']
**template** | [**ATRTemplateReference**](ATRTemplateReference.md) |  | 
**asset_model** | [**AssetModel**](AssetModel.md) |  | [optional] 
**questions** | [**list[AtrQuestion]**](AtrQuestion.md) | ATR questions and associated answers. | 
**inconsistent_answers** | [**list[AtrAnswerContradictions]**](AtrAnswerContradictions.md) | A list of questions and any associated contradictory questions and answers.  This can be used to determine if a client&#x27;s answers contain contradictory statements by comparing answers to individual questions. | [optional] 
**result** | [**AtrResult**](AtrResult.md) |  | [optional] 
**completed_at** | **datetime** | ATR answer completed date. | [optional] 
**completed_by** | [**UserReference**](UserReference.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

