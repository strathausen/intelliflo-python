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

class BaseEmployment(object):
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
        'starts_on': 'datetime',
        'ends_on': 'datetime',
        'occupation': 'str',
        'intended_retirement_age': 'int',
        'employer': 'str',
        'address': 'EmploymentAddressValue',
        'employment_business_type': 'str',
        'in_probation': 'bool',
        'probation_period_in_months': 'int',
        'client': 'ClientRef',
        'incomes_href': 'str',
        'industry_type': 'str',
        'employment_status_description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'starts_on': 'startsOn',
        'ends_on': 'endsOn',
        'occupation': 'occupation',
        'intended_retirement_age': 'intendedRetirementAge',
        'employer': 'employer',
        'address': 'address',
        'employment_business_type': 'employmentBusinessType',
        'in_probation': 'inProbation',
        'probation_period_in_months': 'probationPeriodInMonths',
        'client': 'client',
        'incomes_href': 'incomes_href',
        'industry_type': 'industryType',
        'employment_status_description': 'employmentStatusDescription'
    }

    def __init__(self, id=None, href=None, starts_on=None, ends_on=None, occupation='null', intended_retirement_age=None, employer='null', address=None, employment_business_type='null', in_probation=False, probation_period_in_months=None, client=None, incomes_href=None, industry_type='null', employment_status_description='null'):  # noqa: E501
        """BaseEmployment - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._starts_on = None
        self._ends_on = None
        self._occupation = None
        self._intended_retirement_age = None
        self._employer = None
        self._address = None
        self._employment_business_type = None
        self._in_probation = None
        self._probation_period_in_months = None
        self._client = None
        self._incomes_href = None
        self._industry_type = None
        self._employment_status_description = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if starts_on is not None:
            self.starts_on = starts_on
        if ends_on is not None:
            self.ends_on = ends_on
        if occupation is not None:
            self.occupation = occupation
        if intended_retirement_age is not None:
            self.intended_retirement_age = intended_retirement_age
        if employer is not None:
            self.employer = employer
        if address is not None:
            self.address = address
        if employment_business_type is not None:
            self.employment_business_type = employment_business_type
        if in_probation is not None:
            self.in_probation = in_probation
        if probation_period_in_months is not None:
            self.probation_period_in_months = probation_period_in_months
        if client is not None:
            self.client = client
        if incomes_href is not None:
            self.incomes_href = incomes_href
        if industry_type is not None:
            self.industry_type = industry_type
        if employment_status_description is not None:
            self.employment_status_description = employment_status_description

    @property
    def id(self):
        """Gets the id of this BaseEmployment.  # noqa: E501


        :return: The id of this BaseEmployment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseEmployment.


        :param id: The id of this BaseEmployment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this BaseEmployment.  # noqa: E501


        :return: The href of this BaseEmployment.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BaseEmployment.


        :param href: The href of this BaseEmployment.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def starts_on(self):
        """Gets the starts_on of this BaseEmployment.  # noqa: E501

        Start Date of the employment  # noqa: E501

        :return: The starts_on of this BaseEmployment.  # noqa: E501
        :rtype: datetime
        """
        return self._starts_on

    @starts_on.setter
    def starts_on(self, starts_on):
        """Sets the starts_on of this BaseEmployment.

        Start Date of the employment  # noqa: E501

        :param starts_on: The starts_on of this BaseEmployment.  # noqa: E501
        :type: datetime
        """

        self._starts_on = starts_on

    @property
    def ends_on(self):
        """Gets the ends_on of this BaseEmployment.  # noqa: E501

        End Date of the employment  # noqa: E501

        :return: The ends_on of this BaseEmployment.  # noqa: E501
        :rtype: datetime
        """
        return self._ends_on

    @ends_on.setter
    def ends_on(self, ends_on):
        """Sets the ends_on of this BaseEmployment.

        End Date of the employment  # noqa: E501

        :param ends_on: The ends_on of this BaseEmployment.  # noqa: E501
        :type: datetime
        """

        self._ends_on = ends_on

    @property
    def occupation(self):
        """Gets the occupation of this BaseEmployment.  # noqa: E501

        Description of the occupation of the employment  # noqa: E501

        :return: The occupation of this BaseEmployment.  # noqa: E501
        :rtype: str
        """
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        """Sets the occupation of this BaseEmployment.

        Description of the occupation of the employment  # noqa: E501

        :param occupation: The occupation of this BaseEmployment.  # noqa: E501
        :type: str
        """

        self._occupation = occupation

    @property
    def intended_retirement_age(self):
        """Gets the intended_retirement_age of this BaseEmployment.  # noqa: E501

        Intended Retirement Age  # noqa: E501

        :return: The intended_retirement_age of this BaseEmployment.  # noqa: E501
        :rtype: int
        """
        return self._intended_retirement_age

    @intended_retirement_age.setter
    def intended_retirement_age(self, intended_retirement_age):
        """Sets the intended_retirement_age of this BaseEmployment.

        Intended Retirement Age  # noqa: E501

        :param intended_retirement_age: The intended_retirement_age of this BaseEmployment.  # noqa: E501
        :type: int
        """

        self._intended_retirement_age = intended_retirement_age

    @property
    def employer(self):
        """Gets the employer of this BaseEmployment.  # noqa: E501

        Employer's name.  # noqa: E501

        :return: The employer of this BaseEmployment.  # noqa: E501
        :rtype: str
        """
        return self._employer

    @employer.setter
    def employer(self, employer):
        """Sets the employer of this BaseEmployment.

        Employer's name.  # noqa: E501

        :param employer: The employer of this BaseEmployment.  # noqa: E501
        :type: str
        """

        self._employer = employer

    @property
    def address(self):
        """Gets the address of this BaseEmployment.  # noqa: E501


        :return: The address of this BaseEmployment.  # noqa: E501
        :rtype: EmploymentAddressValue
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this BaseEmployment.


        :param address: The address of this BaseEmployment.  # noqa: E501
        :type: EmploymentAddressValue
        """

        self._address = address

    @property
    def employment_business_type(self):
        """Gets the employment_business_type of this BaseEmployment.  # noqa: E501

        Employment Business type, settable for business types: Sole Trader, Private Limited Company, Partnership, Limited Liability Partnership  # noqa: E501

        :return: The employment_business_type of this BaseEmployment.  # noqa: E501
        :rtype: str
        """
        return self._employment_business_type

    @employment_business_type.setter
    def employment_business_type(self, employment_business_type):
        """Sets the employment_business_type of this BaseEmployment.

        Employment Business type, settable for business types: Sole Trader, Private Limited Company, Partnership, Limited Liability Partnership  # noqa: E501

        :param employment_business_type: The employment_business_type of this BaseEmployment.  # noqa: E501
        :type: str
        """
        allowed_values = ["SoleTrader", "PrivateLimitedCompany", "Partnership", "LimitedLiabilityPartnership"]  # noqa: E501
        if employment_business_type not in allowed_values:
            raise ValueError(
                "Invalid value for `employment_business_type` ({0}), must be one of {1}"  # noqa: E501
                .format(employment_business_type, allowed_values)
            )

        self._employment_business_type = employment_business_type

    @property
    def in_probation(self):
        """Gets the in_probation of this BaseEmployment.  # noqa: E501

        In Probation flag, settable for statuses: Employed, MaternityLeave, LongTermIllness  # noqa: E501

        :return: The in_probation of this BaseEmployment.  # noqa: E501
        :rtype: bool
        """
        return self._in_probation

    @in_probation.setter
    def in_probation(self, in_probation):
        """Sets the in_probation of this BaseEmployment.

        In Probation flag, settable for statuses: Employed, MaternityLeave, LongTermIllness  # noqa: E501

        :param in_probation: The in_probation of this BaseEmployment.  # noqa: E501
        :type: bool
        """

        self._in_probation = in_probation

    @property
    def probation_period_in_months(self):
        """Gets the probation_period_in_months of this BaseEmployment.  # noqa: E501

        Settable when InProbation is set to 'true' and for statuses: Employed, MaternityLeave, LongTermIllness  # noqa: E501

        :return: The probation_period_in_months of this BaseEmployment.  # noqa: E501
        :rtype: int
        """
        return self._probation_period_in_months

    @probation_period_in_months.setter
    def probation_period_in_months(self, probation_period_in_months):
        """Sets the probation_period_in_months of this BaseEmployment.

        Settable when InProbation is set to 'true' and for statuses: Employed, MaternityLeave, LongTermIllness  # noqa: E501

        :param probation_period_in_months: The probation_period_in_months of this BaseEmployment.  # noqa: E501
        :type: int
        """

        self._probation_period_in_months = probation_period_in_months

    @property
    def client(self):
        """Gets the client of this BaseEmployment.  # noqa: E501


        :return: The client of this BaseEmployment.  # noqa: E501
        :rtype: ClientRef
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this BaseEmployment.


        :param client: The client of this BaseEmployment.  # noqa: E501
        :type: ClientRef
        """

        self._client = client

    @property
    def incomes_href(self):
        """Gets the incomes_href of this BaseEmployment.  # noqa: E501

        Incomes reference  # noqa: E501

        :return: The incomes_href of this BaseEmployment.  # noqa: E501
        :rtype: str
        """
        return self._incomes_href

    @incomes_href.setter
    def incomes_href(self, incomes_href):
        """Sets the incomes_href of this BaseEmployment.

        Incomes reference  # noqa: E501

        :param incomes_href: The incomes_href of this BaseEmployment.  # noqa: E501
        :type: str
        """

        self._incomes_href = incomes_href

    @property
    def industry_type(self):
        """Gets the industry_type of this BaseEmployment.  # noqa: E501

        IndustryType.  # noqa: E501

        :return: The industry_type of this BaseEmployment.  # noqa: E501
        :rtype: str
        """
        return self._industry_type

    @industry_type.setter
    def industry_type(self, industry_type):
        """Sets the industry_type of this BaseEmployment.

        IndustryType.  # noqa: E501

        :param industry_type: The industry_type of this BaseEmployment.  # noqa: E501
        :type: str
        """

        self._industry_type = industry_type

    @property
    def employment_status_description(self):
        """Gets the employment_status_description of this BaseEmployment.  # noqa: E501

        Employment Status Description.  # noqa: E501

        :return: The employment_status_description of this BaseEmployment.  # noqa: E501
        :rtype: str
        """
        return self._employment_status_description

    @employment_status_description.setter
    def employment_status_description(self, employment_status_description):
        """Sets the employment_status_description of this BaseEmployment.

        Employment Status Description.  # noqa: E501

        :param employment_status_description: The employment_status_description of this BaseEmployment.  # noqa: E501
        :type: str
        """

        self._employment_status_description = employment_status_description

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
        if issubclass(BaseEmployment, dict):
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
        if not isinstance(other, BaseEmployment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
