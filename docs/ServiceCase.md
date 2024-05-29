# ServiceCase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Service case Unique Identifier. | [optional] 
**href** | **str** | Hypermedia link to Service case. | [optional] 
**document_binder** | [**NamedDocumentBinderRef**](NamedDocumentBinderRef.md) |  | [optional] 
**description** | **str** | Description of the service case. | 
**category** | **str** | Category of the service case. | [optional] 
**reference** | **str** | Sequential reference for the Service case. | [optional] 
**additional_reference** | **str** | Service case reference. | [optional] 
**status** | **str** | Status of the service case. | [optional] 
**started_at** | **datetime** | The date and time when the service case started. | [optional] 
**client** | [**NamedClientValue**](NamedClientValue.md) |  | [optional] 
**joint_client** | [**NamedClientValue**](NamedClientValue.md) |  | [optional] 
**adviser** | [**NamedAdviserRef**](NamedAdviserRef.md) |  | 
**plans** | [**list[PlanRef]**](PlanRef.md) | Linked plans. | [optional] 
**objectives** | [**list[ObjectiveReference]**](ObjectiveReference.md) | Objectives. | [optional] 
**plans_href** | **str** | Hypermedia link to linked plans. | [optional] 
**servicing_administrator** | [**NamedUserReference**](NamedUserReference.md) |  | [optional] 
**paraplanner** | [**NamedUserReference**](NamedUserReference.md) |  | [optional] 
**vulnerability_owner1** | [**LegacyVulnerabilityValue**](LegacyVulnerabilityValue.md) |  | [optional] 
**vulnerability_owner2** | [**LegacyVulnerabilityValue**](LegacyVulnerabilityValue.md) |  | [optional] 
**opportunity** | [**OpportunityRef**](OpportunityRef.md) |  | [optional] 
**is_joint** | **bool** | Determines if the service case is joint. | [optional] 
**is_completed** | **bool** | Determines if the service case is completed. | [optional] 
**properties** | **dict(str, str)** | Service case related properties. | [optional] 
**client1_risk_profile_ref** | [**ClientRiskProfileRef**](ClientRiskProfileRef.md) |  | [optional] 
**client2_risk_profile_ref** | [**ClientRiskProfileRef**](ClientRiskProfileRef.md) |  | [optional] 
**client1_investment_preference** | [**ClientInvestmentPreferenceRef**](ClientInvestmentPreferenceRef.md) |  | [optional] 
**client2_investment_preference** | [**ClientInvestmentPreferenceRef**](ClientInvestmentPreferenceRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

