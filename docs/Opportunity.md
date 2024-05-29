# Opportunity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the Opportunity. | [optional] 
**href** | **str** | Resource link for this Opportunity. | [optional] 
**status** | [**OpportunityStatusRef**](OpportunityStatusRef.md) |  | [optional] 
**type** | [**OpportunityTypeRef**](OpportunityTypeRef.md) |  | 
**prospects** | [**list[PartyNamedRef]**](PartyNamedRef.md) | Array of the Client/Lead references linked to the Opportunity. The first entry in the array is treated as the primary Prospect. if there is a secondary prospect it will be the second entry in the array. | 
**adviser** | [**NamedAdviserRef**](NamedAdviserRef.md) |  | [optional] 
**potential_initial_income** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**potential_ongoing_income** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**asset_value** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**proposition** | [**OpportunityPropositionRef**](OpportunityPropositionRef.md) |  | [optional] 
**campaign** | [**OpportunityCampaignValue**](OpportunityCampaignValue.md) |  | [optional] 
**reference** | **str** | The reference for the Opportunity. | [optional] 
**service_case** | [**ServiceCaseRef**](ServiceCaseRef.md) |  | [optional] 
**created_on** | **datetime** | The date the Opportunity was created. | 
**created_by** | [**NamedUserReference**](NamedUserReference.md) |  | [optional] 
**target_closure_on** | **datetime** | The targeted date for closure of the Opportunity. | [optional] 
**is_closed** | **bool** | Flag indicating if the Opportunity has been closed. | [optional] 
**closed_date** | **datetime** | The date the Opportunity was or will closed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

