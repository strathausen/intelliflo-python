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

class AtrRef(object):
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
        'template': 'RecommendAtrTemplateRef',
        'risk_profile': 'RiskProfileReference',
        'risk_profile_ref': 'NamedRiskProfileRef'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'template': 'template',
        'risk_profile': 'riskProfile',
        'risk_profile_ref': 'riskProfileRef'
    }

    def __init__(self, id=None, href=None, template=None, risk_profile=None, risk_profile_ref=None):  # noqa: E501
        """AtrRef - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._template = None
        self._risk_profile = None
        self._risk_profile_ref = None
        self.discriminator = None
        self.id = id
        if href is not None:
            self.href = href
        if template is not None:
            self.template = template
        if risk_profile is not None:
            self.risk_profile = risk_profile
        if risk_profile_ref is not None:
            self.risk_profile_ref = risk_profile_ref

    @property
    def id(self):
        """Gets the id of this AtrRef.  # noqa: E501

        Atr unique identifier.  # noqa: E501

        :return: The id of this AtrRef.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AtrRef.

        Atr unique identifier.  # noqa: E501

        :param id: The id of this AtrRef.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def href(self):
        """Gets the href of this AtrRef.  # noqa: E501

        Hyperlink to the Atr.  # noqa: E501

        :return: The href of this AtrRef.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AtrRef.

        Hyperlink to the Atr.  # noqa: E501

        :param href: The href of this AtrRef.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def template(self):
        """Gets the template of this AtrRef.  # noqa: E501


        :return: The template of this AtrRef.  # noqa: E501
        :rtype: RecommendAtrTemplateRef
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this AtrRef.


        :param template: The template of this AtrRef.  # noqa: E501
        :type: RecommendAtrTemplateRef
        """

        self._template = template

    @property
    def risk_profile(self):
        """Gets the risk_profile of this AtrRef.  # noqa: E501


        :return: The risk_profile of this AtrRef.  # noqa: E501
        :rtype: RiskProfileReference
        """
        return self._risk_profile

    @risk_profile.setter
    def risk_profile(self, risk_profile):
        """Sets the risk_profile of this AtrRef.


        :param risk_profile: The risk_profile of this AtrRef.  # noqa: E501
        :type: RiskProfileReference
        """

        self._risk_profile = risk_profile

    @property
    def risk_profile_ref(self):
        """Gets the risk_profile_ref of this AtrRef.  # noqa: E501


        :return: The risk_profile_ref of this AtrRef.  # noqa: E501
        :rtype: NamedRiskProfileRef
        """
        return self._risk_profile_ref

    @risk_profile_ref.setter
    def risk_profile_ref(self, risk_profile_ref):
        """Sets the risk_profile_ref of this AtrRef.


        :param risk_profile_ref: The risk_profile_ref of this AtrRef.  # noqa: E501
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
        if issubclass(AtrRef, dict):
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
        if not isinstance(other, AtrRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
