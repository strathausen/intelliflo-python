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
from swagger_client.models.base_configuration_document import BaseConfigurationDocument  # noqa: F401,E501

class IntellifloEnterprise(BaseConfigurationDocument):
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
        'config': 'AmazonS3Config'
    }
    if hasattr(BaseConfigurationDocument, "swagger_types"):
        swagger_types.update(BaseConfigurationDocument.swagger_types)

    attribute_map = {
        'config': 'config'
    }
    if hasattr(BaseConfigurationDocument, "attribute_map"):
        attribute_map.update(BaseConfigurationDocument.attribute_map)

    def __init__(self, config=None, *args, **kwargs):  # noqa: E501
        """IntellifloEnterprise - a model defined in Swagger"""  # noqa: E501
        self._config = None
        self.discriminator = None
        if config is not None:
            self.config = config
        BaseConfigurationDocument.__init__(self, *args, **kwargs)

    @property
    def config(self):
        """Gets the config of this IntellifloEnterprise.  # noqa: E501


        :return: The config of this IntellifloEnterprise.  # noqa: E501
        :rtype: AmazonS3Config
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this IntellifloEnterprise.


        :param config: The config of this IntellifloEnterprise.  # noqa: E501
        :type: AmazonS3Config
        """

        self._config = config

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
        if issubclass(IntellifloEnterprise, dict):
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
        if not isinstance(other, IntellifloEnterprise):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
