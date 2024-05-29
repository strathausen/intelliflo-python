# coding: utf-8

"""
    public-v2-prd-gb-01

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2016-08-19T00:00:00Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PlanpurposesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_planpurposes(self, authorization, x_api_key, **kwargs):  # noqa: E501
        """Returns a list of plan purposes for a specific tenant.   # noqa: E501

        This will return an unfiltered collection of Plan Purpose resources that have been configured for the [Tenant](/apis?tags=tenants).  This collection can be narrowed by specifying a [PlanType](/apis?tags=plantypes) as an optional query parameter. *Example:* `/planpurposes?planType=Cash%20Account`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_planpurposes(authorization, x_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: (required)
        :param str x_api_key: (required)
        :param str accept:
        :param str plan_type: Narrows the scope of the returned collection to only those associated with the given planType
        :param int skip: Number of records to skip. Must be greater than or equal to zero
        :param int tenant_id: Tenant identifier
        :param int top: The number of records to retrieve (default 25, max 100)
        :return: PlanPurposeCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_planpurposes_with_http_info(authorization, x_api_key, **kwargs)  # noqa: E501
        else:
            (data) = self.list_planpurposes_with_http_info(authorization, x_api_key, **kwargs)  # noqa: E501
            return data

    def list_planpurposes_with_http_info(self, authorization, x_api_key, **kwargs):  # noqa: E501
        """Returns a list of plan purposes for a specific tenant.   # noqa: E501

        This will return an unfiltered collection of Plan Purpose resources that have been configured for the [Tenant](/apis?tags=tenants).  This collection can be narrowed by specifying a [PlanType](/apis?tags=plantypes) as an optional query parameter. *Example:* `/planpurposes?planType=Cash%20Account`   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_planpurposes_with_http_info(authorization, x_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: (required)
        :param str x_api_key: (required)
        :param str accept:
        :param str plan_type: Narrows the scope of the returned collection to only those associated with the given planType
        :param int skip: Number of records to skip. Must be greater than or equal to zero
        :param int tenant_id: Tenant identifier
        :param int top: The number of records to retrieve (default 25, max 100)
        :return: PlanPurposeCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_api_key', 'accept', 'plan_type', 'skip', 'tenant_id', 'top']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_planpurposes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `list_planpurposes`")  # noqa: E501
        # verify the required parameter 'x_api_key' is set
        if ('x_api_key' not in params or
                params['x_api_key'] is None):
            raise ValueError("Missing the required parameter `x_api_key` when calling `list_planpurposes`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'plan_type' in params:
            query_params.append(('planType', params['plan_type']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'tenant_id' in params:
            query_params.append(('tenantId', params['tenant_id']))  # noqa: E501
        if 'top' in params:
            query_params.append(('top', params['top']))  # noqa: E501

        header_params = {}
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_api_key' in params:
            header_params['x-api-key'] = params['x_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'oauth2-authorization-code', 'oauth2-implicit', 'oauth2-password']  # noqa: E501

        return self.api_client.call_api(
            '/planpurposes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlanPurposeCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
