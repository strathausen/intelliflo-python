# NewBusinessAnnuityProposal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**premiums** | [**list[ProposedContributionValue]**](ProposedContributionValue.md) | Contributions for the new business plan.  ContributionReference should be null for new business. | [optional] 
**pension_income** | [**list[ProposedWithdrawalValue]**](ProposedWithdrawalValue.md) | Proposed Pension Income (withdrawal for the annuity).  WithdrawalReference should be null for new business. | [optional] 
**proposed_funds** | [**list[ProposedFundValue2]**](ProposedFundValue2.md) | Proposed funds for the annuity plan. | [optional] 
**target_model** | [**ModelPortfolioReference**](ModelPortfolioReference.md) |  | [optional] 
**annuity_payment_type** | **str** | Annuity Payment type. | [optional] [default to 'None']
**new_business_plan** | [**NewBusinessPlanValue**](NewBusinessPlanValue.md) |  | [optional] 
**currency** | **str** | ISO 4217 Currency code for the proposal. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

