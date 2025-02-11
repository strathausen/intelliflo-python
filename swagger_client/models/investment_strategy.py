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

class InvestmentStrategy(object):
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
        'previous_funds': 'list[CurrentFundValue]',
        'proposed_funds': 'list[ProposedFundValue2]',
        'current_model': 'ModelPortfolioReference',
        'target_model': 'ModelPortfolioReference'
    }

    attribute_map = {
        'previous_funds': 'previousFunds',
        'proposed_funds': 'proposedFunds',
        'current_model': 'currentModel',
        'target_model': 'targetModel'
    }

    def __init__(self, previous_funds=None, proposed_funds=None, current_model=None, target_model=None):  # noqa: E501
        """InvestmentStrategy - a model defined in Swagger"""  # noqa: E501
        self._previous_funds = None
        self._proposed_funds = None
        self._current_model = None
        self._target_model = None
        self.discriminator = None
        if previous_funds is not None:
            self.previous_funds = previous_funds
        if proposed_funds is not None:
            self.proposed_funds = proposed_funds
        if current_model is not None:
            self.current_model = current_model
        if target_model is not None:
            self.target_model = target_model

    @property
    def previous_funds(self):
        """Gets the previous_funds of this InvestmentStrategy.  # noqa: E501

        Current funds for the switch.  # noqa: E501

        :return: The previous_funds of this InvestmentStrategy.  # noqa: E501
        :rtype: list[CurrentFundValue]
        """
        return self._previous_funds

    @previous_funds.setter
    def previous_funds(self, previous_funds):
        """Sets the previous_funds of this InvestmentStrategy.

        Current funds for the switch.  # noqa: E501

        :param previous_funds: The previous_funds of this InvestmentStrategy.  # noqa: E501
        :type: list[CurrentFundValue]
        """

        self._previous_funds = previous_funds

    @property
    def proposed_funds(self):
        """Gets the proposed_funds of this InvestmentStrategy.  # noqa: E501

        Proposed funds for the switch.  # noqa: E501

        :return: The proposed_funds of this InvestmentStrategy.  # noqa: E501
        :rtype: list[ProposedFundValue2]
        """
        return self._proposed_funds

    @proposed_funds.setter
    def proposed_funds(self, proposed_funds):
        """Sets the proposed_funds of this InvestmentStrategy.

        Proposed funds for the switch.  # noqa: E501

        :param proposed_funds: The proposed_funds of this InvestmentStrategy.  # noqa: E501
        :type: list[ProposedFundValue2]
        """

        self._proposed_funds = proposed_funds

    @property
    def current_model(self):
        """Gets the current_model of this InvestmentStrategy.  # noqa: E501


        :return: The current_model of this InvestmentStrategy.  # noqa: E501
        :rtype: ModelPortfolioReference
        """
        return self._current_model

    @current_model.setter
    def current_model(self, current_model):
        """Sets the current_model of this InvestmentStrategy.


        :param current_model: The current_model of this InvestmentStrategy.  # noqa: E501
        :type: ModelPortfolioReference
        """

        self._current_model = current_model

    @property
    def target_model(self):
        """Gets the target_model of this InvestmentStrategy.  # noqa: E501


        :return: The target_model of this InvestmentStrategy.  # noqa: E501
        :rtype: ModelPortfolioReference
        """
        return self._target_model

    @target_model.setter
    def target_model(self, target_model):
        """Sets the target_model of this InvestmentStrategy.


        :param target_model: The target_model of this InvestmentStrategy.  # noqa: E501
        :type: ModelPortfolioReference
        """

        self._target_model = target_model

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
        if issubclass(InvestmentStrategy, dict):
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
        if not isinstance(other, InvestmentStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
