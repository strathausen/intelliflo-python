# Client

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the Client. | [optional] 
**href** | **str** | The hypertext reference to the Client. | [optional] 
**name** | **str** | The Client&#x27;s name. This is derived from the Client&#x27;s details, for a Person it is their Firstname and Lastname. | [optional] 
**created_at** | **datetime** | The date the Client was created. | [optional] 
**campaign** | [**CampaignValue**](CampaignValue.md) |  | [optional] 
**category** | **str** | The category of Client to which the Client belongs. | [optional] 
**migration_reference** | **str** | The Client migration reference. Typically a reference set when the Client was imported into the system. | [optional] 
**external_reference** | **str** | An external reference for the Client. | [optional] 
**secondary_reference** | **str** | An secondary external reference for the Client. | [optional] 
**original_adviser** | [**NamedAdviserRef**](NamedAdviserRef.md) |  | [optional] 
**current_adviser** | [**NamedAdviserRef**](NamedAdviserRef.md) |  | 
**type** | **str** |  | [optional] 
**party_type** | **str** | The type of Client, either Person, Trust or Corporate. | [optional] 
**person** | [**PersonValue**](PersonValue.md) |  | [optional] 
**corporate** | [**CorporateValue**](CorporateValue.md) |  | [optional] 
**trust** | [**TrustValue**](TrustValue.md) |  | [optional] 
**addresses_href** | **str** | The hypertext reference to the address or addresses held for the Client. Typically these may be a home, work or correspondance address. | [optional] 
**contactdetails_href** | **str** | The hypertext reference to the list of contact details held for the Client. | [optional] 
**plans_href** | **str** | The hypertext reference to the list of the Client&#x27;s plans. | [optional] 
**relationships_href** | **str** | The hypertext reference to the list of any relevant relationships, professional or personal, that the Client may have. | [optional] 
**servicecases_href** | **str** | The hypertext reference to the Client&#x27;s service cases. | [optional] 
**dependants_href** | **str** | The hypertext reference to the list of the Client&#x27;s dependents, if any. | [optional] 
**is_head_of_family_group** | **bool** | Flag indicating whether or not the Client is the head of a family group. | [optional] 
**servicing_administrator** | [**UserReference**](UserReference.md) |  | [optional] 
**paraplanner** | [**UserReference**](UserReference.md) |  | [optional] 
**tags** | **list[str]** | A list of tags associated with the Client. The list can contain up to 30 tags. Each tag has a maximum length of 100 charecters and may not contain spaces. | [optional] 
**tax_reference_number** | **str** | The Client&#x27;s tax reference number. The value returned will be obfuscated unless the api is called with the scope of the request set to client_identification_data. | [optional] 
**user** | [**UserReference**](UserReference.md) |  | [optional] 
**service_status** | [**ServiceStatusValue**](ServiceStatusValue.md) |  | [optional] 
**client_segment** | [**ClientSegmentValue**](ClientSegmentValue.md) |  | [optional] 
**group** | [**GroupRef**](GroupRef.md) |  | [optional] 
**household** | [**NamedHouseholdReference**](NamedHouseholdReference.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

