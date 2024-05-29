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

class PlanPurposeCollection(object):
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
        'href': 'str',
        'first_href': 'str',
        'last_href': 'str',
        'next_href': 'str',
        'prev_href': 'str',
        'items': 'list[PlanPurpose]',
        'count': 'int'
    }

    attribute_map = {
        'href': 'href',
        'first_href': 'first_href',
        'last_href': 'last_href',
        'next_href': 'next_href',
        'prev_href': 'prev_href',
        'items': 'items',
        'count': 'count'
    }

    def __init__(self, href=None, first_href=None, last_href=None, next_href=None, prev_href=None, items=None, count=None):  # noqa: E501
        """PlanPurposeCollection - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._first_href = None
        self._last_href = None
        self._next_href = None
        self._prev_href = None
        self._items = None
        self._count = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if first_href is not None:
            self.first_href = first_href
        if last_href is not None:
            self.last_href = last_href
        if next_href is not None:
            self.next_href = next_href
        if prev_href is not None:
            self.prev_href = prev_href
        if items is not None:
            self.items = items
        if count is not None:
            self.count = count

    @property
    def href(self):
        """Gets the href of this PlanPurposeCollection.  # noqa: E501


        :return: The href of this PlanPurposeCollection.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this PlanPurposeCollection.


        :param href: The href of this PlanPurposeCollection.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def first_href(self):
        """Gets the first_href of this PlanPurposeCollection.  # noqa: E501


        :return: The first_href of this PlanPurposeCollection.  # noqa: E501
        :rtype: str
        """
        return self._first_href

    @first_href.setter
    def first_href(self, first_href):
        """Sets the first_href of this PlanPurposeCollection.


        :param first_href: The first_href of this PlanPurposeCollection.  # noqa: E501
        :type: str
        """

        self._first_href = first_href

    @property
    def last_href(self):
        """Gets the last_href of this PlanPurposeCollection.  # noqa: E501


        :return: The last_href of this PlanPurposeCollection.  # noqa: E501
        :rtype: str
        """
        return self._last_href

    @last_href.setter
    def last_href(self, last_href):
        """Sets the last_href of this PlanPurposeCollection.


        :param last_href: The last_href of this PlanPurposeCollection.  # noqa: E501
        :type: str
        """

        self._last_href = last_href

    @property
    def next_href(self):
        """Gets the next_href of this PlanPurposeCollection.  # noqa: E501


        :return: The next_href of this PlanPurposeCollection.  # noqa: E501
        :rtype: str
        """
        return self._next_href

    @next_href.setter
    def next_href(self, next_href):
        """Sets the next_href of this PlanPurposeCollection.


        :param next_href: The next_href of this PlanPurposeCollection.  # noqa: E501
        :type: str
        """

        self._next_href = next_href

    @property
    def prev_href(self):
        """Gets the prev_href of this PlanPurposeCollection.  # noqa: E501


        :return: The prev_href of this PlanPurposeCollection.  # noqa: E501
        :rtype: str
        """
        return self._prev_href

    @prev_href.setter
    def prev_href(self, prev_href):
        """Sets the prev_href of this PlanPurposeCollection.


        :param prev_href: The prev_href of this PlanPurposeCollection.  # noqa: E501
        :type: str
        """

        self._prev_href = prev_href

    @property
    def items(self):
        """Gets the items of this PlanPurposeCollection.  # noqa: E501


        :return: The items of this PlanPurposeCollection.  # noqa: E501
        :rtype: list[PlanPurpose]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PlanPurposeCollection.


        :param items: The items of this PlanPurposeCollection.  # noqa: E501
        :type: list[PlanPurpose]
        """

        self._items = items

    @property
    def count(self):
        """Gets the count of this PlanPurposeCollection.  # noqa: E501


        :return: The count of this PlanPurposeCollection.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PlanPurposeCollection.


        :param count: The count of this PlanPurposeCollection.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if issubclass(PlanPurposeCollection, dict):
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
        if not isinstance(other, PlanPurposeCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
