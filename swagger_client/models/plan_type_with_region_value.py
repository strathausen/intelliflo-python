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

class PlanTypeWithRegionValue(object):
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
        'name': 'str',
        'region_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'region_code': 'regionCode'
    }

    def __init__(self, id=None, name=None, region_code=None):  # noqa: E501
        """PlanTypeWithRegionValue - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._region_code = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        if region_code is not None:
            self.region_code = region_code

    @property
    def id(self):
        """Gets the id of this PlanTypeWithRegionValue.  # noqa: E501

        Plan type unique identifier.  # noqa: E501

        :return: The id of this PlanTypeWithRegionValue.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlanTypeWithRegionValue.

        Plan type unique identifier.  # noqa: E501

        :param id: The id of this PlanTypeWithRegionValue.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PlanTypeWithRegionValue.  # noqa: E501

        Plan type name.  # noqa: E501

        :return: The name of this PlanTypeWithRegionValue.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlanTypeWithRegionValue.

        Plan type name.  # noqa: E501

        :param name: The name of this PlanTypeWithRegionValue.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def region_code(self):
        """Gets the region_code of this PlanTypeWithRegionValue.  # noqa: E501

        Plan type region code.  # noqa: E501

        :return: The region_code of this PlanTypeWithRegionValue.  # noqa: E501
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this PlanTypeWithRegionValue.

        Plan type region code.  # noqa: E501

        :param region_code: The region_code of this PlanTypeWithRegionValue.  # noqa: E501
        :type: str
        """

        self._region_code = region_code

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
        if issubclass(PlanTypeWithRegionValue, dict):
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
        if not isinstance(other, PlanTypeWithRegionValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
