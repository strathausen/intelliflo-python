# BeneficiarySubject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | BeneficiarySubject unique identifier.  clientid/personalcontactid, existing db column: BeneficiaryCrmContactId | 
**href** | **str** | Hypermedia link to the BeneficiarySubject | [optional] 
**type** | **str** | BeneficiarySubject discriminator  Client|PersonalContact for personalContact: it&#x27;s always one of the trust&#x27;s personal contacts | 
**name** | **str** | Subject&#x27;s full name | [optional] 
**date_of_birth** | **datetime** | Subject&#x27;s date of birth | [optional] 
**relationship_type** | [**BeneficiaryRelationshipNameRef**](BeneficiaryRelationshipNameRef.md) |  | [optional] 
**external_reference** | **str** |  | [optional] 
**owner_client_id** | **int** | The unique identifier of the plan&#x27;s owner. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

