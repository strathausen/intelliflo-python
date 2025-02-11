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

class AdviceTemplateSolutionStepFee(object):
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
        'show_fee': 'bool'
    }

    attribute_map = {
        'show_fee': 'showFee'
    }

    def __init__(self, show_fee=None):  # noqa: E501
        """AdviceTemplateSolutionStepFee - a model defined in Swagger"""  # noqa: E501
        self._show_fee = None
        self.discriminator = None
        if show_fee is not None:
            self.show_fee = show_fee

    @property
    def show_fee(self):
        """Gets the show_fee of this AdviceTemplateSolutionStepFee.  # noqa: E501

        flag for showing fee section in Solution step  # noqa: E501

        :return: The show_fee of this AdviceTemplateSolutionStepFee.  # noqa: E501
        :rtype: bool
        """
        return self._show_fee

    @show_fee.setter
    def show_fee(self, show_fee):
        """Sets the show_fee of this AdviceTemplateSolutionStepFee.

        flag for showing fee section in Solution step  # noqa: E501

        :param show_fee: The show_fee of this AdviceTemplateSolutionStepFee.  # noqa: E501
        :type: bool
        """

        self._show_fee = show_fee

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
        if issubclass(AdviceTemplateSolutionStepFee, dict):
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
        if not isinstance(other, AdviceTemplateSolutionStepFee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
