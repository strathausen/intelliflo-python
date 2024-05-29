# PlanBeneficiary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Beneficiary unique identifier. | [optional] 
**last_updated_on** | **datetime** | Updated date | [optional] 
**percentage** | **float** | Optional, range: 0-100 | [optional] 
**discriminator** | **str** | Beneficiary discriminator  Readonly, returns according to the endpoint | [optional] 
**type** | **str** | Beneficiary type  Optional, defaults to &#x27;Primary&#x27; | [optional] 
**is_per_stirpes** | **bool** | Optional | [optional] 
**beneficiary_of** | [**BeneficiaryOfRef**](BeneficiaryOfRef.md) |  | [optional] 
**subject** | [**BeneficiarySubject**](BeneficiarySubject.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

