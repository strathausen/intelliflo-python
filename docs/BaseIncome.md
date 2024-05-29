# BaseIncome

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of Income. | [optional] 
**href** | **str** | Income Href. | [optional] 
**category** | **str** | Category of Income. | 
**description** | **str** | Income Description. | [optional] [default to 'null']
**frequency** | **str** | Income Frequency. | 
**gross** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**gross_description** | **str** | Gross Income Amount Description. | [optional] [default to 'null']
**net** | [**CurrencyValue**](CurrencyValue.md) |  | [optional] 
**client** | [**ClientRef**](ClientRef.md) |  | [optional] 
**starts_on** | **datetime** | Start Date of the income (not settable for employment income). | [optional] 
**ends_on** | **datetime** | End Date of the income (not settable for employment income). | [optional] 
**last_updated** | **datetime** | Last Updated date of income. | [optional] 
**joint_client** | [**ClientRef**](ClientRef.md) |  | [optional] 
**withdrawal** | [**WithdrawalRef**](WithdrawalRef.md) |  | [optional] 
**owners** | [**list[ClientRef]**](ClientRef.md) | List Of Owners for income. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

