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

class DpaPolicyAgreementResponseValue(object):
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
        'text': 'str',
        'accepted': 'bool'
    }

    attribute_map = {
        'text': 'text',
        'accepted': 'accepted'
    }

    def __init__(self, text=None, accepted=None):  # noqa: E501
        """DpaPolicyAgreementResponseValue - a model defined in Swagger"""  # noqa: E501
        self._text = None
        self._accepted = None
        self.discriminator = None
        if text is not None:
            self.text = text
        self.accepted = accepted

    @property
    def text(self):
        """Gets the text of this DpaPolicyAgreementResponseValue.  # noqa: E501

        DPA policy agreement response text  # noqa: E501

        :return: The text of this DpaPolicyAgreementResponseValue.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this DpaPolicyAgreementResponseValue.

        DPA policy agreement response text  # noqa: E501

        :param text: The text of this DpaPolicyAgreementResponseValue.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def accepted(self):
        """Gets the accepted of this DpaPolicyAgreementResponseValue.  # noqa: E501

        DPA policy agreement response answer  # noqa: E501

        :return: The accepted of this DpaPolicyAgreementResponseValue.  # noqa: E501
        :rtype: bool
        """
        return self._accepted

    @accepted.setter
    def accepted(self, accepted):
        """Sets the accepted of this DpaPolicyAgreementResponseValue.

        DPA policy agreement response answer  # noqa: E501

        :param accepted: The accepted of this DpaPolicyAgreementResponseValue.  # noqa: E501
        :type: bool
        """
        if accepted is None:
            raise ValueError("Invalid value for `accepted`, must not be `None`")  # noqa: E501

        self._accepted = accepted

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
        if issubclass(DpaPolicyAgreementResponseValue, dict):
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
        if not isinstance(other, DpaPolicyAgreementResponseValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
