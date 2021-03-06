# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class FaceListOperations(object):
    """FaceListOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def create(
            self, face_list_id, name=None, user_data=None, custom_headers=None, raw=False, **operation_config):
        """Create an empty face list. Up to 64 face lists are allowed to exist in
        one subscription.

        :param face_list_id: Id referencing a particular face list.
        :type face_list_id: str
        :param name: Name of the face list, maximum length is 128.
        :type name: str
        :param user_data: Optional user defined data for the face list. Length
         should not exceed 16KB.
        :type user_data: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        body = models.CreateFaceListRequest(name=name, user_data=user_data)

        # Construct URL
        url = '/facelists/{faceListId}'
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'faceListId': self._serialize.url("face_list_id", face_list_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'CreateFaceListRequest')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def get(
            self, face_list_id, custom_headers=None, raw=False, **operation_config):
        """Retrieve a face list's information.

        :param face_list_id: Id referencing a Face List.
        :type face_list_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: GetFaceListResult or ClientRawResponse if raw=true
        :rtype: ~azure.cognitiveservices.vision.face.models.GetFaceListResult
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = '/facelists/{faceListId}'
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'faceListId': self._serialize.url("face_list_id", face_list_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('GetFaceListResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def update(
            self, face_list_id, name=None, user_data=None, custom_headers=None, raw=False, **operation_config):
        """Update information of a face list. .

        :param face_list_id: Id referencing a Face List.
        :type face_list_id: str
        :param name: Name of the face list, maximum length is 128.
        :type name: str
        :param user_data: Optional user defined data for the face list. Length
         should not exceed 16KB.
        :type user_data: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        body = models.CreateFaceListRequest(name=name, user_data=user_data)

        # Construct URL
        url = '/facelists/{faceListId}'
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'faceListId': self._serialize.url("face_list_id", face_list_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'CreateFaceListRequest')

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def delete(
            self, face_list_id, custom_headers=None, raw=False, **operation_config):
        """Delete an existing face list according to faceListId. Persisted face
        images in the face list will also be deleted.

        :param face_list_id: Id referencing a Face List.
        :type face_list_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = '/facelists/{faceListId}'
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'faceListId': self._serialize.url("face_list_id", face_list_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def list(
            self, custom_headers=None, raw=False, **operation_config):
        """Retrieve information about all existing face lists. Only faceListId,
        name and userData will be returned.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype:
         list[~azure.cognitiveservices.vision.face.models.GetFaceListResult] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = '/facelists'
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[GetFaceListResult]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def delete_face(
            self, face_list_id, persisted_face_id, custom_headers=None, raw=False, **operation_config):
        """Delete an existing face from a face list (given by a persisitedFaceId
        and a faceListId). Persisted image related to the face will also be
        deleted.

        :param face_list_id: faceListId of an existing face list.
        :type face_list_id: str
        :param persisted_face_id: persistedFaceId of an existing face.
        :type persisted_face_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = '/facelists/{faceListId}/persistedFaces/{persistedFaceId}'
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'faceListId': self._serialize.url("face_list_id", face_list_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$'),
            'persistedFaceId': self._serialize.url("persisted_face_id", persisted_face_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def add_face(
            self, face_list_id, user_data=None, target_face=None, custom_headers=None, raw=False, **operation_config):
        """Add a face to a face list. The input face is specified as an image with
        a targetFace rectangle. It returns a persistedFaceId representing the
        added face, and persistedFaceId will not expire. .

        :param face_list_id: Id referencing a Face List.
        :type face_list_id: str
        :param user_data: User-specified data about the face list for any
         purpose. The  maximum length is 1KB.
        :type user_data: str
        :param target_face: A face rectangle to specify the target face to be
         added into the face list, in the format of
         "targetFace=left,top,width,height". E.g. "targetFace=10,10,100,100".
         If there is more than one face in the image, targetFace is required to
         specify which face to add. No targetFace means there is only one face
         detected in the entire image.
        :type target_face: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = '/facelists/{faceListId}/persistedFaces'
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'faceListId': self._serialize.url("face_list_id", face_list_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if user_data is not None:
            query_parameters['userData'] = self._serialize.query("user_data", user_data, 'str')
        if target_face is not None:
            query_parameters['targetFace'] = self._serialize.query("target_face", target_face, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def add_face_from_stream(
            self, face_list_id, user_data=None, target_face=None, custom_headers=None, raw=False, **operation_config):
        """Add a face to a face list. The input face is specified as an image with
        a targetFace rectangle. It returns a persistedFaceId representing the
        added face, and persistedFaceId will not expire.

        :param face_list_id: Id referencing a Face List.
        :type face_list_id: str
        :param user_data: User-specified data about the face list for any
         purpose. The  maximum length is 1KB.
        :type user_data: str
        :param target_face: A face rectangle to specify the target face to be
         added into the face list, in the format of
         "targetFace=left,top,width,height". E.g. "targetFace=10,10,100,100".
         If there is more than one face in the image, targetFace is required to
         specify which face to add. No targetFace means there is only one face
         detected in the entire image.
        :type target_face: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.vision.face.models.APIErrorException>`
        """
        # Construct URL
        url = '/facelists/{faceListId}/persistedFaces'
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True),
            'faceListId': self._serialize.url("face_list_id", face_list_id, 'str', max_length=64, pattern=r'^[a-z0-9-_]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if user_data is not None:
            query_parameters['userData'] = self._serialize.query("user_data", user_data, 'str')
        if target_face is not None:
            query_parameters['targetFace'] = self._serialize.query("target_face", target_face, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
