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

class MortgageRedemptionValue3(object):
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
        'terms': 'str',
        '_1st_charge': 'CurrencyValue',
        '_2nd_charge': 'CurrencyValue',
        'expiry_date': 'datetime'
    }

    attribute_map = {
        'terms': 'terms',
        '_1st_charge': '1stCharge',
        '_2nd_charge': '2ndCharge',
        'expiry_date': 'expiryDate'
    }

    def __init__(self, terms='null', _1st_charge=None, _2nd_charge=None, expiry_date=None):  # noqa: E501
        """MortgageRedemptionValue3 - a model defined in Swagger"""  # noqa: E501
        self._terms = None
        self.__1st_charge = None
        self.__2nd_charge = None
        self._expiry_date = None
        self.discriminator = None
        if terms is not None:
            self.terms = terms
        if _1st_charge is not None:
            self._1st_charge = _1st_charge
        if _2nd_charge is not None:
            self._2nd_charge = _2nd_charge
        if expiry_date is not None:
            self.expiry_date = expiry_date

    @property
    def terms(self):
        """Gets the terms of this MortgageRedemptionValue3.  # noqa: E501

        Redemption terms.  # noqa: E501

        :return: The terms of this MortgageRedemptionValue3.  # noqa: E501
        :rtype: str
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this MortgageRedemptionValue3.

        Redemption terms.  # noqa: E501

        :param terms: The terms of this MortgageRedemptionValue3.  # noqa: E501
        :type: str
        """

        self._terms = terms

    @property
    def _1st_charge(self):
        """Gets the _1st_charge of this MortgageRedemptionValue3.  # noqa: E501


        :return: The _1st_charge of this MortgageRedemptionValue3.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self.__1st_charge

    @_1st_charge.setter
    def _1st_charge(self, _1st_charge):
        """Sets the _1st_charge of this MortgageRedemptionValue3.


        :param _1st_charge: The _1st_charge of this MortgageRedemptionValue3.  # noqa: E501
        :type: CurrencyValue
        """

        self.__1st_charge = _1st_charge

    @property
    def _2nd_charge(self):
        """Gets the _2nd_charge of this MortgageRedemptionValue3.  # noqa: E501


        :return: The _2nd_charge of this MortgageRedemptionValue3.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self.__2nd_charge

    @_2nd_charge.setter
    def _2nd_charge(self, _2nd_charge):
        """Sets the _2nd_charge of this MortgageRedemptionValue3.


        :param _2nd_charge: The _2nd_charge of this MortgageRedemptionValue3.  # noqa: E501
        :type: CurrencyValue
        """

        self.__2nd_charge = _2nd_charge

    @property
    def expiry_date(self):
        """Gets the expiry_date of this MortgageRedemptionValue3.  # noqa: E501

        Redemption penalty expiry date.  # noqa: E501

        :return: The expiry_date of this MortgageRedemptionValue3.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this MortgageRedemptionValue3.

        Redemption penalty expiry date.  # noqa: E501

        :param expiry_date: The expiry_date of this MortgageRedemptionValue3.  # noqa: E501
        :type: datetime
        """

        self._expiry_date = expiry_date

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
        if issubclass(MortgageRedemptionValue3, dict):
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
        if not isinstance(other, MortgageRedemptionValue3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
