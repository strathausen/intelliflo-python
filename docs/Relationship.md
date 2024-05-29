# Relationship

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**relationship_type** | [**RelationshipTypeRef**](RelationshipTypeRef.md) |  | 
**subject** | [**SubjectRef**](SubjectRef.md) |  | [optional] 
**relation** | [**RelationRef**](RelationRef.md) |  | [optional] 
**is_financial_partnership** | **bool** | Flag indicating if the relationship is a financial partnership (between clients only). | [optional] 
**is_family_group** | **bool** | Is family group flag | [optional] 
**include_in_relations_family_wealth** | **bool** | Includes family wealth access for the relation (between clients only) | [optional] 
**is_point_of_contact** | **bool** | Specifies if the relation is point of contact | [optional] 
**started_on** | **datetime** | The date the relationship was established. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

