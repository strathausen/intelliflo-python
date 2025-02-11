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

class Document(object):
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
        'title': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'properties': 'dict(str, str)',
        'linked_entities': 'list[DocumentLinkedEntityRef]',
        'object': 'ObjectRef',
        'owners_href': 'str',
        'tags': 'list[str]',
        'is_private': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'title': 'title',
        'description': 'description',
        'created_at': 'createdAt',
        'properties': 'properties',
        'linked_entities': 'linked_entities',
        'object': 'object',
        'owners_href': 'owners_href',
        'tags': 'tags',
        'is_private': 'is_private'
    }

    def __init__(self, id=None, href=None, title=None, description=None, created_at=None, properties=None, linked_entities=None, object=None, owners_href=None, tags=None, is_private=None):  # noqa: E501
        """Document - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._title = None
        self._description = None
        self._created_at = None
        self._properties = None
        self._linked_entities = None
        self._object = None
        self._owners_href = None
        self._tags = None
        self._is_private = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if properties is not None:
            self.properties = properties
        if linked_entities is not None:
            self.linked_entities = linked_entities
        if object is not None:
            self.object = object
        if owners_href is not None:
            self.owners_href = owners_href
        if tags is not None:
            self.tags = tags
        if is_private is not None:
            self.is_private = is_private

    @property
    def id(self):
        """Gets the id of this Document.  # noqa: E501


        :return: The id of this Document.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Document.


        :param id: The id of this Document.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this Document.  # noqa: E501


        :return: The href of this Document.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Document.


        :param href: The href of this Document.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def title(self):
        """Gets the title of this Document.  # noqa: E501

        Editable on POST, PUT  # noqa: E501

        :return: The title of this Document.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Document.

        Editable on POST, PUT  # noqa: E501

        :param title: The title of this Document.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this Document.  # noqa: E501

        Editable on POST, PUT  # noqa: E501

        :return: The description of this Document.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Document.

        Editable on POST, PUT  # noqa: E501

        :param description: The description of this Document.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this Document.  # noqa: E501


        :return: The created_at of this Document.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Document.


        :param created_at: The created_at of this Document.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def properties(self):
        """Gets the properties of this Document.  # noqa: E501

        Editable on POST, PUT.  Limited to 10 items. Excluding reserved properties.  # noqa: E501

        :return: The properties of this Document.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Document.

        Editable on POST, PUT.  Limited to 10 items. Excluding reserved properties.  # noqa: E501

        :param properties: The properties of this Document.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

    @property
    def linked_entities(self):
        """Gets the linked_entities of this Document.  # noqa: E501

        Editable on POST, PUT  Limited to 2 linked entities (one of the items must be a service case if linked entities more than 1).  # noqa: E501

        :return: The linked_entities of this Document.  # noqa: E501
        :rtype: list[DocumentLinkedEntityRef]
        """
        return self._linked_entities

    @linked_entities.setter
    def linked_entities(self, linked_entities):
        """Sets the linked_entities of this Document.

        Editable on POST, PUT  Limited to 2 linked entities (one of the items must be a service case if linked entities more than 1).  # noqa: E501

        :param linked_entities: The linked_entities of this Document.  # noqa: E501
        :type: list[DocumentLinkedEntityRef]
        """

        self._linked_entities = linked_entities

    @property
    def object(self):
        """Gets the object of this Document.  # noqa: E501


        :return: The object of this Document.  # noqa: E501
        :rtype: ObjectRef
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this Document.


        :param object: The object of this Document.  # noqa: E501
        :type: ObjectRef
        """

        self._object = object

    @property
    def owners_href(self):
        """Gets the owners_href of this Document.  # noqa: E501


        :return: The owners_href of this Document.  # noqa: E501
        :rtype: str
        """
        return self._owners_href

    @owners_href.setter
    def owners_href(self, owners_href):
        """Sets the owners_href of this Document.


        :param owners_href: The owners_href of this Document.  # noqa: E501
        :type: str
        """

        self._owners_href = owners_href

    @property
    def tags(self):
        """Gets the tags of this Document.  # noqa: E501


        :return: The tags of this Document.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Document.


        :param tags: The tags of this Document.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def is_private(self):
        """Gets the is_private of this Document.  # noqa: E501


        :return: The is_private of this Document.  # noqa: E501
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """Sets the is_private of this Document.


        :param is_private: The is_private of this Document.  # noqa: E501
        :type: bool
        """

        self._is_private = is_private

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
        if issubclass(Document, dict):
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
        if not isinstance(other, Document):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
