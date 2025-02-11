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

class UnmatchedPlan(object):
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
        'plan_type': 'PlanTypeShortReference',
        'owners': 'list[NamedOwnerRef]',
        'address': 'AddressValueRef',
        'policy_number': 'str',
        'product_name': 'str',
        'selling_adviser': 'NamedAdviserRef',
        'product_provider': 'NamedProductProviderRef',
        'provider_codes': 'ProviderCodesValue',
        'group': 'GroupRef',
        'created_at': 'datetime',
        'changed_at': 'datetime',
        'sort_code': 'str',
        'program_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'plan_type': 'planType',
        'owners': 'owners',
        'address': 'address',
        'policy_number': 'policyNumber',
        'product_name': 'productName',
        'selling_adviser': 'sellingAdviser',
        'product_provider': 'productProvider',
        'provider_codes': 'providerCodes',
        'group': 'group',
        'created_at': 'createdAt',
        'changed_at': 'changedAt',
        'sort_code': 'sortCode',
        'program_id': 'programId'
    }

    def __init__(self, id=None, href=None, plan_type=None, owners=None, address=None, policy_number='null', product_name='null', selling_adviser=None, product_provider=None, provider_codes=None, group=None, created_at=None, changed_at=None, sort_code='null', program_id=None):  # noqa: E501
        """UnmatchedPlan - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._plan_type = None
        self._owners = None
        self._address = None
        self._policy_number = None
        self._product_name = None
        self._selling_adviser = None
        self._product_provider = None
        self._provider_codes = None
        self._group = None
        self._created_at = None
        self._changed_at = None
        self._sort_code = None
        self._program_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        self.plan_type = plan_type
        if owners is not None:
            self.owners = owners
        if address is not None:
            self.address = address
        if policy_number is not None:
            self.policy_number = policy_number
        if product_name is not None:
            self.product_name = product_name
        self.selling_adviser = selling_adviser
        self.product_provider = product_provider
        if provider_codes is not None:
            self.provider_codes = provider_codes
        if group is not None:
            self.group = group
        if created_at is not None:
            self.created_at = created_at
        if changed_at is not None:
            self.changed_at = changed_at
        if sort_code is not None:
            self.sort_code = sort_code
        if program_id is not None:
            self.program_id = program_id

    @property
    def id(self):
        """Gets the id of this UnmatchedPlan.  # noqa: E501

        The UnMatched Plan Identifier.  # noqa: E501

        :return: The id of this UnmatchedPlan.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UnmatchedPlan.

        The UnMatched Plan Identifier.  # noqa: E501

        :param id: The id of this UnmatchedPlan.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this UnmatchedPlan.  # noqa: E501

        The Plan Reference.  # noqa: E501

        :return: The href of this UnmatchedPlan.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this UnmatchedPlan.

        The Plan Reference.  # noqa: E501

        :param href: The href of this UnmatchedPlan.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def plan_type(self):
        """Gets the plan_type of this UnmatchedPlan.  # noqa: E501


        :return: The plan_type of this UnmatchedPlan.  # noqa: E501
        :rtype: PlanTypeShortReference
        """
        return self._plan_type

    @plan_type.setter
    def plan_type(self, plan_type):
        """Sets the plan_type of this UnmatchedPlan.


        :param plan_type: The plan_type of this UnmatchedPlan.  # noqa: E501
        :type: PlanTypeShortReference
        """
        if plan_type is None:
            raise ValueError("Invalid value for `plan_type`, must not be `None`")  # noqa: E501

        self._plan_type = plan_type

    @property
    def owners(self):
        """Gets the owners of this UnmatchedPlan.  # noqa: E501

        Each plan can have one or more owners. The Client could be purchasing the product on behalf of someone else.  # noqa: E501

        :return: The owners of this UnmatchedPlan.  # noqa: E501
        :rtype: list[NamedOwnerRef]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Sets the owners of this UnmatchedPlan.

        Each plan can have one or more owners. The Client could be purchasing the product on behalf of someone else.  # noqa: E501

        :param owners: The owners of this UnmatchedPlan.  # noqa: E501
        :type: list[NamedOwnerRef]
        """

        self._owners = owners

    @property
    def address(self):
        """Gets the address of this UnmatchedPlan.  # noqa: E501


        :return: The address of this UnmatchedPlan.  # noqa: E501
        :rtype: AddressValueRef
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this UnmatchedPlan.


        :param address: The address of this UnmatchedPlan.  # noqa: E501
        :type: AddressValueRef
        """

        self._address = address

    @property
    def policy_number(self):
        """Gets the policy_number of this UnmatchedPlan.  # noqa: E501

        Unique reference number to the Client's Plan as issued by the Platform Provider.  # noqa: E501

        :return: The policy_number of this UnmatchedPlan.  # noqa: E501
        :rtype: str
        """
        return self._policy_number

    @policy_number.setter
    def policy_number(self, policy_number):
        """Sets the policy_number of this UnmatchedPlan.

        Unique reference number to the Client's Plan as issued by the Platform Provider.  # noqa: E501

        :param policy_number: The policy_number of this UnmatchedPlan.  # noqa: E501
        :type: str
        """

        self._policy_number = policy_number

    @property
    def product_name(self):
        """Gets the product_name of this UnmatchedPlan.  # noqa: E501

        Optional name which would usually be the market name of the product.  # noqa: E501

        :return: The product_name of this UnmatchedPlan.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this UnmatchedPlan.

        Optional name which would usually be the market name of the product.  # noqa: E501

        :param product_name: The product_name of this UnmatchedPlan.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def selling_adviser(self):
        """Gets the selling_adviser of this UnmatchedPlan.  # noqa: E501


        :return: The selling_adviser of this UnmatchedPlan.  # noqa: E501
        :rtype: NamedAdviserRef
        """
        return self._selling_adviser

    @selling_adviser.setter
    def selling_adviser(self, selling_adviser):
        """Sets the selling_adviser of this UnmatchedPlan.


        :param selling_adviser: The selling_adviser of this UnmatchedPlan.  # noqa: E501
        :type: NamedAdviserRef
        """
        if selling_adviser is None:
            raise ValueError("Invalid value for `selling_adviser`, must not be `None`")  # noqa: E501

        self._selling_adviser = selling_adviser

    @property
    def product_provider(self):
        """Gets the product_provider of this UnmatchedPlan.  # noqa: E501


        :return: The product_provider of this UnmatchedPlan.  # noqa: E501
        :rtype: NamedProductProviderRef
        """
        return self._product_provider

    @product_provider.setter
    def product_provider(self, product_provider):
        """Sets the product_provider of this UnmatchedPlan.


        :param product_provider: The product_provider of this UnmatchedPlan.  # noqa: E501
        :type: NamedProductProviderRef
        """
        if product_provider is None:
            raise ValueError("Invalid value for `product_provider`, must not be `None`")  # noqa: E501

        self._product_provider = product_provider

    @property
    def provider_codes(self):
        """Gets the provider_codes of this UnmatchedPlan.  # noqa: E501


        :return: The provider_codes of this UnmatchedPlan.  # noqa: E501
        :rtype: ProviderCodesValue
        """
        return self._provider_codes

    @provider_codes.setter
    def provider_codes(self, provider_codes):
        """Sets the provider_codes of this UnmatchedPlan.


        :param provider_codes: The provider_codes of this UnmatchedPlan.  # noqa: E501
        :type: ProviderCodesValue
        """

        self._provider_codes = provider_codes

    @property
    def group(self):
        """Gets the group of this UnmatchedPlan.  # noqa: E501


        :return: The group of this UnmatchedPlan.  # noqa: E501
        :rtype: GroupRef
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this UnmatchedPlan.


        :param group: The group of this UnmatchedPlan.  # noqa: E501
        :type: GroupRef
        """

        self._group = group

    @property
    def created_at(self):
        """Gets the created_at of this UnmatchedPlan.  # noqa: E501

        Created Date.  # noqa: E501

        :return: The created_at of this UnmatchedPlan.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UnmatchedPlan.

        Created Date.  # noqa: E501

        :param created_at: The created_at of this UnmatchedPlan.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def changed_at(self):
        """Gets the changed_at of this UnmatchedPlan.  # noqa: E501

        Last Updated Date.  # noqa: E501

        :return: The changed_at of this UnmatchedPlan.  # noqa: E501
        :rtype: datetime
        """
        return self._changed_at

    @changed_at.setter
    def changed_at(self, changed_at):
        """Sets the changed_at of this UnmatchedPlan.

        Last Updated Date.  # noqa: E501

        :param changed_at: The changed_at of this UnmatchedPlan.  # noqa: E501
        :type: datetime
        """

        self._changed_at = changed_at

    @property
    def sort_code(self):
        """Gets the sort_code of this UnmatchedPlan.  # noqa: E501

        Sort code/routing number/branch code are domestic bank codes used to route money transfers between financial institutions.  # noqa: E501

        :return: The sort_code of this UnmatchedPlan.  # noqa: E501
        :rtype: str
        """
        return self._sort_code

    @sort_code.setter
    def sort_code(self, sort_code):
        """Sets the sort_code of this UnmatchedPlan.

        Sort code/routing number/branch code are domestic bank codes used to route money transfers between financial institutions.  # noqa: E501

        :param sort_code: The sort_code of this UnmatchedPlan.  # noqa: E501
        :type: str
        """

        self._sort_code = sort_code

    @property
    def program_id(self):
        """Gets the program_id of this UnmatchedPlan.  # noqa: E501

        The program identifier.  # noqa: E501

        :return: The program_id of this UnmatchedPlan.  # noqa: E501
        :rtype: int
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id):
        """Sets the program_id of this UnmatchedPlan.

        The program identifier.  # noqa: E501

        :param program_id: The program_id of this UnmatchedPlan.  # noqa: E501
        :type: int
        """

        self._program_id = program_id

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
        if issubclass(UnmatchedPlan, dict):
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
        if not isinstance(other, UnmatchedPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
