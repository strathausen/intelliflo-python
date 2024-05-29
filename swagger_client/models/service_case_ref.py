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

class ServiceCaseRef(object):
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
        'id': 'int',
        'reference': 'str'
    }

    attribute_map = {
        'id': 'id',
        'reference': 'reference'
    }

    def __init__(self, id=None, reference=None):  # noqa: E501
        """ServiceCaseRef - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._reference = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if reference is not None:
            self.reference = reference

    @property
    def id(self):
        """Gets the id of this ServiceCaseRef.  # noqa: E501

        The unique Id  of the Service Case  # noqa: E501

        :return: The id of this ServiceCaseRef.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServiceCaseRef.

        The unique Id  of the Service Case  # noqa: E501

        :param id: The id of this ServiceCaseRef.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def reference(self):
        """Gets the reference of this ServiceCaseRef.  # noqa: E501

        The Service Case reference  # noqa: E501

        :return: The reference of this ServiceCaseRef.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ServiceCaseRef.

        The Service Case reference  # noqa: E501

        :param reference: The reference of this ServiceCaseRef.  # noqa: E501
        :type: str
        """

        self._reference = reference

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
        if issubclass(ServiceCaseRef, dict):
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
        if not isinstance(other, ServiceCaseRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
