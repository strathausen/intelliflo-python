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

class EquityRef(object):
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
        'id': 'str',
        'name': 'str',
        'codes': 'EquityCodes'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'codes': 'codes'
    }

    def __init__(self, id=None, name=None, codes=None):  # noqa: E501
        """EquityRef - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._codes = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if codes is not None:
            self.codes = codes

    @property
    def id(self):
        """Gets the id of this EquityRef.  # noqa: E501

        Equity Id eg. E1234  # noqa: E501

        :return: The id of this EquityRef.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EquityRef.

        Equity Id eg. E1234  # noqa: E501

        :param id: The id of this EquityRef.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this EquityRef.  # noqa: E501

        Equity name  # noqa: E501

        :return: The name of this EquityRef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EquityRef.

        Equity name  # noqa: E501

        :param name: The name of this EquityRef.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def codes(self):
        """Gets the codes of this EquityRef.  # noqa: E501


        :return: The codes of this EquityRef.  # noqa: E501
        :rtype: EquityCodes
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        """Sets the codes of this EquityRef.


        :param codes: The codes of this EquityRef.  # noqa: E501
        :type: EquityCodes
        """

        self._codes = codes

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
        if issubclass(EquityRef, dict):
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
        if not isinstance(other, EquityRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
