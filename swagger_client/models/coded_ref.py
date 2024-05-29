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

class CodedRef(object):
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
        'code': 'str',
        'href': 'str'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'href': 'href'
    }

    def __init__(self, id=None, code=None, href=None):  # noqa: E501
        """CodedRef - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._code = None
        self._href = None
        self.discriminator = None
        self.id = id
        if code is not None:
            self.code = code
        if href is not None:
            self.href = href

    @property
    def id(self):
        """Gets the id of this CodedRef.  # noqa: E501

        Model unique identifier.  # noqa: E501

        :return: The id of this CodedRef.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CodedRef.

        Model unique identifier.  # noqa: E501

        :param id: The id of this CodedRef.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def code(self):
        """Gets the code of this CodedRef.  # noqa: E501

        Model code.  # noqa: E501

        :return: The code of this CodedRef.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CodedRef.

        Model code.  # noqa: E501

        :param code: The code of this CodedRef.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def href(self):
        """Gets the href of this CodedRef.  # noqa: E501

        Model hypermedia link.  # noqa: E501

        :return: The href of this CodedRef.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CodedRef.

        Model hypermedia link.  # noqa: E501

        :param href: The href of this CodedRef.  # noqa: E501
        :type: str
        """

        self._href = href

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
        if issubclass(CodedRef, dict):
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
        if not isinstance(other, CodedRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
