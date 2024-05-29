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

class AdditionalDetailsRef(object):
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
        'external_reference': 'str',
        'migration_reference': 'str'
    }

    attribute_map = {
        'external_reference': 'externalReference',
        'migration_reference': 'migrationReference'
    }

    def __init__(self, external_reference=None, migration_reference=None):  # noqa: E501
        """AdditionalDetailsRef - a model defined in Swagger"""  # noqa: E501
        self._external_reference = None
        self._migration_reference = None
        self.discriminator = None
        if external_reference is not None:
            self.external_reference = external_reference
        if migration_reference is not None:
            self.migration_reference = migration_reference

    @property
    def external_reference(self):
        """Gets the external_reference of this AdditionalDetailsRef.  # noqa: E501

        An external reference identifier.  # noqa: E501

        :return: The external_reference of this AdditionalDetailsRef.  # noqa: E501
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this AdditionalDetailsRef.

        An external reference identifier.  # noqa: E501

        :param external_reference: The external_reference of this AdditionalDetailsRef.  # noqa: E501
        :type: str
        """

        self._external_reference = external_reference

    @property
    def migration_reference(self):
        """Gets the migration_reference of this AdditionalDetailsRef.  # noqa: E501

        An external user identifier. Should be unique by tenant if specified.  # noqa: E501

        :return: The migration_reference of this AdditionalDetailsRef.  # noqa: E501
        :rtype: str
        """
        return self._migration_reference

    @migration_reference.setter
    def migration_reference(self, migration_reference):
        """Sets the migration_reference of this AdditionalDetailsRef.

        An external user identifier. Should be unique by tenant if specified.  # noqa: E501

        :param migration_reference: The migration_reference of this AdditionalDetailsRef.  # noqa: E501
        :type: str
        """

        self._migration_reference = migration_reference

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
        if issubclass(AdditionalDetailsRef, dict):
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
        if not isinstance(other, AdditionalDetailsRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
