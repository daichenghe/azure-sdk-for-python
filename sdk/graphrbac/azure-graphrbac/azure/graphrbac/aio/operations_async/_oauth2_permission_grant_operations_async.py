# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, map_error

from ... import models


class OAuth2PermissionGrantOperations:
    """OAuth2PermissionGrantOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.graphrbac.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    
    def list(self, filter=None, cls=None, **kwargs):
        """Queries OAuth2 permissions grants for the relevant SP ObjectId of an app.

        FIXME: add operation.summary


        :param filter: The filters to apply to the operation.
        :type filter: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: OAuth2PermissionGrantListResult or the result of cls(response)
        :rtype: ~azure.graphrbac.models.OAuth2PermissionGrantListResult
        :raises: ~azure.core.HttpResponseError
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "1.6"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = '/{tenantID}/{nextLink}'
                path_format_arguments = {
                    'nextLink': self._serialize.url("next_link", next_link, 'str', skip_quote=True),
                    'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)

            # Construct parameters
            query_parameters = {}
            if filter is not None:
                query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')


            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(response):
            deserialized = self._deserialize('OAuth2PermissionGrantListResult', response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/{tenantID}/oauth2PermissionGrants'}


    
    async def create(self, body=None, cls=None, **kwargs):
        """Grants OAuth2 permissions for the relevant resource Ids of an app.

        FIXME: add operation.summary

        :param body: The relevant app Service Principal Object Id and the Service Principal Object Id you want to grant.
        :type body: ~azure.graphrbac.models.OAuth2PermissionGrant
        :param callable cls: A custom type or function that will be passed the direct response
        :return: OAuth2PermissionGrant or the result of cls(response)
        :rtype: ~azure.graphrbac.models.OAuth2PermissionGrant
        :raises: ~azure.core.HttpResponseError
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "1.6"

        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if body is not None:
            body_content = self._serialize.body(body, 'OAuth2PermissionGrant')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('OAuth2PermissionGrant', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    create.metadata = {'url': '/{tenantID}/oauth2PermissionGrants'}

    
    async def delete(self, object_id, cls=None, **kwargs):
        """Delete a OAuth2 permission grant for the relevant resource Ids of an app.

        FIXME: add operation.summary

        :param object_id: Application object ID.
        :type object_id: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.graphrbac.models.GraphErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "1.6"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'objectId': self._serialize.url("object_id", object_id, 'str'),
            'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.GraphErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    delete.metadata = {'url': '/{tenantID}/oauth2PermissionGrants/{objectId}'}