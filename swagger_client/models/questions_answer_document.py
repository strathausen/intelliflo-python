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

class QuestionsAnswerDocument(object):
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
        'text': 'str',
        'order': 'int',
        'answer': 'str',
        'notes': 'str',
        'options': 'list[QuestionAnswerOption]',
        'is_archived': 'bool',
        'tags': 'list[str]',
        'attributes': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'text': 'text',
        'order': 'order',
        'answer': 'answer',
        'notes': 'notes',
        'options': 'options',
        'is_archived': 'isArchived',
        'tags': 'tags',
        'attributes': 'attributes'
    }

    def __init__(self, id=None, text=None, order=None, answer=None, notes=None, options=None, is_archived=None, tags=None, attributes=None):  # noqa: E501
        """QuestionsAnswerDocument - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._text = None
        self._order = None
        self._answer = None
        self._notes = None
        self._options = None
        self._is_archived = None
        self._tags = None
        self._attributes = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if text is not None:
            self.text = text
        if order is not None:
            self.order = order
        if answer is not None:
            self.answer = answer
        if notes is not None:
            self.notes = notes
        if options is not None:
            self.options = options
        if is_archived is not None:
            self.is_archived = is_archived
        if tags is not None:
            self.tags = tags
        if attributes is not None:
            self.attributes = attributes

    @property
    def id(self):
        """Gets the id of this QuestionsAnswerDocument.  # noqa: E501

        The identifier for the questions answer.  # noqa: E501

        :return: The id of this QuestionsAnswerDocument.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuestionsAnswerDocument.

        The identifier for the questions answer.  # noqa: E501

        :param id: The id of this QuestionsAnswerDocument.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def text(self):
        """Gets the text of this QuestionsAnswerDocument.  # noqa: E501

        The text of the question.  # noqa: E501

        :return: The text of this QuestionsAnswerDocument.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this QuestionsAnswerDocument.

        The text of the question.  # noqa: E501

        :param text: The text of this QuestionsAnswerDocument.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def order(self):
        """Gets the order of this QuestionsAnswerDocument.  # noqa: E501

        The order of the question in a list of questions.  # noqa: E501

        :return: The order of this QuestionsAnswerDocument.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this QuestionsAnswerDocument.

        The order of the question in a list of questions.  # noqa: E501

        :param order: The order of this QuestionsAnswerDocument.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def answer(self):
        """Gets the answer of this QuestionsAnswerDocument.  # noqa: E501

        The answer to the question. The answer(s) to questions that can potentially have multiple answers (type 'select', 'dropdown' or 'checkbox') are held in the options field.  # noqa: E501

        :return: The answer of this QuestionsAnswerDocument.  # noqa: E501
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this QuestionsAnswerDocument.

        The answer to the question. The answer(s) to questions that can potentially have multiple answers (type 'select', 'dropdown' or 'checkbox') are held in the options field.  # noqa: E501

        :param answer: The answer of this QuestionsAnswerDocument.  # noqa: E501
        :type: str
        """

        self._answer = answer

    @property
    def notes(self):
        """Gets the notes of this QuestionsAnswerDocument.  # noqa: E501

        Supplementary notes related to the answer.  # noqa: E501

        :return: The notes of this QuestionsAnswerDocument.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this QuestionsAnswerDocument.

        Supplementary notes related to the answer.  # noqa: E501

        :param notes: The notes of this QuestionsAnswerDocument.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def options(self):
        """Gets the options of this QuestionsAnswerDocument.  # noqa: E501

        The answer(s) to questions of type 'select', 'dropdown' or 'checkbox'.  # noqa: E501

        :return: The options of this QuestionsAnswerDocument.  # noqa: E501
        :rtype: list[QuestionAnswerOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this QuestionsAnswerDocument.

        The answer(s) to questions of type 'select', 'dropdown' or 'checkbox'.  # noqa: E501

        :param options: The options of this QuestionsAnswerDocument.  # noqa: E501
        :type: list[QuestionAnswerOption]
        """

        self._options = options

    @property
    def is_archived(self):
        """Gets the is_archived of this QuestionsAnswerDocument.  # noqa: E501

        Flag indicating whether the question relating to the answer has been archived or not.  # noqa: E501

        :return: The is_archived of this QuestionsAnswerDocument.  # noqa: E501
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """Sets the is_archived of this QuestionsAnswerDocument.

        Flag indicating whether the question relating to the answer has been archived or not.  # noqa: E501

        :param is_archived: The is_archived of this QuestionsAnswerDocument.  # noqa: E501
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def tags(self):
        """Gets the tags of this QuestionsAnswerDocument.  # noqa: E501

        A list of tags associated with the question. Tags are free text and are used to group a series of questions together.  # noqa: E501

        :return: The tags of this QuestionsAnswerDocument.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this QuestionsAnswerDocument.

        A list of tags associated with the question. Tags are free text and are used to group a series of questions together.  # noqa: E501

        :param tags: The tags of this QuestionsAnswerDocument.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def attributes(self):
        """Gets the attributes of this QuestionsAnswerDocument.  # noqa: E501

        Question related attributes.  # noqa: E501

        :return: The attributes of this QuestionsAnswerDocument.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this QuestionsAnswerDocument.

        Question related attributes.  # noqa: E501

        :param attributes: The attributes of this QuestionsAnswerDocument.  # noqa: E501
        :type: dict(str, str)
        """

        self._attributes = attributes

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
        if issubclass(QuestionsAnswerDocument, dict):
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
        if not isinstance(other, QuestionsAnswerDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
