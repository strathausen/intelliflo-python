# BaseRecommendation2Proposal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discriminator** | **str** | Proposal discriminator value. | 
**id** | **int** | Proposal unique identifier. | [optional] 
**href** | **str** | Proposal hypermedia link. | [optional] 
**status** | **str** | Proposal status. | [optional] 
**implementation_status** | **str** | Implementation status. | [optional] 
**status_at** | **datetime** | Date and time the proposal status was set at. | [optional] 
**status_by** | [**NamedUserRef**](NamedUserRef.md) |  | [optional] 
**recommendation** | [**Recommendation2Ref**](Recommendation2Ref.md) |  | 
**plan** | [**PlanReference**](PlanReference.md) |  | [optional] 
**quote_result** | [**QuoteResultRef2**](QuoteResultRef2.md) |  | [optional] 
**owners** | [**list[NamedClientReference]**](NamedClientReference.md) | Collection of proposal owners (clients only). Owner at index 0 is the primary owner. | 
**properties** | **dict(str, str)** | Editable on POST, PUT.  Limited to 10 items.  Use this to set custom properties for a proposal e.g.      \&quot;properties\&quot;: {         \&quot;myCustomProperty\&quot;: \&quot;A value\&quot;,         \&quot;anotherCustomProperty\&quot;: \&quot;Some other value\&quot;      } | [optional] 
**atr** | [**AtrRef**](AtrRef.md) |  | [optional] 
**fee_model** | [**FeeModelFeeTemplateRef**](FeeModelFeeTemplateRef.md) |  | [optional] 
**program** | [**NamedProgramReference**](NamedProgramReference.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

