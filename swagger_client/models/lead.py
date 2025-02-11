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

class Lead(object):
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
        'created_at': 'datetime',
        'person': 'PersonValue',
        'corporate': 'CorporateValue',
        'trust': 'TrustValue',
        'original_adviser': 'NamedAdviserRef',
        'current_adviser': 'NamedAdviserRef',
        'campaign': 'CampaignValue',
        'type': 'str',
        'party_type': 'str',
        'category': 'str',
        'migration_reference': 'str',
        'external_reference': 'str',
        'secondary_reference': 'str',
        'addresses_href': 'str',
        'contactdetails_href': 'str',
        'relationships_href': 'str',
        'tags': 'list[str]',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'name': 'name',
        'created_at': 'createdAt',
        'person': 'person',
        'corporate': 'corporate',
        'trust': 'trust',
        'original_adviser': 'originalAdviser',
        'current_adviser': 'currentAdviser',
        'campaign': 'campaign',
        'type': 'type',
        'party_type': 'partyType',
        'category': 'category',
        'migration_reference': 'migrationReference',
        'external_reference': 'externalReference',
        'secondary_reference': 'secondaryReference',
        'addresses_href': 'addresses_href',
        'contactdetails_href': 'contactdetails_href',
        'relationships_href': 'relationships_href',
        'tags': 'tags',
        'status': 'status'
    }

    def __init__(self, id=None, href=None, name=None, created_at=None, person=None, corporate=None, trust=None, original_adviser=None, current_adviser=None, campaign=None, type=None, party_type=None, category=None, migration_reference=None, external_reference=None, secondary_reference=None, addresses_href=None, contactdetails_href=None, relationships_href=None, tags=None, status=None):  # noqa: E501
        """Lead - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._name = None
        self._created_at = None
        self._person = None
        self._corporate = None
        self._trust = None
        self._original_adviser = None
        self._current_adviser = None
        self._campaign = None
        self._type = None
        self._party_type = None
        self._category = None
        self._migration_reference = None
        self._external_reference = None
        self._secondary_reference = None
        self._addresses_href = None
        self._contactdetails_href = None
        self._relationships_href = None
        self._tags = None
        self._status = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if person is not None:
            self.person = person
        if corporate is not None:
            self.corporate = corporate
        if trust is not None:
            self.trust = trust
        if original_adviser is not None:
            self.original_adviser = original_adviser
        if current_adviser is not None:
            self.current_adviser = current_adviser
        if campaign is not None:
            self.campaign = campaign
        if type is not None:
            self.type = type
        if party_type is not None:
            self.party_type = party_type
        if category is not None:
            self.category = category
        if migration_reference is not None:
            self.migration_reference = migration_reference
        if external_reference is not None:
            self.external_reference = external_reference
        if secondary_reference is not None:
            self.secondary_reference = secondary_reference
        if addresses_href is not None:
            self.addresses_href = addresses_href
        if contactdetails_href is not None:
            self.contactdetails_href = contactdetails_href
        if relationships_href is not None:
            self.relationships_href = relationships_href
        if tags is not None:
            self.tags = tags
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this Lead.  # noqa: E501

        The unique identifier for the Lead.  # noqa: E501

        :return: The id of this Lead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Lead.

        The unique identifier for the Lead.  # noqa: E501

        :param id: The id of this Lead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this Lead.  # noqa: E501

        The hypertext reference to the Lead.  # noqa: E501

        :return: The href of this Lead.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Lead.

        The hypertext reference to the Lead.  # noqa: E501

        :param href: The href of this Lead.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def name(self):
        """Gets the name of this Lead.  # noqa: E501

        The Lead's name. This is derived from the Lead's details, for a Person it is their Firstname and Lastname.  # noqa: E501

        :return: The name of this Lead.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Lead.

        The Lead's name. This is derived from the Lead's details, for a Person it is their Firstname and Lastname.  # noqa: E501

        :param name: The name of this Lead.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this Lead.  # noqa: E501

        The date the Lead was created.  # noqa: E501

        :return: The created_at of this Lead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Lead.

        The date the Lead was created.  # noqa: E501

        :param created_at: The created_at of this Lead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def person(self):
        """Gets the person of this Lead.  # noqa: E501


        :return: The person of this Lead.  # noqa: E501
        :rtype: PersonValue
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this Lead.


        :param person: The person of this Lead.  # noqa: E501
        :type: PersonValue
        """

        self._person = person

    @property
    def corporate(self):
        """Gets the corporate of this Lead.  # noqa: E501


        :return: The corporate of this Lead.  # noqa: E501
        :rtype: CorporateValue
        """
        return self._corporate

    @corporate.setter
    def corporate(self, corporate):
        """Sets the corporate of this Lead.


        :param corporate: The corporate of this Lead.  # noqa: E501
        :type: CorporateValue
        """

        self._corporate = corporate

    @property
    def trust(self):
        """Gets the trust of this Lead.  # noqa: E501


        :return: The trust of this Lead.  # noqa: E501
        :rtype: TrustValue
        """
        return self._trust

    @trust.setter
    def trust(self, trust):
        """Sets the trust of this Lead.


        :param trust: The trust of this Lead.  # noqa: E501
        :type: TrustValue
        """

        self._trust = trust

    @property
    def original_adviser(self):
        """Gets the original_adviser of this Lead.  # noqa: E501


        :return: The original_adviser of this Lead.  # noqa: E501
        :rtype: NamedAdviserRef
        """
        return self._original_adviser

    @original_adviser.setter
    def original_adviser(self, original_adviser):
        """Sets the original_adviser of this Lead.


        :param original_adviser: The original_adviser of this Lead.  # noqa: E501
        :type: NamedAdviserRef
        """

        self._original_adviser = original_adviser

    @property
    def current_adviser(self):
        """Gets the current_adviser of this Lead.  # noqa: E501


        :return: The current_adviser of this Lead.  # noqa: E501
        :rtype: NamedAdviserRef
        """
        return self._current_adviser

    @current_adviser.setter
    def current_adviser(self, current_adviser):
        """Sets the current_adviser of this Lead.


        :param current_adviser: The current_adviser of this Lead.  # noqa: E501
        :type: NamedAdviserRef
        """

        self._current_adviser = current_adviser

    @property
    def campaign(self):
        """Gets the campaign of this Lead.  # noqa: E501


        :return: The campaign of this Lead.  # noqa: E501
        :rtype: CampaignValue
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign):
        """Sets the campaign of this Lead.


        :param campaign: The campaign of this Lead.  # noqa: E501
        :type: CampaignValue
        """

        self._campaign = campaign

    @property
    def type(self):
        """Gets the type of this Lead.  # noqa: E501


        :return: The type of this Lead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Lead.


        :param type: The type of this Lead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def party_type(self):
        """Gets the party_type of this Lead.  # noqa: E501

        The type of Lead, either Person, Trust or Corporate.  # noqa: E501

        :return: The party_type of this Lead.  # noqa: E501
        :rtype: str
        """
        return self._party_type

    @party_type.setter
    def party_type(self, party_type):
        """Sets the party_type of this Lead.

        The type of Lead, either Person, Trust or Corporate.  # noqa: E501

        :param party_type: The party_type of this Lead.  # noqa: E501
        :type: str
        """

        self._party_type = party_type

    @property
    def category(self):
        """Gets the category of this Lead.  # noqa: E501

        The category of Lead to which the Lead belongs.  # noqa: E501

        :return: The category of this Lead.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Lead.

        The category of Lead to which the Lead belongs.  # noqa: E501

        :param category: The category of this Lead.  # noqa: E501
        :type: str
        """
        allowed_values = ["Retail", "Professional", "EligibleCounterparty", "Customer", "LargeBusinessCustomer", "Consumer", "CommercialCustomer"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def migration_reference(self):
        """Gets the migration_reference of this Lead.  # noqa: E501

        The Lead migration reference. Typically a reference set when the Lead was imported into the system.  # noqa: E501

        :return: The migration_reference of this Lead.  # noqa: E501
        :rtype: str
        """
        return self._migration_reference

    @migration_reference.setter
    def migration_reference(self, migration_reference):
        """Sets the migration_reference of this Lead.

        The Lead migration reference. Typically a reference set when the Lead was imported into the system.  # noqa: E501

        :param migration_reference: The migration_reference of this Lead.  # noqa: E501
        :type: str
        """

        self._migration_reference = migration_reference

    @property
    def external_reference(self):
        """Gets the external_reference of this Lead.  # noqa: E501

        An external reference for the Lead.  # noqa: E501

        :return: The external_reference of this Lead.  # noqa: E501
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this Lead.

        An external reference for the Lead.  # noqa: E501

        :param external_reference: The external_reference of this Lead.  # noqa: E501
        :type: str
        """

        self._external_reference = external_reference

    @property
    def secondary_reference(self):
        """Gets the secondary_reference of this Lead.  # noqa: E501

        An secondary external reference for the Lead.  # noqa: E501

        :return: The secondary_reference of this Lead.  # noqa: E501
        :rtype: str
        """
        return self._secondary_reference

    @secondary_reference.setter
    def secondary_reference(self, secondary_reference):
        """Sets the secondary_reference of this Lead.

        An secondary external reference for the Lead.  # noqa: E501

        :param secondary_reference: The secondary_reference of this Lead.  # noqa: E501
        :type: str
        """

        self._secondary_reference = secondary_reference

    @property
    def addresses_href(self):
        """Gets the addresses_href of this Lead.  # noqa: E501

        The hypertext reference to the address or addresses held for the Lead. Typically these may be a home, work or correspondance address.  # noqa: E501

        :return: The addresses_href of this Lead.  # noqa: E501
        :rtype: str
        """
        return self._addresses_href

    @addresses_href.setter
    def addresses_href(self, addresses_href):
        """Sets the addresses_href of this Lead.

        The hypertext reference to the address or addresses held for the Lead. Typically these may be a home, work or correspondance address.  # noqa: E501

        :param addresses_href: The addresses_href of this Lead.  # noqa: E501
        :type: str
        """

        self._addresses_href = addresses_href

    @property
    def contactdetails_href(self):
        """Gets the contactdetails_href of this Lead.  # noqa: E501

        The hypertext reference to the list of contact details held for the Lead.  # noqa: E501

        :return: The contactdetails_href of this Lead.  # noqa: E501
        :rtype: str
        """
        return self._contactdetails_href

    @contactdetails_href.setter
    def contactdetails_href(self, contactdetails_href):
        """Sets the contactdetails_href of this Lead.

        The hypertext reference to the list of contact details held for the Lead.  # noqa: E501

        :param contactdetails_href: The contactdetails_href of this Lead.  # noqa: E501
        :type: str
        """

        self._contactdetails_href = contactdetails_href

    @property
    def relationships_href(self):
        """Gets the relationships_href of this Lead.  # noqa: E501

        The hypertext reference to the list of any relevant relationships, professional or personal, that the Lead may have.  # noqa: E501

        :return: The relationships_href of this Lead.  # noqa: E501
        :rtype: str
        """
        return self._relationships_href

    @relationships_href.setter
    def relationships_href(self, relationships_href):
        """Sets the relationships_href of this Lead.

        The hypertext reference to the list of any relevant relationships, professional or personal, that the Lead may have.  # noqa: E501

        :param relationships_href: The relationships_href of this Lead.  # noqa: E501
        :type: str
        """

        self._relationships_href = relationships_href

    @property
    def tags(self):
        """Gets the tags of this Lead.  # noqa: E501

        A list of tags associated with the Lead The list can contain up to 30 tags. Each tag has a maximum length of 100 charecters and may not contain spaces.  # noqa: E501

        :return: The tags of this Lead.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Lead.

        A list of tags associated with the Lead The list can contain up to 30 tags. Each tag has a maximum length of 100 charecters and may not contain spaces.  # noqa: E501

        :param tags: The tags of this Lead.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def status(self):
        """Gets the status of this Lead.  # noqa: E501

        The current status of the Lead.  # noqa: E501

        :return: The status of this Lead.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Lead.

        The current status of the Lead.  # noqa: E501

        :param status: The status of this Lead.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(Lead, dict):
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
        if not isinstance(other, Lead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
