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

class DiscountValue(object):
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
        'name': 'str',
        'percentage': 'float',
        'total': 'CurrencyValue'
    }

    attribute_map = {
        'name': 'name',
        'percentage': 'percentage',
        'total': 'total'
    }

    def __init__(self, name=None, percentage=None, total=None):  # noqa: E501
        """DiscountValue - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._percentage = None
        self._total = None
        self.discriminator = None
        self.name = name
        if percentage is not None:
            self.percentage = percentage
        if total is not None:
            self.total = total

    @property
    def name(self):
        """Gets the name of this DiscountValue.  # noqa: E501

        Discount name  # noqa: E501

        :return: The name of this DiscountValue.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DiscountValue.

        Discount name  # noqa: E501

        :param name: The name of this DiscountValue.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def percentage(self):
        """Gets the percentage of this DiscountValue.  # noqa: E501

        Discount percentage  # noqa: E501

        :return: The percentage of this DiscountValue.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this DiscountValue.

        Discount percentage  # noqa: E501

        :param percentage: The percentage of this DiscountValue.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def total(self):
        """Gets the total of this DiscountValue.  # noqa: E501


        :return: The total of this DiscountValue.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this DiscountValue.


        :param total: The total of this DiscountValue.  # noqa: E501
        :type: CurrencyValue
        """

        self._total = total

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
        if issubclass(DiscountValue, dict):
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
        if not isinstance(other, DiscountValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
