# DPAPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of DPA policy | [optional] 
**href** | **str** | Hyperlink to DPA policy | [optional] 
**created_at** | **datetime** | DPA Policy creation date | [optional] 
**name** | **str** | DPA Policy name | 
**is_editable** | **bool** | This field specifies if DPA policy can be edited | [optional] 
**statements** | [**DpaPolicyStatementValues**](DpaPolicyStatementValues.md) |  | [optional] 
**tag** | **str** | DPA Policy Tag | [optional] 
**client_can_accept** | **bool** | Specifies whether DPA policy can be accepted by the clients. | [optional] 
**party_type** | **str** | DPA Party Type. If no party type is specified, the DPA is a default DPA for all party types that do not specifica DPA set. | [optional] 
**has_agreements** | **bool** | Field indicating if DPAs exist for the policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

