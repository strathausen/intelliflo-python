# Recommendation2Document

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Recommendation unique identifier. | [optional] 
**href** | **str** | Recommendation hypermedia link. | [optional] 
**status** | [**RecommendationStatusValue**](RecommendationStatusValue.md) |  | [optional] 
**name** | **str** | Name of the recommendation. | 
**service_case** | [**ServiceCaseReference**](ServiceCaseReference.md) |  | [optional] 
**category** | [**RecommendationCategoryRef**](RecommendationCategoryRef.md) |  | [optional] 
**sub_category** | [**RecommendationSubCategoryRef**](RecommendationSubCategoryRef.md) |  | [optional] 
**created_by** | [**NamedUserRef**](NamedUserRef.md) |  | [optional] 
**created_app** | [**NamedAppRef**](NamedAppRef.md) |  | [optional] 
**created_on** | **datetime** | Recommendation created date. | [optional] 
**owners** | [**list[NamedClientReference]**](NamedClientReference.md) | Collection of recommendation owners (clients only). Owner at index 0 is the primary owner. | 
**documents_href** | **str** | Hyperlink to recommendation documents. | [optional] 
**notes** | **str** | Notes to the recommendation. | [optional] 
**priority** | **int** | Priority of the recommendation. | [optional] 
**requirements** | [**list[ObjectiveRef]**](ObjectiveRef.md) | A collection of client objectives linked to this recommendation | [optional] 
**proposals** | [**list[BaseRecommendation2Proposal]**](BaseRecommendation2Proposal.md) | A collection of proposals linked to this recommendation | [optional] 
**properties** | **dict(str, str)** | Editable on POST, PATCH.  Limited to 10 items.  Use this to set custom properties for a recommendation e.g.      \&quot;properties\&quot;: {         \&quot;myCustomProperty\&quot;: \&quot;A value\&quot;,         \&quot;anotherCustomProperty\&quot;: \&quot;Some other value\&quot;      } | [optional] 
**expires_at** | **datetime** | Recommendation expiry date and time. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

