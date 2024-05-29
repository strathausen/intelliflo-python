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

class PlanTypeRef(object):
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
        'id': 'int',
        'name': 'str',
        'portfolio_category': 'str',
        'region_code': 'str',
        'allows_sub_plans': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'portfolio_category': 'portfolioCategory',
        'region_code': 'regionCode',
        'allows_sub_plans': 'allowsSubPlans'
    }

    def __init__(self, id=None, name='null', portfolio_category=None, region_code=None, allows_sub_plans=None):  # noqa: E501
        """PlanTypeRef - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._portfolio_category = None
        self._region_code = None
        self._allows_sub_plans = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        if portfolio_category is not None:
            self.portfolio_category = portfolio_category
        if region_code is not None:
            self.region_code = region_code
        if allows_sub_plans is not None:
            self.allows_sub_plans = allows_sub_plans

    @property
    def id(self):
        """Gets the id of this PlanTypeRef.  # noqa: E501


        :return: The id of this PlanTypeRef.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlanTypeRef.


        :param id: The id of this PlanTypeRef.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PlanTypeRef.  # noqa: E501


        :return: The name of this PlanTypeRef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlanTypeRef.


        :param name: The name of this PlanTypeRef.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def portfolio_category(self):
        """Gets the portfolio_category of this PlanTypeRef.  # noqa: E501


        :return: The portfolio_category of this PlanTypeRef.  # noqa: E501
        :rtype: str
        """
        return self._portfolio_category

    @portfolio_category.setter
    def portfolio_category(self, portfolio_category):
        """Sets the portfolio_category of this PlanTypeRef.


        :param portfolio_category: The portfolio_category of this PlanTypeRef.  # noqa: E501
        :type: str
        """

        self._portfolio_category = portfolio_category

    @property
    def region_code(self):
        """Gets the region_code of this PlanTypeRef.  # noqa: E501


        :return: The region_code of this PlanTypeRef.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this PlanTypeRef.


        :param region_code: The region_code of this PlanTypeRef.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

    @property
    def allows_sub_plans(self):
        """Gets the allows_sub_plans of this PlanTypeRef.  # noqa: E501

        Returns true if current plan type allows adding SubPlans.  # noqa: E501

        :return: The allows_sub_plans of this PlanTypeRef.  # noqa: E501
        :rtype: bool
        """
        return self._allows_sub_plans

    @allows_sub_plans.setter
    def allows_sub_plans(self, allows_sub_plans):
        """Sets the allows_sub_plans of this PlanTypeRef.

        Returns true if current plan type allows adding SubPlans.  # noqa: E501

        :param allows_sub_plans: The allows_sub_plans of this PlanTypeRef.  # noqa: E501
        :type: bool
        """

        self._allows_sub_plans = allows_sub_plans

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
        if issubclass(PlanTypeRef, dict):
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
        if not isinstance(other, PlanTypeRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
