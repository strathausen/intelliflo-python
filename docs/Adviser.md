# Adviser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the Adviser. | [optional] 
**href** | **str** | The hypertext reference to the Adviser. | [optional] 
**name** | **str** | The Adviser&#x27;s name consisting of their Firstname and Lastname. | [optional] 
**authorised_on** | **datetime** | The date the Adviser was authorised. | [optional] 
**fca_ref_no** | **str** | Authorisation number from the local Financial Regulatory Body. | [optional] 
**person** | [**PersonValue**](PersonValue.md) |  | [optional] 
**joined_firm_on** | **datetime** | The date the Adviser joined the advising company. | [optional] 
**left_firm_on** | **datetime** | The date the Adviser left the advising company. | [optional] 
**migration_ref** | **str** | The Adviser&#x27;s migration reference. Typically a reference set when the Adviser was imported into the system. | [optional] 
**external_ref1** | **str** | An external reference for the Adviser. | [optional] 
**external_ref2** | **str** | An secondary external reference for the Adviser. | [optional] 
**addresses_href** | **str** | The hypertext reference to the address or addresses held for the Adviser. Typically these may be a home, work or correspondance address. | [optional] 
**contact_details_href** | **str** | The hypertext reference to the list of contact details held for the Adviser. | [optional] 
**tand_c_coach** | [**TandCCoachRef**](TandCCoachRef.md) |  | [optional] 
**user** | [**UserReference**](UserReference.md) |  | [optional] 
**group** | [**NamedGroupReference**](NamedGroupReference.md) |  | [optional] 
**can_sell_off_panel** | **bool** | Indicating whether the Adviser can sell off panel. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

