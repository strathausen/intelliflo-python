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

class BasePortfolioModel(object):
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
        'href': 'str',
        'id': 'int',
        'code': 'str',
        'name': 'str',
        'change_description': 'str',
        'market_commentary_rss_href': 'str',
        'atrs': 'list[AttitudeToRiskRef]',
        'is_active': 'bool',
        'group_owner': 'GroupOwnerRef',
        'fact_sheet_link': 'str',
        'charges': 'Charges',
        'is_discretionary_fund_managed': 'bool',
        'platform_provider': 'str',
        'product_provider': 'ProductProviderExternalRef'
    }

    attribute_map = {
        'href': 'href',
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'change_description': 'changeDescription',
        'market_commentary_rss_href': 'marketCommentaryRssHref',
        'atrs': 'atrs',
        'is_active': 'isActive',
        'group_owner': 'groupOwner',
        'fact_sheet_link': 'factSheetLink',
        'charges': 'charges',
        'is_discretionary_fund_managed': 'isDiscretionaryFundManaged',
        'platform_provider': 'platformProvider',
        'product_provider': 'productProvider'
    }

    def __init__(self, href=None, id=None, code=None, name=None, change_description=None, market_commentary_rss_href=None, atrs=None, is_active=None, group_owner=None, fact_sheet_link=None, charges=None, is_discretionary_fund_managed=None, platform_provider=None, product_provider=None):  # noqa: E501
        """BasePortfolioModel - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._id = None
        self._code = None
        self._name = None
        self._change_description = None
        self._market_commentary_rss_href = None
        self._atrs = None
        self._is_active = None
        self._group_owner = None
        self._fact_sheet_link = None
        self._charges = None
        self._is_discretionary_fund_managed = None
        self._platform_provider = None
        self._product_provider = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        self.code = code
        self.name = name
        if change_description is not None:
            self.change_description = change_description
        if market_commentary_rss_href is not None:
            self.market_commentary_rss_href = market_commentary_rss_href
        self.atrs = atrs
        if is_active is not None:
            self.is_active = is_active
        if group_owner is not None:
            self.group_owner = group_owner
        if fact_sheet_link is not None:
            self.fact_sheet_link = fact_sheet_link
        if charges is not None:
            self.charges = charges
        if is_discretionary_fund_managed is not None:
            self.is_discretionary_fund_managed = is_discretionary_fund_managed
        if platform_provider is not None:
            self.platform_provider = platform_provider
        if product_provider is not None:
            self.product_provider = product_provider

    @property
    def href(self):
        """Gets the href of this BasePortfolioModel.  # noqa: E501

        The portfolio model reference.  # noqa: E501

        :return: The href of this BasePortfolioModel.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BasePortfolioModel.

        The portfolio model reference.  # noqa: E501

        :param href: The href of this BasePortfolioModel.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this BasePortfolioModel.  # noqa: E501

        The portfolio model identifier.  # noqa: E501

        :return: The id of this BasePortfolioModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BasePortfolioModel.

        The portfolio model identifier.  # noqa: E501

        :param id: The id of this BasePortfolioModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def code(self):
        """Gets the code of this BasePortfolioModel.  # noqa: E501

        The portfolio model code.  # noqa: E501

        :return: The code of this BasePortfolioModel.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BasePortfolioModel.

        The portfolio model code.  # noqa: E501

        :param code: The code of this BasePortfolioModel.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def name(self):
        """Gets the name of this BasePortfolioModel.  # noqa: E501

        The portfolio model name.  # noqa: E501

        :return: The name of this BasePortfolioModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BasePortfolioModel.

        The portfolio model name.  # noqa: E501

        :param name: The name of this BasePortfolioModel.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def change_description(self):
        """Gets the change_description of this BasePortfolioModel.  # noqa: E501

        The description of changes to the portfolio model.  # noqa: E501

        :return: The change_description of this BasePortfolioModel.  # noqa: E501
        :rtype: str
        """
        return self._change_description

    @change_description.setter
    def change_description(self, change_description):
        """Sets the change_description of this BasePortfolioModel.

        The description of changes to the portfolio model.  # noqa: E501

        :param change_description: The change_description of this BasePortfolioModel.  # noqa: E501
        :type: str
        """

        self._change_description = change_description

    @property
    def market_commentary_rss_href(self):
        """Gets the market_commentary_rss_href of this BasePortfolioModel.  # noqa: E501

        The reference to the market commentary feed.  # noqa: E501

        :return: The market_commentary_rss_href of this BasePortfolioModel.  # noqa: E501
        :rtype: str
        """
        return self._market_commentary_rss_href

    @market_commentary_rss_href.setter
    def market_commentary_rss_href(self, market_commentary_rss_href):
        """Sets the market_commentary_rss_href of this BasePortfolioModel.

        The reference to the market commentary feed.  # noqa: E501

        :param market_commentary_rss_href: The market_commentary_rss_href of this BasePortfolioModel.  # noqa: E501
        :type: str
        """

        self._market_commentary_rss_href = market_commentary_rss_href

    @property
    def atrs(self):
        """Gets the atrs of this BasePortfolioModel.  # noqa: E501

        Attitudes to Risk associated with the portfolio model.  # noqa: E501

        :return: The atrs of this BasePortfolioModel.  # noqa: E501
        :rtype: list[AttitudeToRiskRef]
        """
        return self._atrs

    @atrs.setter
    def atrs(self, atrs):
        """Sets the atrs of this BasePortfolioModel.

        Attitudes to Risk associated with the portfolio model.  # noqa: E501

        :param atrs: The atrs of this BasePortfolioModel.  # noqa: E501
        :type: list[AttitudeToRiskRef]
        """
        if atrs is None:
            raise ValueError("Invalid value for `atrs`, must not be `None`")  # noqa: E501

        self._atrs = atrs

    @property
    def is_active(self):
        """Gets the is_active of this BasePortfolioModel.  # noqa: E501

        Is this version of the portfolio model active?  # noqa: E501

        :return: The is_active of this BasePortfolioModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this BasePortfolioModel.

        Is this version of the portfolio model active?  # noqa: E501

        :param is_active: The is_active of this BasePortfolioModel.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def group_owner(self):
        """Gets the group_owner of this BasePortfolioModel.  # noqa: E501


        :return: The group_owner of this BasePortfolioModel.  # noqa: E501
        :rtype: GroupOwnerRef
        """
        return self._group_owner

    @group_owner.setter
    def group_owner(self, group_owner):
        """Sets the group_owner of this BasePortfolioModel.


        :param group_owner: The group_owner of this BasePortfolioModel.  # noqa: E501
        :type: GroupOwnerRef
        """

        self._group_owner = group_owner

    @property
    def fact_sheet_link(self):
        """Gets the fact_sheet_link of this BasePortfolioModel.  # noqa: E501

        Link to the fact sheet  # noqa: E501

        :return: The fact_sheet_link of this BasePortfolioModel.  # noqa: E501
        :rtype: str
        """
        return self._fact_sheet_link

    @fact_sheet_link.setter
    def fact_sheet_link(self, fact_sheet_link):
        """Sets the fact_sheet_link of this BasePortfolioModel.

        Link to the fact sheet  # noqa: E501

        :param fact_sheet_link: The fact_sheet_link of this BasePortfolioModel.  # noqa: E501
        :type: str
        """

        self._fact_sheet_link = fact_sheet_link

    @property
    def charges(self):
        """Gets the charges of this BasePortfolioModel.  # noqa: E501


        :return: The charges of this BasePortfolioModel.  # noqa: E501
        :rtype: Charges
        """
        return self._charges

    @charges.setter
    def charges(self, charges):
        """Sets the charges of this BasePortfolioModel.


        :param charges: The charges of this BasePortfolioModel.  # noqa: E501
        :type: Charges
        """

        self._charges = charges

    @property
    def is_discretionary_fund_managed(self):
        """Gets the is_discretionary_fund_managed of this BasePortfolioModel.  # noqa: E501

        Indicating whether this instance is discretionary fund managed.  # noqa: E501

        :return: The is_discretionary_fund_managed of this BasePortfolioModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_discretionary_fund_managed

    @is_discretionary_fund_managed.setter
    def is_discretionary_fund_managed(self, is_discretionary_fund_managed):
        """Sets the is_discretionary_fund_managed of this BasePortfolioModel.

        Indicating whether this instance is discretionary fund managed.  # noqa: E501

        :param is_discretionary_fund_managed: The is_discretionary_fund_managed of this BasePortfolioModel.  # noqa: E501
        :type: bool
        """

        self._is_discretionary_fund_managed = is_discretionary_fund_managed

    @property
    def platform_provider(self):
        """Gets the platform_provider of this BasePortfolioModel.  # noqa: E501

        The platform provider.  # noqa: E501

        :return: The platform_provider of this BasePortfolioModel.  # noqa: E501
        :rtype: str
        """
        return self._platform_provider

    @platform_provider.setter
    def platform_provider(self, platform_provider):
        """Sets the platform_provider of this BasePortfolioModel.

        The platform provider.  # noqa: E501

        :param platform_provider: The platform_provider of this BasePortfolioModel.  # noqa: E501
        :type: str
        """

        self._platform_provider = platform_provider

    @property
    def product_provider(self):
        """Gets the product_provider of this BasePortfolioModel.  # noqa: E501


        :return: The product_provider of this BasePortfolioModel.  # noqa: E501
        :rtype: ProductProviderExternalRef
        """
        return self._product_provider

    @product_provider.setter
    def product_provider(self, product_provider):
        """Sets the product_provider of this BasePortfolioModel.


        :param product_provider: The product_provider of this BasePortfolioModel.  # noqa: E501
        :type: ProductProviderExternalRef
        """

        self._product_provider = product_provider

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
        if issubclass(BasePortfolioModel, dict):
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
        if not isinstance(other, BasePortfolioModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
