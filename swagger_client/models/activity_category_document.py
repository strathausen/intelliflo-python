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

class ActivityCategoryDocument(object):
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
        'href': 'str',
        'name': 'str',
        'is_archived': 'bool',
        'is_deletable': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'name': 'name',
        'is_archived': 'isArchived',
        'is_deletable': 'isDeletable'
    }

    def __init__(self, id=None, href=None, name=None, is_archived=None, is_deletable=False):  # noqa: E501
        """ActivityCategoryDocument - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._name = None
        self._is_archived = None
        self._is_deletable = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        self.name = name
        self.is_archived = is_archived
        if is_deletable is not None:
            self.is_deletable = is_deletable

    @property
    def id(self):
        """Gets the id of this ActivityCategoryDocument.  # noqa: E501

        The identifier for the activity category.  # noqa: E501

        :return: The id of this ActivityCategoryDocument.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ActivityCategoryDocument.

        The identifier for the activity category.  # noqa: E501

        :param id: The id of this ActivityCategoryDocument.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this ActivityCategoryDocument.  # noqa: E501

        The hypertext reference to the activity category.  # noqa: E501

        :return: The href of this ActivityCategoryDocument.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ActivityCategoryDocument.

        The hypertext reference to the activity category.  # noqa: E501

        :param href: The href of this ActivityCategoryDocument.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def name(self):
        """Gets the name of this ActivityCategoryDocument.  # noqa: E501

        The name of the activity category.  # noqa: E501

        :return: The name of this ActivityCategoryDocument.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ActivityCategoryDocument.

        The name of the activity category.  # noqa: E501

        :param name: The name of this ActivityCategoryDocument.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def is_archived(self):
        """Gets the is_archived of this ActivityCategoryDocument.  # noqa: E501

        Flag indicating if the activity category is archived or not.  # noqa: E501

        :return: The is_archived of this ActivityCategoryDocument.  # noqa: E501
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """Sets the is_archived of this ActivityCategoryDocument.

        Flag indicating if the activity category is archived or not.  # noqa: E501

        :param is_archived: The is_archived of this ActivityCategoryDocument.  # noqa: E501
        :type: bool
        """
        if is_archived is None:
            raise ValueError("Invalid value for `is_archived`, must not be `None`")  # noqa: E501

        self._is_archived = is_archived

    @property
    def is_deletable(self):
        """Gets the is_deletable of this ActivityCategoryDocument.  # noqa: E501

        Flag indicating if the activity category can be deleted or not. if activity category is used in any of the activity types or tasks or appointments then we cannot delete the activity category.  # noqa: E501

        :return: The is_deletable of this ActivityCategoryDocument.  # noqa: E501
        :rtype: bool
        """
        return self._is_deletable

    @is_deletable.setter
    def is_deletable(self, is_deletable):
        """Sets the is_deletable of this ActivityCategoryDocument.

        Flag indicating if the activity category can be deleted or not. if activity category is used in any of the activity types or tasks or appointments then we cannot delete the activity category.  # noqa: E501

        :param is_deletable: The is_deletable of this ActivityCategoryDocument.  # noqa: E501
        :type: bool
        """

        self._is_deletable = is_deletable

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
        if issubclass(ActivityCategoryDocument, dict):
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
        if not isinstance(other, ActivityCategoryDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
