# Address

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**residency_status** | **str** | Residency status | [optional] [default to 'null']
**type** | **str** | Address type | [optional] 
**resident_from** | **datetime** | Resident from | [optional] 
**resident_to** | **datetime** | Resident to | [optional] 
**status** | **str** | Address status | [optional] [default to 'null']
**is_default** | **bool** | Is default address flag | [optional] [default to False]
**address** | [**AddressDetailsValue**](AddressDetailsValue.md) |  | 
**is_registered_on_electoral_roll** | **bool** | This parameter indicates whether the addressee is registered at this address to vote within the electoral district. | [optional] [default to False]
**is_potential_mortgage** | **bool** | This parameter indicates whether the address can be mortgage. | [optional] [default to False]
**_property** | [**PropertyDetailsValue**](PropertyDetailsValue.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

