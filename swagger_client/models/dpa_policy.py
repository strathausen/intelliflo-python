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

class DPAPolicy(object):
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
        'created_at': 'datetime',
        'name': 'str',
        'is_editable': 'bool',
        'statements': 'DpaPolicyStatementValues',
        'tag': 'str',
        'client_can_accept': 'bool',
        'party_type': 'str',
        'has_agreements': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'created_at': 'createdAt',
        'name': 'name',
        'is_editable': 'isEditable',
        'statements': 'statements',
        'tag': 'tag',
        'client_can_accept': 'clientCanAccept',
        'party_type': 'partyType',
        'has_agreements': 'hasAgreements'
    }

    def __init__(self, id=None, href=None, created_at=None, name=None, is_editable=None, statements=None, tag=None, client_can_accept=None, party_type=None, has_agreements=None):  # noqa: E501
        """DPAPolicy - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._created_at = None
        self._name = None
        self._is_editable = None
        self._statements = None
        self._tag = None
        self._client_can_accept = None
        self._party_type = None
        self._has_agreements = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if created_at is not None:
            self.created_at = created_at
        self.name = name
        if is_editable is not None:
            self.is_editable = is_editable
        if statements is not None:
            self.statements = statements
        if tag is not None:
            self.tag = tag
        if client_can_accept is not None:
            self.client_can_accept = client_can_accept
        if party_type is not None:
            self.party_type = party_type
        if has_agreements is not None:
            self.has_agreements = has_agreements

    @property
    def id(self):
        """Gets the id of this DPAPolicy.  # noqa: E501

        Id of DPA policy  # noqa: E501

        :return: The id of this DPAPolicy.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DPAPolicy.

        Id of DPA policy  # noqa: E501

        :param id: The id of this DPAPolicy.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this DPAPolicy.  # noqa: E501

        Hyperlink to DPA policy  # noqa: E501

        :return: The href of this DPAPolicy.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this DPAPolicy.

        Hyperlink to DPA policy  # noqa: E501

        :param href: The href of this DPAPolicy.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def created_at(self):
        """Gets the created_at of this DPAPolicy.  # noqa: E501

        DPA Policy creation date  # noqa: E501

        :return: The created_at of this DPAPolicy.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DPAPolicy.

        DPA Policy creation date  # noqa: E501

        :param created_at: The created_at of this DPAPolicy.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def name(self):
        """Gets the name of this DPAPolicy.  # noqa: E501

        DPA Policy name  # noqa: E501

        :return: The name of this DPAPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DPAPolicy.

        DPA Policy name  # noqa: E501

        :param name: The name of this DPAPolicy.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def is_editable(self):
        """Gets the is_editable of this DPAPolicy.  # noqa: E501

        This field specifies if DPA policy can be edited  # noqa: E501

        :return: The is_editable of this DPAPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._is_editable

    @is_editable.setter
    def is_editable(self, is_editable):
        """Sets the is_editable of this DPAPolicy.

        This field specifies if DPA policy can be edited  # noqa: E501

        :param is_editable: The is_editable of this DPAPolicy.  # noqa: E501
        :type: bool
        """

        self._is_editable = is_editable

    @property
    def statements(self):
        """Gets the statements of this DPAPolicy.  # noqa: E501


        :return: The statements of this DPAPolicy.  # noqa: E501
        :rtype: DpaPolicyStatementValues
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """Sets the statements of this DPAPolicy.


        :param statements: The statements of this DPAPolicy.  # noqa: E501
        :type: DpaPolicyStatementValues
        """

        self._statements = statements

    @property
    def tag(self):
        """Gets the tag of this DPAPolicy.  # noqa: E501

        DPA Policy Tag  # noqa: E501

        :return: The tag of this DPAPolicy.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this DPAPolicy.

        DPA Policy Tag  # noqa: E501

        :param tag: The tag of this DPAPolicy.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def client_can_accept(self):
        """Gets the client_can_accept of this DPAPolicy.  # noqa: E501

        Specifies whether DPA policy can be accepted by the clients.  # noqa: E501

        :return: The client_can_accept of this DPAPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._client_can_accept

    @client_can_accept.setter
    def client_can_accept(self, client_can_accept):
        """Sets the client_can_accept of this DPAPolicy.

        Specifies whether DPA policy can be accepted by the clients.  # noqa: E501

        :param client_can_accept: The client_can_accept of this DPAPolicy.  # noqa: E501
        :type: bool
        """

        self._client_can_accept = client_can_accept

    @property
    def party_type(self):
        """Gets the party_type of this DPAPolicy.  # noqa: E501

        DPA Party Type. If no party type is specified, the DPA is a default DPA for all party types that do not specifica DPA set.  # noqa: E501

        :return: The party_type of this DPAPolicy.  # noqa: E501
        :rtype: str
        """
        return self._party_type

    @party_type.setter
    def party_type(self, party_type):
        """Sets the party_type of this DPAPolicy.

        DPA Party Type. If no party type is specified, the DPA is a default DPA for all party types that do not specifica DPA set.  # noqa: E501

        :param party_type: The party_type of this DPAPolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["Person", "Corporate", "Trust"]  # noqa: E501
        if party_type not in allowed_values:
            raise ValueError(
                "Invalid value for `party_type` ({0}), must be one of {1}"  # noqa: E501
                .format(party_type, allowed_values)
            )

        self._party_type = party_type

    @property
    def has_agreements(self):
        """Gets the has_agreements of this DPAPolicy.  # noqa: E501

        Field indicating if DPAs exist for the policy.  # noqa: E501

        :return: The has_agreements of this DPAPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._has_agreements

    @has_agreements.setter
    def has_agreements(self, has_agreements):
        """Sets the has_agreements of this DPAPolicy.

        Field indicating if DPAs exist for the policy.  # noqa: E501

        :param has_agreements: The has_agreements of this DPAPolicy.  # noqa: E501
        :type: bool
        """

        self._has_agreements = has_agreements

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
        if issubclass(DPAPolicy, dict):
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
        if not isinstance(other, DPAPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
