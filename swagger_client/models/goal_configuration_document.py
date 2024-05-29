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

class GoalConfigurationDocument(object):
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
        'product_category': 'str',
        'goal_categories': 'list[NamedGoalCategoryRef]'
    }

    attribute_map = {
        'product_category': 'productCategory',
        'goal_categories': 'goalCategories'
    }

    def __init__(self, product_category=None, goal_categories=None):  # noqa: E501
        """GoalConfigurationDocument - a model defined in Swagger"""  # noqa: E501
        self._product_category = None
        self._goal_categories = None
        self.discriminator = None
        self.product_category = product_category
        self.goal_categories = goal_categories

    @property
    def product_category(self):
        """Gets the product_category of this GoalConfigurationDocument.  # noqa: E501

        Product Category  # noqa: E501

        :return: The product_category of this GoalConfigurationDocument.  # noqa: E501
        :rtype: str
        """
        return self._product_category

    @product_category.setter
    def product_category(self, product_category):
        """Sets the product_category of this GoalConfigurationDocument.

        Product Category  # noqa: E501

        :param product_category: The product_category of this GoalConfigurationDocument.  # noqa: E501
        :type: str
        """
        if product_category is None:
            raise ValueError("Invalid value for `product_category`, must not be `None`")  # noqa: E501
        allowed_values = ["Retirement", "Investment", "Mortgage", "Protection"]  # noqa: E501
        if product_category not in allowed_values:
            raise ValueError(
                "Invalid value for `product_category` ({0}), must be one of {1}"  # noqa: E501
                .format(product_category, allowed_values)
            )

        self._product_category = product_category

    @property
    def goal_categories(self):
        """Gets the goal_categories of this GoalConfigurationDocument.  # noqa: E501

        List of Goal Category  # noqa: E501

        :return: The goal_categories of this GoalConfigurationDocument.  # noqa: E501
        :rtype: list[NamedGoalCategoryRef]
        """
        return self._goal_categories

    @goal_categories.setter
    def goal_categories(self, goal_categories):
        """Sets the goal_categories of this GoalConfigurationDocument.

        List of Goal Category  # noqa: E501

        :param goal_categories: The goal_categories of this GoalConfigurationDocument.  # noqa: E501
        :type: list[NamedGoalCategoryRef]
        """
        if goal_categories is None:
            raise ValueError("Invalid value for `goal_categories`, must not be `None`")  # noqa: E501

        self._goal_categories = goal_categories

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
        if issubclass(GoalConfigurationDocument, dict):
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
        if not isinstance(other, GoalConfigurationDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
