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

class AtrChosenRiskProfile(object):
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
        'code': 'str',
        'chosen_on': 'datetime',
        'chosen_by': 'UserReference',
        'title': 'str',
        'description': 'str',
        'order': 'int',
        'lower_band': 'int',
        'upper_band': 'int',
        'risk_tolerance': 'str',
        'risk_profile_ref': 'NamedRiskProfileRef'
    }

    attribute_map = {
        'code': 'code',
        'chosen_on': 'chosenOn',
        'chosen_by': 'chosenBy',
        'title': 'title',
        'description': 'description',
        'order': 'order',
        'lower_band': 'lowerBand',
        'upper_band': 'upperBand',
        'risk_tolerance': 'riskTolerance',
        'risk_profile_ref': 'riskProfileRef'
    }

    def __init__(self, code=None, chosen_on=None, chosen_by=None, title=None, description=None, order=None, lower_band=None, upper_band=None, risk_tolerance=None, risk_profile_ref=None):  # noqa: E501
        """AtrChosenRiskProfile - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._chosen_on = None
        self._chosen_by = None
        self._title = None
        self._description = None
        self._order = None
        self._lower_band = None
        self._upper_band = None
        self._risk_tolerance = None
        self._risk_profile_ref = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if chosen_on is not None:
            self.chosen_on = chosen_on
        if chosen_by is not None:
            self.chosen_by = chosen_by
        self.title = title
        if description is not None:
            self.description = description
        self.order = order
        self.lower_band = lower_band
        self.upper_band = upper_band
        if risk_tolerance is not None:
            self.risk_tolerance = risk_tolerance
        if risk_profile_ref is not None:
            self.risk_profile_ref = risk_profile_ref

    @property
    def code(self):
        """Gets the code of this AtrChosenRiskProfile.  # noqa: E501

        Risk profile code chosen by the client.  # noqa: E501

        :return: The code of this AtrChosenRiskProfile.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AtrChosenRiskProfile.

        Risk profile code chosen by the client.  # noqa: E501

        :param code: The code of this AtrChosenRiskProfile.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def chosen_on(self):
        """Gets the chosen_on of this AtrChosenRiskProfile.  # noqa: E501

        Risk profile chosen date.  # noqa: E501

        :return: The chosen_on of this AtrChosenRiskProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._chosen_on

    @chosen_on.setter
    def chosen_on(self, chosen_on):
        """Sets the chosen_on of this AtrChosenRiskProfile.

        Risk profile chosen date.  # noqa: E501

        :param chosen_on: The chosen_on of this AtrChosenRiskProfile.  # noqa: E501
        :type: datetime
        """

        self._chosen_on = chosen_on

    @property
    def chosen_by(self):
        """Gets the chosen_by of this AtrChosenRiskProfile.  # noqa: E501


        :return: The chosen_by of this AtrChosenRiskProfile.  # noqa: E501
        :rtype: UserReference
        """
        return self._chosen_by

    @chosen_by.setter
    def chosen_by(self, chosen_by):
        """Sets the chosen_by of this AtrChosenRiskProfile.


        :param chosen_by: The chosen_by of this AtrChosenRiskProfile.  # noqa: E501
        :type: UserReference
        """

        self._chosen_by = chosen_by

    @property
    def title(self):
        """Gets the title of this AtrChosenRiskProfile.  # noqa: E501

        Risk profile title.  # noqa: E501

        :return: The title of this AtrChosenRiskProfile.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AtrChosenRiskProfile.

        Risk profile title.  # noqa: E501

        :param title: The title of this AtrChosenRiskProfile.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this AtrChosenRiskProfile.  # noqa: E501

        Risk profile description.  # noqa: E501

        :return: The description of this AtrChosenRiskProfile.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AtrChosenRiskProfile.

        Risk profile description.  # noqa: E501

        :param description: The description of this AtrChosenRiskProfile.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def order(self):
        """Gets the order of this AtrChosenRiskProfile.  # noqa: E501

        Risk profile order number.  # noqa: E501

        :return: The order of this AtrChosenRiskProfile.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this AtrChosenRiskProfile.

        Risk profile order number.  # noqa: E501

        :param order: The order of this AtrChosenRiskProfile.  # noqa: E501
        :type: int
        """
        if order is None:
            raise ValueError("Invalid value for `order`, must not be `None`")  # noqa: E501

        self._order = order

    @property
    def lower_band(self):
        """Gets the lower_band of this AtrChosenRiskProfile.  # noqa: E501

        Risk profile lower score limit.  # noqa: E501

        :return: The lower_band of this AtrChosenRiskProfile.  # noqa: E501
        :rtype: int
        """
        return self._lower_band

    @lower_band.setter
    def lower_band(self, lower_band):
        """Sets the lower_band of this AtrChosenRiskProfile.

        Risk profile lower score limit.  # noqa: E501

        :param lower_band: The lower_band of this AtrChosenRiskProfile.  # noqa: E501
        :type: int
        """
        if lower_band is None:
            raise ValueError("Invalid value for `lower_band`, must not be `None`")  # noqa: E501

        self._lower_band = lower_band

    @property
    def upper_band(self):
        """Gets the upper_band of this AtrChosenRiskProfile.  # noqa: E501

        Risk profile upper score limit.  # noqa: E501

        :return: The upper_band of this AtrChosenRiskProfile.  # noqa: E501
        :rtype: int
        """
        return self._upper_band

    @upper_band.setter
    def upper_band(self, upper_band):
        """Sets the upper_band of this AtrChosenRiskProfile.

        Risk profile upper score limit.  # noqa: E501

        :param upper_band: The upper_band of this AtrChosenRiskProfile.  # noqa: E501
        :type: int
        """
        if upper_band is None:
            raise ValueError("Invalid value for `upper_band`, must not be `None`")  # noqa: E501

        self._upper_band = upper_band

    @property
    def risk_tolerance(self):
        """Gets the risk_tolerance of this AtrChosenRiskProfile.  # noqa: E501

        ATR risk tolerance.  # noqa: E501

        :return: The risk_tolerance of this AtrChosenRiskProfile.  # noqa: E501
        :rtype: str
        """
        return self._risk_tolerance

    @risk_tolerance.setter
    def risk_tolerance(self, risk_tolerance):
        """Sets the risk_tolerance of this AtrChosenRiskProfile.

        ATR risk tolerance.  # noqa: E501

        :param risk_tolerance: The risk_tolerance of this AtrChosenRiskProfile.  # noqa: E501
        :type: str
        """

        self._risk_tolerance = risk_tolerance

    @property
    def risk_profile_ref(self):
        """Gets the risk_profile_ref of this AtrChosenRiskProfile.  # noqa: E501


        :return: The risk_profile_ref of this AtrChosenRiskProfile.  # noqa: E501
        :rtype: NamedRiskProfileRef
        """
        return self._risk_profile_ref

    @risk_profile_ref.setter
    def risk_profile_ref(self, risk_profile_ref):
        """Sets the risk_profile_ref of this AtrChosenRiskProfile.


        :param risk_profile_ref: The risk_profile_ref of this AtrChosenRiskProfile.  # noqa: E501
        :type: NamedRiskProfileRef
        """

        self._risk_profile_ref = risk_profile_ref

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
        if issubclass(AtrChosenRiskProfile, dict):
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
        if not isinstance(other, AtrChosenRiskProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
