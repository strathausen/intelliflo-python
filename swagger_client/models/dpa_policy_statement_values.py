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

class DpaPolicyStatementValues(object):
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
        'statement1': 'DpaPolicyStatementValue',
        'statement2': 'DpaPolicyStatementValue',
        'statement3': 'DpaPolicyStatementValue',
        'statement4': 'DpaPolicyStatementValue',
        'statement5': 'DpaPolicyStatementValue'
    }

    attribute_map = {
        'statement1': 'statement1',
        'statement2': 'statement2',
        'statement3': 'statement3',
        'statement4': 'statement4',
        'statement5': 'statement5'
    }

    def __init__(self, statement1=None, statement2=None, statement3=None, statement4=None, statement5=None):  # noqa: E501
        """DpaPolicyStatementValues - a model defined in Swagger"""  # noqa: E501
        self._statement1 = None
        self._statement2 = None
        self._statement3 = None
        self._statement4 = None
        self._statement5 = None
        self.discriminator = None
        self.statement1 = statement1
        if statement2 is not None:
            self.statement2 = statement2
        if statement3 is not None:
            self.statement3 = statement3
        if statement4 is not None:
            self.statement4 = statement4
        if statement5 is not None:
            self.statement5 = statement5

    @property
    def statement1(self):
        """Gets the statement1 of this DpaPolicyStatementValues.  # noqa: E501


        :return: The statement1 of this DpaPolicyStatementValues.  # noqa: E501
        :rtype: DpaPolicyStatementValue
        """
        return self._statement1

    @statement1.setter
    def statement1(self, statement1):
        """Sets the statement1 of this DpaPolicyStatementValues.


        :param statement1: The statement1 of this DpaPolicyStatementValues.  # noqa: E501
        :type: DpaPolicyStatementValue
        """
        if statement1 is None:
            raise ValueError("Invalid value for `statement1`, must not be `None`")  # noqa: E501

        self._statement1 = statement1

    @property
    def statement2(self):
        """Gets the statement2 of this DpaPolicyStatementValues.  # noqa: E501


        :return: The statement2 of this DpaPolicyStatementValues.  # noqa: E501
        :rtype: DpaPolicyStatementValue
        """
        return self._statement2

    @statement2.setter
    def statement2(self, statement2):
        """Sets the statement2 of this DpaPolicyStatementValues.


        :param statement2: The statement2 of this DpaPolicyStatementValues.  # noqa: E501
        :type: DpaPolicyStatementValue
        """

        self._statement2 = statement2

    @property
    def statement3(self):
        """Gets the statement3 of this DpaPolicyStatementValues.  # noqa: E501


        :return: The statement3 of this DpaPolicyStatementValues.  # noqa: E501
        :rtype: DpaPolicyStatementValue
        """
        return self._statement3

    @statement3.setter
    def statement3(self, statement3):
        """Sets the statement3 of this DpaPolicyStatementValues.


        :param statement3: The statement3 of this DpaPolicyStatementValues.  # noqa: E501
        :type: DpaPolicyStatementValue
        """

        self._statement3 = statement3

    @property
    def statement4(self):
        """Gets the statement4 of this DpaPolicyStatementValues.  # noqa: E501


        :return: The statement4 of this DpaPolicyStatementValues.  # noqa: E501
        :rtype: DpaPolicyStatementValue
        """
        return self._statement4

    @statement4.setter
    def statement4(self, statement4):
        """Sets the statement4 of this DpaPolicyStatementValues.


        :param statement4: The statement4 of this DpaPolicyStatementValues.  # noqa: E501
        :type: DpaPolicyStatementValue
        """

        self._statement4 = statement4

    @property
    def statement5(self):
        """Gets the statement5 of this DpaPolicyStatementValues.  # noqa: E501


        :return: The statement5 of this DpaPolicyStatementValues.  # noqa: E501
        :rtype: DpaPolicyStatementValue
        """
        return self._statement5

    @statement5.setter
    def statement5(self, statement5):
        """Sets the statement5 of this DpaPolicyStatementValues.


        :param statement5: The statement5 of this DpaPolicyStatementValues.  # noqa: E501
        :type: DpaPolicyStatementValue
        """

        self._statement5 = statement5

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
        if issubclass(DpaPolicyStatementValues, dict):
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
        if not isinstance(other, DpaPolicyStatementValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
