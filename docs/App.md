# App

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**name** | **str** |  | 
**content** | **dict(str, str)** | Content, this is a collection of content that is available to the app. Current supported content values are icon, video_01, img_01, img_02, img_03. Example: ...apps/{appId}/content/icon | [optional] 
**description** | **str** |  | [optional] 
**categories** | **list[str]** |  | [optional] 
**publisher** | **str** |  | [optional] 
**published_targets** | [**list[AppPublishedTargetValue]**](AppPublishedTargetValue.md) |  | [optional] 
**is_approved_for_install** | **bool** |  | [optional] 
**is_approved_by_group** | **bool** |  | [optional] 
**summary** | **str** |  | [optional] 
**last_updated_at** | **datetime** |  | [optional] 
**last_published_at** | **datetime** |  | [optional] 
**publish_requested_at** | **datetime** |  | [optional] 
**metadata** | **str** |  | [optional] 
**collaborators** | [**list[AppCollaborator]**](AppCollaborator.md) |  | [optional] 
**billing_model** | [**AppBillingModelValue2**](AppBillingModelValue2.md) |  | [optional] 
**app_claims** | **dict(str, str)** |  | [optional] 
**secrets** | [**AppSecrets**](AppSecrets.md) |  | [optional] 
**terms_and_conditions_href** | **str** |  | [optional] 
**required_scopes** | **list[str]** |  | [optional] 
**approved_scopes** | **list[str]** |  | [optional] 
**version** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

