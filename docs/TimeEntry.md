# TimeEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**client** | [**NamedClientRef**](NamedClientRef.md) |  | [optional] 
**category** | **str** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**elapsed_seconds** | **int** |  | [optional] 
**hourly_billing_rate** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**is_all_day** | **bool** |  | [optional] 
**notes** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**tenant** | [**TenantReference**](TenantReference.md) |  | [optional] 
**owner** | [**NamedUserRef**](NamedUserRef.md) |  | [optional] 
**billable_total** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**is_chargeable** | **bool** |  | [optional] 
**task** | [**TaskRef**](TaskRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

