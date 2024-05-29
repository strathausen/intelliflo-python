# BenefitsPayableValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefit_frequency** | **str** | How often Benefit payments are made. | [optional] [default to 'Single']
**benefit_period** | [**BenefitPeriodValue**](BenefitPeriodValue.md) |  | [optional] 
**benefit_amount** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**deferred_period** | **str** | Period between going off work and your income payments commencing.The Period should be specified in ISO-8601 format. | [optional] 
**qualification_period** | [**QualificationPeriodValue**](QualificationPeriodValue.md) |  | [optional] 
**split_benefit_frequency** | **str** | How often Split Benefit payments are made. | [optional] 
**split_benefit_value** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**split_deferred_period** | **str** | The split deferred period specifies the time between when the Deferred period payments commence and the subsequent Split Deferred payments commence.Duration in ISO-8601 format (P[n][YMD]). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

