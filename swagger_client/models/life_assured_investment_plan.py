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
from swagger_client.models.asset_plan import AssetPlan  # noqa: F401,E501

class LifeAssuredInvestmentPlan(AssetPlan):
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
        'maturity_low_value': 'CurrencyValue',
        'maturity_medium_value': 'CurrencyValue',
        'maturity_high_value': 'CurrencyValue',
        'maturity_projection_details': 'str',
        'has_guarantee_of_original_investment': 'bool'
    }
    if hasattr(AssetPlan, "swagger_types"):
        swagger_types.update(AssetPlan.swagger_types)

    attribute_map = {
        'maturity_low_value': 'maturityLowValue',
        'maturity_medium_value': 'maturityMediumValue',
        'maturity_high_value': 'maturityHighValue',
        'maturity_projection_details': 'maturityProjectionDetails',
        'has_guarantee_of_original_investment': 'hasGuaranteeOfOriginalInvestment'
    }
    if hasattr(AssetPlan, "attribute_map"):
        attribute_map.update(AssetPlan.attribute_map)

    def __init__(self, maturity_low_value=None, maturity_medium_value=None, maturity_high_value=None, maturity_projection_details='null', has_guarantee_of_original_investment=False, *args, **kwargs):  # noqa: E501
        """LifeAssuredInvestmentPlan - a model defined in Swagger"""  # noqa: E501
        self._maturity_low_value = None
        self._maturity_medium_value = None
        self._maturity_high_value = None
        self._maturity_projection_details = None
        self._has_guarantee_of_original_investment = None
        self.discriminator = None
        if maturity_low_value is not None:
            self.maturity_low_value = maturity_low_value
        if maturity_medium_value is not None:
            self.maturity_medium_value = maturity_medium_value
        if maturity_high_value is not None:
            self.maturity_high_value = maturity_high_value
        if maturity_projection_details is not None:
            self.maturity_projection_details = maturity_projection_details
        if has_guarantee_of_original_investment is not None:
            self.has_guarantee_of_original_investment = has_guarantee_of_original_investment
        AssetPlan.__init__(self, *args, **kwargs)

    @property
    def maturity_low_value(self):
        """Gets the maturity_low_value of this LifeAssuredInvestmentPlan.  # noqa: E501


        :return: The maturity_low_value of this LifeAssuredInvestmentPlan.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._maturity_low_value

    @maturity_low_value.setter
    def maturity_low_value(self, maturity_low_value):
        """Sets the maturity_low_value of this LifeAssuredInvestmentPlan.


        :param maturity_low_value: The maturity_low_value of this LifeAssuredInvestmentPlan.  # noqa: E501
        :type: CurrencyValue
        """

        self._maturity_low_value = maturity_low_value

    @property
    def maturity_medium_value(self):
        """Gets the maturity_medium_value of this LifeAssuredInvestmentPlan.  # noqa: E501


        :return: The maturity_medium_value of this LifeAssuredInvestmentPlan.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._maturity_medium_value

    @maturity_medium_value.setter
    def maturity_medium_value(self, maturity_medium_value):
        """Sets the maturity_medium_value of this LifeAssuredInvestmentPlan.


        :param maturity_medium_value: The maturity_medium_value of this LifeAssuredInvestmentPlan.  # noqa: E501
        :type: CurrencyValue
        """

        self._maturity_medium_value = maturity_medium_value

    @property
    def maturity_high_value(self):
        """Gets the maturity_high_value of this LifeAssuredInvestmentPlan.  # noqa: E501


        :return: The maturity_high_value of this LifeAssuredInvestmentPlan.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._maturity_high_value

    @maturity_high_value.setter
    def maturity_high_value(self, maturity_high_value):
        """Sets the maturity_high_value of this LifeAssuredInvestmentPlan.


        :param maturity_high_value: The maturity_high_value of this LifeAssuredInvestmentPlan.  # noqa: E501
        :type: CurrencyValue
        """

        self._maturity_high_value = maturity_high_value

    @property
    def maturity_projection_details(self):
        """Gets the maturity_projection_details of this LifeAssuredInvestmentPlan.  # noqa: E501

        Maturity projection details.  # noqa: E501

        :return: The maturity_projection_details of this LifeAssuredInvestmentPlan.  # noqa: E501
        :rtype: str
        """
        return self._maturity_projection_details

    @maturity_projection_details.setter
    def maturity_projection_details(self, maturity_projection_details):
        """Sets the maturity_projection_details of this LifeAssuredInvestmentPlan.

        Maturity projection details.  # noqa: E501

        :param maturity_projection_details: The maturity_projection_details of this LifeAssuredInvestmentPlan.  # noqa: E501
        :type: str
        """

        self._maturity_projection_details = maturity_projection_details

    @property
    def has_guarantee_of_original_investment(self):
        """Gets the has_guarantee_of_original_investment of this LifeAssuredInvestmentPlan.  # noqa: E501

        Is the original investment amount guaranteed/protected?  # noqa: E501

        :return: The has_guarantee_of_original_investment of this LifeAssuredInvestmentPlan.  # noqa: E501
        :rtype: bool
        """
        return self._has_guarantee_of_original_investment

    @has_guarantee_of_original_investment.setter
    def has_guarantee_of_original_investment(self, has_guarantee_of_original_investment):
        """Sets the has_guarantee_of_original_investment of this LifeAssuredInvestmentPlan.

        Is the original investment amount guaranteed/protected?  # noqa: E501

        :param has_guarantee_of_original_investment: The has_guarantee_of_original_investment of this LifeAssuredInvestmentPlan.  # noqa: E501
        :type: bool
        """

        self._has_guarantee_of_original_investment = has_guarantee_of_original_investment

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
        if issubclass(LifeAssuredInvestmentPlan, dict):
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
        if not isinstance(other, LifeAssuredInvestmentPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
