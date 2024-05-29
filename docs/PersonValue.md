# PersonValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**salutation** | **str** | The Person&#x27;s preferred salutation if known. | [optional] 
**title** | **str** | The Person&#x27;s title. | [optional] 
**first_name** | **str** | The Person&#x27;s first name. | 
**middle_name** | **str** | The Person&#x27;s middle name if they have one. | [optional] 
**last_name** | **str** | The Person&#x27;s last name. | 
**date_of_birth** | **date** | The Person&#x27;s date of birth. | [optional] 
**gender** | **str** | The Person&#x27;s gender. | [optional] 
**maiden_name** | **str** | The Person&#x27;s maiden name. | [optional] 
**ni_number** | **str** | The Person&#x27;s National Insurance number (in UK), Social Security Number (in US) or local equivalent. | [optional] 
**marital_status** | **str** | The Person&#x27;s marital status. | [optional] 
**marital_status_since** | **datetime** | The date the Person was married if appropriate. | [optional] 
**nationality** | **str** | This property has been depricated and will be removed in future. Please use NationalityCountry instead. | [optional] 
**nationality_country** | [**NationalityCountryValue**](NationalityCountryValue.md) |  | [optional] 
**is_deceased** | **bool** | Flag indicating whether the Person has died. If set to true the deceasedOn date must also be set. | [optional] 
**deceased_on** | **datetime** | The date of the Person&#x27;s death. This must be set if isDeceased is true. | [optional] 
**territorial_profile** | [**TerritorialProfileValue**](TerritorialProfileValue.md) |  | [optional] 
**health_profile** | [**HealthProfileValue**](HealthProfileValue.md) |  | [optional] 
**has_will** | **bool** | Flag indicatiing whether the Person has a will or not. | [optional] 
**is_will_upto_date** | **bool** | Flag indicatiing whether the Person&#x27;s will is upto date or not. | [optional] 
**is_power_of_attorney_granted** | **bool** | Flag indicating if the Person has assigned someone to act on their behalf in legal or financial matters. | [optional] 
**national_client_identifier** | **str** | The National Client Identifier associated with the Person. This is a unique country specific client identifier eg. National Insurance number for UK. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

