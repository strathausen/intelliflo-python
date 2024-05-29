# FeeDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_charging_type** | **str** | Fee charging type | 
**name** | **str** | Fee charging type name | [optional] 
**min_fee** | [**Value**](Value.md) |  | [optional] 
**max_fee** | [**Value**](Value.md) |  | [optional] 
**min_percentage** | **float** | Required if fee is percentage based. Value has to be exact match of the value that is set for the fee type within IO.  Contact your IO tenant administrator to get information about available fee charging options. | [optional] 
**max_percentage** | **float** | Required if fee is percentage based. Value has to be exact match of the value that is set for the fee type within IO.  Contact your IO tenant administrator to get information about available fee charging options. | [optional] 
**is_plan_fee** | **bool** |  | [optional] 
**is_regular_contribution_fee** | **bool** |  | [optional] 
**is_lump_sum_contribution_fee** | **bool** |  | [optional] 
**is_transfer_fee** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

