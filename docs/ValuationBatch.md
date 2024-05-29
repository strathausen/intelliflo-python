# ValuationBatch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**product_provider** | [**NamedProductProviderRef**](NamedProductProviderRef.md) |  | [optional] 
**tenant** | [**TenantRef3**](TenantRef3.md) |  | [optional] 
**planmatch_includeportalreference** | **bool** | Determines whether to include the portal reference in matching algorithm. | [optional] 
**planmatch_normalised** | **bool** | Determines whether to normalize the formats of values used in the matching algorithm. | [optional] 
**created_at** | **datetime** | Valuation batch enqueued date time | [optional] 
**state** | **str** | Current status of the valuation batch | [optional] 
**items_imported** | **int** | Number of items imported successfully | [optional] 
**items_failed** | **int** | Number of items either not matched or failed to import | [optional] 
**created_by** | [**NamedUserRef**](NamedUserRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

