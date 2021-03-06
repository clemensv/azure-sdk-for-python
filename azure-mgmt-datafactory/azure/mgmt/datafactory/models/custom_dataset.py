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

from .dataset import Dataset


class CustomDataset(Dataset):
    """The custom dataset.

    :param description: Dataset description.
    :type description: str
    :param structure: Columns that define the structure of the dataset. Type:
     array (or Expression with resultType array), itemType: DatasetDataElement.
    :type structure: object
    :param linked_service_name: Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param parameters: Parameters for dataset.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param type: Constant filled by server.
    :type type: str
    :param type_properties: Custom dataset properties.
    :type type_properties: object
    """

    _validation = {
        'linked_service_name': {'required': True},
        'type': {'required': True},
        'type_properties': {'required': True},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'structure': {'key': 'structure', 'type': 'object'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'type': {'key': 'type', 'type': 'str'},
        'type_properties': {'key': 'typeProperties', 'type': 'object'},
    }

    def __init__(self, linked_service_name, type_properties, description=None, structure=None, parameters=None):
        super(CustomDataset, self).__init__(description=description, structure=structure, linked_service_name=linked_service_name, parameters=parameters)
        self.type_properties = type_properties
        self.type = 'CustomDataset'
