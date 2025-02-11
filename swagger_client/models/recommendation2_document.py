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

class Recommendation2Document(object):
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
        'status': 'RecommendationStatusValue',
        'name': 'str',
        'service_case': 'ServiceCaseReference',
        'category': 'RecommendationCategoryRef',
        'sub_category': 'RecommendationSubCategoryRef',
        'created_by': 'NamedUserRef',
        'created_app': 'NamedAppRef',
        'created_on': 'datetime',
        'owners': 'list[NamedClientReference]',
        'documents_href': 'str',
        'notes': 'str',
        'priority': 'int',
        'requirements': 'list[ObjectiveRef]',
        'proposals': 'list[BaseRecommendation2Proposal]',
        'properties': 'dict(str, str)',
        'expires_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'status': 'status',
        'name': 'name',
        'service_case': 'serviceCase',
        'category': 'category',
        'sub_category': 'subCategory',
        'created_by': 'createdBy',
        'created_app': 'createdApp',
        'created_on': 'createdOn',
        'owners': 'owners',
        'documents_href': 'documents_href',
        'notes': 'notes',
        'priority': 'priority',
        'requirements': 'requirements',
        'proposals': 'proposals',
        'properties': 'properties',
        'expires_at': 'expiresAt'
    }

    def __init__(self, id=None, href=None, status=None, name=None, service_case=None, category=None, sub_category=None, created_by=None, created_app=None, created_on=None, owners=None, documents_href=None, notes=None, priority=None, requirements=None, proposals=None, properties=None, expires_at=None):  # noqa: E501
        """Recommendation2Document - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._status = None
        self._name = None
        self._service_case = None
        self._category = None
        self._sub_category = None
        self._created_by = None
        self._created_app = None
        self._created_on = None
        self._owners = None
        self._documents_href = None
        self._notes = None
        self._priority = None
        self._requirements = None
        self._proposals = None
        self._properties = None
        self._expires_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if status is not None:
            self.status = status
        self.name = name
        if service_case is not None:
            self.service_case = service_case
        if category is not None:
            self.category = category
        if sub_category is not None:
            self.sub_category = sub_category
        if created_by is not None:
            self.created_by = created_by
        if created_app is not None:
            self.created_app = created_app
        if created_on is not None:
            self.created_on = created_on
        self.owners = owners
        if documents_href is not None:
            self.documents_href = documents_href
        if notes is not None:
            self.notes = notes
        if priority is not None:
            self.priority = priority
        if requirements is not None:
            self.requirements = requirements
        if proposals is not None:
            self.proposals = proposals
        if properties is not None:
            self.properties = properties
        if expires_at is not None:
            self.expires_at = expires_at

    @property
    def id(self):
        """Gets the id of this Recommendation2Document.  # noqa: E501

        Recommendation unique identifier.  # noqa: E501

        :return: The id of this Recommendation2Document.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Recommendation2Document.

        Recommendation unique identifier.  # noqa: E501

        :param id: The id of this Recommendation2Document.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this Recommendation2Document.  # noqa: E501

        Recommendation hypermedia link.  # noqa: E501

        :return: The href of this Recommendation2Document.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Recommendation2Document.

        Recommendation hypermedia link.  # noqa: E501

        :param href: The href of this Recommendation2Document.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def status(self):
        """Gets the status of this Recommendation2Document.  # noqa: E501


        :return: The status of this Recommendation2Document.  # noqa: E501
        :rtype: RecommendationStatusValue
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Recommendation2Document.


        :param status: The status of this Recommendation2Document.  # noqa: E501
        :type: RecommendationStatusValue
        """

        self._status = status

    @property
    def name(self):
        """Gets the name of this Recommendation2Document.  # noqa: E501

        Name of the recommendation.  # noqa: E501

        :return: The name of this Recommendation2Document.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Recommendation2Document.

        Name of the recommendation.  # noqa: E501

        :param name: The name of this Recommendation2Document.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def service_case(self):
        """Gets the service_case of this Recommendation2Document.  # noqa: E501


        :return: The service_case of this Recommendation2Document.  # noqa: E501
        :rtype: ServiceCaseReference
        """
        return self._service_case

    @service_case.setter
    def service_case(self, service_case):
        """Sets the service_case of this Recommendation2Document.


        :param service_case: The service_case of this Recommendation2Document.  # noqa: E501
        :type: ServiceCaseReference
        """

        self._service_case = service_case

    @property
    def category(self):
        """Gets the category of this Recommendation2Document.  # noqa: E501


        :return: The category of this Recommendation2Document.  # noqa: E501
        :rtype: RecommendationCategoryRef
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Recommendation2Document.


        :param category: The category of this Recommendation2Document.  # noqa: E501
        :type: RecommendationCategoryRef
        """

        self._category = category

    @property
    def sub_category(self):
        """Gets the sub_category of this Recommendation2Document.  # noqa: E501


        :return: The sub_category of this Recommendation2Document.  # noqa: E501
        :rtype: RecommendationSubCategoryRef
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        """Sets the sub_category of this Recommendation2Document.


        :param sub_category: The sub_category of this Recommendation2Document.  # noqa: E501
        :type: RecommendationSubCategoryRef
        """

        self._sub_category = sub_category

    @property
    def created_by(self):
        """Gets the created_by of this Recommendation2Document.  # noqa: E501


        :return: The created_by of this Recommendation2Document.  # noqa: E501
        :rtype: NamedUserRef
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Recommendation2Document.


        :param created_by: The created_by of this Recommendation2Document.  # noqa: E501
        :type: NamedUserRef
        """

        self._created_by = created_by

    @property
    def created_app(self):
        """Gets the created_app of this Recommendation2Document.  # noqa: E501


        :return: The created_app of this Recommendation2Document.  # noqa: E501
        :rtype: NamedAppRef
        """
        return self._created_app

    @created_app.setter
    def created_app(self, created_app):
        """Sets the created_app of this Recommendation2Document.


        :param created_app: The created_app of this Recommendation2Document.  # noqa: E501
        :type: NamedAppRef
        """

        self._created_app = created_app

    @property
    def created_on(self):
        """Gets the created_on of this Recommendation2Document.  # noqa: E501

        Recommendation created date.  # noqa: E501

        :return: The created_on of this Recommendation2Document.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Recommendation2Document.

        Recommendation created date.  # noqa: E501

        :param created_on: The created_on of this Recommendation2Document.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def owners(self):
        """Gets the owners of this Recommendation2Document.  # noqa: E501

        Collection of recommendation owners (clients only). Owner at index 0 is the primary owner.  # noqa: E501

        :return: The owners of this Recommendation2Document.  # noqa: E501
        :rtype: list[NamedClientReference]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Sets the owners of this Recommendation2Document.

        Collection of recommendation owners (clients only). Owner at index 0 is the primary owner.  # noqa: E501

        :param owners: The owners of this Recommendation2Document.  # noqa: E501
        :type: list[NamedClientReference]
        """
        if owners is None:
            raise ValueError("Invalid value for `owners`, must not be `None`")  # noqa: E501

        self._owners = owners

    @property
    def documents_href(self):
        """Gets the documents_href of this Recommendation2Document.  # noqa: E501

        Hyperlink to recommendation documents.  # noqa: E501

        :return: The documents_href of this Recommendation2Document.  # noqa: E501
        :rtype: str
        """
        return self._documents_href

    @documents_href.setter
    def documents_href(self, documents_href):
        """Sets the documents_href of this Recommendation2Document.

        Hyperlink to recommendation documents.  # noqa: E501

        :param documents_href: The documents_href of this Recommendation2Document.  # noqa: E501
        :type: str
        """

        self._documents_href = documents_href

    @property
    def notes(self):
        """Gets the notes of this Recommendation2Document.  # noqa: E501

        Notes to the recommendation.  # noqa: E501

        :return: The notes of this Recommendation2Document.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Recommendation2Document.

        Notes to the recommendation.  # noqa: E501

        :param notes: The notes of this Recommendation2Document.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def priority(self):
        """Gets the priority of this Recommendation2Document.  # noqa: E501

        Priority of the recommendation.  # noqa: E501

        :return: The priority of this Recommendation2Document.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Recommendation2Document.

        Priority of the recommendation.  # noqa: E501

        :param priority: The priority of this Recommendation2Document.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def requirements(self):
        """Gets the requirements of this Recommendation2Document.  # noqa: E501

        A collection of client objectives linked to this recommendation  # noqa: E501

        :return: The requirements of this Recommendation2Document.  # noqa: E501
        :rtype: list[ObjectiveRef]
        """
        return self._requirements

    @requirements.setter
    def requirements(self, requirements):
        """Sets the requirements of this Recommendation2Document.

        A collection of client objectives linked to this recommendation  # noqa: E501

        :param requirements: The requirements of this Recommendation2Document.  # noqa: E501
        :type: list[ObjectiveRef]
        """

        self._requirements = requirements

    @property
    def proposals(self):
        """Gets the proposals of this Recommendation2Document.  # noqa: E501

        A collection of proposals linked to this recommendation  # noqa: E501

        :return: The proposals of this Recommendation2Document.  # noqa: E501
        :rtype: list[BaseRecommendation2Proposal]
        """
        return self._proposals

    @proposals.setter
    def proposals(self, proposals):
        """Sets the proposals of this Recommendation2Document.

        A collection of proposals linked to this recommendation  # noqa: E501

        :param proposals: The proposals of this Recommendation2Document.  # noqa: E501
        :type: list[BaseRecommendation2Proposal]
        """

        self._proposals = proposals

    @property
    def properties(self):
        """Gets the properties of this Recommendation2Document.  # noqa: E501

        Editable on POST, PATCH.  Limited to 10 items.  Use this to set custom properties for a recommendation e.g.      \"properties\": {         \"myCustomProperty\": \"A value\",         \"anotherCustomProperty\": \"Some other value\"      }  # noqa: E501

        :return: The properties of this Recommendation2Document.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Recommendation2Document.

        Editable on POST, PATCH.  Limited to 10 items.  Use this to set custom properties for a recommendation e.g.      \"properties\": {         \"myCustomProperty\": \"A value\",         \"anotherCustomProperty\": \"Some other value\"      }  # noqa: E501

        :param properties: The properties of this Recommendation2Document.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

    @property
    def expires_at(self):
        """Gets the expires_at of this Recommendation2Document.  # noqa: E501

        Recommendation expiry date and time.  # noqa: E501

        :return: The expires_at of this Recommendation2Document.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this Recommendation2Document.

        Recommendation expiry date and time.  # noqa: E501

        :param expires_at: The expires_at of this Recommendation2Document.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

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
        if issubclass(Recommendation2Document, dict):
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
        if not isinstance(other, Recommendation2Document):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
