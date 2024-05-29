# ActivityLinkedEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the linked entity. | 
**href** | **str** | The hypertext reference to the linked entity | [optional] 
**type** | **str** | The type of entity. Allowed values are: &#x27;Plan&#x27;,&#x27;Opportunity&#x27;,&#x27;ServiceCase&#x27;.The linked entity will be dependent on RelateTo - Type  If RelatedTo - Type is Client, allowed LinkedEntity types are “Plan”, “Opportunity”,\&quot;ServiceCase\&quot;  If RelatedTo - Type is Lead, allowed LinkedEntity types is “Opportunity”,  If RelatedTo - Type is Account or Adviser, then LinkedEntity is not valid.”, | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

