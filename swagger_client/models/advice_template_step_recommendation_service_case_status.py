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

class AdviceTemplateStepRecommendationServiceCaseStatus(object):
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
        'on_step': 'NamedServiceCaseStatusRef',
        'on_accept': 'NamedServiceCaseStatusRef',
        'on_reject': 'NamedServiceCaseStatusRef'
    }

    attribute_map = {
        'on_step': 'onStep',
        'on_accept': 'onAccept',
        'on_reject': 'onReject'
    }

    def __init__(self, on_step=None, on_accept=None, on_reject=None):  # noqa: E501
        """AdviceTemplateStepRecommendationServiceCaseStatus - a model defined in Swagger"""  # noqa: E501
        self._on_step = None
        self._on_accept = None
        self._on_reject = None
        self.discriminator = None
        if on_step is not None:
            self.on_step = on_step
        if on_accept is not None:
            self.on_accept = on_accept
        if on_reject is not None:
            self.on_reject = on_reject

    @property
    def on_step(self):
        """Gets the on_step of this AdviceTemplateStepRecommendationServiceCaseStatus.  # noqa: E501


        :return: The on_step of this AdviceTemplateStepRecommendationServiceCaseStatus.  # noqa: E501
        :rtype: NamedServiceCaseStatusRef
        """
        return self._on_step

    @on_step.setter
    def on_step(self, on_step):
        """Sets the on_step of this AdviceTemplateStepRecommendationServiceCaseStatus.


        :param on_step: The on_step of this AdviceTemplateStepRecommendationServiceCaseStatus.  # noqa: E501
        :type: NamedServiceCaseStatusRef
        """

        self._on_step = on_step

    @property
    def on_accept(self):
        """Gets the on_accept of this AdviceTemplateStepRecommendationServiceCaseStatus.  # noqa: E501


        :return: The on_accept of this AdviceTemplateStepRecommendationServiceCaseStatus.  # noqa: E501
        :rtype: NamedServiceCaseStatusRef
        """
        return self._on_accept

    @on_accept.setter
    def on_accept(self, on_accept):
        """Sets the on_accept of this AdviceTemplateStepRecommendationServiceCaseStatus.


        :param on_accept: The on_accept of this AdviceTemplateStepRecommendationServiceCaseStatus.  # noqa: E501
        :type: NamedServiceCaseStatusRef
        """

        self._on_accept = on_accept

    @property
    def on_reject(self):
        """Gets the on_reject of this AdviceTemplateStepRecommendationServiceCaseStatus.  # noqa: E501


        :return: The on_reject of this AdviceTemplateStepRecommendationServiceCaseStatus.  # noqa: E501
        :rtype: NamedServiceCaseStatusRef
        """
        return self._on_reject

    @on_reject.setter
    def on_reject(self, on_reject):
        """Sets the on_reject of this AdviceTemplateStepRecommendationServiceCaseStatus.


        :param on_reject: The on_reject of this AdviceTemplateStepRecommendationServiceCaseStatus.  # noqa: E501
        :type: NamedServiceCaseStatusRef
        """

        self._on_reject = on_reject

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
        if issubclass(AdviceTemplateStepRecommendationServiceCaseStatus, dict):
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
        if not isinstance(other, AdviceTemplateStepRecommendationServiceCaseStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
