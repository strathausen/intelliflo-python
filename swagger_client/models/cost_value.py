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

class CostValue(object):
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
        'fee_type': 'str',
        'charge_type': 'str',
        'products_value': 'CostProductsValue'
    }

    attribute_map = {
        'fee_type': 'feeType',
        'charge_type': 'chargeType',
        'products_value': 'productsValue'
    }

    def __init__(self, fee_type=None, charge_type='None', products_value=None):  # noqa: E501
        """CostValue - a model defined in Swagger"""  # noqa: E501
        self._fee_type = None
        self._charge_type = None
        self._products_value = None
        self.discriminator = None
        self.fee_type = fee_type
        if charge_type is not None:
            self.charge_type = charge_type
        if products_value is not None:
            self.products_value = products_value

    @property
    def fee_type(self):
        """Gets the fee_type of this CostValue.  # noqa: E501

        Cost fee type.  # noqa: E501

        :return: The fee_type of this CostValue.  # noqa: E501
        :rtype: str
        """
        return self._fee_type

    @fee_type.setter
    def fee_type(self, fee_type):
        """Sets the fee_type of this CostValue.

        Cost fee type.  # noqa: E501

        :param fee_type: The fee_type of this CostValue.  # noqa: E501
        :type: str
        """
        if fee_type is None:
            raise ValueError("Invalid value for `fee_type`, must not be `None`")  # noqa: E501

        self._fee_type = fee_type

    @property
    def charge_type(self):
        """Gets the charge_type of this CostValue.  # noqa: E501

        Cost charge type.  # noqa: E501

        :return: The charge_type of this CostValue.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this CostValue.

        Cost charge type.  # noqa: E501

        :param charge_type: The charge_type of this CostValue.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "OneOffCharge", "OngoingCharge", "TransactionCost", "IncidentalCost"]  # noqa: E501
        if charge_type not in allowed_values:
            raise ValueError(
                "Invalid value for `charge_type` ({0}), must be one of {1}"  # noqa: E501
                .format(charge_type, allowed_values)
            )

        self._charge_type = charge_type

    @property
    def products_value(self):
        """Gets the products_value of this CostValue.  # noqa: E501


        :return: The products_value of this CostValue.  # noqa: E501
        :rtype: CostProductsValue
        """
        return self._products_value

    @products_value.setter
    def products_value(self, products_value):
        """Sets the products_value of this CostValue.


        :param products_value: The products_value of this CostValue.  # noqa: E501
        :type: CostProductsValue
        """

        self._products_value = products_value

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
        if issubclass(CostValue, dict):
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
        if not isinstance(other, CostValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
