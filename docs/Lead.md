# Lead

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the Lead. | [optional] 
**href** | **str** | The hypertext reference to the Lead. | [optional] 
**name** | **str** | The Lead&#x27;s name. This is derived from the Lead&#x27;s details, for a Person it is their Firstname and Lastname. | [optional] 
**created_at** | **datetime** | The date the Lead was created. | [optional] 
**person** | [**PersonValue**](PersonValue.md) |  | [optional] 
**corporate** | [**CorporateValue**](CorporateValue.md) |  | [optional] 
**trust** | [**TrustValue**](TrustValue.md) |  | [optional] 
**original_adviser** | [**NamedAdviserRef**](NamedAdviserRef.md) |  | [optional] 
**current_adviser** | [**NamedAdviserRef**](NamedAdviserRef.md) |  | [optional] 
**campaign** | [**CampaignValue**](CampaignValue.md) |  | [optional] 
**type** | **str** |  | [optional] 
**party_type** | **str** | The type of Lead, either Person, Trust or Corporate. | [optional] 
**category** | **str** | The category of Lead to which the Lead belongs. | [optional] 
**migration_reference** | **str** | The Lead migration reference. Typically a reference set when the Lead was imported into the system. | [optional] 
**external_reference** | **str** | An external reference for the Lead. | [optional] 
**secondary_reference** | **str** | An secondary external reference for the Lead. | [optional] 
**addresses_href** | **str** | The hypertext reference to the address or addresses held for the Lead. Typically these may be a home, work or correspondance address. | [optional] 
**contactdetails_href** | **str** | The hypertext reference to the list of contact details held for the Lead. | [optional] 
**relationships_href** | **str** | The hypertext reference to the list of any relevant relationships, professional or personal, that the Lead may have. | [optional] 
**tags** | **list[str]** | A list of tags associated with the Lead The list can contain up to 30 tags. Each tag has a maximum length of 100 charecters and may not contain spaces. | [optional] 
**status** | **str** | The current status of the Lead. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

