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

from msrest.service_client import ServiceClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from . import models


class TextAnalyticsAPIConfiguration(Configuration):
    """Configuration for TextAnalyticsAPI
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param azure_region: Supported Azure regions for Cognitive Services
     endpoints. Possible values include: 'westus', 'westeurope',
     'southeastasia', 'eastus2', 'westcentralus'
    :type azure_region: str or
     ~azure.cognitiveservices.language.textanalytics.models.AzureRegions
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, azure_region, credentials):

        if azure_region is None:
            raise ValueError("Parameter 'azure_region' must not be None.")
        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        base_url = 'https://{AzureRegion}.api.cognitive.microsoft.com/text/analytics'

        super(TextAnalyticsAPIConfiguration, self).__init__(base_url)

        self.add_user_agent('textanalyticsapi/{}'.format(VERSION))

        self.azure_region = azure_region
        self.credentials = credentials


class TextAnalyticsAPI(object):
    """The Text Analytics API is a suite of text analytics web services built with best-in-class Microsoft machine learning algorithms. The API can be used to analyze unstructured text for tasks such as sentiment analysis, key phrase extraction and language detection. No training data is needed to use this API; just bring your text data. This API uses advanced natural language processing techniques to deliver best in class predictions. Further documentation can be found in https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview

    :ivar config: Configuration for client.
    :vartype config: TextAnalyticsAPIConfiguration

    :param azure_region: Supported Azure regions for Cognitive Services
     endpoints. Possible values include: 'westus', 'westeurope',
     'southeastasia', 'eastus2', 'westcentralus'
    :type azure_region: str or
     ~azure.cognitiveservices.language.textanalytics.models.AzureRegions
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, azure_region, credentials):

        self.config = TextAnalyticsAPIConfiguration(azure_region, credentials)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = 'v2.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)


    def key_phrases(
            self, documents=None, custom_headers=None, raw=False, **operation_config):
        """The API returns a list of strings denoting the key talking points in
        the input text.

        We employ techniques from Microsoft Office's sophisticated Natural
        Language Processing toolkit. See the <a
        href="https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview#supported-languages">Text
        Analytics Documentation</a> for details about the languages that are
        supported by key phrase extraction.

        :param documents:
        :type documents:
         list[~azure.cognitiveservices.language.textanalytics.models.MultiLanguageInput]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: KeyPhraseBatchResult or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.language.textanalytics.models.KeyPhraseBatchResult
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.textanalytics.models.ErrorResponseException>`
        """
        input = models.MultiLanguageBatchInput(documents=documents)

        # Construct URL
        url = '/v2.0/keyPhrases'
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

        # Construct body
        body_content = self._serialize.body(input, 'MultiLanguageBatchInput')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('KeyPhraseBatchResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def detect_language(
            self, number_of_languages_to_detect=None, documents=None, custom_headers=None, raw=False, **operation_config):
        """The API returns the detected language and a numeric score between 0 and
        1.

        Scores close to 1 indicate 100% certainty that the identified language
        is true. A total of 120 languages are supported.

        :param number_of_languages_to_detect: (Optional. Deprecated) Number of
         languages to detect. Set to 1 by default. Irrespective of the value,
         the language with the highest score is returned.
        :type number_of_languages_to_detect: int
        :param documents:
        :type documents:
         list[~azure.cognitiveservices.language.textanalytics.models.Input]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LanguageBatchResult or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.language.textanalytics.models.LanguageBatchResult
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.textanalytics.models.ErrorResponseException>`
        """
        input = models.BatchInput(documents=documents)

        # Construct URL
        url = '/v2.0/languages'
        path_format_arguments = {
            'AzureRegion': self._serialize.url("self.config.azure_region", self.config.azure_region, 'AzureRegions', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if number_of_languages_to_detect is not None:
            query_parameters['numberOfLanguagesToDetect'] = self._serialize.query("number_of_languages_to_detect", number_of_languages_to_detect, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(input, 'BatchInput')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LanguageBatchResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def sentiment(
            self, documents=None, custom_headers=None, raw=False, **operation_config):
        """The API returns a numeric score between 0 and 1.

        Scores close to 1 indicate positive sentiment, while scores close to 0
        indicate negative sentiment. Sentiment score is generated using
        classification techniques. The input features to the classifier include
        n-grams, features generated from part-of-speech tags, and word
        embeddings. See the <a
        href="https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview#supported-languages">Text
        Analytics Documentation</a> for details about the languages that are
        supported by sentiment analysis.

        :param documents:
        :type documents:
         list[~azure.cognitiveservices.language.textanalytics.models.MultiLanguageInput]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SentimentBatchResult or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.language.textanalytics.models.SentimentBatchResult
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.language.textanalytics.models.ErrorResponseException>`
        """
        input = models.MultiLanguageBatchInput(documents=documents)

        # Construct URL
        url = '/v2.0/sentiment'
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

        # Construct body
        body_content = self._serialize.body(input, 'MultiLanguageBatchInput')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SentimentBatchResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
