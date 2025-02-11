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

class AdviceTemplateInvestmentStrategy(object):
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
        'allowed_fund_sources': 'list[str]',
        'allow_withdrawals': 'bool',
        'apply_risk_tolerance': 'bool',
        'allow_sum_of_holdings_to_be_zero': 'bool'
    }

    attribute_map = {
        'allowed_fund_sources': 'allowedFundSources',
        'allow_withdrawals': 'allowWithdrawals',
        'apply_risk_tolerance': 'applyRiskTolerance',
        'allow_sum_of_holdings_to_be_zero': 'allowSumOfHoldingsToBeZero'
    }

    def __init__(self, allowed_fund_sources=None, allow_withdrawals=None, apply_risk_tolerance=None, allow_sum_of_holdings_to_be_zero=None):  # noqa: E501
        """AdviceTemplateInvestmentStrategy - a model defined in Swagger"""  # noqa: E501
        self._allowed_fund_sources = None
        self._allow_withdrawals = None
        self._apply_risk_tolerance = None
        self._allow_sum_of_holdings_to_be_zero = None
        self.discriminator = None
        self.allowed_fund_sources = allowed_fund_sources
        if allow_withdrawals is not None:
            self.allow_withdrawals = allow_withdrawals
        if apply_risk_tolerance is not None:
            self.apply_risk_tolerance = apply_risk_tolerance
        if allow_sum_of_holdings_to_be_zero is not None:
            self.allow_sum_of_holdings_to_be_zero = allow_sum_of_holdings_to_be_zero

    @property
    def allowed_fund_sources(self):
        """Gets the allowed_fund_sources of this AdviceTemplateInvestmentStrategy.  # noqa: E501

        List of allowed fund sources for investment strategy.  # noqa: E501

        :return: The allowed_fund_sources of this AdviceTemplateInvestmentStrategy.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_fund_sources

    @allowed_fund_sources.setter
    def allowed_fund_sources(self, allowed_fund_sources):
        """Sets the allowed_fund_sources of this AdviceTemplateInvestmentStrategy.

        List of allowed fund sources for investment strategy.  # noqa: E501

        :param allowed_fund_sources: The allowed_fund_sources of this AdviceTemplateInvestmentStrategy.  # noqa: E501
        :type: list[str]
        """
        if allowed_fund_sources is None:
            raise ValueError("Invalid value for `allowed_fund_sources`, must not be `None`")  # noqa: E501
        allowed_values = ["Models", "SecurityLists", "FundPanel", "NoRestriction"]  # noqa: E501
        if not set(allowed_fund_sources).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `allowed_fund_sources` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(allowed_fund_sources) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._allowed_fund_sources = allowed_fund_sources

    @property
    def allow_withdrawals(self):
        """Gets the allow_withdrawals of this AdviceTemplateInvestmentStrategy.  # noqa: E501

        Withdrawal section would be shown for relevant products.  # noqa: E501

        :return: The allow_withdrawals of this AdviceTemplateInvestmentStrategy.  # noqa: E501
        :rtype: bool
        """
        return self._allow_withdrawals

    @allow_withdrawals.setter
    def allow_withdrawals(self, allow_withdrawals):
        """Sets the allow_withdrawals of this AdviceTemplateInvestmentStrategy.

        Withdrawal section would be shown for relevant products.  # noqa: E501

        :param allow_withdrawals: The allow_withdrawals of this AdviceTemplateInvestmentStrategy.  # noqa: E501
        :type: bool
        """

        self._allow_withdrawals = allow_withdrawals

    @property
    def apply_risk_tolerance(self):
        """Gets the apply_risk_tolerance of this AdviceTemplateInvestmentStrategy.  # noqa: E501

        Apply risk Tolerance - if ticked the investment strategy will consider the tolerance for the selection of the investment funds.  # noqa: E501

        :return: The apply_risk_tolerance of this AdviceTemplateInvestmentStrategy.  # noqa: E501
        :rtype: bool
        """
        return self._apply_risk_tolerance

    @apply_risk_tolerance.setter
    def apply_risk_tolerance(self, apply_risk_tolerance):
        """Sets the apply_risk_tolerance of this AdviceTemplateInvestmentStrategy.

        Apply risk Tolerance - if ticked the investment strategy will consider the tolerance for the selection of the investment funds.  # noqa: E501

        :param apply_risk_tolerance: The apply_risk_tolerance of this AdviceTemplateInvestmentStrategy.  # noqa: E501
        :type: bool
        """

        self._apply_risk_tolerance = apply_risk_tolerance

    @property
    def allow_sum_of_holdings_to_be_zero(self):
        """Gets the allow_sum_of_holdings_to_be_zero of this AdviceTemplateInvestmentStrategy.  # noqa: E501

        Allow Saving Investment Strategy when sum of Holdings for Selected Securities is equal to '0'.  # noqa: E501

        :return: The allow_sum_of_holdings_to_be_zero of this AdviceTemplateInvestmentStrategy.  # noqa: E501
        :rtype: bool
        """
        return self._allow_sum_of_holdings_to_be_zero

    @allow_sum_of_holdings_to_be_zero.setter
    def allow_sum_of_holdings_to_be_zero(self, allow_sum_of_holdings_to_be_zero):
        """Sets the allow_sum_of_holdings_to_be_zero of this AdviceTemplateInvestmentStrategy.

        Allow Saving Investment Strategy when sum of Holdings for Selected Securities is equal to '0'.  # noqa: E501

        :param allow_sum_of_holdings_to_be_zero: The allow_sum_of_holdings_to_be_zero of this AdviceTemplateInvestmentStrategy.  # noqa: E501
        :type: bool
        """

        self._allow_sum_of_holdings_to_be_zero = allow_sum_of_holdings_to_be_zero

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
        if issubclass(AdviceTemplateInvestmentStrategy, dict):
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
        if not isinstance(other, AdviceTemplateInvestmentStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
