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

class BasePortfolioModelFundRef(object):
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
        'allocation': 'float'
    }

    attribute_map = {
        'name': 'name',
        'allocation': 'allocation'
    }

    def __init__(self, name=None, allocation=None):  # noqa: E501
        """BasePortfolioModelFundRef - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._allocation = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if allocation is not None:
            self.allocation = allocation

    @property
    def name(self):
        """Gets the name of this BasePortfolioModelFundRef.  # noqa: E501

        The fund name.  # noqa: E501

        :return: The name of this BasePortfolioModelFundRef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BasePortfolioModelFundRef.

        The fund name.  # noqa: E501

        :param name: The name of this BasePortfolioModelFundRef.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def allocation(self):
        """Gets the allocation of this BasePortfolioModelFundRef.  # noqa: E501

        The fund allocation.  # noqa: E501

        :return: The allocation of this BasePortfolioModelFundRef.  # noqa: E501
        :rtype: float
        """
        return self._allocation

    @allocation.setter
    def allocation(self, allocation):
        """Sets the allocation of this BasePortfolioModelFundRef.

        The fund allocation.  # noqa: E501

        :param allocation: The allocation of this BasePortfolioModelFundRef.  # noqa: E501
        :type: float
        """

        self._allocation = allocation

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
        if issubclass(BasePortfolioModelFundRef, dict):
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
        if not isinstance(other, BasePortfolioModelFundRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
