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

class NationalityCountryValue(object):
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
        'iso_code': 'str'
    }

    attribute_map = {
        'name': 'name',
        'iso_code': 'isoCode'
    }

    def __init__(self, name=None, iso_code=None):  # noqa: E501
        """NationalityCountryValue - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._iso_code = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if iso_code is not None:
            self.iso_code = iso_code

    @property
    def name(self):
        """Gets the name of this NationalityCountryValue.  # noqa: E501

        The countries name. This is derived from the IsoCode.  # noqa: E501

        :return: The name of this NationalityCountryValue.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NationalityCountryValue.

        The countries name. This is derived from the IsoCode.  # noqa: E501

        :param name: The name of this NationalityCountryValue.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def iso_code(self):
        """Gets the iso_code of this NationalityCountryValue.  # noqa: E501

        The ISO country code (ISO 3166-1 alpha-3) for the country.  If this IsoCode is provided during creation or update of the Client or Lead, the Nationality  property on the Person will be set according to the value of this IsoCode property.  # noqa: E501

        :return: The iso_code of this NationalityCountryValue.  # noqa: E501
        :rtype: str
        """
        return self._iso_code

    @iso_code.setter
    def iso_code(self, iso_code):
        """Sets the iso_code of this NationalityCountryValue.

        The ISO country code (ISO 3166-1 alpha-3) for the country.  If this IsoCode is provided during creation or update of the Client or Lead, the Nationality  property on the Person will be set according to the value of this IsoCode property.  # noqa: E501

        :param iso_code: The iso_code of this NationalityCountryValue.  # noqa: E501
        :type: str
        """

        self._iso_code = iso_code

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
        if issubclass(NationalityCountryValue, dict):
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
        if not isinstance(other, NationalityCountryValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
