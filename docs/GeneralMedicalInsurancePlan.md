# GeneralMedicalInsurancePlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | **str** | Policy duration in years (ISO-8601: P[n][Y]) | [optional] [default to 'null']
**cover_type** | **str** | Insurance cover type. | [optional] [default to 'null']
**cover_options** | **list[str]** | List of cover options.  Valid options are: None, AccidentalDamage, HomeEmergency, LegalFees,  PersonalPossessions, Family, WaterDangerousSports. | [optional] 
**cover_area** | **str** | Geographic area over which the policy is valid. | [optional] [default to 'null']
**is_cover_note_issued** | **bool** | Policy cover notes issued flag. | [optional] [default to False]
**excess** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**sum_insured** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**buildings** | [**BuildingContentsInsuranceValue**](BuildingContentsInsuranceValue.md) |  | [optional] 
**contents** | [**BuildingContentsInsuranceValue**](BuildingContentsInsuranceValue.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

