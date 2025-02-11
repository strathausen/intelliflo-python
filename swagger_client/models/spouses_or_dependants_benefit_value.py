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

class SpousesOrDependantsBenefitValue(object):
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
        'percentage': 'float',
        'is_with_over_lap': 'bool'
    }

    attribute_map = {
        'percentage': 'percentage',
        'is_with_over_lap': 'isWithOverLap'
    }

    def __init__(self, percentage=None, is_with_over_lap=False):  # noqa: E501
        """SpousesOrDependantsBenefitValue - a model defined in Swagger"""  # noqa: E501
        self._percentage = None
        self._is_with_over_lap = None
        self.discriminator = None
        if percentage is not None:
            self.percentage = percentage
        if is_with_over_lap is not None:
            self.is_with_over_lap = is_with_over_lap

    @property
    def percentage(self):
        """Gets the percentage of this SpousesOrDependantsBenefitValue.  # noqa: E501


        :return: The percentage of this SpousesOrDependantsBenefitValue.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this SpousesOrDependantsBenefitValue.


        :param percentage: The percentage of this SpousesOrDependantsBenefitValue.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def is_with_over_lap(self):
        """Gets the is_with_over_lap of this SpousesOrDependantsBenefitValue.  # noqa: E501


        :return: The is_with_over_lap of this SpousesOrDependantsBenefitValue.  # noqa: E501
        :rtype: bool
        """
        return self._is_with_over_lap

    @is_with_over_lap.setter
    def is_with_over_lap(self, is_with_over_lap):
        """Sets the is_with_over_lap of this SpousesOrDependantsBenefitValue.


        :param is_with_over_lap: The is_with_over_lap of this SpousesOrDependantsBenefitValue.  # noqa: E501
        :type: bool
        """

        self._is_with_over_lap = is_with_over_lap

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
        if issubclass(SpousesOrDependantsBenefitValue, dict):
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
        if not isinstance(other, SpousesOrDependantsBenefitValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
