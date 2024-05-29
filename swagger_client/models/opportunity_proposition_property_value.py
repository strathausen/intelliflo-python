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

class OpportunityPropositionPropertyValue(object):
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
        'is_archived': 'bool',
        'opportunity_types': 'list[OpportunityTypeValue]',
        'plan_types': 'list[PlanTypeWithRegionValue]'
    }

    attribute_map = {
        'is_archived': 'isArchived',
        'opportunity_types': 'opportunityTypes',
        'plan_types': 'planTypes'
    }

    def __init__(self, is_archived=False, opportunity_types=None, plan_types=None):  # noqa: E501
        """OpportunityPropositionPropertyValue - a model defined in Swagger"""  # noqa: E501
        self._is_archived = None
        self._opportunity_types = None
        self._plan_types = None
        self.discriminator = None
        if is_archived is not None:
            self.is_archived = is_archived
        if opportunity_types is not None:
            self.opportunity_types = opportunity_types
        if plan_types is not None:
            self.plan_types = plan_types

    @property
    def is_archived(self):
        """Gets the is_archived of this OpportunityPropositionPropertyValue.  # noqa: E501

        Flag indicating whether or not the opportunity proposition is archived.  # noqa: E501

        :return: The is_archived of this OpportunityPropositionPropertyValue.  # noqa: E501
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """Sets the is_archived of this OpportunityPropositionPropertyValue.

        Flag indicating whether or not the opportunity proposition is archived.  # noqa: E501

        :param is_archived: The is_archived of this OpportunityPropositionPropertyValue.  # noqa: E501
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def opportunity_types(self):
        """Gets the opportunity_types of this OpportunityPropositionPropertyValue.  # noqa: E501

        Opportunity types associated with the opportunity proposition.  # noqa: E501

        :return: The opportunity_types of this OpportunityPropositionPropertyValue.  # noqa: E501
        :rtype: list[OpportunityTypeValue]
        """
        return self._opportunity_types

    @opportunity_types.setter
    def opportunity_types(self, opportunity_types):
        """Sets the opportunity_types of this OpportunityPropositionPropertyValue.

        Opportunity types associated with the opportunity proposition.  # noqa: E501

        :param opportunity_types: The opportunity_types of this OpportunityPropositionPropertyValue.  # noqa: E501
        :type: list[OpportunityTypeValue]
        """

        self._opportunity_types = opportunity_types

    @property
    def plan_types(self):
        """Gets the plan_types of this OpportunityPropositionPropertyValue.  # noqa: E501

        Plan types associated with the opportunity proposition.  # noqa: E501

        :return: The plan_types of this OpportunityPropositionPropertyValue.  # noqa: E501
        :rtype: list[PlanTypeWithRegionValue]
        """
        return self._plan_types

    @plan_types.setter
    def plan_types(self, plan_types):
        """Sets the plan_types of this OpportunityPropositionPropertyValue.

        Plan types associated with the opportunity proposition.  # noqa: E501

        :param plan_types: The plan_types of this OpportunityPropositionPropertyValue.  # noqa: E501
        :type: list[PlanTypeWithRegionValue]
        """

        self._plan_types = plan_types

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
        if issubclass(OpportunityPropositionPropertyValue, dict):
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
        if not isinstance(other, OpportunityPropositionPropertyValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
