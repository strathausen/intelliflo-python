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

class BaseConfigurationDocument(object):
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
        'discriminator': 'str',
        'id': 'int',
        'href': 'str',
        'name': 'str',
        'type': 'str',
        'default': 'bool',
        'read_only': 'bool',
        'created_at': 'datetime',
        'metrics': 'StorageConfigurationMetric'
    }

    attribute_map = {
        'discriminator': 'discriminator',
        'id': 'id',
        'href': 'href',
        'name': 'name',
        'type': 'type',
        'default': 'default',
        'read_only': 'readOnly',
        'created_at': 'createdAt',
        'metrics': 'metrics'
    }

    discriminator_value_class_map = {
          'IntellifloStandard': 'IntellifloStandard',
'AmazonS3': 'AmazonS3',
'IntellifloEnterprise': 'IntellifloEnterprise'    }

    def __init__(self, discriminator=None, id=None, href=None, name=None, type=None, default=None, read_only=None, created_at=None, metrics=None):  # noqa: E501
        """BaseConfigurationDocument - a model defined in Swagger"""  # noqa: E501
        self._discriminator = None
        self._id = None
        self._href = None
        self._name = None
        self._type = None
        self._default = None
        self._read_only = None
        self._created_at = None
        self._metrics = None
        self.discriminator = 'discriminator'
        self.discriminator = discriminator
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if name is not None:
            self.name = name
        self.type = type
        if default is not None:
            self.default = default
        if read_only is not None:
            self.read_only = read_only
        if created_at is not None:
            self.created_at = created_at
        if metrics is not None:
            self.metrics = metrics

    @property
    def discriminator(self):
        """Gets the discriminator of this BaseConfigurationDocument.  # noqa: E501


        :return: The discriminator of this BaseConfigurationDocument.  # noqa: E501
        :rtype: str
        """
        return self._discriminator

    @discriminator.setter
    def discriminator(self, discriminator):
        """Sets the discriminator of this BaseConfigurationDocument.


        :param discriminator: The discriminator of this BaseConfigurationDocument.  # noqa: E501
        :type: str
        """
        if discriminator is None:
            raise ValueError("Invalid value for `discriminator`, must not be `None`")  # noqa: E501
        allowed_values = ["AmazonS3", "DefaultConfiguration", "IntellifloEnterprise", "IntellifloStandard"]  # noqa: E501
        if discriminator not in allowed_values:
            raise ValueError(
                "Invalid value for `discriminator` ({0}), must be one of {1}"  # noqa: E501
                .format(discriminator, allowed_values)
            )

        self._discriminator = discriminator

    @property
    def id(self):
        """Gets the id of this BaseConfigurationDocument.  # noqa: E501


        :return: The id of this BaseConfigurationDocument.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseConfigurationDocument.


        :param id: The id of this BaseConfigurationDocument.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this BaseConfigurationDocument.  # noqa: E501


        :return: The href of this BaseConfigurationDocument.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BaseConfigurationDocument.


        :param href: The href of this BaseConfigurationDocument.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def name(self):
        """Gets the name of this BaseConfigurationDocument.  # noqa: E501

        Editable on POST, PUT  # noqa: E501

        :return: The name of this BaseConfigurationDocument.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BaseConfigurationDocument.

        Editable on POST, PUT  # noqa: E501

        :param name: The name of this BaseConfigurationDocument.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this BaseConfigurationDocument.  # noqa: E501


        :return: The type of this BaseConfigurationDocument.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BaseConfigurationDocument.


        :param type: The type of this BaseConfigurationDocument.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Default", "AmazonS3", "IntellifloStandard", "IntellifloEnterprise"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def default(self):
        """Gets the default of this BaseConfigurationDocument.  # noqa: E501


        :return: The default of this BaseConfigurationDocument.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this BaseConfigurationDocument.


        :param default: The default of this BaseConfigurationDocument.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def read_only(self):
        """Gets the read_only of this BaseConfigurationDocument.  # noqa: E501


        :return: The read_only of this BaseConfigurationDocument.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this BaseConfigurationDocument.


        :param read_only: The read_only of this BaseConfigurationDocument.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def created_at(self):
        """Gets the created_at of this BaseConfigurationDocument.  # noqa: E501


        :return: The created_at of this BaseConfigurationDocument.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BaseConfigurationDocument.


        :param created_at: The created_at of this BaseConfigurationDocument.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def metrics(self):
        """Gets the metrics of this BaseConfigurationDocument.  # noqa: E501


        :return: The metrics of this BaseConfigurationDocument.  # noqa: E501
        :rtype: StorageConfigurationMetric
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this BaseConfigurationDocument.


        :param metrics: The metrics of this BaseConfigurationDocument.  # noqa: E501
        :type: StorageConfigurationMetric
        """

        self._metrics = metrics

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(BaseConfigurationDocument, dict):
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
        if not isinstance(other, BaseConfigurationDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
