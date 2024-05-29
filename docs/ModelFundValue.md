# ModelFundValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of this fund | 
**allocation** | **float** | The recommended percentage allocation of this fund. Should be a value between 0.00 and 100.00. The sum of allocations must equal 100. | [optional] [default to 0.0]
**currency_code** | **str** | The Currency Code for the fund. 3 letter currency code (ISO 4217: GBP) | 
**fund_code_type** | **str** | The Type of instrument code used to identify the Fund.  Note that for feed funds, the underlying fund must have an ISIN code to generate references to KIID documents,  so the preferred codeType value for funds is &#x27;isin&#x27;.  You can use other code types to upload the model but KIID documents can only be referenced if the underlying feed fund has an ISIN code. | 
**code** | **str** | The instrument code for this fund | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

