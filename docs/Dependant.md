# Dependant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Dependant identifier | [optional] 
**href** | **str** | Hypermedia link | [optional] 
**name** | **str** | Dependant name | 
**date_of_birth** | **datetime** | Date of birth - min value: 01/01/1900 - max value: Current Date | [optional] 
**is_living_with** | **bool** | Specifies whether dependant is living with client(s) | [optional] [default to False]
**is_financially_dependant** | **bool** | Specifies whether dependant is financially dependant | [optional] 
**financial_dependency_ends_on** | **datetime** | Financial dependency end date - min value: 01/01/1900 - max value: 31/12/2150 | [optional] 
**relationship_type** | **str** | Relationship type with client(s) | 
**notes** | **str** | Notes | [optional] [default to 'null']
**clients** | [**list[ClientRef]**](ClientRef.md) | List of related clients | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

