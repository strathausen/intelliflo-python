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

class BaseWithdrawal(object):
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
        'plan': 'PlanProviderRef',
        'value': 'CurrencyValue',
        'frequency': 'str',
        'percentage': 'float',
        'starts_on': 'datetime',
        'stops_on': 'datetime',
        'note': 'str',
        'escalation': 'EscalationValue',
        'contribution': 'ContributionRef'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'plan': 'plan',
        'value': 'value',
        'frequency': 'frequency',
        'percentage': 'percentage',
        'starts_on': 'startsOn',
        'stops_on': 'stopsOn',
        'note': 'note',
        'escalation': 'escalation',
        'contribution': 'contribution'
    }

    def __init__(self, id=None, href=None, plan=None, value=None, frequency='Single', percentage=None, starts_on=None, stops_on=None, note=None, escalation=None, contribution=None):  # noqa: E501
        """BaseWithdrawal - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._plan = None
        self._value = None
        self._frequency = None
        self._percentage = None
        self._starts_on = None
        self._stops_on = None
        self._note = None
        self._escalation = None
        self._contribution = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if plan is not None:
            self.plan = plan
        self.value = value
        self.frequency = frequency
        if percentage is not None:
            self.percentage = percentage
        self.starts_on = starts_on
        if stops_on is not None:
            self.stops_on = stops_on
        if note is not None:
            self.note = note
        if escalation is not None:
            self.escalation = escalation
        if contribution is not None:
            self.contribution = contribution

    @property
    def id(self):
        """Gets the id of this BaseWithdrawal.  # noqa: E501

        Withdrawal identifier.  # noqa: E501

        :return: The id of this BaseWithdrawal.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseWithdrawal.

        Withdrawal identifier.  # noqa: E501

        :param id: The id of this BaseWithdrawal.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this BaseWithdrawal.  # noqa: E501

        Withdrawal reference.  # noqa: E501

        :return: The href of this BaseWithdrawal.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BaseWithdrawal.

        Withdrawal reference.  # noqa: E501

        :param href: The href of this BaseWithdrawal.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def plan(self):
        """Gets the plan of this BaseWithdrawal.  # noqa: E501


        :return: The plan of this BaseWithdrawal.  # noqa: E501
        :rtype: PlanProviderRef
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this BaseWithdrawal.


        :param plan: The plan of this BaseWithdrawal.  # noqa: E501
        :type: PlanProviderRef
        """

        self._plan = plan

    @property
    def value(self):
        """Gets the value of this BaseWithdrawal.  # noqa: E501


        :return: The value of this BaseWithdrawal.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BaseWithdrawal.


        :param value: The value of this BaseWithdrawal.  # noqa: E501
        :type: CurrencyValue
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def frequency(self):
        """Gets the frequency of this BaseWithdrawal.  # noqa: E501

        Frequency type.  # noqa: E501

        :return: The frequency of this BaseWithdrawal.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this BaseWithdrawal.

        Frequency type.  # noqa: E501

        :param frequency: The frequency of this BaseWithdrawal.  # noqa: E501
        :type: str
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "Weekly", "Fortnightly", "FourWeekly", "Monthly", "Quarterly", "HalfYearly", "Annually", "Single"]  # noqa: E501
        if frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(frequency, allowed_values)
            )

        self._frequency = frequency

    @property
    def percentage(self):
        """Gets the percentage of this BaseWithdrawal.  # noqa: E501

        Percentage value, used for percentage based types only as PercentageOfInvestment or PercentageOfFund.  # noqa: E501

        :return: The percentage of this BaseWithdrawal.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this BaseWithdrawal.

        Percentage value, used for percentage based types only as PercentageOfInvestment or PercentageOfFund.  # noqa: E501

        :param percentage: The percentage of this BaseWithdrawal.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def starts_on(self):
        """Gets the starts_on of this BaseWithdrawal.  # noqa: E501

        The date when the withdrawal started.  # noqa: E501

        :return: The starts_on of this BaseWithdrawal.  # noqa: E501
        :rtype: datetime
        """
        return self._starts_on

    @starts_on.setter
    def starts_on(self, starts_on):
        """Sets the starts_on of this BaseWithdrawal.

        The date when the withdrawal started.  # noqa: E501

        :param starts_on: The starts_on of this BaseWithdrawal.  # noqa: E501
        :type: datetime
        """
        if starts_on is None:
            raise ValueError("Invalid value for `starts_on`, must not be `None`")  # noqa: E501

        self._starts_on = starts_on

    @property
    def stops_on(self):
        """Gets the stops_on of this BaseWithdrawal.  # noqa: E501

        The date when the withdrawal will stop. Needed for Regular withdrawal types only.  # noqa: E501

        :return: The stops_on of this BaseWithdrawal.  # noqa: E501
        :rtype: datetime
        """
        return self._stops_on

    @stops_on.setter
    def stops_on(self, stops_on):
        """Sets the stops_on of this BaseWithdrawal.

        The date when the withdrawal will stop. Needed for Regular withdrawal types only.  # noqa: E501

        :param stops_on: The stops_on of this BaseWithdrawal.  # noqa: E501
        :type: datetime
        """

        self._stops_on = stops_on

    @property
    def note(self):
        """Gets the note of this BaseWithdrawal.  # noqa: E501

        Represents additional details about this resource.  # noqa: E501

        :return: The note of this BaseWithdrawal.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this BaseWithdrawal.

        Represents additional details about this resource.  # noqa: E501

        :param note: The note of this BaseWithdrawal.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def escalation(self):
        """Gets the escalation of this BaseWithdrawal.  # noqa: E501


        :return: The escalation of this BaseWithdrawal.  # noqa: E501
        :rtype: EscalationValue
        """
        return self._escalation

    @escalation.setter
    def escalation(self, escalation):
        """Sets the escalation of this BaseWithdrawal.


        :param escalation: The escalation of this BaseWithdrawal.  # noqa: E501
        :type: EscalationValue
        """

        self._escalation = escalation

    @property
    def contribution(self):
        """Gets the contribution of this BaseWithdrawal.  # noqa: E501


        :return: The contribution of this BaseWithdrawal.  # noqa: E501
        :rtype: ContributionRef
        """
        return self._contribution

    @contribution.setter
    def contribution(self, contribution):
        """Sets the contribution of this BaseWithdrawal.


        :param contribution: The contribution of this BaseWithdrawal.  # noqa: E501
        :type: ContributionRef
        """

        self._contribution = contribution

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
        if issubclass(BaseWithdrawal, dict):
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
        if not isinstance(other, BaseWithdrawal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
