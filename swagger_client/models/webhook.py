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

class Webhook(object):
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
        'href': 'str',
        'topic': 'str',
        'callback': 'str',
        'lease_seconds': 'str'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'topic': 'topic',
        'callback': 'callback',
        'lease_seconds': 'leaseSeconds'
    }

    def __init__(self, id=None, href=None, topic=None, callback=None, lease_seconds=None):  # noqa: E501
        """Webhook - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._topic = None
        self._callback = None
        self._lease_seconds = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        self.topic = topic
        self.callback = callback
        if lease_seconds is not None:
            self.lease_seconds = lease_seconds

    @property
    def id(self):
        """Gets the id of this Webhook.  # noqa: E501

        Subscription identifier.  # noqa: E501

        :return: The id of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Webhook.

        Subscription identifier.  # noqa: E501

        :param id: The id of this Webhook.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this Webhook.  # noqa: E501

        Subscription href.  # noqa: E501

        :return: The href of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Webhook.

        Subscription href.  # noqa: E501

        :param href: The href of this Webhook.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def topic(self):
        """Gets the topic of this Webhook.  # noqa: E501

        The topic URL that the subscriber wishes to subscribe to or unsubscribe from.  # noqa: E501

        :return: The topic of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this Webhook.

        The topic URL that the subscriber wishes to subscribe to or unsubscribe from.  # noqa: E501

        :param topic: The topic of this Webhook.  # noqa: E501
        :type: str
        """
        if topic is None:
            raise ValueError("Invalid value for `topic`, must not be `None`")  # noqa: E501

        self._topic = topic

    @property
    def callback(self):
        """Gets the callback of this Webhook.  # noqa: E501

        The subscriber's callback URL where content distribution notifications should be delivered.  # noqa: E501

        :return: The callback of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._callback

    @callback.setter
    def callback(self, callback):
        """Sets the callback of this Webhook.

        The subscriber's callback URL where content distribution notifications should be delivered.  # noqa: E501

        :param callback: The callback of this Webhook.  # noqa: E501
        :type: str
        """
        if callback is None:
            raise ValueError("Invalid value for `callback`, must not be `None`")  # noqa: E501

        self._callback = callback

    @property
    def lease_seconds(self):
        """Gets the lease_seconds of this Webhook.  # noqa: E501

        Number of seconds to have the subscription active.  # noqa: E501

        :return: The lease_seconds of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._lease_seconds

    @lease_seconds.setter
    def lease_seconds(self, lease_seconds):
        """Sets the lease_seconds of this Webhook.

        Number of seconds to have the subscription active.  # noqa: E501

        :param lease_seconds: The lease_seconds of this Webhook.  # noqa: E501
        :type: str
        """

        self._lease_seconds = lease_seconds

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
        if issubclass(Webhook, dict):
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
        if not isinstance(other, Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
