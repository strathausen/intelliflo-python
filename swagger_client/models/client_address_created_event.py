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

class ClientAddressCreatedEvent(object):
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
        'event': 'str',
        'payload': 'Address',
        'time_stamp': 'datetime',
        'tenant_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'event': 'event',
        'payload': 'payload',
        'time_stamp': 'timeStamp',
        'tenant_id': 'tenantId'
    }

    def __init__(self, id=None, event=None, payload=None, time_stamp=None, tenant_id=None):  # noqa: E501
        """ClientAddressCreatedEvent - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._event = None
        self._payload = None
        self._time_stamp = None
        self._tenant_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if event is not None:
            self.event = event
        if payload is not None:
            self.payload = payload
        if time_stamp is not None:
            self.time_stamp = time_stamp
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def id(self):
        """Gets the id of this ClientAddressCreatedEvent.  # noqa: E501

        Event identifier.  # noqa: E501

        :return: The id of this ClientAddressCreatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClientAddressCreatedEvent.

        Event identifier.  # noqa: E501

        :param id: The id of this ClientAddressCreatedEvent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def event(self):
        """Gets the event of this ClientAddressCreatedEvent.  # noqa: E501

        Event name.  # noqa: E501

        :return: The event of this ClientAddressCreatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this ClientAddressCreatedEvent.

        Event name.  # noqa: E501

        :param event: The event of this ClientAddressCreatedEvent.  # noqa: E501
        :type: str
        """

        self._event = event

    @property
    def payload(self):
        """Gets the payload of this ClientAddressCreatedEvent.  # noqa: E501


        :return: The payload of this ClientAddressCreatedEvent.  # noqa: E501
        :rtype: Address
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this ClientAddressCreatedEvent.


        :param payload: The payload of this ClientAddressCreatedEvent.  # noqa: E501
        :type: Address
        """

        self._payload = payload

    @property
    def time_stamp(self):
        """Gets the time_stamp of this ClientAddressCreatedEvent.  # noqa: E501

        UTC datetime when the event occurred.  # noqa: E501

        :return: The time_stamp of this ClientAddressCreatedEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this ClientAddressCreatedEvent.

        UTC datetime when the event occurred.  # noqa: E501

        :param time_stamp: The time_stamp of this ClientAddressCreatedEvent.  # noqa: E501
        :type: datetime
        """

        self._time_stamp = time_stamp

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ClientAddressCreatedEvent.  # noqa: E501

        TenantId for which the event occurred.  # noqa: E501

        :return: The tenant_id of this ClientAddressCreatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ClientAddressCreatedEvent.

        TenantId for which the event occurred.  # noqa: E501

        :param tenant_id: The tenant_id of this ClientAddressCreatedEvent.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

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
        if issubclass(ClientAddressCreatedEvent, dict):
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
        if not isinstance(other, ClientAddressCreatedEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
