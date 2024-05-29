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

class NewBusinessPlanValue(object):
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
        'product_name': 'str',
        'external_reference': 'str',
        'bundle_reference': 'str',
        'provider': 'ProductProviderRef2',
        'plan_type': 'PlanTypeReference',
        'selling_adviser': 'AdviserRef',
        'life_cycle': 'NamedLifecycleRef',
        'is_advice_off_panel': 'bool',
        'commission_rate': 'str',
        'split_template': 'SplitTemplateValue',
        'fees': 'list[FeeRef]',
        'wrap': 'WrapPlanValue'
    }

    attribute_map = {
        'product_name': 'productName',
        'external_reference': 'externalReference',
        'bundle_reference': 'bundleReference',
        'provider': 'provider',
        'plan_type': 'planType',
        'selling_adviser': 'sellingAdviser',
        'life_cycle': 'lifeCycle',
        'is_advice_off_panel': 'isAdviceOffPanel',
        'commission_rate': 'commissionRate',
        'split_template': 'splitTemplate',
        'fees': 'fees',
        'wrap': 'wrap'
    }

    def __init__(self, product_name=None, external_reference=None, bundle_reference=None, provider=None, plan_type=None, selling_adviser=None, life_cycle=None, is_advice_off_panel=False, commission_rate=None, split_template=None, fees=None, wrap=None):  # noqa: E501
        """NewBusinessPlanValue - a model defined in Swagger"""  # noqa: E501
        self._product_name = None
        self._external_reference = None
        self._bundle_reference = None
        self._provider = None
        self._plan_type = None
        self._selling_adviser = None
        self._life_cycle = None
        self._is_advice_off_panel = None
        self._commission_rate = None
        self._split_template = None
        self._fees = None
        self._wrap = None
        self.discriminator = None
        if product_name is not None:
            self.product_name = product_name
        if external_reference is not None:
            self.external_reference = external_reference
        if bundle_reference is not None:
            self.bundle_reference = bundle_reference
        self.provider = provider
        self.plan_type = plan_type
        self.selling_adviser = selling_adviser
        self.life_cycle = life_cycle
        if is_advice_off_panel is not None:
            self.is_advice_off_panel = is_advice_off_panel
        if commission_rate is not None:
            self.commission_rate = commission_rate
        if split_template is not None:
            self.split_template = split_template
        if fees is not None:
            self.fees = fees
        if wrap is not None:
            self.wrap = wrap

    @property
    def product_name(self):
        """Gets the product_name of this NewBusinessPlanValue.  # noqa: E501

        Product name for the new business plan.  # noqa: E501

        :return: The product_name of this NewBusinessPlanValue.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this NewBusinessPlanValue.

        Product name for the new business plan.  # noqa: E501

        :param product_name: The product_name of this NewBusinessPlanValue.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def external_reference(self):
        """Gets the external_reference of this NewBusinessPlanValue.  # noqa: E501

        External reference for the new business plan  # noqa: E501

        :return: The external_reference of this NewBusinessPlanValue.  # noqa: E501
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this NewBusinessPlanValue.

        External reference for the new business plan  # noqa: E501

        :param external_reference: The external_reference of this NewBusinessPlanValue.  # noqa: E501
        :type: str
        """

        self._external_reference = external_reference

    @property
    def bundle_reference(self):
        """Gets the bundle_reference of this NewBusinessPlanValue.  # noqa: E501

        Reference for the Recommendation proposal created from a bundled group.  # noqa: E501

        :return: The bundle_reference of this NewBusinessPlanValue.  # noqa: E501
        :rtype: str
        """
        return self._bundle_reference

    @bundle_reference.setter
    def bundle_reference(self, bundle_reference):
        """Sets the bundle_reference of this NewBusinessPlanValue.

        Reference for the Recommendation proposal created from a bundled group.  # noqa: E501

        :param bundle_reference: The bundle_reference of this NewBusinessPlanValue.  # noqa: E501
        :type: str
        """

        self._bundle_reference = bundle_reference

    @property
    def provider(self):
        """Gets the provider of this NewBusinessPlanValue.  # noqa: E501


        :return: The provider of this NewBusinessPlanValue.  # noqa: E501
        :rtype: ProductProviderRef2
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this NewBusinessPlanValue.


        :param provider: The provider of this NewBusinessPlanValue.  # noqa: E501
        :type: ProductProviderRef2
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501

        self._provider = provider

    @property
    def plan_type(self):
        """Gets the plan_type of this NewBusinessPlanValue.  # noqa: E501


        :return: The plan_type of this NewBusinessPlanValue.  # noqa: E501
        :rtype: PlanTypeReference
        """
        return self._plan_type

    @plan_type.setter
    def plan_type(self, plan_type):
        """Sets the plan_type of this NewBusinessPlanValue.


        :param plan_type: The plan_type of this NewBusinessPlanValue.  # noqa: E501
        :type: PlanTypeReference
        """
        if plan_type is None:
            raise ValueError("Invalid value for `plan_type`, must not be `None`")  # noqa: E501

        self._plan_type = plan_type

    @property
    def selling_adviser(self):
        """Gets the selling_adviser of this NewBusinessPlanValue.  # noqa: E501


        :return: The selling_adviser of this NewBusinessPlanValue.  # noqa: E501
        :rtype: AdviserRef
        """
        return self._selling_adviser

    @selling_adviser.setter
    def selling_adviser(self, selling_adviser):
        """Sets the selling_adviser of this NewBusinessPlanValue.


        :param selling_adviser: The selling_adviser of this NewBusinessPlanValue.  # noqa: E501
        :type: AdviserRef
        """
        if selling_adviser is None:
            raise ValueError("Invalid value for `selling_adviser`, must not be `None`")  # noqa: E501

        self._selling_adviser = selling_adviser

    @property
    def life_cycle(self):
        """Gets the life_cycle of this NewBusinessPlanValue.  # noqa: E501


        :return: The life_cycle of this NewBusinessPlanValue.  # noqa: E501
        :rtype: NamedLifecycleRef
        """
        return self._life_cycle

    @life_cycle.setter
    def life_cycle(self, life_cycle):
        """Sets the life_cycle of this NewBusinessPlanValue.


        :param life_cycle: The life_cycle of this NewBusinessPlanValue.  # noqa: E501
        :type: NamedLifecycleRef
        """
        if life_cycle is None:
            raise ValueError("Invalid value for `life_cycle`, must not be `None`")  # noqa: E501

        self._life_cycle = life_cycle

    @property
    def is_advice_off_panel(self):
        """Gets the is_advice_off_panel of this NewBusinessPlanValue.  # noqa: E501

        Is the Adviser recommending a product which is outside of their regulated sphere?  This would be considered \"Off-panel\" advice. Only assignable on POST.  # noqa: E501

        :return: The is_advice_off_panel of this NewBusinessPlanValue.  # noqa: E501
        :rtype: bool
        """
        return self._is_advice_off_panel

    @is_advice_off_panel.setter
    def is_advice_off_panel(self, is_advice_off_panel):
        """Sets the is_advice_off_panel of this NewBusinessPlanValue.

        Is the Adviser recommending a product which is outside of their regulated sphere?  This would be considered \"Off-panel\" advice. Only assignable on POST.  # noqa: E501

        :param is_advice_off_panel: The is_advice_off_panel of this NewBusinessPlanValue.  # noqa: E501
        :type: bool
        """

        self._is_advice_off_panel = is_advice_off_panel

    @property
    def commission_rate(self):
        """Gets the commission_rate of this NewBusinessPlanValue.  # noqa: E501

        Commission rate for top up plan.  # noqa: E501

        :return: The commission_rate of this NewBusinessPlanValue.  # noqa: E501
        :rtype: str
        """
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, commission_rate):
        """Sets the commission_rate of this NewBusinessPlanValue.

        Commission rate for top up plan.  # noqa: E501

        :param commission_rate: The commission_rate of this NewBusinessPlanValue.  # noqa: E501
        :type: str
        """

        self._commission_rate = commission_rate

    @property
    def split_template(self):
        """Gets the split_template of this NewBusinessPlanValue.  # noqa: E501


        :return: The split_template of this NewBusinessPlanValue.  # noqa: E501
        :rtype: SplitTemplateValue
        """
        return self._split_template

    @split_template.setter
    def split_template(self, split_template):
        """Sets the split_template of this NewBusinessPlanValue.


        :param split_template: The split_template of this NewBusinessPlanValue.  # noqa: E501
        :type: SplitTemplateValue
        """

        self._split_template = split_template

    @property
    def fees(self):
        """Gets the fees of this NewBusinessPlanValue.  # noqa: E501

        List of fees for the Top up plan.  # noqa: E501

        :return: The fees of this NewBusinessPlanValue.  # noqa: E501
        :rtype: list[FeeRef]
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this NewBusinessPlanValue.

        List of fees for the Top up plan.  # noqa: E501

        :param fees: The fees of this NewBusinessPlanValue.  # noqa: E501
        :type: list[FeeRef]
        """

        self._fees = fees

    @property
    def wrap(self):
        """Gets the wrap of this NewBusinessPlanValue.  # noqa: E501


        :return: The wrap of this NewBusinessPlanValue.  # noqa: E501
        :rtype: WrapPlanValue
        """
        return self._wrap

    @wrap.setter
    def wrap(self, wrap):
        """Sets the wrap of this NewBusinessPlanValue.


        :param wrap: The wrap of this NewBusinessPlanValue.  # noqa: E501
        :type: WrapPlanValue
        """

        self._wrap = wrap

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
        if issubclass(NewBusinessPlanValue, dict):
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
        if not isinstance(other, NewBusinessPlanValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
