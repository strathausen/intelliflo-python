# BaseEmployment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**starts_on** | **datetime** | Start Date of the employment | [optional] 
**ends_on** | **datetime** | End Date of the employment | [optional] 
**occupation** | **str** | Description of the occupation of the employment | [optional] [default to 'null']
**intended_retirement_age** | **int** | Intended Retirement Age | [optional] 
**employer** | **str** | Employer&#x27;s name. | [optional] [default to 'null']
**address** | [**EmploymentAddressValue**](EmploymentAddressValue.md) |  | [optional] 
**employment_business_type** | **str** | Employment Business type, settable for business types: Sole Trader, Private Limited Company, Partnership, Limited Liability Partnership | [optional] [default to 'null']
**in_probation** | **bool** | In Probation flag, settable for statuses: Employed, MaternityLeave, LongTermIllness | [optional] [default to False]
**probation_period_in_months** | **int** | Settable when InProbation is set to &#x27;true&#x27; and for statuses: Employed, MaternityLeave, LongTermIllness | [optional] 
**client** | [**ClientRef**](ClientRef.md) |  | [optional] 
**incomes_href** | **str** | Incomes reference | [optional] 
**industry_type** | **str** | IndustryType. | [optional] [default to 'null']
**employment_status_description** | **str** | Employment Status Description. | [optional] [default to 'null']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

