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

class FundProposalHoldingValue(object):
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
        'fund': 'FundRef',
        'equity': 'EquityRef',
        'percentage_of_lumpsum': 'float',
        'percentage_of_recurring': 'float'
    }

    attribute_map = {
        'fund': 'fund',
        'equity': 'equity',
        'percentage_of_lumpsum': 'percentageOfLumpsum',
        'percentage_of_recurring': 'percentageOfRecurring'
    }

    def __init__(self, fund=None, equity=None, percentage_of_lumpsum=0.0, percentage_of_recurring=0.0):  # noqa: E501
        """FundProposalHoldingValue - a model defined in Swagger"""  # noqa: E501
        self._fund = None
        self._equity = None
        self._percentage_of_lumpsum = None
        self._percentage_of_recurring = None
        self.discriminator = None
        if fund is not None:
            self.fund = fund
        if equity is not None:
            self.equity = equity
        if percentage_of_lumpsum is not None:
            self.percentage_of_lumpsum = percentage_of_lumpsum
        if percentage_of_recurring is not None:
            self.percentage_of_recurring = percentage_of_recurring

    @property
    def fund(self):
        """Gets the fund of this FundProposalHoldingValue.  # noqa: E501


        :return: The fund of this FundProposalHoldingValue.  # noqa: E501
        :rtype: FundRef
        """
        return self._fund

    @fund.setter
    def fund(self, fund):
        """Sets the fund of this FundProposalHoldingValue.


        :param fund: The fund of this FundProposalHoldingValue.  # noqa: E501
        :type: FundRef
        """

        self._fund = fund

    @property
    def equity(self):
        """Gets the equity of this FundProposalHoldingValue.  # noqa: E501


        :return: The equity of this FundProposalHoldingValue.  # noqa: E501
        :rtype: EquityRef
        """
        return self._equity

    @equity.setter
    def equity(self, equity):
        """Sets the equity of this FundProposalHoldingValue.


        :param equity: The equity of this FundProposalHoldingValue.  # noqa: E501
        :type: EquityRef
        """

        self._equity = equity

    @property
    def percentage_of_lumpsum(self):
        """Gets the percentage_of_lumpsum of this FundProposalHoldingValue.  # noqa: E501

        Percentage of Lumpsum  # noqa: E501

        :return: The percentage_of_lumpsum of this FundProposalHoldingValue.  # noqa: E501
        :rtype: float
        """
        return self._percentage_of_lumpsum

    @percentage_of_lumpsum.setter
    def percentage_of_lumpsum(self, percentage_of_lumpsum):
        """Sets the percentage_of_lumpsum of this FundProposalHoldingValue.

        Percentage of Lumpsum  # noqa: E501

        :param percentage_of_lumpsum: The percentage_of_lumpsum of this FundProposalHoldingValue.  # noqa: E501
        :type: float
        """

        self._percentage_of_lumpsum = percentage_of_lumpsum

    @property
    def percentage_of_recurring(self):
        """Gets the percentage_of_recurring of this FundProposalHoldingValue.  # noqa: E501

        Percentage of recurring  # noqa: E501

        :return: The percentage_of_recurring of this FundProposalHoldingValue.  # noqa: E501
        :rtype: float
        """
        return self._percentage_of_recurring

    @percentage_of_recurring.setter
    def percentage_of_recurring(self, percentage_of_recurring):
        """Sets the percentage_of_recurring of this FundProposalHoldingValue.

        Percentage of recurring  # noqa: E501

        :param percentage_of_recurring: The percentage_of_recurring of this FundProposalHoldingValue.  # noqa: E501
        :type: float
        """

        self._percentage_of_recurring = percentage_of_recurring

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
        if issubclass(FundProposalHoldingValue, dict):
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
        if not isinstance(other, FundProposalHoldingValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
