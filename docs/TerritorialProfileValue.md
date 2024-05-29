# TerritorialProfileValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uk_resident** | **bool** | Flag indicating if the person is a resident of the UK or not?  Note: This property has been depricated and will be removed in future. Please use CountryOfResidence instead.  If provided the CountryOfResidence property will be used to set the the value of the UkResident property. | [optional] 
**country_of_birth** | **str** | The person&#x27;s country of birth.  Note: This property has been depricated and will be removed in future. Please use CountryOfOrigin instead. | [optional] 
**uk_domicile** | **bool** | Flag indicating if the person is domiciled in the UK or not?  Note: This property has been depricated and will be removed in future. Please use CountryOfDomicile instead.  If provided the CountryOfDomicile property will be used to set the the value of the UkDomicile property. | [optional] 
**expatriate** | **bool** | Flag indicating if the person an expatriate or not? | [optional] 
**country_of_residence** | [**CountryValue**](CountryValue.md) |  | [optional] 
**country_of_domicile** | [**CountryValue**](CountryValue.md) |  | [optional] 
**country_of_origin** | [**CountryValue**](CountryValue.md) |  | [optional] 
**place_of_birth** | **str** | Place of birth of the person. | [optional] 
**countries_of_citizenship** | [**list[CountryValue]**](CountryValue.md) | Countries where the person has citizenship. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

