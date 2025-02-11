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

class Opportunity(object):
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
        'status': 'OpportunityStatusRef',
        'type': 'OpportunityTypeRef',
        'prospects': 'list[PartyNamedRef]',
        'adviser': 'NamedAdviserRef',
        'potential_initial_income': 'CurrencyValue',
        'potential_ongoing_income': 'CurrencyValue',
        'asset_value': 'CurrencyValue',
        'proposition': 'OpportunityPropositionRef',
        'campaign': 'OpportunityCampaignValue',
        'reference': 'str',
        'service_case': 'ServiceCaseRef',
        'created_on': 'datetime',
        'created_by': 'NamedUserReference',
        'target_closure_on': 'datetime',
        'is_closed': 'bool',
        'closed_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'status': 'status',
        'type': 'type',
        'prospects': 'prospects',
        'adviser': 'adviser',
        'potential_initial_income': 'potentialInitialIncome',
        'potential_ongoing_income': 'potentialOngoingIncome',
        'asset_value': 'assetValue',
        'proposition': 'proposition',
        'campaign': 'campaign',
        'reference': 'reference',
        'service_case': 'serviceCase',
        'created_on': 'createdOn',
        'created_by': 'createdBy',
        'target_closure_on': 'targetClosureOn',
        'is_closed': 'isClosed',
        'closed_date': 'closedDate'
    }

    def __init__(self, id=None, href=None, status=None, type=None, prospects=None, adviser=None, potential_initial_income=None, potential_ongoing_income=None, asset_value=None, proposition=None, campaign=None, reference=None, service_case=None, created_on=None, created_by=None, target_closure_on=None, is_closed=None, closed_date=None):  # noqa: E501
        """Opportunity - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._status = None
        self._type = None
        self._prospects = None
        self._adviser = None
        self._potential_initial_income = None
        self._potential_ongoing_income = None
        self._asset_value = None
        self._proposition = None
        self._campaign = None
        self._reference = None
        self._service_case = None
        self._created_on = None
        self._created_by = None
        self._target_closure_on = None
        self._is_closed = None
        self._closed_date = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if status is not None:
            self.status = status
        self.type = type
        self.prospects = prospects
        if adviser is not None:
            self.adviser = adviser
        if potential_initial_income is not None:
            self.potential_initial_income = potential_initial_income
        if potential_ongoing_income is not None:
            self.potential_ongoing_income = potential_ongoing_income
        if asset_value is not None:
            self.asset_value = asset_value
        if proposition is not None:
            self.proposition = proposition
        if campaign is not None:
            self.campaign = campaign
        if reference is not None:
            self.reference = reference
        if service_case is not None:
            self.service_case = service_case
        self.created_on = created_on
        if created_by is not None:
            self.created_by = created_by
        if target_closure_on is not None:
            self.target_closure_on = target_closure_on
        if is_closed is not None:
            self.is_closed = is_closed
        if closed_date is not None:
            self.closed_date = closed_date

    @property
    def id(self):
        """Gets the id of this Opportunity.  # noqa: E501

        The unique identifier for the Opportunity.  # noqa: E501

        :return: The id of this Opportunity.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Opportunity.

        The unique identifier for the Opportunity.  # noqa: E501

        :param id: The id of this Opportunity.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this Opportunity.  # noqa: E501

        Resource link for this Opportunity.  # noqa: E501

        :return: The href of this Opportunity.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Opportunity.

        Resource link for this Opportunity.  # noqa: E501

        :param href: The href of this Opportunity.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def status(self):
        """Gets the status of this Opportunity.  # noqa: E501


        :return: The status of this Opportunity.  # noqa: E501
        :rtype: OpportunityStatusRef
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Opportunity.


        :param status: The status of this Opportunity.  # noqa: E501
        :type: OpportunityStatusRef
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this Opportunity.  # noqa: E501


        :return: The type of this Opportunity.  # noqa: E501
        :rtype: OpportunityTypeRef
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Opportunity.


        :param type: The type of this Opportunity.  # noqa: E501
        :type: OpportunityTypeRef
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def prospects(self):
        """Gets the prospects of this Opportunity.  # noqa: E501

        Array of the Client/Lead references linked to the Opportunity. The first entry in the array is treated as the primary Prospect. if there is a secondary prospect it will be the second entry in the array.  # noqa: E501

        :return: The prospects of this Opportunity.  # noqa: E501
        :rtype: list[PartyNamedRef]
        """
        return self._prospects

    @prospects.setter
    def prospects(self, prospects):
        """Sets the prospects of this Opportunity.

        Array of the Client/Lead references linked to the Opportunity. The first entry in the array is treated as the primary Prospect. if there is a secondary prospect it will be the second entry in the array.  # noqa: E501

        :param prospects: The prospects of this Opportunity.  # noqa: E501
        :type: list[PartyNamedRef]
        """
        if prospects is None:
            raise ValueError("Invalid value for `prospects`, must not be `None`")  # noqa: E501

        self._prospects = prospects

    @property
    def adviser(self):
        """Gets the adviser of this Opportunity.  # noqa: E501


        :return: The adviser of this Opportunity.  # noqa: E501
        :rtype: NamedAdviserRef
        """
        return self._adviser

    @adviser.setter
    def adviser(self, adviser):
        """Sets the adviser of this Opportunity.


        :param adviser: The adviser of this Opportunity.  # noqa: E501
        :type: NamedAdviserRef
        """

        self._adviser = adviser

    @property
    def potential_initial_income(self):
        """Gets the potential_initial_income of this Opportunity.  # noqa: E501


        :return: The potential_initial_income of this Opportunity.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._potential_initial_income

    @potential_initial_income.setter
    def potential_initial_income(self, potential_initial_income):
        """Sets the potential_initial_income of this Opportunity.


        :param potential_initial_income: The potential_initial_income of this Opportunity.  # noqa: E501
        :type: CurrencyValue
        """

        self._potential_initial_income = potential_initial_income

    @property
    def potential_ongoing_income(self):
        """Gets the potential_ongoing_income of this Opportunity.  # noqa: E501


        :return: The potential_ongoing_income of this Opportunity.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._potential_ongoing_income

    @potential_ongoing_income.setter
    def potential_ongoing_income(self, potential_ongoing_income):
        """Sets the potential_ongoing_income of this Opportunity.


        :param potential_ongoing_income: The potential_ongoing_income of this Opportunity.  # noqa: E501
        :type: CurrencyValue
        """

        self._potential_ongoing_income = potential_ongoing_income

    @property
    def asset_value(self):
        """Gets the asset_value of this Opportunity.  # noqa: E501


        :return: The asset_value of this Opportunity.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        """Sets the asset_value of this Opportunity.


        :param asset_value: The asset_value of this Opportunity.  # noqa: E501
        :type: CurrencyValue
        """

        self._asset_value = asset_value

    @property
    def proposition(self):
        """Gets the proposition of this Opportunity.  # noqa: E501


        :return: The proposition of this Opportunity.  # noqa: E501
        :rtype: OpportunityPropositionRef
        """
        return self._proposition

    @proposition.setter
    def proposition(self, proposition):
        """Sets the proposition of this Opportunity.


        :param proposition: The proposition of this Opportunity.  # noqa: E501
        :type: OpportunityPropositionRef
        """

        self._proposition = proposition

    @property
    def campaign(self):
        """Gets the campaign of this Opportunity.  # noqa: E501


        :return: The campaign of this Opportunity.  # noqa: E501
        :rtype: OpportunityCampaignValue
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign):
        """Sets the campaign of this Opportunity.


        :param campaign: The campaign of this Opportunity.  # noqa: E501
        :type: OpportunityCampaignValue
        """

        self._campaign = campaign

    @property
    def reference(self):
        """Gets the reference of this Opportunity.  # noqa: E501

        The reference for the Opportunity.  # noqa: E501

        :return: The reference of this Opportunity.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Opportunity.

        The reference for the Opportunity.  # noqa: E501

        :param reference: The reference of this Opportunity.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def service_case(self):
        """Gets the service_case of this Opportunity.  # noqa: E501


        :return: The service_case of this Opportunity.  # noqa: E501
        :rtype: ServiceCaseRef
        """
        return self._service_case

    @service_case.setter
    def service_case(self, service_case):
        """Sets the service_case of this Opportunity.


        :param service_case: The service_case of this Opportunity.  # noqa: E501
        :type: ServiceCaseRef
        """

        self._service_case = service_case

    @property
    def created_on(self):
        """Gets the created_on of this Opportunity.  # noqa: E501

        The date the Opportunity was created.  # noqa: E501

        :return: The created_on of this Opportunity.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Opportunity.

        The date the Opportunity was created.  # noqa: E501

        :param created_on: The created_on of this Opportunity.  # noqa: E501
        :type: datetime
        """
        if created_on is None:
            raise ValueError("Invalid value for `created_on`, must not be `None`")  # noqa: E501

        self._created_on = created_on

    @property
    def created_by(self):
        """Gets the created_by of this Opportunity.  # noqa: E501


        :return: The created_by of this Opportunity.  # noqa: E501
        :rtype: NamedUserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Opportunity.


        :param created_by: The created_by of this Opportunity.  # noqa: E501
        :type: NamedUserReference
        """

        self._created_by = created_by

    @property
    def target_closure_on(self):
        """Gets the target_closure_on of this Opportunity.  # noqa: E501

        The targeted date for closure of the Opportunity.  # noqa: E501

        :return: The target_closure_on of this Opportunity.  # noqa: E501
        :rtype: datetime
        """
        return self._target_closure_on

    @target_closure_on.setter
    def target_closure_on(self, target_closure_on):
        """Sets the target_closure_on of this Opportunity.

        The targeted date for closure of the Opportunity.  # noqa: E501

        :param target_closure_on: The target_closure_on of this Opportunity.  # noqa: E501
        :type: datetime
        """

        self._target_closure_on = target_closure_on

    @property
    def is_closed(self):
        """Gets the is_closed of this Opportunity.  # noqa: E501

        Flag indicating if the Opportunity has been closed.  # noqa: E501

        :return: The is_closed of this Opportunity.  # noqa: E501
        :rtype: bool
        """
        return self._is_closed

    @is_closed.setter
    def is_closed(self, is_closed):
        """Sets the is_closed of this Opportunity.

        Flag indicating if the Opportunity has been closed.  # noqa: E501

        :param is_closed: The is_closed of this Opportunity.  # noqa: E501
        :type: bool
        """

        self._is_closed = is_closed

    @property
    def closed_date(self):
        """Gets the closed_date of this Opportunity.  # noqa: E501

        The date the Opportunity was or will closed.  # noqa: E501

        :return: The closed_date of this Opportunity.  # noqa: E501
        :rtype: datetime
        """
        return self._closed_date

    @closed_date.setter
    def closed_date(self, closed_date):
        """Sets the closed_date of this Opportunity.

        The date the Opportunity was or will closed.  # noqa: E501

        :param closed_date: The closed_date of this Opportunity.  # noqa: E501
        :type: datetime
        """

        self._closed_date = closed_date

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
        if issubclass(Opportunity, dict):
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
        if not isinstance(other, Opportunity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
