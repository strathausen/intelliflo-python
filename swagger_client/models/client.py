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

class Client(object):
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
        'campaign': 'CampaignValue',
        'category': 'str',
        'migration_reference': 'str',
        'external_reference': 'str',
        'secondary_reference': 'str',
        'original_adviser': 'NamedAdviserRef',
        'current_adviser': 'NamedAdviserRef',
        'type': 'str',
        'party_type': 'str',
        'person': 'PersonValue',
        'corporate': 'CorporateValue',
        'trust': 'TrustValue',
        'addresses_href': 'str',
        'contactdetails_href': 'str',
        'plans_href': 'str',
        'relationships_href': 'str',
        'servicecases_href': 'str',
        'dependants_href': 'str',
        'is_head_of_family_group': 'bool',
        'servicing_administrator': 'UserReference',
        'paraplanner': 'UserReference',
        'tags': 'list[str]',
        'tax_reference_number': 'str',
        'user': 'UserReference',
        'service_status': 'ServiceStatusValue',
        'client_segment': 'ClientSegmentValue',
        'group': 'GroupRef',
        'household': 'NamedHouseholdReference'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'name': 'name',
        'created_at': 'createdAt',
        'campaign': 'campaign',
        'category': 'category',
        'migration_reference': 'migrationReference',
        'external_reference': 'externalReference',
        'secondary_reference': 'secondaryReference',
        'original_adviser': 'originalAdviser',
        'current_adviser': 'currentAdviser',
        'type': 'type',
        'party_type': 'partyType',
        'person': 'person',
        'corporate': 'corporate',
        'trust': 'trust',
        'addresses_href': 'addresses_href',
        'contactdetails_href': 'contactdetails_href',
        'plans_href': 'plans_href',
        'relationships_href': 'relationships_href',
        'servicecases_href': 'servicecases_href',
        'dependants_href': 'dependants_href',
        'is_head_of_family_group': 'isHeadOfFamilyGroup',
        'servicing_administrator': 'servicingAdministrator',
        'paraplanner': 'paraplanner',
        'tags': 'tags',
        'tax_reference_number': 'taxReferenceNumber',
        'user': 'user',
        'service_status': 'serviceStatus',
        'client_segment': 'clientSegment',
        'group': 'group',
        'household': 'household'
    }

    def __init__(self, id=None, href=None, name=None, created_at=None, campaign=None, category=None, migration_reference=None, external_reference=None, secondary_reference=None, original_adviser=None, current_adviser=None, type=None, party_type=None, person=None, corporate=None, trust=None, addresses_href=None, contactdetails_href=None, plans_href=None, relationships_href=None, servicecases_href=None, dependants_href=None, is_head_of_family_group=None, servicing_administrator=None, paraplanner=None, tags=None, tax_reference_number=None, user=None, service_status=None, client_segment=None, group=None, household=None):  # noqa: E501
        """Client - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._name = None
        self._created_at = None
        self._campaign = None
        self._category = None
        self._migration_reference = None
        self._external_reference = None
        self._secondary_reference = None
        self._original_adviser = None
        self._current_adviser = None
        self._type = None
        self._party_type = None
        self._person = None
        self._corporate = None
        self._trust = None
        self._addresses_href = None
        self._contactdetails_href = None
        self._plans_href = None
        self._relationships_href = None
        self._servicecases_href = None
        self._dependants_href = None
        self._is_head_of_family_group = None
        self._servicing_administrator = None
        self._paraplanner = None
        self._tags = None
        self._tax_reference_number = None
        self._user = None
        self._service_status = None
        self._client_segment = None
        self._group = None
        self._household = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if campaign is not None:
            self.campaign = campaign
        if category is not None:
            self.category = category
        if migration_reference is not None:
            self.migration_reference = migration_reference
        if external_reference is not None:
            self.external_reference = external_reference
        if secondary_reference is not None:
            self.secondary_reference = secondary_reference
        if original_adviser is not None:
            self.original_adviser = original_adviser
        self.current_adviser = current_adviser
        if type is not None:
            self.type = type
        if party_type is not None:
            self.party_type = party_type
        if person is not None:
            self.person = person
        if corporate is not None:
            self.corporate = corporate
        if trust is not None:
            self.trust = trust
        if addresses_href is not None:
            self.addresses_href = addresses_href
        if contactdetails_href is not None:
            self.contactdetails_href = contactdetails_href
        if plans_href is not None:
            self.plans_href = plans_href
        if relationships_href is not None:
            self.relationships_href = relationships_href
        if servicecases_href is not None:
            self.servicecases_href = servicecases_href
        if dependants_href is not None:
            self.dependants_href = dependants_href
        if is_head_of_family_group is not None:
            self.is_head_of_family_group = is_head_of_family_group
        if servicing_administrator is not None:
            self.servicing_administrator = servicing_administrator
        if paraplanner is not None:
            self.paraplanner = paraplanner
        if tags is not None:
            self.tags = tags
        if tax_reference_number is not None:
            self.tax_reference_number = tax_reference_number
        if user is not None:
            self.user = user
        if service_status is not None:
            self.service_status = service_status
        if client_segment is not None:
            self.client_segment = client_segment
        if group is not None:
            self.group = group
        if household is not None:
            self.household = household

    @property
    def id(self):
        """Gets the id of this Client.  # noqa: E501

        The unique identifier for the Client.  # noqa: E501

        :return: The id of this Client.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Client.

        The unique identifier for the Client.  # noqa: E501

        :param id: The id of this Client.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this Client.  # noqa: E501

        The hypertext reference to the Client.  # noqa: E501

        :return: The href of this Client.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Client.

        The hypertext reference to the Client.  # noqa: E501

        :param href: The href of this Client.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def name(self):
        """Gets the name of this Client.  # noqa: E501

        The Client's name. This is derived from the Client's details, for a Person it is their Firstname and Lastname.  # noqa: E501

        :return: The name of this Client.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Client.

        The Client's name. This is derived from the Client's details, for a Person it is their Firstname and Lastname.  # noqa: E501

        :param name: The name of this Client.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this Client.  # noqa: E501

        The date the Client was created.  # noqa: E501

        :return: The created_at of this Client.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Client.

        The date the Client was created.  # noqa: E501

        :param created_at: The created_at of this Client.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def campaign(self):
        """Gets the campaign of this Client.  # noqa: E501


        :return: The campaign of this Client.  # noqa: E501
        :rtype: CampaignValue
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign):
        """Sets the campaign of this Client.


        :param campaign: The campaign of this Client.  # noqa: E501
        :type: CampaignValue
        """

        self._campaign = campaign

    @property
    def category(self):
        """Gets the category of this Client.  # noqa: E501

        The category of Client to which the Client belongs.  # noqa: E501

        :return: The category of this Client.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Client.

        The category of Client to which the Client belongs.  # noqa: E501

        :param category: The category of this Client.  # noqa: E501
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
        """Gets the migration_reference of this Client.  # noqa: E501

        The Client migration reference. Typically a reference set when the Client was imported into the system.  # noqa: E501

        :return: The migration_reference of this Client.  # noqa: E501
        :rtype: str
        """
        return self._migration_reference

    @migration_reference.setter
    def migration_reference(self, migration_reference):
        """Sets the migration_reference of this Client.

        The Client migration reference. Typically a reference set when the Client was imported into the system.  # noqa: E501

        :param migration_reference: The migration_reference of this Client.  # noqa: E501
        :type: str
        """

        self._migration_reference = migration_reference

    @property
    def external_reference(self):
        """Gets the external_reference of this Client.  # noqa: E501

        An external reference for the Client.  # noqa: E501

        :return: The external_reference of this Client.  # noqa: E501
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this Client.

        An external reference for the Client.  # noqa: E501

        :param external_reference: The external_reference of this Client.  # noqa: E501
        :type: str
        """

        self._external_reference = external_reference

    @property
    def secondary_reference(self):
        """Gets the secondary_reference of this Client.  # noqa: E501

        An secondary external reference for the Client.  # noqa: E501

        :return: The secondary_reference of this Client.  # noqa: E501
        :rtype: str
        """
        return self._secondary_reference

    @secondary_reference.setter
    def secondary_reference(self, secondary_reference):
        """Sets the secondary_reference of this Client.

        An secondary external reference for the Client.  # noqa: E501

        :param secondary_reference: The secondary_reference of this Client.  # noqa: E501
        :type: str
        """

        self._secondary_reference = secondary_reference

    @property
    def original_adviser(self):
        """Gets the original_adviser of this Client.  # noqa: E501


        :return: The original_adviser of this Client.  # noqa: E501
        :rtype: NamedAdviserRef
        """
        return self._original_adviser

    @original_adviser.setter
    def original_adviser(self, original_adviser):
        """Sets the original_adviser of this Client.


        :param original_adviser: The original_adviser of this Client.  # noqa: E501
        :type: NamedAdviserRef
        """

        self._original_adviser = original_adviser

    @property
    def current_adviser(self):
        """Gets the current_adviser of this Client.  # noqa: E501


        :return: The current_adviser of this Client.  # noqa: E501
        :rtype: NamedAdviserRef
        """
        return self._current_adviser

    @current_adviser.setter
    def current_adviser(self, current_adviser):
        """Sets the current_adviser of this Client.


        :param current_adviser: The current_adviser of this Client.  # noqa: E501
        :type: NamedAdviserRef
        """
        if current_adviser is None:
            raise ValueError("Invalid value for `current_adviser`, must not be `None`")  # noqa: E501

        self._current_adviser = current_adviser

    @property
    def type(self):
        """Gets the type of this Client.  # noqa: E501


        :return: The type of this Client.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Client.


        :param type: The type of this Client.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def party_type(self):
        """Gets the party_type of this Client.  # noqa: E501

        The type of Client, either Person, Trust or Corporate.  # noqa: E501

        :return: The party_type of this Client.  # noqa: E501
        :rtype: str
        """
        return self._party_type

    @party_type.setter
    def party_type(self, party_type):
        """Sets the party_type of this Client.

        The type of Client, either Person, Trust or Corporate.  # noqa: E501

        :param party_type: The party_type of this Client.  # noqa: E501
        :type: str
        """

        self._party_type = party_type

    @property
    def person(self):
        """Gets the person of this Client.  # noqa: E501


        :return: The person of this Client.  # noqa: E501
        :rtype: PersonValue
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this Client.


        :param person: The person of this Client.  # noqa: E501
        :type: PersonValue
        """

        self._person = person

    @property
    def corporate(self):
        """Gets the corporate of this Client.  # noqa: E501


        :return: The corporate of this Client.  # noqa: E501
        :rtype: CorporateValue
        """
        return self._corporate

    @corporate.setter
    def corporate(self, corporate):
        """Sets the corporate of this Client.


        :param corporate: The corporate of this Client.  # noqa: E501
        :type: CorporateValue
        """

        self._corporate = corporate

    @property
    def trust(self):
        """Gets the trust of this Client.  # noqa: E501


        :return: The trust of this Client.  # noqa: E501
        :rtype: TrustValue
        """
        return self._trust

    @trust.setter
    def trust(self, trust):
        """Sets the trust of this Client.


        :param trust: The trust of this Client.  # noqa: E501
        :type: TrustValue
        """

        self._trust = trust

    @property
    def addresses_href(self):
        """Gets the addresses_href of this Client.  # noqa: E501

        The hypertext reference to the address or addresses held for the Client. Typically these may be a home, work or correspondance address.  # noqa: E501

        :return: The addresses_href of this Client.  # noqa: E501
        :rtype: str
        """
        return self._addresses_href

    @addresses_href.setter
    def addresses_href(self, addresses_href):
        """Sets the addresses_href of this Client.

        The hypertext reference to the address or addresses held for the Client. Typically these may be a home, work or correspondance address.  # noqa: E501

        :param addresses_href: The addresses_href of this Client.  # noqa: E501
        :type: str
        """

        self._addresses_href = addresses_href

    @property
    def contactdetails_href(self):
        """Gets the contactdetails_href of this Client.  # noqa: E501

        The hypertext reference to the list of contact details held for the Client.  # noqa: E501

        :return: The contactdetails_href of this Client.  # noqa: E501
        :rtype: str
        """
        return self._contactdetails_href

    @contactdetails_href.setter
    def contactdetails_href(self, contactdetails_href):
        """Sets the contactdetails_href of this Client.

        The hypertext reference to the list of contact details held for the Client.  # noqa: E501

        :param contactdetails_href: The contactdetails_href of this Client.  # noqa: E501
        :type: str
        """

        self._contactdetails_href = contactdetails_href

    @property
    def plans_href(self):
        """Gets the plans_href of this Client.  # noqa: E501

        The hypertext reference to the list of the Client's plans.  # noqa: E501

        :return: The plans_href of this Client.  # noqa: E501
        :rtype: str
        """
        return self._plans_href

    @plans_href.setter
    def plans_href(self, plans_href):
        """Sets the plans_href of this Client.

        The hypertext reference to the list of the Client's plans.  # noqa: E501

        :param plans_href: The plans_href of this Client.  # noqa: E501
        :type: str
        """

        self._plans_href = plans_href

    @property
    def relationships_href(self):
        """Gets the relationships_href of this Client.  # noqa: E501

        The hypertext reference to the list of any relevant relationships, professional or personal, that the Client may have.  # noqa: E501

        :return: The relationships_href of this Client.  # noqa: E501
        :rtype: str
        """
        return self._relationships_href

    @relationships_href.setter
    def relationships_href(self, relationships_href):
        """Sets the relationships_href of this Client.

        The hypertext reference to the list of any relevant relationships, professional or personal, that the Client may have.  # noqa: E501

        :param relationships_href: The relationships_href of this Client.  # noqa: E501
        :type: str
        """

        self._relationships_href = relationships_href

    @property
    def servicecases_href(self):
        """Gets the servicecases_href of this Client.  # noqa: E501

        The hypertext reference to the Client's service cases.  # noqa: E501

        :return: The servicecases_href of this Client.  # noqa: E501
        :rtype: str
        """
        return self._servicecases_href

    @servicecases_href.setter
    def servicecases_href(self, servicecases_href):
        """Sets the servicecases_href of this Client.

        The hypertext reference to the Client's service cases.  # noqa: E501

        :param servicecases_href: The servicecases_href of this Client.  # noqa: E501
        :type: str
        """

        self._servicecases_href = servicecases_href

    @property
    def dependants_href(self):
        """Gets the dependants_href of this Client.  # noqa: E501

        The hypertext reference to the list of the Client's dependents, if any.  # noqa: E501

        :return: The dependants_href of this Client.  # noqa: E501
        :rtype: str
        """
        return self._dependants_href

    @dependants_href.setter
    def dependants_href(self, dependants_href):
        """Sets the dependants_href of this Client.

        The hypertext reference to the list of the Client's dependents, if any.  # noqa: E501

        :param dependants_href: The dependants_href of this Client.  # noqa: E501
        :type: str
        """

        self._dependants_href = dependants_href

    @property
    def is_head_of_family_group(self):
        """Gets the is_head_of_family_group of this Client.  # noqa: E501

        Flag indicating whether or not the Client is the head of a family group.  # noqa: E501

        :return: The is_head_of_family_group of this Client.  # noqa: E501
        :rtype: bool
        """
        return self._is_head_of_family_group

    @is_head_of_family_group.setter
    def is_head_of_family_group(self, is_head_of_family_group):
        """Sets the is_head_of_family_group of this Client.

        Flag indicating whether or not the Client is the head of a family group.  # noqa: E501

        :param is_head_of_family_group: The is_head_of_family_group of this Client.  # noqa: E501
        :type: bool
        """

        self._is_head_of_family_group = is_head_of_family_group

    @property
    def servicing_administrator(self):
        """Gets the servicing_administrator of this Client.  # noqa: E501


        :return: The servicing_administrator of this Client.  # noqa: E501
        :rtype: UserReference
        """
        return self._servicing_administrator

    @servicing_administrator.setter
    def servicing_administrator(self, servicing_administrator):
        """Sets the servicing_administrator of this Client.


        :param servicing_administrator: The servicing_administrator of this Client.  # noqa: E501
        :type: UserReference
        """

        self._servicing_administrator = servicing_administrator

    @property
    def paraplanner(self):
        """Gets the paraplanner of this Client.  # noqa: E501


        :return: The paraplanner of this Client.  # noqa: E501
        :rtype: UserReference
        """
        return self._paraplanner

    @paraplanner.setter
    def paraplanner(self, paraplanner):
        """Sets the paraplanner of this Client.


        :param paraplanner: The paraplanner of this Client.  # noqa: E501
        :type: UserReference
        """

        self._paraplanner = paraplanner

    @property
    def tags(self):
        """Gets the tags of this Client.  # noqa: E501

        A list of tags associated with the Client. The list can contain up to 30 tags. Each tag has a maximum length of 100 charecters and may not contain spaces.  # noqa: E501

        :return: The tags of this Client.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Client.

        A list of tags associated with the Client. The list can contain up to 30 tags. Each tag has a maximum length of 100 charecters and may not contain spaces.  # noqa: E501

        :param tags: The tags of this Client.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def tax_reference_number(self):
        """Gets the tax_reference_number of this Client.  # noqa: E501

        The Client's tax reference number. The value returned will be obfuscated unless the api is called with the scope of the request set to client_identification_data.  # noqa: E501

        :return: The tax_reference_number of this Client.  # noqa: E501
        :rtype: str
        """
        return self._tax_reference_number

    @tax_reference_number.setter
    def tax_reference_number(self, tax_reference_number):
        """Sets the tax_reference_number of this Client.

        The Client's tax reference number. The value returned will be obfuscated unless the api is called with the scope of the request set to client_identification_data.  # noqa: E501

        :param tax_reference_number: The tax_reference_number of this Client.  # noqa: E501
        :type: str
        """

        self._tax_reference_number = tax_reference_number

    @property
    def user(self):
        """Gets the user of this Client.  # noqa: E501


        :return: The user of this Client.  # noqa: E501
        :rtype: UserReference
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Client.


        :param user: The user of this Client.  # noqa: E501
        :type: UserReference
        """

        self._user = user

    @property
    def service_status(self):
        """Gets the service_status of this Client.  # noqa: E501


        :return: The service_status of this Client.  # noqa: E501
        :rtype: ServiceStatusValue
        """
        return self._service_status

    @service_status.setter
    def service_status(self, service_status):
        """Sets the service_status of this Client.


        :param service_status: The service_status of this Client.  # noqa: E501
        :type: ServiceStatusValue
        """

        self._service_status = service_status

    @property
    def client_segment(self):
        """Gets the client_segment of this Client.  # noqa: E501


        :return: The client_segment of this Client.  # noqa: E501
        :rtype: ClientSegmentValue
        """
        return self._client_segment

    @client_segment.setter
    def client_segment(self, client_segment):
        """Sets the client_segment of this Client.


        :param client_segment: The client_segment of this Client.  # noqa: E501
        :type: ClientSegmentValue
        """

        self._client_segment = client_segment

    @property
    def group(self):
        """Gets the group of this Client.  # noqa: E501


        :return: The group of this Client.  # noqa: E501
        :rtype: GroupRef
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this Client.


        :param group: The group of this Client.  # noqa: E501
        :type: GroupRef
        """

        self._group = group

    @property
    def household(self):
        """Gets the household of this Client.  # noqa: E501


        :return: The household of this Client.  # noqa: E501
        :rtype: NamedHouseholdReference
        """
        return self._household

    @household.setter
    def household(self, household):
        """Sets the household of this Client.


        :param household: The household of this Client.  # noqa: E501
        :type: NamedHouseholdReference
        """

        self._household = household

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
        if issubclass(Client, dict):
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
        if not isinstance(other, Client):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
