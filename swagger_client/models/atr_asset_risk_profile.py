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

class AtrAssetRiskProfile(object):
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
        'risk_profile': 'str',
        'asset_allocations': 'list[AtrAssetAllocation]'
    }

    attribute_map = {
        'risk_profile': 'riskProfile',
        'asset_allocations': 'assetAllocations'
    }

    def __init__(self, risk_profile=None, asset_allocations=None):  # noqa: E501
        """AtrAssetRiskProfile - a model defined in Swagger"""  # noqa: E501
        self._risk_profile = None
        self._asset_allocations = None
        self.discriminator = None
        self.risk_profile = risk_profile
        self.asset_allocations = asset_allocations

    @property
    def risk_profile(self):
        """Gets the risk_profile of this AtrAssetRiskProfile.  # noqa: E501

        Risk profile.  # noqa: E501

        :return: The risk_profile of this AtrAssetRiskProfile.  # noqa: E501
        :rtype: str
        """
        return self._risk_profile

    @risk_profile.setter
    def risk_profile(self, risk_profile):
        """Sets the risk_profile of this AtrAssetRiskProfile.

        Risk profile.  # noqa: E501

        :param risk_profile: The risk_profile of this AtrAssetRiskProfile.  # noqa: E501
        :type: str
        """
        if risk_profile is None:
            raise ValueError("Invalid value for `risk_profile`, must not be `None`")  # noqa: E501

        self._risk_profile = risk_profile

    @property
    def asset_allocations(self):
        """Gets the asset_allocations of this AtrAssetRiskProfile.  # noqa: E501

        Asset allocations.  # noqa: E501

        :return: The asset_allocations of this AtrAssetRiskProfile.  # noqa: E501
        :rtype: list[AtrAssetAllocation]
        """
        return self._asset_allocations

    @asset_allocations.setter
    def asset_allocations(self, asset_allocations):
        """Sets the asset_allocations of this AtrAssetRiskProfile.

        Asset allocations.  # noqa: E501

        :param asset_allocations: The asset_allocations of this AtrAssetRiskProfile.  # noqa: E501
        :type: list[AtrAssetAllocation]
        """
        if asset_allocations is None:
            raise ValueError("Invalid value for `asset_allocations`, must not be `None`")  # noqa: E501

        self._asset_allocations = asset_allocations

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
        if issubclass(AtrAssetRiskProfile, dict):
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
        if not isinstance(other, AtrAssetRiskProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
