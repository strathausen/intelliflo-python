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

class AdviceTemplateNewBusinessProposalType(object):
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
        'types': 'list[str]',
        'plan_types': 'list[NamedPlanTypeRef]',
        'life_cycle': 'NamedLifecycleRef',
        'investment_strategy': 'AdviceTemplateInvestmentStrategy'
    }

    attribute_map = {
        'types': 'types',
        'plan_types': 'planTypes',
        'life_cycle': 'lifeCycle',
        'investment_strategy': 'investmentStrategy'
    }

    def __init__(self, types=None, plan_types=None, life_cycle=None, investment_strategy=None):  # noqa: E501
        """AdviceTemplateNewBusinessProposalType - a model defined in Swagger"""  # noqa: E501
        self._types = None
        self._plan_types = None
        self._life_cycle = None
        self._investment_strategy = None
        self.discriminator = None
        self.types = types
        if plan_types is not None:
            self.plan_types = plan_types
        if life_cycle is not None:
            self.life_cycle = life_cycle
        if investment_strategy is not None:
            self.investment_strategy = investment_strategy

    @property
    def types(self):
        """Gets the types of this AdviceTemplateNewBusinessProposalType.  # noqa: E501

        New business proposal types.  # noqa: E501

        :return: The types of this AdviceTemplateNewBusinessProposalType.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this AdviceTemplateNewBusinessProposalType.

        New business proposal types.  # noqa: E501

        :param types: The types of this AdviceTemplateNewBusinessProposalType.  # noqa: E501
        :type: list[str]
        """
        if types is None:
            raise ValueError("Invalid value for `types`, must not be `None`")  # noqa: E501
        allowed_values = ["Investment", "Pension", "Annuity", "PersonalProtection", "Mortgage", "EquityRelease", "GeneralInsurance"]  # noqa: E501
        if not set(types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._types = types

    @property
    def plan_types(self):
        """Gets the plan_types of this AdviceTemplateNewBusinessProposalType.  # noqa: E501

        List of supported plan types.  # noqa: E501

        :return: The plan_types of this AdviceTemplateNewBusinessProposalType.  # noqa: E501
        :rtype: list[NamedPlanTypeRef]
        """
        return self._plan_types

    @plan_types.setter
    def plan_types(self, plan_types):
        """Sets the plan_types of this AdviceTemplateNewBusinessProposalType.

        List of supported plan types.  # noqa: E501

        :param plan_types: The plan_types of this AdviceTemplateNewBusinessProposalType.  # noqa: E501
        :type: list[NamedPlanTypeRef]
        """

        self._plan_types = plan_types

    @property
    def life_cycle(self):
        """Gets the life_cycle of this AdviceTemplateNewBusinessProposalType.  # noqa: E501


        :return: The life_cycle of this AdviceTemplateNewBusinessProposalType.  # noqa: E501
        :rtype: NamedLifecycleRef
        """
        return self._life_cycle

    @life_cycle.setter
    def life_cycle(self, life_cycle):
        """Sets the life_cycle of this AdviceTemplateNewBusinessProposalType.


        :param life_cycle: The life_cycle of this AdviceTemplateNewBusinessProposalType.  # noqa: E501
        :type: NamedLifecycleRef
        """

        self._life_cycle = life_cycle

    @property
    def investment_strategy(self):
        """Gets the investment_strategy of this AdviceTemplateNewBusinessProposalType.  # noqa: E501


        :return: The investment_strategy of this AdviceTemplateNewBusinessProposalType.  # noqa: E501
        :rtype: AdviceTemplateInvestmentStrategy
        """
        return self._investment_strategy

    @investment_strategy.setter
    def investment_strategy(self, investment_strategy):
        """Sets the investment_strategy of this AdviceTemplateNewBusinessProposalType.


        :param investment_strategy: The investment_strategy of this AdviceTemplateNewBusinessProposalType.  # noqa: E501
        :type: AdviceTemplateInvestmentStrategy
        """

        self._investment_strategy = investment_strategy

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
        if issubclass(AdviceTemplateNewBusinessProposalType, dict):
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
        if not isinstance(other, AdviceTemplateNewBusinessProposalType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
