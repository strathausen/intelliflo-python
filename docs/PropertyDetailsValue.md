# PropertyDetailsValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Description of property type | [optional] [default to 'null']
**type_detail** | **str** | Additional property details | [optional] [default to 'null']
**tenure_type** | **str** | The conditions under which the property is held or occupied (ie rented or owned). | [optional] [default to 'null']
**leasehold_ends_on** | **datetime** | Leasehold End Date, not null if PropertyTenureTypeValue is Leasehold | [optional] 
**status** | **str** | Property status | [optional] [default to 'null']
**construction** | **str** | Construction definition | [optional] [default to 'null']
**construction_notes** | **str** | Construction notes | [optional] [default to 'null']
**roof_construction** | **str** | Roof construction definition | [optional] [default to 'null']
**number_of_bedrooms** | **int** | Number of bedrooms | [optional] 
**year_built** | **int** | The year was the property was built. | [optional] 
**is_ex_local_authority** | **bool** | Indicates if a property was bought from a council at a discounted rate. | [optional] [default to False]
**number_of_outbuildings** | **int** | Number of outbuildings | [optional] 
**new_build** | [**PropertyDetailsNewBuildValue**](PropertyDetailsNewBuildValue.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

