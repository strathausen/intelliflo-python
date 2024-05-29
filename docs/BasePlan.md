# BasePlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**currency** | **str** | Optional three-letter ISO 4217 alphabetic currency code. If different from the default currency | [optional] [default to 'null']
**exchange_rate** | [**CurrencyRef**](CurrencyRef.md) |  | [optional] 
**discriminator** | **str** |  | 
**plan_type** | [**PlanTypeRef**](PlanTypeRef.md) |  | 
**policy_number** | **str** | Unique reference number to the Client&#x27;s Plan as issued by the Platform Provider. | [optional] [default to 'null']
**starts_on** | **datetime** | Policy Start Date of the plan (when it has been placed \&quot;in force\&quot;). | [optional] 
**ends_on** | **datetime** | Policy End Date of the plan (if it has one). | [optional] 
**product_name** | **str** | Optional name which would usually be the market name of the product. | [optional] [default to 'null']
**product_provider** | [**NamedProductProviderRef**](NamedProductProviderRef.md) |  | 
**selling_adviser** | [**AdviserRef**](AdviserRef.md) |  | 
**owners** | [**list[PlanOwnerRef]**](PlanOwnerRef.md) | Each plan can have one or more owners. The Client could be purchasing the product on behalf of someone else. | 
**is_visible_to_client** | **bool** | Indicates whether or not the plan is visible to the client. | [optional] 
**current_status** | **str** | Indicates whether or not the plan is currently marked as \&quot;In force\&quot;. | [optional] [default to 'null']
**system_status** | **str** | System name of the plan status. | [optional] 
**is_pre_existing** | **bool** | The Client has an existing plan which pre-dates their association with this Adviser firm. | [optional] [default to False]
**reference** | **str** | Internally assigned IO plan reference - generated at plan creation. | [optional] 
**latest_valuation** | [**PlanValuation**](PlanValuation.md) |  | [optional] 
**plan_types_href** | **str** |  | [optional] 
**valuations_href** | **str** |  | [optional] 
**contributions_href** | **str** |  | [optional] 
**topups_href** | **str** |  | [optional] 
**plan_holdings_href** | **str** |  | [optional] 
**lifecycle** | [**NamedLifecycleRef**](NamedLifecycleRef.md) |  | 
**is_topup** | **bool** | Does the plan represent a TopUp of a Parent/Master plan? | [optional] 
**parent** | [**PlanRef**](PlanRef.md) |  | [optional] 
**is_sub_plan** | **bool** | Returns true if the plan is part of a wrapper (has a parent plan). | [optional] 
**is_advice_off_panel** | **bool** | Is the Adviser recommending a product which is outside of their regulated sphere?  This would be considered \&quot;Off-panel\&quot; advice. Only assignable on POST. | [optional] [default to False]
**other_references** | [**PlanReferences**](PlanReferences.md) |  | [optional] 
**client_category** | **str** | The categorisation of a client defines the level of protection to which they are entitled based upon their experience, knowledge and expertise in making financial decisions.  There are three areas of business which these categories will cover: Retail, which contains the categories of Retail, Professional and Eligible Counterparty;  Mortgage, which will contain the categories of Customer and Large Business Customer; and Insurance, which will cover Client (Consumer) and Commercial Client (Commercial Customer). | [optional] [default to 'null']
**available_plan_purposes_href** | **str** |  | [optional] 
**plan_purposes_href** | **str** |  | [optional] 
**withdrawals_href** | **str** |  | [optional] 
**sub_plans_href** | **str** |  | [optional] 
**is_client_suitable_for_target_market** | **bool** | Is the Adviser happy that the Client, to whom this product is being sold, belongs to the target market as defined by the product provider? | [optional] [default to False]
**quote_result** | [**QuoteResultRef**](QuoteResultRef.md) |  | [optional] 
**banding** | [**PlanBandingRef**](PlanBandingRef.md) |  | [optional] 
**forward_income_to** | [**ForwardIncomeToRef**](ForwardIncomeToRef.md) |  | [optional] 
**administrator** | [**UserRef2**](UserRef2.md) |  | [optional] 
**paraplanner** | [**UserRef2**](UserRef2.md) |  | [optional] 
**advice_status** | [**AdviceStatusValue**](AdviceStatusValue.md) |  | [optional] 
**tags** | **list[str]** | Client Tags. | [optional] 
**group** | [**GroupRef**](GroupRef.md) |  | [optional] 
**created_by** | [**UserRef2**](UserRef2.md) |  | [optional] 
**document_delivery** | [**DocumentDeliveryValue**](DocumentDeliveryValue.md) |  | [optional] 
**is_provider_managed** | **bool** | Indicates if the plan is managed by the Provider.  Can only be set under tenant reach or system reach, and not set at all for topups operations. | [optional] [default to False]
**performance_starts_on** | **datetime** | Portfolio analysis start date. | [optional] 
**performance_ends_on** | **datetime** | Portfolio analysis end date. | [optional] 
**provider_codes** | [**ProviderCodesValue**](ProviderCodesValue.md) |  | [optional] 
**created_at** | **datetime** | CreatedAt date and time | [optional] 
**program** | [**ProgramNamedRef**](ProgramNamedRef.md) |  | [optional] 
**risk_profile** | [**RiskProfileRef**](RiskProfileRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

