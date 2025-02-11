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

class ATRQuestionAnswer(object):
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
        'question_id': 'str',
        'answer_id': 'str'
    }

    attribute_map = {
        'question_id': 'questionId',
        'answer_id': 'answerId'
    }

    def __init__(self, question_id=None, answer_id=None):  # noqa: E501
        """ATRQuestionAnswer - a model defined in Swagger"""  # noqa: E501
        self._question_id = None
        self._answer_id = None
        self.discriminator = None
        self.question_id = question_id
        self.answer_id = answer_id

    @property
    def question_id(self):
        """Gets the question_id of this ATRQuestionAnswer.  # noqa: E501


        :return: The question_id of this ATRQuestionAnswer.  # noqa: E501
        :rtype: str
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        """Sets the question_id of this ATRQuestionAnswer.


        :param question_id: The question_id of this ATRQuestionAnswer.  # noqa: E501
        :type: str
        """
        if question_id is None:
            raise ValueError("Invalid value for `question_id`, must not be `None`")  # noqa: E501

        self._question_id = question_id

    @property
    def answer_id(self):
        """Gets the answer_id of this ATRQuestionAnswer.  # noqa: E501


        :return: The answer_id of this ATRQuestionAnswer.  # noqa: E501
        :rtype: str
        """
        return self._answer_id

    @answer_id.setter
    def answer_id(self, answer_id):
        """Sets the answer_id of this ATRQuestionAnswer.


        :param answer_id: The answer_id of this ATRQuestionAnswer.  # noqa: E501
        :type: str
        """
        if answer_id is None:
            raise ValueError("Invalid value for `answer_id`, must not be `None`")  # noqa: E501

        self._answer_id = answer_id

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
        if issubclass(ATRQuestionAnswer, dict):
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
        if not isinstance(other, ATRQuestionAnswer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
