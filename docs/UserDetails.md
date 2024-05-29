# UserDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User unique identifier. | [optional] 
**href** | **str** | User hypermedia link. | [optional] 
**user_name** | **str** | User unique username. | 
**email** | **str** | User email address. | [optional] 
**subject** | **str** | Unique identifier Guid. If one is not provided, then we will generate one for you. | [optional] 
**application_type** | **str** | Application Type | [optional] 
**first_name** | **str** | User first name. | 
**last_name** | **str** | User last name. | 
**time_zone** | **str** | User timezone. The timezone should be a valid timezoneid from the IANA time zone database. E.g: Europe/London or America/New_York. | [optional] 
**status** | **str** | User status. | [optional] 
**references** | [**AdditionalDetailsRef**](AdditionalDetailsRef.md) |  | [optional] 
**tenant** | [**NamedTenantRef**](NamedTenantRef.md) |  | [optional] 
**client** | [**ClientRef**](ClientRef.md) |  | [optional] 
**group** | [**NamedGroupRef**](NamedGroupRef.md) |  | [optional] 
**last_login_at** | **datetime** | Last logon time of user | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

