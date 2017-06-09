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

from .protected_item import ProtectedItem


class MabFileFolderProtectedItem(ProtectedItem):
    """MAB workload-specific backup item.

    :param backup_management_type: Type of backup managemenent for the backed
     up item. Possible values include: 'Invalid', 'AzureIaasVM', 'MAB', 'DPM',
     'AzureBackupServer', 'AzureSql'
    :type backup_management_type: str or :class:`BackupManagementType
     <azure.mgmt.recoveryservicesbackup.models.BackupManagementType>`
    :param workload_type: Type of workload this item represents. Possible
     values include: 'Invalid', 'VM', 'FileFolder', 'AzureSqlDb', 'SQLDB',
     'Exchange', 'Sharepoint', 'VMwareVM', 'SystemState', 'Client',
     'GenericDataSource'
    :type workload_type: str or :class:`DataSourceType
     <azure.mgmt.recoveryservicesbackup.models.DataSourceType>`
    :param container_name: Unique name of container
    :type container_name: str
    :param source_resource_id: ARM ID of the resource to be backed up.
    :type source_resource_id: str
    :param policy_id: ID of the backup policy with which this item is backed
     up.
    :type policy_id: str
    :param last_recovery_point: Timestamp when the last (latest) backup copy
     was created for this backup item.
    :type last_recovery_point: datetime
    :param protected_item_type: Polymorphic Discriminator
    :type protected_item_type: str
    :param friendly_name: Friendly name of this backup item.
    :type friendly_name: str
    :param computer_name: Name of the computer associated with this backup
     item.
    :type computer_name: str
    :param last_backup_status: Status of last backup operation.
    :type last_backup_status: str
    :param protection_state: Protected, ProtectionStopped, IRPending or
     ProtectionError
    :type protection_state: str
    :param is_scheduled_for_deferred_delete: Specifies if the item is
     scheduled for deferred deletion.
    :type is_scheduled_for_deferred_delete: bool
    :param deferred_delete_sync_time_in_utc: Sync time for deferred deletion.
    :type deferred_delete_sync_time_in_utc: long
    :param extended_info: Additional information with this backup item.
    :type extended_info: :class:`MabFileFolderProtectedItemExtendedInfo
     <azure.mgmt.recoveryservicesbackup.models.MabFileFolderProtectedItemExtendedInfo>`
    """

    _validation = {
        'protected_item_type': {'required': True},
    }

    _attribute_map = {
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'workload_type': {'key': 'workloadType', 'type': 'str'},
        'container_name': {'key': 'containerName', 'type': 'str'},
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
        'policy_id': {'key': 'policyId', 'type': 'str'},
        'last_recovery_point': {'key': 'lastRecoveryPoint', 'type': 'iso-8601'},
        'protected_item_type': {'key': 'protectedItemType', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'computer_name': {'key': 'computerName', 'type': 'str'},
        'last_backup_status': {'key': 'lastBackupStatus', 'type': 'str'},
        'protection_state': {'key': 'protectionState', 'type': 'str'},
        'is_scheduled_for_deferred_delete': {'key': 'isScheduledForDeferredDelete', 'type': 'bool'},
        'deferred_delete_sync_time_in_utc': {'key': 'deferredDeleteSyncTimeInUTC', 'type': 'long'},
        'extended_info': {'key': 'extendedInfo', 'type': 'MabFileFolderProtectedItemExtendedInfo'},
    }

    def __init__(self, backup_management_type=None, workload_type=None, container_name=None, source_resource_id=None, policy_id=None, last_recovery_point=None, friendly_name=None, computer_name=None, last_backup_status=None, protection_state=None, is_scheduled_for_deferred_delete=None, deferred_delete_sync_time_in_utc=None, extended_info=None):
        super(MabFileFolderProtectedItem, self).__init__(backup_management_type=backup_management_type, workload_type=workload_type, container_name=container_name, source_resource_id=source_resource_id, policy_id=policy_id, last_recovery_point=last_recovery_point)
        self.friendly_name = friendly_name
        self.computer_name = computer_name
        self.last_backup_status = last_backup_status
        self.protection_state = protection_state
        self.is_scheduled_for_deferred_delete = is_scheduled_for_deferred_delete
        self.deferred_delete_sync_time_in_utc = deferred_delete_sync_time_in_utc
        self.extended_info = extended_info
        self.protected_item_type = 'MabFileFolderProtectedItem'