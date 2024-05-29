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

class Charges(object):
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
        'rate': 'float',
        'currency': 'str',
        'vat': 'str'
    }

    attribute_map = {
        'rate': 'rate',
        'currency': 'currency',
        'vat': 'vat'
    }

    def __init__(self, rate=None, currency=None, vat=None):  # noqa: E501
        """Charges - a model defined in Swagger"""  # noqa: E501
        self._rate = None
        self._currency = None
        self._vat = None
        self.discriminator = None
        if rate is not None:
            self.rate = rate
        if currency is not None:
            self.currency = currency
        if vat is not None:
            self.vat = vat

    @property
    def rate(self):
        """Gets the rate of this Charges.  # noqa: E501

        Gets or sets the rate.  # noqa: E501

        :return: The rate of this Charges.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this Charges.

        Gets or sets the rate.  # noqa: E501

        :param rate: The rate of this Charges.  # noqa: E501
        :type: float
        """

        self._rate = rate

    @property
    def currency(self):
        """Gets the currency of this Charges.  # noqa: E501

        Gets or sets the currency.  # noqa: E501

        :return: The currency of this Charges.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Charges.

        Gets or sets the currency.  # noqa: E501

        :param currency: The currency of this Charges.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def vat(self):
        """Gets the vat of this Charges.  # noqa: E501

        Gets or sets the vat.  # noqa: E501

        :return: The vat of this Charges.  # noqa: E501
        :rtype: str
        """
        return self._vat

    @vat.setter
    def vat(self, vat):
        """Sets the vat of this Charges.

        Gets or sets the vat.  # noqa: E501

        :param vat: The vat of this Charges.  # noqa: E501
        :type: str
        """
        allowed_values = ["Inclusive", "Exclusive", "NonVatable"]  # noqa: E501
        if vat not in allowed_values:
            raise ValueError(
                "Invalid value for `vat` ({0}), must be one of {1}"  # noqa: E501
                .format(vat, allowed_values)
            )

        self._vat = vat

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
        if issubclass(Charges, dict):
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
        if not isinstance(other, Charges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
