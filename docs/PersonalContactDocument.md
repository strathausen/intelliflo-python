# PersonalContactDocument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Personal contact identifies | [optional] 
**href** | **str** | Personal contact link | [optional] 
**name** | **str** | Personal contact name | [optional] 
**party_type** | **str** | Personal contact party type | 
**party** | [**PartyReference**](PartyReference.md) |  | [optional] 
**person** | [**PersonValue**](PersonValue.md) |  | [optional] 
**corporate** | [**CorporateValue**](CorporateValue.md) |  | [optional] 
**trust** | [**TrustValue**](TrustValue.md) |  | [optional] 
**addresses__href** | **str** | Personal contact address link | [optional] 
**contactdetails__href** | **str** | Personal contact contact details link | [optional] 
**tags** | **list[str]** | List of tags for personal contact | [optional] 
**created_at** | **datetime** | Date of creation personal contact | [optional] 
**created_by_user** | [**UserReference**](UserReference.md) |  | [optional] 
**belongs_to** | [**list[ClientRef]**](ClientRef.md) | List of related clients for personal contact | [optional] 
**external_reference** | **str** | The external reference. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

