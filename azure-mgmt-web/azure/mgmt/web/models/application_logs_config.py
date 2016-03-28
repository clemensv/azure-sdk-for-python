# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApplicationLogsConfig(Model):
    """
    Application logs configuration

    :param file_system: Application logs to file system configuration
    :type file_system: :class:`FileSystemApplicationLogsConfig
     <azure.mgmt.web.models.FileSystemApplicationLogsConfig>`
    :param azure_table_storage: Application logs to azure table storage
     configuration
    :type azure_table_storage: :class:`AzureTableStorageApplicationLogsConfig
     <azure.mgmt.web.models.AzureTableStorageApplicationLogsConfig>`
    :param azure_blob_storage: Application logs to blob storage configuration
    :type azure_blob_storage: :class:`AzureBlobStorageApplicationLogsConfig
     <azure.mgmt.web.models.AzureBlobStorageApplicationLogsConfig>`
    """ 

    _attribute_map = {
        'file_system': {'key': 'fileSystem', 'type': 'FileSystemApplicationLogsConfig'},
        'azure_table_storage': {'key': 'azureTableStorage', 'type': 'AzureTableStorageApplicationLogsConfig'},
        'azure_blob_storage': {'key': 'azureBlobStorage', 'type': 'AzureBlobStorageApplicationLogsConfig'},
    }

    def __init__(self, file_system=None, azure_table_storage=None, azure_blob_storage=None, **kwargs):
        self.file_system = file_system
        self.azure_table_storage = azure_table_storage
        self.azure_blob_storage = azure_blob_storage