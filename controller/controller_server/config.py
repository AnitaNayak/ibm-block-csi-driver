from controller.csi_general import csi_pb2

SUPPORTED_FS_TYPES = ["ext4", "xfs"]

access_mode = csi_pb2.VolumeCapability.AccessMode
SUPPORTED_ACCESS_MODE = [access_mode.SINGLE_NODE_WRITER]

# VolumeCapabilities fields which specify if it is volume with fs or raw block volume
VOLUME_CAPABILITIES_FIELD_ACCESS_TYPE_MOUNT = 'mount'
VOLUME_CAPABILITIES_FIELD_ACCESS_TYPE_BLOCK = 'block'

SECRET_USERNAME_PARAMETER = "username"
SECRET_PASSWORD_PARAMETER = "password"
SECRET_ARRAY_PARAMETER = "management_address"

PARAMETERS_POOL = "pool"
PARAMETERS_CAPABILITIES_SPACEEFFICIENCY = "SpaceEfficiency"
PARAMETERS_VOLUME_NAME_PREFIX = "volume_name_prefix"
PARAMETERS_SNAPSHOT_NAME_PREFIX = "snapshot_name_prefix"
PARAMETERS_CAPACITY_DELIMITER = "="
PARAMETERS_CAPABILITIES_DELIMITER = "="
PARAMETERS_OBJECT_ID_DELIMITER = ":"
PARAMETERS_NODE_ID_DELIMITER = ";"
PARAMETERS_FC_WWN_DELIMITER = ":"

SUPPORTED_CONNECTIVITY_TYPES = 2

SNAPSHOT_TYPE_NAME = "snapshot"
VOLUME_TYPE_NAME = "volume"
VOLUME_SOURCE_ID_FIELDS = {SNAPSHOT_TYPE_NAME: 'snapshot_id', VOLUME_TYPE_NAME: 'volume_id'}
