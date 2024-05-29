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

class AppEventPayloadValue(object):
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
        'id': 'str',
        'name': 'str',
        'is_approved_for_install': 'bool',
        'summary': 'str',
        'last_updated_at': 'datetime',
        'billing_model': 'AppBillingModelValue',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'is_approved_for_install': 'isApprovedForInstall',
        'summary': 'summary',
        'last_updated_at': 'lastUpdatedAt',
        'billing_model': 'billingModel',
        'version': 'version'
    }

    def __init__(self, id=None, name=None, is_approved_for_install=None, summary=None, last_updated_at=None, billing_model=None, version=None):  # noqa: E501
        """AppEventPayloadValue - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._is_approved_for_install = None
        self._summary = None
        self._last_updated_at = None
        self._billing_model = None
        self._version = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if is_approved_for_install is not None:
            self.is_approved_for_install = is_approved_for_install
        if summary is not None:
            self.summary = summary
        if last_updated_at is not None:
            self.last_updated_at = last_updated_at
        if billing_model is not None:
            self.billing_model = billing_model
        if version is not None:
            self.version = version

    @property
    def id(self):
        """Gets the id of this AppEventPayloadValue.  # noqa: E501


        :return: The id of this AppEventPayloadValue.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppEventPayloadValue.


        :param id: The id of this AppEventPayloadValue.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AppEventPayloadValue.  # noqa: E501


        :return: The name of this AppEventPayloadValue.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppEventPayloadValue.


        :param name: The name of this AppEventPayloadValue.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_approved_for_install(self):
        """Gets the is_approved_for_install of this AppEventPayloadValue.  # noqa: E501


        :return: The is_approved_for_install of this AppEventPayloadValue.  # noqa: E501
        :rtype: bool
        """
        return self._is_approved_for_install

    @is_approved_for_install.setter
    def is_approved_for_install(self, is_approved_for_install):
        """Sets the is_approved_for_install of this AppEventPayloadValue.


        :param is_approved_for_install: The is_approved_for_install of this AppEventPayloadValue.  # noqa: E501
        :type: bool
        """

        self._is_approved_for_install = is_approved_for_install

    @property
    def summary(self):
        """Gets the summary of this AppEventPayloadValue.  # noqa: E501


        :return: The summary of this AppEventPayloadValue.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this AppEventPayloadValue.


        :param summary: The summary of this AppEventPayloadValue.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this AppEventPayloadValue.  # noqa: E501


        :return: The last_updated_at of this AppEventPayloadValue.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this AppEventPayloadValue.


        :param last_updated_at: The last_updated_at of this AppEventPayloadValue.  # noqa: E501
        :type: datetime
        """

        self._last_updated_at = last_updated_at

    @property
    def billing_model(self):
        """Gets the billing_model of this AppEventPayloadValue.  # noqa: E501


        :return: The billing_model of this AppEventPayloadValue.  # noqa: E501
        :rtype: AppBillingModelValue
        """
        return self._billing_model

    @billing_model.setter
    def billing_model(self, billing_model):
        """Sets the billing_model of this AppEventPayloadValue.


        :param billing_model: The billing_model of this AppEventPayloadValue.  # noqa: E501
        :type: AppBillingModelValue
        """

        self._billing_model = billing_model

    @property
    def version(self):
        """Gets the version of this AppEventPayloadValue.  # noqa: E501


        :return: The version of this AppEventPayloadValue.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AppEventPayloadValue.


        :param version: The version of this AppEventPayloadValue.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(AppEventPayloadValue, dict):
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
        if not isinstance(other, AppEventPayloadValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
