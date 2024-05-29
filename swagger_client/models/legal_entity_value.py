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

class LegalEntityValue(object):
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
        'identifier': 'str',
        'expires_on': 'datetime'
    }

    attribute_map = {
        'identifier': 'identifier',
        'expires_on': 'expiresOn'
    }

    def __init__(self, identifier=None, expires_on=None):  # noqa: E501
        """LegalEntityValue - a model defined in Swagger"""  # noqa: E501
        self._identifier = None
        self._expires_on = None
        self.discriminator = None
        if identifier is not None:
            self.identifier = identifier
        if expires_on is not None:
            self.expires_on = expires_on

    @property
    def identifier(self):
        """Gets the identifier of this LegalEntityValue.  # noqa: E501

        Legal entity identifier.  # noqa: E501

        :return: The identifier of this LegalEntityValue.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this LegalEntityValue.

        Legal entity identifier.  # noqa: E501

        :param identifier: The identifier of this LegalEntityValue.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def expires_on(self):
        """Gets the expires_on of this LegalEntityValue.  # noqa: E501

        Expiry date of legal identifier.  # noqa: E501

        :return: The expires_on of this LegalEntityValue.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_on

    @expires_on.setter
    def expires_on(self, expires_on):
        """Sets the expires_on of this LegalEntityValue.

        Expiry date of legal identifier.  # noqa: E501

        :param expires_on: The expires_on of this LegalEntityValue.  # noqa: E501
        :type: datetime
        """

        self._expires_on = expires_on

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
        if issubclass(LegalEntityValue, dict):
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
        if not isinstance(other, LegalEntityValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
