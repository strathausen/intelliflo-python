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

class AtrAssetAllocation(object):
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
        'term_start': 'int',
        'term_end': 'int',
        'volatility': 'float',
        '_return': 'float',
        'asset_classes': 'list[AtrAssetClass]'
    }

    attribute_map = {
        'term_start': 'termStart',
        'term_end': 'termEnd',
        'volatility': 'volatility',
        '_return': 'return',
        'asset_classes': 'assetClasses'
    }

    def __init__(self, term_start=None, term_end=None, volatility=None, _return=None, asset_classes=None):  # noqa: E501
        """AtrAssetAllocation - a model defined in Swagger"""  # noqa: E501
        self._term_start = None
        self._term_end = None
        self._volatility = None
        self.__return = None
        self._asset_classes = None
        self.discriminator = None
        self.term_start = term_start
        self.term_end = term_end
        self.volatility = volatility
        self._return = _return
        self.asset_classes = asset_classes

    @property
    def term_start(self):
        """Gets the term_start of this AtrAssetAllocation.  # noqa: E501

        When asset allocation starts.Term Start date and end date defines the length of the asset allocation and it has impact on what types and percentage of assets the model will contain.  # noqa: E501

        :return: The term_start of this AtrAssetAllocation.  # noqa: E501
        :rtype: int
        """
        return self._term_start

    @term_start.setter
    def term_start(self, term_start):
        """Sets the term_start of this AtrAssetAllocation.

        When asset allocation starts.Term Start date and end date defines the length of the asset allocation and it has impact on what types and percentage of assets the model will contain.  # noqa: E501

        :param term_start: The term_start of this AtrAssetAllocation.  # noqa: E501
        :type: int
        """
        if term_start is None:
            raise ValueError("Invalid value for `term_start`, must not be `None`")  # noqa: E501

        self._term_start = term_start

    @property
    def term_end(self):
        """Gets the term_end of this AtrAssetAllocation.  # noqa: E501

        When asset allocation ends.Term Start date and end date defines the length of the asset allocation and it has impact on what types and percentage of assets the model will contain.  # noqa: E501

        :return: The term_end of this AtrAssetAllocation.  # noqa: E501
        :rtype: int
        """
        return self._term_end

    @term_end.setter
    def term_end(self, term_end):
        """Sets the term_end of this AtrAssetAllocation.

        When asset allocation ends.Term Start date and end date defines the length of the asset allocation and it has impact on what types and percentage of assets the model will contain.  # noqa: E501

        :param term_end: The term_end of this AtrAssetAllocation.  # noqa: E501
        :type: int
        """
        if term_end is None:
            raise ValueError("Invalid value for `term_end`, must not be `None`")  # noqa: E501

        self._term_end = term_end

    @property
    def volatility(self):
        """Gets the volatility of this AtrAssetAllocation.  # noqa: E501

        Risk volatility percentage.  # noqa: E501

        :return: The volatility of this AtrAssetAllocation.  # noqa: E501
        :rtype: float
        """
        return self._volatility

    @volatility.setter
    def volatility(self, volatility):
        """Sets the volatility of this AtrAssetAllocation.

        Risk volatility percentage.  # noqa: E501

        :param volatility: The volatility of this AtrAssetAllocation.  # noqa: E501
        :type: float
        """
        if volatility is None:
            raise ValueError("Invalid value for `volatility`, must not be `None`")  # noqa: E501

        self._volatility = volatility

    @property
    def _return(self):
        """Gets the _return of this AtrAssetAllocation.  # noqa: E501

        Annual return percentage.  # noqa: E501

        :return: The _return of this AtrAssetAllocation.  # noqa: E501
        :rtype: float
        """
        return self.__return

    @_return.setter
    def _return(self, _return):
        """Sets the _return of this AtrAssetAllocation.

        Annual return percentage.  # noqa: E501

        :param _return: The _return of this AtrAssetAllocation.  # noqa: E501
        :type: float
        """
        if _return is None:
            raise ValueError("Invalid value for `_return`, must not be `None`")  # noqa: E501

        self.__return = _return

    @property
    def asset_classes(self):
        """Gets the asset_classes of this AtrAssetAllocation.  # noqa: E501

        Percentages of all asset classes allocations should add up to 100%.  # noqa: E501

        :return: The asset_classes of this AtrAssetAllocation.  # noqa: E501
        :rtype: list[AtrAssetClass]
        """
        return self._asset_classes

    @asset_classes.setter
    def asset_classes(self, asset_classes):
        """Sets the asset_classes of this AtrAssetAllocation.

        Percentages of all asset classes allocations should add up to 100%.  # noqa: E501

        :param asset_classes: The asset_classes of this AtrAssetAllocation.  # noqa: E501
        :type: list[AtrAssetClass]
        """
        if asset_classes is None:
            raise ValueError("Invalid value for `asset_classes`, must not be `None`")  # noqa: E501

        self._asset_classes = asset_classes

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
        if issubclass(AtrAssetAllocation, dict):
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
        if not isinstance(other, AtrAssetAllocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
