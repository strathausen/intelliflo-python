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

class ModelAtrValue(object):
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
        'code': 'str',
        'description': 'str'
    }

    attribute_map = {
        'code': 'code',
        'description': 'description'
    }

    def __init__(self, code=None, description=None):  # noqa: E501
        """ModelAtrValue - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._description = None
        self.discriminator = None
        self.code = code
        self.description = description

    @property
    def code(self):
        """Gets the code of this ModelAtrValue.  # noqa: E501

        A code that identifies the Attitude to risk.  An ATR reference is made up of a code (key) and description (value)  The code/key will use a naming convention [A - Z]{3}-[%.,+0-z]{1,3}(-T[0 - 9]{0,3}|)  (providername abbreviation)-(risk)-[T(term)]  # noqa: E501

        :return: The code of this ModelAtrValue.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ModelAtrValue.

        A code that identifies the Attitude to risk.  An ATR reference is made up of a code (key) and description (value)  The code/key will use a naming convention [A - Z]{3}-[%.,+0-z]{1,3}(-T[0 - 9]{0,3}|)  (providername abbreviation)-(risk)-[T(term)]  # noqa: E501

        :param code: The code of this ModelAtrValue.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def description(self):
        """Gets the description of this ModelAtrValue.  # noqa: E501

        Description of the ATR  # noqa: E501

        :return: The description of this ModelAtrValue.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelAtrValue.

        Description of the ATR  # noqa: E501

        :param description: The description of this ModelAtrValue.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

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
        if issubclass(ModelAtrValue, dict):
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
        if not isinstance(other, ModelAtrValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
