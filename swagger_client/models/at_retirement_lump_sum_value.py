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

class AtRetirementLumpSumValue(object):
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
        'amount': 'CurrencyValue',
        'percentage': 'float'
    }

    attribute_map = {
        'amount': 'amount',
        'percentage': 'percentage'
    }

    def __init__(self, amount=None, percentage=None):  # noqa: E501
        """AtRetirementLumpSumValue - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._percentage = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if percentage is not None:
            self.percentage = percentage

    @property
    def amount(self):
        """Gets the amount of this AtRetirementLumpSumValue.  # noqa: E501


        :return: The amount of this AtRetirementLumpSumValue.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AtRetirementLumpSumValue.


        :param amount: The amount of this AtRetirementLumpSumValue.  # noqa: E501
        :type: CurrencyValue
        """

        self._amount = amount

    @property
    def percentage(self):
        """Gets the percentage of this AtRetirementLumpSumValue.  # noqa: E501

        Percentage of lump sum at retirement.  # noqa: E501

        :return: The percentage of this AtRetirementLumpSumValue.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this AtRetirementLumpSumValue.

        Percentage of lump sum at retirement.  # noqa: E501

        :param percentage: The percentage of this AtRetirementLumpSumValue.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

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
        if issubclass(AtRetirementLumpSumValue, dict):
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
        if not isinstance(other, AtRetirementLumpSumValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
