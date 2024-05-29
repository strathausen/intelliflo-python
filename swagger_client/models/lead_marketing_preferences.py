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

class LeadMarketingPreferences(object):
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
        'lead': 'LeadRef',
        'id': 'int',
        'allow_company_contact_by_telephone': 'bool',
        'allow_company_contact_by_mail': 'bool',
        'allow_company_contact_by_email': 'bool',
        'allow_company_contact_by_sms': 'bool',
        'allow_company_contact_by_social_media': 'bool',
        'allow_company_contact_by_automated_calls': 'bool',
        'allow_company_contact_by_pfp': 'bool',
        'allow_third_party_contact_by_telephone': 'bool',
        'allow_third_party_contact_by_mail': 'bool',
        'allow_third_party_contact_by_email': 'bool',
        'allow_third_party_contact_by_sms': 'bool',
        'allow_third_party_contact_by_social_media': 'bool',
        'allow_third_party_contact_by_automated_calls': 'bool',
        'allow_third_party_contact_by_pfp': 'bool',
        'can_contact_for_marketing_purposes': 'str',
        'consented_at': 'datetime',
        'delivery_method': 'str',
        'accessible_format': 'str'
    }

    attribute_map = {
        'href': 'href',
        'lead': 'lead',
        'id': 'id',
        'allow_company_contact_by_telephone': 'allowCompanyContactByTelephone',
        'allow_company_contact_by_mail': 'allowCompanyContactByMail',
        'allow_company_contact_by_email': 'allowCompanyContactByEmail',
        'allow_company_contact_by_sms': 'allowCompanyContactBySms',
        'allow_company_contact_by_social_media': 'allowCompanyContactBySocialMedia',
        'allow_company_contact_by_automated_calls': 'allowCompanyContactByAutomatedCalls',
        'allow_company_contact_by_pfp': 'allowCompanyContactByPfp',
        'allow_third_party_contact_by_telephone': 'allowThirdPartyContactByTelephone',
        'allow_third_party_contact_by_mail': 'allowThirdPartyContactByMail',
        'allow_third_party_contact_by_email': 'allowThirdPartyContactByEmail',
        'allow_third_party_contact_by_sms': 'allowThirdPartyContactBySms',
        'allow_third_party_contact_by_social_media': 'allowThirdPartyContactBySocialMedia',
        'allow_third_party_contact_by_automated_calls': 'allowThirdPartyContactByAutomatedCalls',
        'allow_third_party_contact_by_pfp': 'allowThirdPartyContactByPfp',
        'can_contact_for_marketing_purposes': 'canContactForMarketingPurposes',
        'consented_at': 'consentedAt',
        'delivery_method': 'deliveryMethod',
        'accessible_format': 'accessibleFormat'
    }

    def __init__(self, href=None, lead=None, id=None, allow_company_contact_by_telephone=None, allow_company_contact_by_mail=None, allow_company_contact_by_email=None, allow_company_contact_by_sms=None, allow_company_contact_by_social_media=None, allow_company_contact_by_automated_calls=None, allow_company_contact_by_pfp=None, allow_third_party_contact_by_telephone=None, allow_third_party_contact_by_mail=None, allow_third_party_contact_by_email=None, allow_third_party_contact_by_sms=None, allow_third_party_contact_by_social_media=None, allow_third_party_contact_by_automated_calls=None, allow_third_party_contact_by_pfp=None, can_contact_for_marketing_purposes=None, consented_at=None, delivery_method=None, accessible_format=None):  # noqa: E501
        """LeadMarketingPreferences - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._lead = None
        self._id = None
        self._allow_company_contact_by_telephone = None
        self._allow_company_contact_by_mail = None
        self._allow_company_contact_by_email = None
        self._allow_company_contact_by_sms = None
        self._allow_company_contact_by_social_media = None
        self._allow_company_contact_by_automated_calls = None
        self._allow_company_contact_by_pfp = None
        self._allow_third_party_contact_by_telephone = None
        self._allow_third_party_contact_by_mail = None
        self._allow_third_party_contact_by_email = None
        self._allow_third_party_contact_by_sms = None
        self._allow_third_party_contact_by_social_media = None
        self._allow_third_party_contact_by_automated_calls = None
        self._allow_third_party_contact_by_pfp = None
        self._can_contact_for_marketing_purposes = None
        self._consented_at = None
        self._delivery_method = None
        self._accessible_format = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if lead is not None:
            self.lead = lead
        if id is not None:
            self.id = id
        if allow_company_contact_by_telephone is not None:
            self.allow_company_contact_by_telephone = allow_company_contact_by_telephone
        if allow_company_contact_by_mail is not None:
            self.allow_company_contact_by_mail = allow_company_contact_by_mail
        if allow_company_contact_by_email is not None:
            self.allow_company_contact_by_email = allow_company_contact_by_email
        if allow_company_contact_by_sms is not None:
            self.allow_company_contact_by_sms = allow_company_contact_by_sms
        if allow_company_contact_by_social_media is not None:
            self.allow_company_contact_by_social_media = allow_company_contact_by_social_media
        if allow_company_contact_by_automated_calls is not None:
            self.allow_company_contact_by_automated_calls = allow_company_contact_by_automated_calls
        if allow_company_contact_by_pfp is not None:
            self.allow_company_contact_by_pfp = allow_company_contact_by_pfp
        if allow_third_party_contact_by_telephone is not None:
            self.allow_third_party_contact_by_telephone = allow_third_party_contact_by_telephone
        if allow_third_party_contact_by_mail is not None:
            self.allow_third_party_contact_by_mail = allow_third_party_contact_by_mail
        if allow_third_party_contact_by_email is not None:
            self.allow_third_party_contact_by_email = allow_third_party_contact_by_email
        if allow_third_party_contact_by_sms is not None:
            self.allow_third_party_contact_by_sms = allow_third_party_contact_by_sms
        if allow_third_party_contact_by_social_media is not None:
            self.allow_third_party_contact_by_social_media = allow_third_party_contact_by_social_media
        if allow_third_party_contact_by_automated_calls is not None:
            self.allow_third_party_contact_by_automated_calls = allow_third_party_contact_by_automated_calls
        if allow_third_party_contact_by_pfp is not None:
            self.allow_third_party_contact_by_pfp = allow_third_party_contact_by_pfp
        if can_contact_for_marketing_purposes is not None:
            self.can_contact_for_marketing_purposes = can_contact_for_marketing_purposes
        if consented_at is not None:
            self.consented_at = consented_at
        if delivery_method is not None:
            self.delivery_method = delivery_method
        if accessible_format is not None:
            self.accessible_format = accessible_format

    @property
    def href(self):
        """Gets the href of this LeadMarketingPreferences.  # noqa: E501


        :return: The href of this LeadMarketingPreferences.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this LeadMarketingPreferences.


        :param href: The href of this LeadMarketingPreferences.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def lead(self):
        """Gets the lead of this LeadMarketingPreferences.  # noqa: E501


        :return: The lead of this LeadMarketingPreferences.  # noqa: E501
        :rtype: LeadRef
        """
        return self._lead

    @lead.setter
    def lead(self, lead):
        """Sets the lead of this LeadMarketingPreferences.


        :param lead: The lead of this LeadMarketingPreferences.  # noqa: E501
        :type: LeadRef
        """

        self._lead = lead

    @property
    def id(self):
        """Gets the id of this LeadMarketingPreferences.  # noqa: E501


        :return: The id of this LeadMarketingPreferences.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LeadMarketingPreferences.


        :param id: The id of this LeadMarketingPreferences.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def allow_company_contact_by_telephone(self):
        """Gets the allow_company_contact_by_telephone of this LeadMarketingPreferences.  # noqa: E501

        Would like to be contacted by the company using telephone  # noqa: E501

        :return: The allow_company_contact_by_telephone of this LeadMarketingPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._allow_company_contact_by_telephone

    @allow_company_contact_by_telephone.setter
    def allow_company_contact_by_telephone(self, allow_company_contact_by_telephone):
        """Sets the allow_company_contact_by_telephone of this LeadMarketingPreferences.

        Would like to be contacted by the company using telephone  # noqa: E501

        :param allow_company_contact_by_telephone: The allow_company_contact_by_telephone of this LeadMarketingPreferences.  # noqa: E501
        :type: bool
        """

        self._allow_company_contact_by_telephone = allow_company_contact_by_telephone

    @property
    def allow_company_contact_by_mail(self):
        """Gets the allow_company_contact_by_mail of this LeadMarketingPreferences.  # noqa: E501

        Would like to be contacted by the company using mail  # noqa: E501

        :return: The allow_company_contact_by_mail of this LeadMarketingPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._allow_company_contact_by_mail

    @allow_company_contact_by_mail.setter
    def allow_company_contact_by_mail(self, allow_company_contact_by_mail):
        """Sets the allow_company_contact_by_mail of this LeadMarketingPreferences.

        Would like to be contacted by the company using mail  # noqa: E501

        :param allow_company_contact_by_mail: The allow_company_contact_by_mail of this LeadMarketingPreferences.  # noqa: E501
        :type: bool
        """

        self._allow_company_contact_by_mail = allow_company_contact_by_mail

    @property
    def allow_company_contact_by_email(self):
        """Gets the allow_company_contact_by_email of this LeadMarketingPreferences.  # noqa: E501

        Would like to be contacted by the company using email  # noqa: E501

        :return: The allow_company_contact_by_email of this LeadMarketingPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._allow_company_contact_by_email

    @allow_company_contact_by_email.setter
    def allow_company_contact_by_email(self, allow_company_contact_by_email):
        """Sets the allow_company_contact_by_email of this LeadMarketingPreferences.

        Would like to be contacted by the company using email  # noqa: E501

        :param allow_company_contact_by_email: The allow_company_contact_by_email of this LeadMarketingPreferences.  # noqa: E501
        :type: bool
        """

        self._allow_company_contact_by_email = allow_company_contact_by_email

    @property
    def allow_company_contact_by_sms(self):
        """Gets the allow_company_contact_by_sms of this LeadMarketingPreferences.  # noqa: E501

        Would like to be contacted by the company using SMS  # noqa: E501

        :return: The allow_company_contact_by_sms of this LeadMarketingPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._allow_company_contact_by_sms

    @allow_company_contact_by_sms.setter
    def allow_company_contact_by_sms(self, allow_company_contact_by_sms):
        """Sets the allow_company_contact_by_sms of this LeadMarketingPreferences.

        Would like to be contacted by the company using SMS  # noqa: E501

        :param allow_company_contact_by_sms: The allow_company_contact_by_sms of this LeadMarketingPreferences.  # noqa: E501
        :type: bool
        """

        self._allow_company_contact_by_sms = allow_company_contact_by_sms

    @property
    def allow_company_contact_by_social_media(self):
        """Gets the allow_company_contact_by_social_media of this LeadMarketingPreferences.  # noqa: E501

        Would like to be contacted by the company using social media networks  # noqa: E501

        :return: The allow_company_contact_by_social_media of this LeadMarketingPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._allow_company_contact_by_social_media

    @allow_company_contact_by_social_media.setter
    def allow_company_contact_by_social_media(self, allow_company_contact_by_social_media):
        """Sets the allow_company_contact_by_social_media of this LeadMarketingPreferences.

        Would like to be contacted by the company using social media networks  # noqa: E501

        :param allow_company_contact_by_social_media: The allow_company_contact_by_social_media of this LeadMarketingPreferences.  # noqa: E501
        :type: bool
        """

        self._allow_company_contact_by_social_media = allow_company_contact_by_social_media

    @property
    def allow_company_contact_by_automated_calls(self):
        """Gets the allow_company_contact_by_automated_calls of this LeadMarketingPreferences.  # noqa: E501

        Would like to be contacted by the company using automated calls  # noqa: E501

        :return: The allow_company_contact_by_automated_calls of this LeadMarketingPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._allow_company_contact_by_automated_calls

    @allow_company_contact_by_automated_calls.setter
    def allow_company_contact_by_automated_calls(self, allow_company_contact_by_automated_calls):
        """Sets the allow_company_contact_by_automated_calls of this LeadMarketingPreferences.

        Would like to be contacted by the company using automated calls  # noqa: E501

        :param allow_company_contact_by_automated_calls: The allow_company_contact_by_automated_calls of this LeadMarketingPreferences.  # noqa: E501
        :type: bool
        """

        self._allow_company_contact_by_automated_calls = allow_company_contact_by_automated_calls

    @property
    def allow_company_contact_by_pfp(self):
        """Gets the allow_company_contact_by_pfp of this LeadMarketingPreferences.  # noqa: E501

        Would like to be contacted by the company using PFP  # noqa: E501

        :return: The allow_company_contact_by_pfp of this LeadMarketingPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._allow_company_contact_by_pfp

    @allow_company_contact_by_pfp.setter
    def allow_company_contact_by_pfp(self, allow_company_contact_by_pfp):
        """Sets the allow_company_contact_by_pfp of this LeadMarketingPreferences.

        Would like to be contacted by the company using PFP  # noqa: E501

        :param allow_company_contact_by_pfp: The allow_company_contact_by_pfp of this LeadMarketingPreferences.  # noqa: E501
        :type: bool
        """

        self._allow_company_contact_by_pfp = allow_company_contact_by_pfp

    @property
    def allow_third_party_contact_by_telephone(self):
        """Gets the allow_third_party_contact_by_telephone of this LeadMarketingPreferences.  # noqa: E501

        Would like to be contacted by third party companies using telephone  # noqa: E501

        :return: The allow_third_party_contact_by_telephone of this LeadMarketingPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._allow_third_party_contact_by_telephone

    @allow_third_party_contact_by_telephone.setter
    def allow_third_party_contact_by_telephone(self, allow_third_party_contact_by_telephone):
        """Sets the allow_third_party_contact_by_telephone of this LeadMarketingPreferences.

        Would like to be contacted by third party companies using telephone  # noqa: E501

        :param allow_third_party_contact_by_telephone: The allow_third_party_contact_by_telephone of this LeadMarketingPreferences.  # noqa: E501
        :type: bool
        """

        self._allow_third_party_contact_by_telephone = allow_third_party_contact_by_telephone

    @property
    def allow_third_party_contact_by_mail(self):
        """Gets the allow_third_party_contact_by_mail of this LeadMarketingPreferences.  # noqa: E501

        Would like to be contacted by third party companies using mail  # noqa: E501

        :return: The allow_third_party_contact_by_mail of this LeadMarketingPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._allow_third_party_contact_by_mail

    @allow_third_party_contact_by_mail.setter
    def allow_third_party_contact_by_mail(self, allow_third_party_contact_by_mail):
        """Sets the allow_third_party_contact_by_mail of this LeadMarketingPreferences.

        Would like to be contacted by third party companies using mail  # noqa: E501

        :param allow_third_party_contact_by_mail: The allow_third_party_contact_by_mail of this LeadMarketingPreferences.  # noqa: E501
        :type: bool
        """

        self._allow_third_party_contact_by_mail = allow_third_party_contact_by_mail

    @property
    def allow_third_party_contact_by_email(self):
        """Gets the allow_third_party_contact_by_email of this LeadMarketingPreferences.  # noqa: E501

        Would like to be contacted by third party companies using email  # noqa: E501

        :return: The allow_third_party_contact_by_email of this LeadMarketingPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._allow_third_party_contact_by_email

    @allow_third_party_contact_by_email.setter
    def allow_third_party_contact_by_email(self, allow_third_party_contact_by_email):
        """Sets the allow_third_party_contact_by_email of this LeadMarketingPreferences.

        Would like to be contacted by third party companies using email  # noqa: E501

        :param allow_third_party_contact_by_email: The allow_third_party_contact_by_email of this LeadMarketingPreferences.  # noqa: E501
        :type: bool
        """

        self._allow_third_party_contact_by_email = allow_third_party_contact_by_email

    @property
    def allow_third_party_contact_by_sms(self):
        """Gets the allow_third_party_contact_by_sms of this LeadMarketingPreferences.  # noqa: E501

        Would like to be contacted by third party companies using SMS  # noqa: E501

        :return: The allow_third_party_contact_by_sms of this LeadMarketingPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._allow_third_party_contact_by_sms

    @allow_third_party_contact_by_sms.setter
    def allow_third_party_contact_by_sms(self, allow_third_party_contact_by_sms):
        """Sets the allow_third_party_contact_by_sms of this LeadMarketingPreferences.

        Would like to be contacted by third party companies using SMS  # noqa: E501

        :param allow_third_party_contact_by_sms: The allow_third_party_contact_by_sms of this LeadMarketingPreferences.  # noqa: E501
        :type: bool
        """

        self._allow_third_party_contact_by_sms = allow_third_party_contact_by_sms

    @property
    def allow_third_party_contact_by_social_media(self):
        """Gets the allow_third_party_contact_by_social_media of this LeadMarketingPreferences.  # noqa: E501

        Would like to be contacted by third party companies using social media networks  # noqa: E501

        :return: The allow_third_party_contact_by_social_media of this LeadMarketingPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._allow_third_party_contact_by_social_media

    @allow_third_party_contact_by_social_media.setter
    def allow_third_party_contact_by_social_media(self, allow_third_party_contact_by_social_media):
        """Sets the allow_third_party_contact_by_social_media of this LeadMarketingPreferences.

        Would like to be contacted by third party companies using social media networks  # noqa: E501

        :param allow_third_party_contact_by_social_media: The allow_third_party_contact_by_social_media of this LeadMarketingPreferences.  # noqa: E501
        :type: bool
        """

        self._allow_third_party_contact_by_social_media = allow_third_party_contact_by_social_media

    @property
    def allow_third_party_contact_by_automated_calls(self):
        """Gets the allow_third_party_contact_by_automated_calls of this LeadMarketingPreferences.  # noqa: E501

        Would like to be contacted by third party companies using automated calls  # noqa: E501

        :return: The allow_third_party_contact_by_automated_calls of this LeadMarketingPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._allow_third_party_contact_by_automated_calls

    @allow_third_party_contact_by_automated_calls.setter
    def allow_third_party_contact_by_automated_calls(self, allow_third_party_contact_by_automated_calls):
        """Sets the allow_third_party_contact_by_automated_calls of this LeadMarketingPreferences.

        Would like to be contacted by third party companies using automated calls  # noqa: E501

        :param allow_third_party_contact_by_automated_calls: The allow_third_party_contact_by_automated_calls of this LeadMarketingPreferences.  # noqa: E501
        :type: bool
        """

        self._allow_third_party_contact_by_automated_calls = allow_third_party_contact_by_automated_calls

    @property
    def allow_third_party_contact_by_pfp(self):
        """Gets the allow_third_party_contact_by_pfp of this LeadMarketingPreferences.  # noqa: E501

        Would like to be contacted by third party companies using PFP  # noqa: E501

        :return: The allow_third_party_contact_by_pfp of this LeadMarketingPreferences.  # noqa: E501
        :rtype: bool
        """
        return self._allow_third_party_contact_by_pfp

    @allow_third_party_contact_by_pfp.setter
    def allow_third_party_contact_by_pfp(self, allow_third_party_contact_by_pfp):
        """Sets the allow_third_party_contact_by_pfp of this LeadMarketingPreferences.

        Would like to be contacted by third party companies using PFP  # noqa: E501

        :param allow_third_party_contact_by_pfp: The allow_third_party_contact_by_pfp of this LeadMarketingPreferences.  # noqa: E501
        :type: bool
        """

        self._allow_third_party_contact_by_pfp = allow_third_party_contact_by_pfp

    @property
    def can_contact_for_marketing_purposes(self):
        """Gets the can_contact_for_marketing_purposes of this LeadMarketingPreferences.  # noqa: E501

        A general and overriding consent statement.  A Yes means that the preferences in this document must be honored, a No means no contact at all (preferences can be ignored)  and a RelatedProductsOnly answer is the same as a Yes but narrows the consent to related products only.  # noqa: E501

        :return: The can_contact_for_marketing_purposes of this LeadMarketingPreferences.  # noqa: E501
        :rtype: str
        """
        return self._can_contact_for_marketing_purposes

    @can_contact_for_marketing_purposes.setter
    def can_contact_for_marketing_purposes(self, can_contact_for_marketing_purposes):
        """Sets the can_contact_for_marketing_purposes of this LeadMarketingPreferences.

        A general and overriding consent statement.  A Yes means that the preferences in this document must be honored, a No means no contact at all (preferences can be ignored)  and a RelatedProductsOnly answer is the same as a Yes but narrows the consent to related products only.  # noqa: E501

        :param can_contact_for_marketing_purposes: The can_contact_for_marketing_purposes of this LeadMarketingPreferences.  # noqa: E501
        :type: str
        """
        allowed_values = ["No", "Yes", "RelatedProductsOnly"]  # noqa: E501
        if can_contact_for_marketing_purposes not in allowed_values:
            raise ValueError(
                "Invalid value for `can_contact_for_marketing_purposes` ({0}), must be one of {1}"  # noqa: E501
                .format(can_contact_for_marketing_purposes, allowed_values)
            )

        self._can_contact_for_marketing_purposes = can_contact_for_marketing_purposes

    @property
    def consented_at(self):
        """Gets the consented_at of this LeadMarketingPreferences.  # noqa: E501

        The date at which consent was given.  # noqa: E501

        :return: The consented_at of this LeadMarketingPreferences.  # noqa: E501
        :rtype: datetime
        """
        return self._consented_at

    @consented_at.setter
    def consented_at(self, consented_at):
        """Sets the consented_at of this LeadMarketingPreferences.

        The date at which consent was given.  # noqa: E501

        :param consented_at: The consented_at of this LeadMarketingPreferences.  # noqa: E501
        :type: datetime
        """

        self._consented_at = consented_at

    @property
    def delivery_method(self):
        """Gets the delivery_method of this LeadMarketingPreferences.  # noqa: E501

        Method of delivering information  # noqa: E501

        :return: The delivery_method of this LeadMarketingPreferences.  # noqa: E501
        :rtype: str
        """
        return self._delivery_method

    @delivery_method.setter
    def delivery_method(self, delivery_method):
        """Sets the delivery_method of this LeadMarketingPreferences.

        Method of delivering information  # noqa: E501

        :param delivery_method: The delivery_method of this LeadMarketingPreferences.  # noqa: E501
        :type: str
        """
        allowed_values = ["NoPreference", "Electronic", "Post"]  # noqa: E501
        if delivery_method not in allowed_values:
            raise ValueError(
                "Invalid value for `delivery_method` ({0}), must be one of {1}"  # noqa: E501
                .format(delivery_method, allowed_values)
            )

        self._delivery_method = delivery_method

    @property
    def accessible_format(self):
        """Gets the accessible_format of this LeadMarketingPreferences.  # noqa: E501

        Special accessibility options  # noqa: E501

        :return: The accessible_format of this LeadMarketingPreferences.  # noqa: E501
        :rtype: str
        """
        return self._accessible_format

    @accessible_format.setter
    def accessible_format(self, accessible_format):
        """Sets the accessible_format of this LeadMarketingPreferences.

        Special accessibility options  # noqa: E501

        :param accessible_format: The accessible_format of this LeadMarketingPreferences.  # noqa: E501
        :type: str
        """
        allowed_values = ["NoRequirement", "LargePrint", "AudioTape", "Braille"]  # noqa: E501
        if accessible_format not in allowed_values:
            raise ValueError(
                "Invalid value for `accessible_format` ({0}), must be one of {1}"  # noqa: E501
                .format(accessible_format, allowed_values)
            )

        self._accessible_format = accessible_format

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
        if issubclass(LeadMarketingPreferences, dict):
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
        if not isinstance(other, LeadMarketingPreferences):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
