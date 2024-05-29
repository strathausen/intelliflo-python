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

class ClientInvestmentPreferenceQuestionConfiguration(object):
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
        'question_ref': 'ClientInvestmentPreferenceQuestionRef',
        'product_categories': 'list[str]',
        'override_answer_options': 'bool',
        'answer_options': 'list[ClientInvestmentPreferenceAnswerOption]'
    }

    attribute_map = {
        'question_ref': 'questionRef',
        'product_categories': 'productCategories',
        'override_answer_options': 'overrideAnswerOptions',
        'answer_options': 'answerOptions'
    }

    def __init__(self, question_ref=None, product_categories=None, override_answer_options=None, answer_options=None):  # noqa: E501
        """ClientInvestmentPreferenceQuestionConfiguration - a model defined in Swagger"""  # noqa: E501
        self._question_ref = None
        self._product_categories = None
        self._override_answer_options = None
        self._answer_options = None
        self.discriminator = None
        self.question_ref = question_ref
        if product_categories is not None:
            self.product_categories = product_categories
        if override_answer_options is not None:
            self.override_answer_options = override_answer_options
        if answer_options is not None:
            self.answer_options = answer_options

    @property
    def question_ref(self):
        """Gets the question_ref of this ClientInvestmentPreferenceQuestionConfiguration.  # noqa: E501


        :return: The question_ref of this ClientInvestmentPreferenceQuestionConfiguration.  # noqa: E501
        :rtype: ClientInvestmentPreferenceQuestionRef
        """
        return self._question_ref

    @question_ref.setter
    def question_ref(self, question_ref):
        """Sets the question_ref of this ClientInvestmentPreferenceQuestionConfiguration.


        :param question_ref: The question_ref of this ClientInvestmentPreferenceQuestionConfiguration.  # noqa: E501
        :type: ClientInvestmentPreferenceQuestionRef
        """
        if question_ref is None:
            raise ValueError("Invalid value for `question_ref`, must not be `None`")  # noqa: E501

        self._question_ref = question_ref

    @property
    def product_categories(self):
        """Gets the product_categories of this ClientInvestmentPreferenceQuestionConfiguration.  # noqa: E501

        Client InvestmentPreference Question ProductCategories.  # noqa: E501

        :return: The product_categories of this ClientInvestmentPreferenceQuestionConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._product_categories

    @product_categories.setter
    def product_categories(self, product_categories):
        """Sets the product_categories of this ClientInvestmentPreferenceQuestionConfiguration.

        Client InvestmentPreference Question ProductCategories.  # noqa: E501

        :param product_categories: The product_categories of this ClientInvestmentPreferenceQuestionConfiguration.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Retirement", "Investment", "Mortgage", "Protection"]  # noqa: E501
        if not set(product_categories).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `product_categories` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(product_categories) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._product_categories = product_categories

    @property
    def override_answer_options(self):
        """Gets the override_answer_options of this ClientInvestmentPreferenceQuestionConfiguration.  # noqa: E501

        Client InvestmentPreference Override AnswerOptions.  # noqa: E501

        :return: The override_answer_options of this ClientInvestmentPreferenceQuestionConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._override_answer_options

    @override_answer_options.setter
    def override_answer_options(self, override_answer_options):
        """Sets the override_answer_options of this ClientInvestmentPreferenceQuestionConfiguration.

        Client InvestmentPreference Override AnswerOptions.  # noqa: E501

        :param override_answer_options: The override_answer_options of this ClientInvestmentPreferenceQuestionConfiguration.  # noqa: E501
        :type: bool
        """

        self._override_answer_options = override_answer_options

    @property
    def answer_options(self):
        """Gets the answer_options of this ClientInvestmentPreferenceQuestionConfiguration.  # noqa: E501

        Client InvestmentPreference AnswerOptions.  # noqa: E501

        :return: The answer_options of this ClientInvestmentPreferenceQuestionConfiguration.  # noqa: E501
        :rtype: list[ClientInvestmentPreferenceAnswerOption]
        """
        return self._answer_options

    @answer_options.setter
    def answer_options(self, answer_options):
        """Sets the answer_options of this ClientInvestmentPreferenceQuestionConfiguration.

        Client InvestmentPreference AnswerOptions.  # noqa: E501

        :param answer_options: The answer_options of this ClientInvestmentPreferenceQuestionConfiguration.  # noqa: E501
        :type: list[ClientInvestmentPreferenceAnswerOption]
        """

        self._answer_options = answer_options

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
        if issubclass(ClientInvestmentPreferenceQuestionConfiguration, dict):
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
        if not isinstance(other, ClientInvestmentPreferenceQuestionConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
