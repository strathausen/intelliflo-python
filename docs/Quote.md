# Quote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Quote unique identifier. | [optional] 
**href** | **str** | URI for given quote. | [optional] 
**reference** | **str** | Auto-generated Intelliflo reference number. | [optional] 
**created_user** | [**NamedUserRef**](NamedUserRef.md) |  | [optional] 
**created_app** | [**NamedAppRef**](NamedAppRef.md) |  | [optional] 
**created_at** | **datetime** | Quote created date. | [optional] 
**custom_reference** | **str** | Quote free text reference. | [optional] 
**contains_bundle** | **bool** | Indicates whether the quote expects multiple results grouped by bundle reference. | [optional] [default to False]
**status** | **str** | The current status of the quote.  One of &#x27;Initiated&#x27;, &#x27;Submitted&#x27;, &#x27;Failed&#x27;, &#x27;Expired&#x27;, &#x27;Complete&#x27;. | [optional] [default to 'Initiated']
**product_group** | **str** | Product group for the quote. | [optional] 
**applicants** | [**list[PartyRef]**](PartyRef.md) | Applicants the quote was requested for. Applicant at index 0 is the primary applicant. | [optional] 
**quote_results_href** | **str** | Quote results hypermedia link. | [optional] 
**documents_href** | **str** | Documents hypermedia link. | [optional] 
**originating_quote** | [**OriginatingQuoteRef**](OriginatingQuoteRef.md) |  | [optional] 
**attributes** | **object** | Additional quote attributes as key value pairs. | [optional] 
**service_case** | [**QuotationServiceCaseReference**](QuotationServiceCaseReference.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

