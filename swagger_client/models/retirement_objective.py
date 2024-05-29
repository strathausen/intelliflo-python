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
from swagger_client.models.base_objective import BaseObjective  # noqa: F401,E501

class RetirementObjective(BaseObjective):
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
        'lump_sum': 'AtRetirementLumpSumValue',
        'income': 'RetirementIncomeValue',
        'target_age': 'int',
        'term': 'int',
        'has_investment_preference': 'str',
        'investment_preferences': 'str',
        'risk_profile': 'RiskProfileValue',
        'risk_profile_named_ref': 'RiskProfileNamedRef',
        'atr_ref': 'ATRRef',
        'investment_preference_ref': 'InvestmentPreferenceRef'
    }
    if hasattr(BaseObjective, "swagger_types"):
        swagger_types.update(BaseObjective.swagger_types)

    attribute_map = {
        'lump_sum': 'lumpSum',
        'income': 'income',
        'target_age': 'targetAge',
        'term': 'term',
        'has_investment_preference': 'hasInvestmentPreference',
        'investment_preferences': 'investmentPreferences',
        'risk_profile': 'riskProfile',
        'risk_profile_named_ref': 'riskProfileNamedRef',
        'atr_ref': 'atrRef',
        'investment_preference_ref': 'investmentPreferenceRef'
    }
    if hasattr(BaseObjective, "attribute_map"):
        attribute_map.update(BaseObjective.attribute_map)

    def __init__(self, lump_sum=None, income=None, target_age=None, term=None, has_investment_preference=None, investment_preferences=None, risk_profile=None, risk_profile_named_ref=None, atr_ref=None, investment_preference_ref=None, *args, **kwargs):  # noqa: E501
        """RetirementObjective - a model defined in Swagger"""  # noqa: E501
        self._lump_sum = None
        self._income = None
        self._target_age = None
        self._term = None
        self._has_investment_preference = None
        self._investment_preferences = None
        self._risk_profile = None
        self._risk_profile_named_ref = None
        self._atr_ref = None
        self._investment_preference_ref = None
        self.discriminator = None
        if lump_sum is not None:
            self.lump_sum = lump_sum
        if income is not None:
            self.income = income
        if target_age is not None:
            self.target_age = target_age
        if term is not None:
            self.term = term
        if has_investment_preference is not None:
            self.has_investment_preference = has_investment_preference
        if investment_preferences is not None:
            self.investment_preferences = investment_preferences
        if risk_profile is not None:
            self.risk_profile = risk_profile
        if risk_profile_named_ref is not None:
            self.risk_profile_named_ref = risk_profile_named_ref
        if atr_ref is not None:
            self.atr_ref = atr_ref
        if investment_preference_ref is not None:
            self.investment_preference_ref = investment_preference_ref
        BaseObjective.__init__(self, *args, **kwargs)

    @property
    def lump_sum(self):
        """Gets the lump_sum of this RetirementObjective.  # noqa: E501


        :return: The lump_sum of this RetirementObjective.  # noqa: E501
        :rtype: AtRetirementLumpSumValue
        """
        return self._lump_sum

    @lump_sum.setter
    def lump_sum(self, lump_sum):
        """Sets the lump_sum of this RetirementObjective.


        :param lump_sum: The lump_sum of this RetirementObjective.  # noqa: E501
        :type: AtRetirementLumpSumValue
        """

        self._lump_sum = lump_sum

    @property
    def income(self):
        """Gets the income of this RetirementObjective.  # noqa: E501


        :return: The income of this RetirementObjective.  # noqa: E501
        :rtype: RetirementIncomeValue
        """
        return self._income

    @income.setter
    def income(self, income):
        """Sets the income of this RetirementObjective.


        :param income: The income of this RetirementObjective.  # noqa: E501
        :type: RetirementIncomeValue
        """

        self._income = income

    @property
    def target_age(self):
        """Gets the target_age of this RetirementObjective.  # noqa: E501

        Target age of the retirement.  # noqa: E501

        :return: The target_age of this RetirementObjective.  # noqa: E501
        :rtype: int
        """
        return self._target_age

    @target_age.setter
    def target_age(self, target_age):
        """Sets the target_age of this RetirementObjective.

        Target age of the retirement.  # noqa: E501

        :param target_age: The target_age of this RetirementObjective.  # noqa: E501
        :type: int
        """

        self._target_age = target_age

    @property
    def term(self):
        """Gets the term of this RetirementObjective.  # noqa: E501

        Retirement term in months.  # noqa: E501

        :return: The term of this RetirementObjective.  # noqa: E501
        :rtype: int
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this RetirementObjective.

        Retirement term in months.  # noqa: E501

        :param term: The term of this RetirementObjective.  # noqa: E501
        :type: int
        """

        self._term = term

    @property
    def has_investment_preference(self):
        """Gets the has_investment_preference of this RetirementObjective.  # noqa: E501

        Has Investment Preference?  # noqa: E501

        :return: The has_investment_preference of this RetirementObjective.  # noqa: E501
        :rtype: str
        """
        return self._has_investment_preference

    @has_investment_preference.setter
    def has_investment_preference(self, has_investment_preference):
        """Sets the has_investment_preference of this RetirementObjective.

        Has Investment Preference?  # noqa: E501

        :param has_investment_preference: The has_investment_preference of this RetirementObjective.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unanswered", "Yes", "No"]  # noqa: E501
        if has_investment_preference not in allowed_values:
            raise ValueError(
                "Invalid value for `has_investment_preference` ({0}), must be one of {1}"  # noqa: E501
                .format(has_investment_preference, allowed_values)
            )

        self._has_investment_preference = has_investment_preference

    @property
    def investment_preferences(self):
        """Gets the investment_preferences of this RetirementObjective.  # noqa: E501

        Investment Preference details.  # noqa: E501

        :return: The investment_preferences of this RetirementObjective.  # noqa: E501
        :rtype: str
        """
        return self._investment_preferences

    @investment_preferences.setter
    def investment_preferences(self, investment_preferences):
        """Sets the investment_preferences of this RetirementObjective.

        Investment Preference details.  # noqa: E501

        :param investment_preferences: The investment_preferences of this RetirementObjective.  # noqa: E501
        :type: str
        """

        self._investment_preferences = investment_preferences

    @property
    def risk_profile(self):
        """Gets the risk_profile of this RetirementObjective.  # noqa: E501


        :return: The risk_profile of this RetirementObjective.  # noqa: E501
        :rtype: RiskProfileValue
        """
        return self._risk_profile

    @risk_profile.setter
    def risk_profile(self, risk_profile):
        """Sets the risk_profile of this RetirementObjective.


        :param risk_profile: The risk_profile of this RetirementObjective.  # noqa: E501
        :type: RiskProfileValue
        """

        self._risk_profile = risk_profile

    @property
    def risk_profile_named_ref(self):
        """Gets the risk_profile_named_ref of this RetirementObjective.  # noqa: E501


        :return: The risk_profile_named_ref of this RetirementObjective.  # noqa: E501
        :rtype: RiskProfileNamedRef
        """
        return self._risk_profile_named_ref

    @risk_profile_named_ref.setter
    def risk_profile_named_ref(self, risk_profile_named_ref):
        """Sets the risk_profile_named_ref of this RetirementObjective.


        :param risk_profile_named_ref: The risk_profile_named_ref of this RetirementObjective.  # noqa: E501
        :type: RiskProfileNamedRef
        """

        self._risk_profile_named_ref = risk_profile_named_ref

    @property
    def atr_ref(self):
        """Gets the atr_ref of this RetirementObjective.  # noqa: E501


        :return: The atr_ref of this RetirementObjective.  # noqa: E501
        :rtype: ATRRef
        """
        return self._atr_ref

    @atr_ref.setter
    def atr_ref(self, atr_ref):
        """Sets the atr_ref of this RetirementObjective.


        :param atr_ref: The atr_ref of this RetirementObjective.  # noqa: E501
        :type: ATRRef
        """

        self._atr_ref = atr_ref

    @property
    def investment_preference_ref(self):
        """Gets the investment_preference_ref of this RetirementObjective.  # noqa: E501


        :return: The investment_preference_ref of this RetirementObjective.  # noqa: E501
        :rtype: InvestmentPreferenceRef
        """
        return self._investment_preference_ref

    @investment_preference_ref.setter
    def investment_preference_ref(self, investment_preference_ref):
        """Sets the investment_preference_ref of this RetirementObjective.


        :param investment_preference_ref: The investment_preference_ref of this RetirementObjective.  # noqa: E501
        :type: InvestmentPreferenceRef
        """

        self._investment_preference_ref = investment_preference_ref

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
        if issubclass(RetirementObjective, dict):
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
        if not isinstance(other, RetirementObjective):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
