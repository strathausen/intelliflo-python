# FeeDocument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**sequential_ref** | **str** | Auto-generated reference number | [optional] 
**selling_adviser** | [**AdviserRef**](AdviserRef.md) |  | 
**advice_category** | **str** | Advice category | 
**fee_type** | [**FeeTypeRef**](FeeTypeRef.md) |  | 
**payment_type** | [**PaymentTypeRef**](PaymentTypeRef.md) |  | 
**fee_charging_type** | [**FeeChargingTypeRef**](FeeChargingTypeRef.md) |  | [optional] 
**fee_percentage** | **float** | Fee percentage | [optional] [default to 0.0]
**net** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**vat** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**vat_rate** | [**VatRateValue**](VatRateValue.md) |  | [optional] 
**status** | **str** | Fee status | [optional] [default to 'null']
**status_date** | **datetime** |  | [optional] 
**recurring** | [**FeeRecurring**](FeeRecurring.md) |  | [optional] 
**initial_period** | **int** | Initial period in months (only applicable to initial fees) | [optional] 
**is_consultancy_fee** | **bool** | Is the fee a consultancy fee? | [optional] [default to False]
**instalment** | [**Instalment**](Instalment.md) |  | [optional] 
**sent_to_client_on** | **datetime** |  | [optional] 
**discount** | [**DiscountValue**](DiscountValue.md) |  | [optional] 
**banding** | [**BandingRef**](BandingRef.md) |  | [optional] 
**forward_income_to** | [**ForwardIncomeToRef**](ForwardIncomeToRef.md) |  | [optional] 
**clients** | [**list[ClientRef]**](ClientRef.md) |  | [optional] 
**plan_href** | **str** |  | [optional] 
**plans** | [**list[PlanRef]**](PlanRef.md) |  | [optional] 
**is_retainer** | **bool** | Indicates a retainer fee (only applicable when the Advice category is N\\A). | [optional] [default to False]
**fee_model** | [**FeeModelRef**](FeeModelRef.md) |  | [optional] 
**tierings** | [**list[FeeTiering]**](FeeTiering.md) | Fee tiering | [optional] 
**fee_detail** | [**FeeDetail**](FeeDetail.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

