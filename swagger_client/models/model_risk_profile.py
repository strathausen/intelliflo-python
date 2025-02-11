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

class ModelRiskProfile(object):
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
        'risk_profile_ref': 'RiskProfileRef',
        'group_ref': 'GroupRef'
    }

    attribute_map = {
        'risk_profile_ref': 'riskProfileRef',
        'group_ref': 'groupRef'
    }

    def __init__(self, risk_profile_ref=None, group_ref=None):  # noqa: E501
        """ModelRiskProfile - a model defined in Swagger"""  # noqa: E501
        self._risk_profile_ref = None
        self._group_ref = None
        self.discriminator = None
        if risk_profile_ref is not None:
            self.risk_profile_ref = risk_profile_ref
        if group_ref is not None:
            self.group_ref = group_ref

    @property
    def risk_profile_ref(self):
        """Gets the risk_profile_ref of this ModelRiskProfile.  # noqa: E501


        :return: The risk_profile_ref of this ModelRiskProfile.  # noqa: E501
        :rtype: RiskProfileRef
        """
        return self._risk_profile_ref

    @risk_profile_ref.setter
    def risk_profile_ref(self, risk_profile_ref):
        """Sets the risk_profile_ref of this ModelRiskProfile.


        :param risk_profile_ref: The risk_profile_ref of this ModelRiskProfile.  # noqa: E501
        :type: RiskProfileRef
        """

        self._risk_profile_ref = risk_profile_ref

    @property
    def group_ref(self):
        """Gets the group_ref of this ModelRiskProfile.  # noqa: E501


        :return: The group_ref of this ModelRiskProfile.  # noqa: E501
        :rtype: GroupRef
        """
        return self._group_ref

    @group_ref.setter
    def group_ref(self, group_ref):
        """Sets the group_ref of this ModelRiskProfile.


        :param group_ref: The group_ref of this ModelRiskProfile.  # noqa: E501
        :type: GroupRef
        """

        self._group_ref = group_ref

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
        if issubclass(ModelRiskProfile, dict):
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
        if not isinstance(other, ModelRiskProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
