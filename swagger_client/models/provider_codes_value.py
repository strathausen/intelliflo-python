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

class ProviderCodesValue(object):
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
        'code1': 'str',
        'code2': 'str',
        'code3': 'str'
    }

    attribute_map = {
        'code1': 'code1',
        'code2': 'code2',
        'code3': 'code3'
    }

    def __init__(self, code1='null', code2='null', code3='null'):  # noqa: E501
        """ProviderCodesValue - a model defined in Swagger"""  # noqa: E501
        self._code1 = None
        self._code2 = None
        self._code3 = None
        self.discriminator = None
        if code1 is not None:
            self.code1 = code1
        if code2 is not None:
            self.code2 = code2
        if code3 is not None:
            self.code3 = code3

    @property
    def code1(self):
        """Gets the code1 of this ProviderCodesValue.  # noqa: E501

        Provider code1.  # noqa: E501

        :return: The code1 of this ProviderCodesValue.  # noqa: E501
        :rtype: str
        """
        return self._code1

    @code1.setter
    def code1(self, code1):
        """Sets the code1 of this ProviderCodesValue.

        Provider code1.  # noqa: E501

        :param code1: The code1 of this ProviderCodesValue.  # noqa: E501
        :type: str
        """

        self._code1 = code1

    @property
    def code2(self):
        """Gets the code2 of this ProviderCodesValue.  # noqa: E501

        Provider code2.  # noqa: E501

        :return: The code2 of this ProviderCodesValue.  # noqa: E501
        :rtype: str
        """
        return self._code2

    @code2.setter
    def code2(self, code2):
        """Sets the code2 of this ProviderCodesValue.

        Provider code2.  # noqa: E501

        :param code2: The code2 of this ProviderCodesValue.  # noqa: E501
        :type: str
        """

        self._code2 = code2

    @property
    def code3(self):
        """Gets the code3 of this ProviderCodesValue.  # noqa: E501

        Provider code3.  # noqa: E501

        :return: The code3 of this ProviderCodesValue.  # noqa: E501
        :rtype: str
        """
        return self._code3

    @code3.setter
    def code3(self, code3):
        """Sets the code3 of this ProviderCodesValue.

        Provider code3.  # noqa: E501

        :param code3: The code3 of this ProviderCodesValue.  # noqa: E501
        :type: str
        """

        self._code3 = code3

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
        if issubclass(ProviderCodesValue, dict):
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
        if not isinstance(other, ProviderCodesValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
