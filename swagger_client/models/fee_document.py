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

class FeeDocument(object):
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
        'sequential_ref': 'str',
        'selling_adviser': 'AdviserRef',
        'advice_category': 'str',
        'fee_type': 'FeeTypeRef',
        'payment_type': 'PaymentTypeRef',
        'fee_charging_type': 'FeeChargingTypeRef',
        'fee_percentage': 'float',
        'net': 'CurrencyValue',
        'vat': 'CurrencyValue',
        'vat_rate': 'VatRateValue',
        'status': 'str',
        'status_date': 'datetime',
        'recurring': 'FeeRecurring',
        'initial_period': 'int',
        'is_consultancy_fee': 'bool',
        'instalment': 'Instalment',
        'sent_to_client_on': 'datetime',
        'discount': 'DiscountValue',
        'banding': 'BandingRef',
        'forward_income_to': 'ForwardIncomeToRef',
        'clients': 'list[ClientRef]',
        'plan_href': 'str',
        'plans': 'list[PlanRef]',
        'is_retainer': 'bool',
        'fee_model': 'FeeModelRef',
        'tierings': 'list[FeeTiering]',
        'fee_detail': 'FeeDetail'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'sequential_ref': 'sequentialRef',
        'selling_adviser': 'sellingAdviser',
        'advice_category': 'adviceCategory',
        'fee_type': 'feeType',
        'payment_type': 'paymentType',
        'fee_charging_type': 'feeChargingType',
        'fee_percentage': 'feePercentage',
        'net': 'net',
        'vat': 'vat',
        'vat_rate': 'vatRate',
        'status': 'status',
        'status_date': 'statusDate',
        'recurring': 'recurring',
        'initial_period': 'initialPeriod',
        'is_consultancy_fee': 'isConsultancyFee',
        'instalment': 'instalment',
        'sent_to_client_on': 'sentToClientOn',
        'discount': 'discount',
        'banding': 'banding',
        'forward_income_to': 'forwardIncomeTo',
        'clients': 'clients',
        'plan_href': 'plan_href',
        'plans': 'plans',
        'is_retainer': 'isRetainer',
        'fee_model': 'feeModel',
        'tierings': 'tierings',
        'fee_detail': 'feeDetail'
    }

    def __init__(self, id=None, href=None, sequential_ref=None, selling_adviser=None, advice_category=None, fee_type=None, payment_type=None, fee_charging_type=None, fee_percentage=0.0, net=None, vat=None, vat_rate=None, status='null', status_date=None, recurring=None, initial_period=None, is_consultancy_fee=False, instalment=None, sent_to_client_on=None, discount=None, banding=None, forward_income_to=None, clients=None, plan_href=None, plans=None, is_retainer=False, fee_model=None, tierings=None, fee_detail=None):  # noqa: E501
        """FeeDocument - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._sequential_ref = None
        self._selling_adviser = None
        self._advice_category = None
        self._fee_type = None
        self._payment_type = None
        self._fee_charging_type = None
        self._fee_percentage = None
        self._net = None
        self._vat = None
        self._vat_rate = None
        self._status = None
        self._status_date = None
        self._recurring = None
        self._initial_period = None
        self._is_consultancy_fee = None
        self._instalment = None
        self._sent_to_client_on = None
        self._discount = None
        self._banding = None
        self._forward_income_to = None
        self._clients = None
        self._plan_href = None
        self._plans = None
        self._is_retainer = None
        self._fee_model = None
        self._tierings = None
        self._fee_detail = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if sequential_ref is not None:
            self.sequential_ref = sequential_ref
        self.selling_adviser = selling_adviser
        self.advice_category = advice_category
        self.fee_type = fee_type
        self.payment_type = payment_type
        if fee_charging_type is not None:
            self.fee_charging_type = fee_charging_type
        if fee_percentage is not None:
            self.fee_percentage = fee_percentage
        if net is not None:
            self.net = net
        if vat is not None:
            self.vat = vat
        if vat_rate is not None:
            self.vat_rate = vat_rate
        if status is not None:
            self.status = status
        if status_date is not None:
            self.status_date = status_date
        if recurring is not None:
            self.recurring = recurring
        if initial_period is not None:
            self.initial_period = initial_period
        if is_consultancy_fee is not None:
            self.is_consultancy_fee = is_consultancy_fee
        if instalment is not None:
            self.instalment = instalment
        if sent_to_client_on is not None:
            self.sent_to_client_on = sent_to_client_on
        if discount is not None:
            self.discount = discount
        if banding is not None:
            self.banding = banding
        if forward_income_to is not None:
            self.forward_income_to = forward_income_to
        if clients is not None:
            self.clients = clients
        if plan_href is not None:
            self.plan_href = plan_href
        if plans is not None:
            self.plans = plans
        if is_retainer is not None:
            self.is_retainer = is_retainer
        if fee_model is not None:
            self.fee_model = fee_model
        if tierings is not None:
            self.tierings = tierings
        if fee_detail is not None:
            self.fee_detail = fee_detail

    @property
    def id(self):
        """Gets the id of this FeeDocument.  # noqa: E501


        :return: The id of this FeeDocument.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FeeDocument.


        :param id: The id of this FeeDocument.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this FeeDocument.  # noqa: E501


        :return: The href of this FeeDocument.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this FeeDocument.


        :param href: The href of this FeeDocument.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def sequential_ref(self):
        """Gets the sequential_ref of this FeeDocument.  # noqa: E501

        Auto-generated reference number  # noqa: E501

        :return: The sequential_ref of this FeeDocument.  # noqa: E501
        :rtype: str
        """
        return self._sequential_ref

    @sequential_ref.setter
    def sequential_ref(self, sequential_ref):
        """Sets the sequential_ref of this FeeDocument.

        Auto-generated reference number  # noqa: E501

        :param sequential_ref: The sequential_ref of this FeeDocument.  # noqa: E501
        :type: str
        """

        self._sequential_ref = sequential_ref

    @property
    def selling_adviser(self):
        """Gets the selling_adviser of this FeeDocument.  # noqa: E501


        :return: The selling_adviser of this FeeDocument.  # noqa: E501
        :rtype: AdviserRef
        """
        return self._selling_adviser

    @selling_adviser.setter
    def selling_adviser(self, selling_adviser):
        """Sets the selling_adviser of this FeeDocument.


        :param selling_adviser: The selling_adviser of this FeeDocument.  # noqa: E501
        :type: AdviserRef
        """
        if selling_adviser is None:
            raise ValueError("Invalid value for `selling_adviser`, must not be `None`")  # noqa: E501

        self._selling_adviser = selling_adviser

    @property
    def advice_category(self):
        """Gets the advice_category of this FeeDocument.  # noqa: E501

        Advice category  # noqa: E501

        :return: The advice_category of this FeeDocument.  # noqa: E501
        :rtype: str
        """
        return self._advice_category

    @advice_category.setter
    def advice_category(self, advice_category):
        """Sets the advice_category of this FeeDocument.

        Advice category  # noqa: E501

        :param advice_category: The advice_category of this FeeDocument.  # noqa: E501
        :type: str
        """
        if advice_category is None:
            raise ValueError("Invalid value for `advice_category`, must not be `None`")  # noqa: E501
        allowed_values = ["IndependentAdvice", "RestrictedAdvice", "NA", "Abridged", "RestrictedCarveOut"]  # noqa: E501
        if advice_category not in allowed_values:
            raise ValueError(
                "Invalid value for `advice_category` ({0}), must be one of {1}"  # noqa: E501
                .format(advice_category, allowed_values)
            )

        self._advice_category = advice_category

    @property
    def fee_type(self):
        """Gets the fee_type of this FeeDocument.  # noqa: E501


        :return: The fee_type of this FeeDocument.  # noqa: E501
        :rtype: FeeTypeRef
        """
        return self._fee_type

    @fee_type.setter
    def fee_type(self, fee_type):
        """Sets the fee_type of this FeeDocument.


        :param fee_type: The fee_type of this FeeDocument.  # noqa: E501
        :type: FeeTypeRef
        """
        if fee_type is None:
            raise ValueError("Invalid value for `fee_type`, must not be `None`")  # noqa: E501

        self._fee_type = fee_type

    @property
    def payment_type(self):
        """Gets the payment_type of this FeeDocument.  # noqa: E501


        :return: The payment_type of this FeeDocument.  # noqa: E501
        :rtype: PaymentTypeRef
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this FeeDocument.


        :param payment_type: The payment_type of this FeeDocument.  # noqa: E501
        :type: PaymentTypeRef
        """
        if payment_type is None:
            raise ValueError("Invalid value for `payment_type`, must not be `None`")  # noqa: E501

        self._payment_type = payment_type

    @property
    def fee_charging_type(self):
        """Gets the fee_charging_type of this FeeDocument.  # noqa: E501


        :return: The fee_charging_type of this FeeDocument.  # noqa: E501
        :rtype: FeeChargingTypeRef
        """
        return self._fee_charging_type

    @fee_charging_type.setter
    def fee_charging_type(self, fee_charging_type):
        """Sets the fee_charging_type of this FeeDocument.


        :param fee_charging_type: The fee_charging_type of this FeeDocument.  # noqa: E501
        :type: FeeChargingTypeRef
        """

        self._fee_charging_type = fee_charging_type

    @property
    def fee_percentage(self):
        """Gets the fee_percentage of this FeeDocument.  # noqa: E501

        Fee percentage  # noqa: E501

        :return: The fee_percentage of this FeeDocument.  # noqa: E501
        :rtype: float
        """
        return self._fee_percentage

    @fee_percentage.setter
    def fee_percentage(self, fee_percentage):
        """Sets the fee_percentage of this FeeDocument.

        Fee percentage  # noqa: E501

        :param fee_percentage: The fee_percentage of this FeeDocument.  # noqa: E501
        :type: float
        """

        self._fee_percentage = fee_percentage

    @property
    def net(self):
        """Gets the net of this FeeDocument.  # noqa: E501


        :return: The net of this FeeDocument.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._net

    @net.setter
    def net(self, net):
        """Sets the net of this FeeDocument.


        :param net: The net of this FeeDocument.  # noqa: E501
        :type: CurrencyValue
        """

        self._net = net

    @property
    def vat(self):
        """Gets the vat of this FeeDocument.  # noqa: E501


        :return: The vat of this FeeDocument.  # noqa: E501
        :rtype: CurrencyValue
        """
        return self._vat

    @vat.setter
    def vat(self, vat):
        """Sets the vat of this FeeDocument.


        :param vat: The vat of this FeeDocument.  # noqa: E501
        :type: CurrencyValue
        """

        self._vat = vat

    @property
    def vat_rate(self):
        """Gets the vat_rate of this FeeDocument.  # noqa: E501


        :return: The vat_rate of this FeeDocument.  # noqa: E501
        :rtype: VatRateValue
        """
        return self._vat_rate

    @vat_rate.setter
    def vat_rate(self, vat_rate):
        """Sets the vat_rate of this FeeDocument.


        :param vat_rate: The vat_rate of this FeeDocument.  # noqa: E501
        :type: VatRateValue
        """

        self._vat_rate = vat_rate

    @property
    def status(self):
        """Gets the status of this FeeDocument.  # noqa: E501

        Fee status  # noqa: E501

        :return: The status of this FeeDocument.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FeeDocument.

        Fee status  # noqa: E501

        :param status: The status of this FeeDocument.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_date(self):
        """Gets the status_date of this FeeDocument.  # noqa: E501


        :return: The status_date of this FeeDocument.  # noqa: E501
        :rtype: datetime
        """
        return self._status_date

    @status_date.setter
    def status_date(self, status_date):
        """Sets the status_date of this FeeDocument.


        :param status_date: The status_date of this FeeDocument.  # noqa: E501
        :type: datetime
        """

        self._status_date = status_date

    @property
    def recurring(self):
        """Gets the recurring of this FeeDocument.  # noqa: E501


        :return: The recurring of this FeeDocument.  # noqa: E501
        :rtype: FeeRecurring
        """
        return self._recurring

    @recurring.setter
    def recurring(self, recurring):
        """Sets the recurring of this FeeDocument.


        :param recurring: The recurring of this FeeDocument.  # noqa: E501
        :type: FeeRecurring
        """

        self._recurring = recurring

    @property
    def initial_period(self):
        """Gets the initial_period of this FeeDocument.  # noqa: E501

        Initial period in months (only applicable to initial fees)  # noqa: E501

        :return: The initial_period of this FeeDocument.  # noqa: E501
        :rtype: int
        """
        return self._initial_period

    @initial_period.setter
    def initial_period(self, initial_period):
        """Sets the initial_period of this FeeDocument.

        Initial period in months (only applicable to initial fees)  # noqa: E501

        :param initial_period: The initial_period of this FeeDocument.  # noqa: E501
        :type: int
        """

        self._initial_period = initial_period

    @property
    def is_consultancy_fee(self):
        """Gets the is_consultancy_fee of this FeeDocument.  # noqa: E501

        Is the fee a consultancy fee?  # noqa: E501

        :return: The is_consultancy_fee of this FeeDocument.  # noqa: E501
        :rtype: bool
        """
        return self._is_consultancy_fee

    @is_consultancy_fee.setter
    def is_consultancy_fee(self, is_consultancy_fee):
        """Sets the is_consultancy_fee of this FeeDocument.

        Is the fee a consultancy fee?  # noqa: E501

        :param is_consultancy_fee: The is_consultancy_fee of this FeeDocument.  # noqa: E501
        :type: bool
        """

        self._is_consultancy_fee = is_consultancy_fee

    @property
    def instalment(self):
        """Gets the instalment of this FeeDocument.  # noqa: E501


        :return: The instalment of this FeeDocument.  # noqa: E501
        :rtype: Instalment
        """
        return self._instalment

    @instalment.setter
    def instalment(self, instalment):
        """Sets the instalment of this FeeDocument.


        :param instalment: The instalment of this FeeDocument.  # noqa: E501
        :type: Instalment
        """

        self._instalment = instalment

    @property
    def sent_to_client_on(self):
        """Gets the sent_to_client_on of this FeeDocument.  # noqa: E501


        :return: The sent_to_client_on of this FeeDocument.  # noqa: E501
        :rtype: datetime
        """
        return self._sent_to_client_on

    @sent_to_client_on.setter
    def sent_to_client_on(self, sent_to_client_on):
        """Sets the sent_to_client_on of this FeeDocument.


        :param sent_to_client_on: The sent_to_client_on of this FeeDocument.  # noqa: E501
        :type: datetime
        """

        self._sent_to_client_on = sent_to_client_on

    @property
    def discount(self):
        """Gets the discount of this FeeDocument.  # noqa: E501


        :return: The discount of this FeeDocument.  # noqa: E501
        :rtype: DiscountValue
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this FeeDocument.


        :param discount: The discount of this FeeDocument.  # noqa: E501
        :type: DiscountValue
        """

        self._discount = discount

    @property
    def banding(self):
        """Gets the banding of this FeeDocument.  # noqa: E501


        :return: The banding of this FeeDocument.  # noqa: E501
        :rtype: BandingRef
        """
        return self._banding

    @banding.setter
    def banding(self, banding):
        """Sets the banding of this FeeDocument.


        :param banding: The banding of this FeeDocument.  # noqa: E501
        :type: BandingRef
        """

        self._banding = banding

    @property
    def forward_income_to(self):
        """Gets the forward_income_to of this FeeDocument.  # noqa: E501


        :return: The forward_income_to of this FeeDocument.  # noqa: E501
        :rtype: ForwardIncomeToRef
        """
        return self._forward_income_to

    @forward_income_to.setter
    def forward_income_to(self, forward_income_to):
        """Sets the forward_income_to of this FeeDocument.


        :param forward_income_to: The forward_income_to of this FeeDocument.  # noqa: E501
        :type: ForwardIncomeToRef
        """

        self._forward_income_to = forward_income_to

    @property
    def clients(self):
        """Gets the clients of this FeeDocument.  # noqa: E501


        :return: The clients of this FeeDocument.  # noqa: E501
        :rtype: list[ClientRef]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this FeeDocument.


        :param clients: The clients of this FeeDocument.  # noqa: E501
        :type: list[ClientRef]
        """

        self._clients = clients

    @property
    def plan_href(self):
        """Gets the plan_href of this FeeDocument.  # noqa: E501


        :return: The plan_href of this FeeDocument.  # noqa: E501
        :rtype: str
        """
        return self._plan_href

    @plan_href.setter
    def plan_href(self, plan_href):
        """Sets the plan_href of this FeeDocument.


        :param plan_href: The plan_href of this FeeDocument.  # noqa: E501
        :type: str
        """

        self._plan_href = plan_href

    @property
    def plans(self):
        """Gets the plans of this FeeDocument.  # noqa: E501


        :return: The plans of this FeeDocument.  # noqa: E501
        :rtype: list[PlanRef]
        """
        return self._plans

    @plans.setter
    def plans(self, plans):
        """Sets the plans of this FeeDocument.


        :param plans: The plans of this FeeDocument.  # noqa: E501
        :type: list[PlanRef]
        """

        self._plans = plans

    @property
    def is_retainer(self):
        """Gets the is_retainer of this FeeDocument.  # noqa: E501

        Indicates a retainer fee (only applicable when the Advice category is N\\A).  # noqa: E501

        :return: The is_retainer of this FeeDocument.  # noqa: E501
        :rtype: bool
        """
        return self._is_retainer

    @is_retainer.setter
    def is_retainer(self, is_retainer):
        """Sets the is_retainer of this FeeDocument.

        Indicates a retainer fee (only applicable when the Advice category is N\\A).  # noqa: E501

        :param is_retainer: The is_retainer of this FeeDocument.  # noqa: E501
        :type: bool
        """

        self._is_retainer = is_retainer

    @property
    def fee_model(self):
        """Gets the fee_model of this FeeDocument.  # noqa: E501


        :return: The fee_model of this FeeDocument.  # noqa: E501
        :rtype: FeeModelRef
        """
        return self._fee_model

    @fee_model.setter
    def fee_model(self, fee_model):
        """Sets the fee_model of this FeeDocument.


        :param fee_model: The fee_model of this FeeDocument.  # noqa: E501
        :type: FeeModelRef
        """

        self._fee_model = fee_model

    @property
    def tierings(self):
        """Gets the tierings of this FeeDocument.  # noqa: E501

        Fee tiering  # noqa: E501

        :return: The tierings of this FeeDocument.  # noqa: E501
        :rtype: list[FeeTiering]
        """
        return self._tierings

    @tierings.setter
    def tierings(self, tierings):
        """Sets the tierings of this FeeDocument.

        Fee tiering  # noqa: E501

        :param tierings: The tierings of this FeeDocument.  # noqa: E501
        :type: list[FeeTiering]
        """

        self._tierings = tierings

    @property
    def fee_detail(self):
        """Gets the fee_detail of this FeeDocument.  # noqa: E501


        :return: The fee_detail of this FeeDocument.  # noqa: E501
        :rtype: FeeDetail
        """
        return self._fee_detail

    @fee_detail.setter
    def fee_detail(self, fee_detail):
        """Sets the fee_detail of this FeeDocument.


        :param fee_detail: The fee_detail of this FeeDocument.  # noqa: E501
        :type: FeeDetail
        """

        self._fee_detail = fee_detail

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
        if issubclass(FeeDocument, dict):
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
        if not isinstance(other, FeeDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
