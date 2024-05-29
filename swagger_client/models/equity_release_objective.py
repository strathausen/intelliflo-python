# coding: utf-8

"""
    public-v2-prd-gb-01

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2016-08-19T00:00:00Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.base_objective import BaseObjective  # noqa: F401,E501

class EquityReleaseObjective(BaseObjective):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'equity_release_type': 'EquityReleaseTypeValue',
        'monthly_income': 'CurrencyValue',
        'ownership_sold': 'float',
        'lumpsum': 'CurrencyValue',
        'equity': 'CurrencyValue',
        'loan': 'CurrencyValue',
        'term': 'MortgageRequirementTermValue',
        'loan_to_value': 'float',
        'repayment_method': 'RepaymentMethodValue',
        'capital_repayment': 'CurrencyValue',
        'interest_only_repayment': 'CurrencyValue',
        'property_valuation': 'CurrencyValue',
        'interest_only_repayment_vehicle': 'str',
        'guarantor': 'GuarantorValue',
        'debt_consolidation': 'DebtConsolidationValue',
        'current_provider': 'NamedProductProviderRef',
        'property_address': 'NamedPropertyAddressRef'
    }
    if hasattr(BaseObjective, "swagger_types"):
        swagger_types.update(BaseObjective.swagger_types)

    attribute_map = {
        'equity_release_type': 'equityReleaseType',
        'monthly_income': 'monthlyIncome',
        'ownership_sold': 'ownershipSold',
        'lumpsum': 'lumpsum',
        'equity': 'equity',
        'loan': 'loan',
        'term': 'term',
        'loan_to_value': 'loanToValue',
        'repayment_method': 'repaymentMethod',
        'capital_repayment': 'capitalRepayment',
        'interest_only_repayment': 'interestOnlyRepayment',
        'property_valuation': 'propertyValuation',
        'interest_only_repayment_vehicle': 'interestOnlyRepaymentVehicle',
        'guarantor': 'guarantor',
        'debt_consolidation': 'debtConsolidation',
        'current_provider': 'currentProvider',
        'property_address': 'propertyAddress'
    }
    if hasattr(BaseObjective, "attribute_map"):
        attribute_map.update(BaseObjective.attribute_map)

    def __init__(self, equity_release_type=None, monthly_income=None, ownership_sold=None, lumpsum=None, equity=None, loan=None, term=None, loan_to_value=None, repayment_method=None, capital_repayment=None, interest_only_repayment=None, property_valuation=None, interest_only_repayment_vehicle=None, guarantor=None, debt_consolidation=None, current_provider=None, property_address=None, *args, **kwargs):  # noqa: E501
        """EquityReleaseObjective - a model defined in Swagger"""  # noqa: E501
        self._equity_release_type = None
        self._monthly_income = None
        self._ownership_sold = None
        self._lumpsum = None
        self._equity = None
        self._loan = None
        self._term = None
        self._loan_to_value = None
        self._repayment_method = None
        self._capital_repayment = None
        self._interest_only_repayment = None
        self._property_valuation = None
        self._interest_only_repayment_vehicle = None
        self._guarantor = None
        self._debt_consolidation = None
        self._current_provider = None
        self._property_address = None
        self.discriminator = None
        if equity_release_type is not None:
            self.equity_release_type = equity_release_type
        if monthly_income is not None:
            self.monthly_income = monthly_income
        if ownership_sold is not None:
            self.ownership_sold = ownership_sold
        if lumpsum is not None:
            self.lumpsum = lumpsum
        if equity is not None:
            self.equity = equity
        if loan is not None:
            self.loan = loan
        if term is not None:
            self.term = term
        if loan_to_value is not None:
            self.loan_to_value = loan_to_value
        if repayment_method is not None:
            self.repayment_method = repayment_method
        if capital_repayment is not None:
            self.capital_repayment = capital_repayment
        if interest_only_repayment is not None:
            self.interest_only_repayment = interest_only_repayment
        if property_valuation is not None:
            self.property_valuation = property_valuation
        if interest_only_repayment_vehicle is not None:
            self.interest_only_repayment_vehicle = interest_only_repayment_vehicle
        if guarantor is not None:
            self.guarantor = guarantor
        if debt_consolidation is not None:
            self.debt_consolidation = debt_consolidation
        if current_provider is not None:
            self.current_provider = current_provider
        if property_address is not None:
            self.property_address = property_address
        BaseObjective.__init__(self, *args, **kwargs)

    @property
    def equity_release_type(self):
        """Gets the equity_release_type of this EquityReleaseObjective.  # noqa: E501


        :return: The equity_release_type of this EquityReleaseObjective.  # noqa: E501
        :rtype: EquityReleaseTypeValue
        """
        return self._equity_release_type

    @equity_release_type.setter
    def equity_release_type(self, equity_release_type):
        """Sets the equity_release_type of this EquityReleaseObjective.


        :param equity_release_type: The equity_release_type of this EquityReleaseObjective.  # noqa: E501
        :type: EquityReleaseTypeValue
        """

        self._equity_release_type = equity_release_type

    @property
    def monthly_income(self):
        """Gets the monthly_income of this EquityReleaseObjective.  # noqa: E501


        :return: The monthly_income of this EquityReleaseObjective.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._monthly_income

    @monthly_income.setter
    def monthly_income(self, monthly_income):
        """Sets the monthly_income of this EquityReleaseObjective.


        :param monthly_income: The monthly_income of this EquityReleaseObjective.  # noqa: E501
        :type: CurrencyValue
        """

        self._monthly_income = monthly_income

    @property
    def ownership_sold(self):
        """Gets the ownership_sold of this EquityReleaseObjective.  # noqa: E501

        Percentage of ownership sold.  # noqa: E501

        :return: The ownership_sold of this EquityReleaseObjective.  # noqa: E501
        :rtype: float
        """
        return self._ownership_sold

    @ownership_sold.setter
    def ownership_sold(self, ownership_sold):
        """Sets the ownership_sold of this EquityReleaseObjective.

        Percentage of ownership sold.  # noqa: E501

        :param ownership_sold: The ownership_sold of this EquityReleaseObjective.  # noqa: E501
        :type: float
        """

        self._ownership_sold = ownership_sold

    @property
    def lumpsum(self):
        """Gets the lumpsum of this EquityReleaseObjective.  # noqa: E501


        :return: The lumpsum of this EquityReleaseObjective.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._lumpsum

    @lumpsum.setter
    def lumpsum(self, lumpsum):
        """Sets the lumpsum of this EquityReleaseObjective.


        :param lumpsum: The lumpsum of this EquityReleaseObjective.  # noqa: E501
        :type: CurrencyValue
        """

        self._lumpsum = lumpsum

    @property
    def equity(self):
        """Gets the equity of this EquityReleaseObjective.  # noqa: E501


        :return: The equity of this EquityReleaseObjective.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._equity

    @equity.setter
    def equity(self, equity):
        """Sets the equity of this EquityReleaseObjective.


        :param equity: The equity of this EquityReleaseObjective.  # noqa: E501
        :type: CurrencyValue
        """

        self._equity = equity

    @property
    def loan(self):
        """Gets the loan of this EquityReleaseObjective.  # noqa: E501


        :return: The loan of this EquityReleaseObjective.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._loan

    @loan.setter
    def loan(self, loan):
        """Sets the loan of this EquityReleaseObjective.


        :param loan: The loan of this EquityReleaseObjective.  # noqa: E501
        :type: CurrencyValue
        """

        self._loan = loan

    @property
    def term(self):
        """Gets the term of this EquityReleaseObjective.  # noqa: E501


        :return: The term of this EquityReleaseObjective.  # noqa: E501
        :rtype: MortgageRequirementTermValue
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this EquityReleaseObjective.


        :param term: The term of this EquityReleaseObjective.  # noqa: E501
        :type: MortgageRequirementTermValue
        """

        self._term = term

    @property
    def loan_to_value(self):
        """Gets the loan_to_value of this EquityReleaseObjective.  # noqa: E501

        loan to value percentage.  # noqa: E501

        :return: The loan_to_value of this EquityReleaseObjective.  # noqa: E501
        :rtype: float
        """
        return self._loan_to_value

    @loan_to_value.setter
    def loan_to_value(self, loan_to_value):
        """Sets the loan_to_value of this EquityReleaseObjective.

        loan to value percentage.  # noqa: E501

        :param loan_to_value: The loan_to_value of this EquityReleaseObjective.  # noqa: E501
        :type: float
        """

        self._loan_to_value = loan_to_value

    @property
    def repayment_method(self):
        """Gets the repayment_method of this EquityReleaseObjective.  # noqa: E501


        :return: The repayment_method of this EquityReleaseObjective.  # noqa: E501
        :rtype: RepaymentMethodValue
        """
        return self._repayment_method

    @repayment_method.setter
    def repayment_method(self, repayment_method):
        """Sets the repayment_method of this EquityReleaseObjective.


        :param repayment_method: The repayment_method of this EquityReleaseObjective.  # noqa: E501
        :type: RepaymentMethodValue
        """

        self._repayment_method = repayment_method

    @property
    def capital_repayment(self):
        """Gets the capital_repayment of this EquityReleaseObjective.  # noqa: E501


        :return: The capital_repayment of this EquityReleaseObjective.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._capital_repayment

    @capital_repayment.setter
    def capital_repayment(self, capital_repayment):
        """Sets the capital_repayment of this EquityReleaseObjective.


        :param capital_repayment: The capital_repayment of this EquityReleaseObjective.  # noqa: E501
        :type: CurrencyValue
        """

        self._capital_repayment = capital_repayment

    @property
    def interest_only_repayment(self):
        """Gets the interest_only_repayment of this EquityReleaseObjective.  # noqa: E501


        :return: The interest_only_repayment of this EquityReleaseObjective.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._interest_only_repayment

    @interest_only_repayment.setter
    def interest_only_repayment(self, interest_only_repayment):
        """Sets the interest_only_repayment of this EquityReleaseObjective.


        :param interest_only_repayment: The interest_only_repayment of this EquityReleaseObjective.  # noqa: E501
        :type: CurrencyValue
        """

        self._interest_only_repayment = interest_only_repayment

    @property
    def property_valuation(self):
        """Gets the property_valuation of this EquityReleaseObjective.  # noqa: E501


        :return: The property_valuation of this EquityReleaseObjective.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._property_valuation

    @property_valuation.setter
    def property_valuation(self, property_valuation):
        """Sets the property_valuation of this EquityReleaseObjective.


        :param property_valuation: The property_valuation of this EquityReleaseObjective.  # noqa: E501
        :type: CurrencyValue
        """

        self._property_valuation = property_valuation

    @property
    def interest_only_repayment_vehicle(self):
        """Gets the interest_only_repayment_vehicle of this EquityReleaseObjective.  # noqa: E501

        Interest only repayment vehicle.  # noqa: E501

        :return: The interest_only_repayment_vehicle of this EquityReleaseObjective.  # noqa: E501
        :rtype: str
        """
        return self._interest_only_repayment_vehicle

    @interest_only_repayment_vehicle.setter
    def interest_only_repayment_vehicle(self, interest_only_repayment_vehicle):
        """Sets the interest_only_repayment_vehicle of this EquityReleaseObjective.

        Interest only repayment vehicle.  # noqa: E501

        :param interest_only_repayment_vehicle: The interest_only_repayment_vehicle of this EquityReleaseObjective.  # noqa: E501
        :type: str
        """

        self._interest_only_repayment_vehicle = interest_only_repayment_vehicle

    @property
    def guarantor(self):
        """Gets the guarantor of this EquityReleaseObjective.  # noqa: E501


        :return: The guarantor of this EquityReleaseObjective.  # noqa: E501
        :rtype: GuarantorValue
        """
        return self._guarantor

    @guarantor.setter
    def guarantor(self, guarantor):
        """Sets the guarantor of this EquityReleaseObjective.


        :param guarantor: The guarantor of this EquityReleaseObjective.  # noqa: E501
        :type: GuarantorValue
        """

        self._guarantor = guarantor

    @property
    def debt_consolidation(self):
        """Gets the debt_consolidation of this EquityReleaseObjective.  # noqa: E501


        :return: The debt_consolidation of this EquityReleaseObjective.  # noqa: E501
        :rtype: DebtConsolidationValue
        """
        return self._debt_consolidation

    @debt_consolidation.setter
    def debt_consolidation(self, debt_consolidation):
        """Sets the debt_consolidation of this EquityReleaseObjective.


        :param debt_consolidation: The debt_consolidation of this EquityReleaseObjective.  # noqa: E501
        :type: DebtConsolidationValue
        """

        self._debt_consolidation = debt_consolidation

    @property
    def current_provider(self):
        """Gets the current_provider of this EquityReleaseObjective.  # noqa: E501


        :return: The current_provider of this EquityReleaseObjective.  # noqa: E501
        :rtype: NamedProductProviderRef
        """
        return self._current_provider

    @current_provider.setter
    def current_provider(self, current_provider):
        """Sets the current_provider of this EquityReleaseObjective.


        :param current_provider: The current_provider of this EquityReleaseObjective.  # noqa: E501
        :type: NamedProductProviderRef
        """

        self._current_provider = current_provider

    @property
    def property_address(self):
        """Gets the property_address of this EquityReleaseObjective.  # noqa: E501


        :return: The property_address of this EquityReleaseObjective.  # noqa: E501
        :rtype: NamedPropertyAddressRef
        """
        return self._property_address

    @property_address.setter
    def property_address(self, property_address):
        """Sets the property_address of this EquityReleaseObjective.


        :param property_address: The property_address of this EquityReleaseObjective.  # noqa: E501
        :type: NamedPropertyAddressRef
        """

        self._property_address = property_address

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EquityReleaseObjective, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EquityReleaseObjective):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
