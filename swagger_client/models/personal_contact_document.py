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

class PersonalContactDocument(object):
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
        'party_type': 'str',
        'party': 'PartyReference',
        'person': 'PersonValue',
        'corporate': 'CorporateValue',
        'trust': 'TrustValue',
        'addresses__href': 'str',
        'contactdetails__href': 'str',
        'tags': 'list[str]',
        'created_at': 'datetime',
        'created_by_user': 'UserReference',
        'belongs_to': 'list[ClientRef]',
        'external_reference': 'str'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'name': 'name',
        'party_type': 'partyType',
        'party': 'party',
        'person': 'person',
        'corporate': 'corporate',
        'trust': 'trust',
        'addresses__href': 'addresses__href',
        'contactdetails__href': 'contactdetails__href',
        'tags': 'tags',
        'created_at': 'createdAt',
        'created_by_user': 'createdByUser',
        'belongs_to': 'belongsTo',
        'external_reference': 'externalReference'
    }

    def __init__(self, id=None, href=None, name=None, party_type=None, party=None, person=None, corporate=None, trust=None, addresses__href=None, contactdetails__href=None, tags=None, created_at=None, created_by_user=None, belongs_to=None, external_reference=None):  # noqa: E501
        """PersonalContactDocument - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._name = None
        self._party_type = None
        self._party = None
        self._person = None
        self._corporate = None
        self._trust = None
        self._addresses__href = None
        self._contactdetails__href = None
        self._tags = None
        self._created_at = None
        self._created_by_user = None
        self._belongs_to = None
        self._external_reference = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if name is not None:
            self.name = name
        self.party_type = party_type
        if party is not None:
            self.party = party
        if person is not None:
            self.person = person
        if corporate is not None:
            self.corporate = corporate
        if trust is not None:
            self.trust = trust
        if addresses__href is not None:
            self.addresses__href = addresses__href
        if contactdetails__href is not None:
            self.contactdetails__href = contactdetails__href
        if tags is not None:
            self.tags = tags
        if created_at is not None:
            self.created_at = created_at
        if created_by_user is not None:
            self.created_by_user = created_by_user
        if belongs_to is not None:
            self.belongs_to = belongs_to
        if external_reference is not None:
            self.external_reference = external_reference

    @property
    def id(self):
        """Gets the id of this PersonalContactDocument.  # noqa: E501

        Personal contact identifies  # noqa: E501

        :return: The id of this PersonalContactDocument.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PersonalContactDocument.

        Personal contact identifies  # noqa: E501

        :param id: The id of this PersonalContactDocument.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this PersonalContactDocument.  # noqa: E501

        Personal contact link  # noqa: E501

        :return: The href of this PersonalContactDocument.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this PersonalContactDocument.

        Personal contact link  # noqa: E501

        :param href: The href of this PersonalContactDocument.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def name(self):
        """Gets the name of this PersonalContactDocument.  # noqa: E501

        Personal contact name  # noqa: E501

        :return: The name of this PersonalContactDocument.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PersonalContactDocument.

        Personal contact name  # noqa: E501

        :param name: The name of this PersonalContactDocument.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def party_type(self):
        """Gets the party_type of this PersonalContactDocument.  # noqa: E501

        Personal contact party type  # noqa: E501

        :return: The party_type of this PersonalContactDocument.  # noqa: E501
        :rtype: str
        """
        return self._party_type

    @party_type.setter
    def party_type(self, party_type):
        """Sets the party_type of this PersonalContactDocument.

        Personal contact party type  # noqa: E501

        :param party_type: The party_type of this PersonalContactDocument.  # noqa: E501
        :type: str
        """
        if party_type is None:
            raise ValueError("Invalid value for `party_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Person", "Trust", "Corporate"]  # noqa: E501
        if party_type not in allowed_values:
            raise ValueError(
                "Invalid value for `party_type` ({0}), must be one of {1}"  # noqa: E501
                .format(party_type, allowed_values)
            )

        self._party_type = party_type

    @property
    def party(self):
        """Gets the party of this PersonalContactDocument.  # noqa: E501


        :return: The party of this PersonalContactDocument.  # noqa: E501
        :rtype: PartyReference
        """
        return self._party

    @party.setter
    def party(self, party):
        """Sets the party of this PersonalContactDocument.


        :param party: The party of this PersonalContactDocument.  # noqa: E501
        :type: PartyReference
        """

        self._party = party

    @property
    def person(self):
        """Gets the person of this PersonalContactDocument.  # noqa: E501


        :return: The person of this PersonalContactDocument.  # noqa: E501
        :rtype: PersonValue
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this PersonalContactDocument.


        :param person: The person of this PersonalContactDocument.  # noqa: E501
        :type: PersonValue
        """

        self._person = person

    @property
    def corporate(self):
        """Gets the corporate of this PersonalContactDocument.  # noqa: E501


        :return: The corporate of this PersonalContactDocument.  # noqa: E501
        :rtype: CorporateValue
        """
        return self._corporate

    @corporate.setter
    def corporate(self, corporate):
        """Sets the corporate of this PersonalContactDocument.


        :param corporate: The corporate of this PersonalContactDocument.  # noqa: E501
        :type: CorporateValue
        """

        self._corporate = corporate

    @property
    def trust(self):
        """Gets the trust of this PersonalContactDocument.  # noqa: E501


        :return: The trust of this PersonalContactDocument.  # noqa: E501
        :rtype: TrustValue
        """
        return self._trust

    @trust.setter
    def trust(self, trust):
        """Sets the trust of this PersonalContactDocument.


        :param trust: The trust of this PersonalContactDocument.  # noqa: E501
        :type: TrustValue
        """

        self._trust = trust

    @property
    def addresses__href(self):
        """Gets the addresses__href of this PersonalContactDocument.  # noqa: E501

        Personal contact address link  # noqa: E501

        :return: The addresses__href of this PersonalContactDocument.  # noqa: E501
        :rtype: str
        """
        return self._addresses__href

    @addresses__href.setter
    def addresses__href(self, addresses__href):
        """Sets the addresses__href of this PersonalContactDocument.

        Personal contact address link  # noqa: E501

        :param addresses__href: The addresses__href of this PersonalContactDocument.  # noqa: E501
        :type: str
        """

        self._addresses__href = addresses__href

    @property
    def contactdetails__href(self):
        """Gets the contactdetails__href of this PersonalContactDocument.  # noqa: E501

        Personal contact contact details link  # noqa: E501

        :return: The contactdetails__href of this PersonalContactDocument.  # noqa: E501
        :rtype: str
        """
        return self._contactdetails__href

    @contactdetails__href.setter
    def contactdetails__href(self, contactdetails__href):
        """Sets the contactdetails__href of this PersonalContactDocument.

        Personal contact contact details link  # noqa: E501

        :param contactdetails__href: The contactdetails__href of this PersonalContactDocument.  # noqa: E501
        :type: str
        """

        self._contactdetails__href = contactdetails__href

    @property
    def tags(self):
        """Gets the tags of this PersonalContactDocument.  # noqa: E501

        List of tags for personal contact  # noqa: E501

        :return: The tags of this PersonalContactDocument.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PersonalContactDocument.

        List of tags for personal contact  # noqa: E501

        :param tags: The tags of this PersonalContactDocument.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def created_at(self):
        """Gets the created_at of this PersonalContactDocument.  # noqa: E501

        Date of creation personal contact  # noqa: E501

        :return: The created_at of this PersonalContactDocument.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PersonalContactDocument.

        Date of creation personal contact  # noqa: E501

        :param created_at: The created_at of this PersonalContactDocument.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by_user(self):
        """Gets the created_by_user of this PersonalContactDocument.  # noqa: E501


        :return: The created_by_user of this PersonalContactDocument.  # noqa: E501
        :rtype: UserReference
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user):
        """Sets the created_by_user of this PersonalContactDocument.


        :param created_by_user: The created_by_user of this PersonalContactDocument.  # noqa: E501
        :type: UserReference
        """

        self._created_by_user = created_by_user

    @property
    def belongs_to(self):
        """Gets the belongs_to of this PersonalContactDocument.  # noqa: E501

        List of related clients for personal contact  # noqa: E501

        :return: The belongs_to of this PersonalContactDocument.  # noqa: E501
        :rtype: list[ClientRef]
        """
        return self._belongs_to

    @belongs_to.setter
    def belongs_to(self, belongs_to):
        """Sets the belongs_to of this PersonalContactDocument.

        List of related clients for personal contact  # noqa: E501

        :param belongs_to: The belongs_to of this PersonalContactDocument.  # noqa: E501
        :type: list[ClientRef]
        """

        self._belongs_to = belongs_to

    @property
    def external_reference(self):
        """Gets the external_reference of this PersonalContactDocument.  # noqa: E501

        The external reference.  # noqa: E501

        :return: The external_reference of this PersonalContactDocument.  # noqa: E501
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this PersonalContactDocument.

        The external reference.  # noqa: E501

        :param external_reference: The external_reference of this PersonalContactDocument.  # noqa: E501
        :type: str
        """

        self._external_reference = external_reference

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
        if issubclass(PersonalContactDocument, dict):
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
        if not isinstance(other, PersonalContactDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
