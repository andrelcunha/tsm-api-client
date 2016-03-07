from __future__ import (absolute_import, unicode_literals)
from ctypes import c_char, c_char_p, c_ubyte, c_short, c_ushort, c_int, c_uint, \
    c_ulong, c_long, Structure, Union, POINTER

__author__ = 'bbrauns'

dsInt8_t = c_char
dsUint8_t = c_ubyte
dsInt16_t = c_short
dsUint16_t = c_ushort
dsInt32_t = c_int
dsUint32_t = c_uint
dsULong_t = c_ulong
dsLong_t = c_long
dsInt64_t = c_long
dsUint64_t = c_long

DSM_MAX_CG_DEST_LENGTH = 30  # copy group destination
DSM_MAX_CG_NAME_LENGTH = 30  # copy group name
DSM_MAX_DESCR_LENGTH = 255  # archive description
DSM_MAX_DOMAIN_LENGTH = 30  # policy domain name
DSM_MAX_FSINFO_LENGTH = 500  # filespace info
DSM_MAX_USER_FSINFO_LENGTH = 480  # max user filespace info
DSM_MAX_FSNAME_LENGTH = 1024  # filespace name
DSM_MAX_FSTYPE_LENGTH = 32  # filespace type
DSM_MAX_HL_LENGTH = 1024  # object high level name
DSM_MAX_ID_LENGTH = 64  # session node name
DSM_MAX_LL_LENGTH = 256  # object low level name
DSM_MAX_MC_NAME_LENGTH = 30  # management class name
DSM_MAX_OBJINFO_LENGTH = 255  # object info
DSM_MAX_OWNER_LENGTH = 64  # object owner name
DSM_MAX_PLATFORM_LENGTH = 16  # application type
DSM_MAX_PS_NAME_LENGTH = 30  # policy set name
DSM_MAX_SERVERTYPE_LENGTH = 32  # server platform type
DSM_MAX_VERIFIER_LENGTH = 64  # password
DSM_PATH_MAX = 1024  # API config file path
DSM_NAME_MAX = 255  # API config file name
DSM_MAX_NODE_LENGTH = 64  # node/machine name
DSM_MAX_RC_MSG_LENGTH = 1024  # msg parm for dsmRCMsg
DSM_MAX_SERVER_ADDRESS = 1024  # server address

DSM_MAX_MC_DESCR_LENGTH = DSM_MAX_DESCR_LENGTH  # mgmt class
DSM_MAX_SERVERNAME_LENGTH = DSM_MAX_ID_LENGTH  # server name
DSM_MAX_GET_OBJ = 4080  # max objs on BeginGetData
DSM_MAX_PARTIAL_GET_OBJ = 1300  # max partial objs on BeginGetData

DSM_OBJ_FILE = 0x01  # object has attrib info & data
DSM_OBJ_DIRECTORY = 0x02  # obj has only attribute info
DSM_OBJ_RESERVED1 = 0x04  # for future use
DSM_OBJ_RESERVED2 = 0x05  # for future use
DSM_OBJ_RESERVED3 = 0x06  # for future use
DSM_OBJ_WILDCARD = 0xFE  # Any object type
DSM_OBJ_ANY_TYPE = 0xFF  # for future use

DSM_VOTE_COMMIT = 1  # commit current transaction
DSM_VOTE_ABORT = 2  # roll back current transaction

MEDIA_FIXED = 0x10  # Fixed: represents the class of on-line, fixed media (such as hard disks).
MEDIA_LIBRARY = 0x20  # Library: represents the class of mountable media accessible
# through a mechanical mounting device.
MEDIA_NETWORK = 0x30  # following stuff is for future use
MEDIA_SHELF = 0x40
MEDIA_OFFSITE = 0x50
MEDIA_UNAVAILABLE = 0xF0

DSM_API_VERSION = 7
DSM_API_RELEASE = 1
DSM_API_LEVEL = 1
DSM_API_SUBLEVEL = 0

DATE_MINUS_INFINITE = 0x0000
DATE_PLUS_INFINITE = 0xFFFF

apiVersionExVer = 2
dsmInitExInVersion = 5
dsmInitExOutVersion = 3
ApiSessInfoVersion = 6

dsmBool_t = c_int
dsmFalse, dsmTrue = (0, 1)


# noinspection PyPep8Naming
class dsmApiVersionEx(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('version', dsUint16_t),
        ('release', dsUint16_t),
        ('level', dsUint16_t),
        ('subLevel', dsUint16_t),
        ('unicode', c_int),  # bool
    ]


# noinspection PyPep8Naming
class dsmDate(Structure):
    _fields_ = [
        ('year', dsUint16_t),
        ('month', dsUint8_t),
        ('day', dsUint8_t),
        ('hour', dsUint8_t),
        ('minute', dsUint8_t),
        ('second', dsUint8_t)
    ]


# noinspection PyPep8Naming
class dsStruct64_t(Structure):
    _fields_ = [
        ('hi', dsUint32_t),
        ('lo', dsUint32_t)
    ]


dsmDedupType = c_int
dsmFailOvrCfgType = c_int


# noinspection PyPep8Naming
class ApiSessInfo(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('serverHost', c_char * (DSM_MAX_SERVERNAME_LENGTH + 1)),
        ('serverPort', dsUint16_t),
        ('serverDate', dsmDate),
        ('serverType', c_char * (DSM_MAX_SERVERTYPE_LENGTH + 1)),
        ('serverVer', dsUint16_t),
        ('serverRel', dsUint16_t),
        ('serverLev', dsUint16_t),
        ('serverSubLev', dsUint16_t),
        ('nodeType', c_char * (DSM_MAX_PLATFORM_LENGTH + 1)),
        ('fsdelim', c_char),
        ('hldelim', c_char),
        ('compression', dsUint8_t),
        ('archDel', dsUint8_t),
        ('backDel', dsUint8_t),
        ('maxBytesPerTxn', dsUint32_t),
        ('maxObjPerTxn', dsUint16_t),
        ('id', c_char * (DSM_MAX_ID_LENGTH + 1)),
        ('owner', c_char * (DSM_MAX_OWNER_LENGTH + 1)),
        ('confFile', c_char * (DSM_PATH_MAX + DSM_NAME_MAX + 1)),
        ('opNoTrace', dsUint8_t),
        ('domainName', c_char * (DSM_MAX_DOMAIN_LENGTH + 1)),
        ('policySetName', c_char * (DSM_MAX_PS_NAME_LENGTH + 1)),
        ('polActDate', dsmDate),
        ('dfltMCName', c_char * (DSM_MAX_MC_NAME_LENGTH + 1)),
        ('gpBackRetn', dsUint16_t),
        ('gpArchRetn', dsUint16_t),
        ('adsmServerName', c_char * (DSM_MAX_SERVERNAME_LENGTH + 1)),
        ('archiveRetentionProtection', dsmBool_t),
        ('maxBytesPerTxn_64', dsStruct64_t),
        ('lanFreeEnabled', dsmBool_t),
        ('dedupType', dsmDedupType),  # enum
        ('accessNode', c_char * (DSM_MAX_ID_LENGTH + 1)),
        ('failOverCfgType', dsmFailOvrCfgType),  # enum
        ('replServerName', c_char * (DSM_MAX_SERVERNAME_LENGTH + 1)),
        ('homeServerName', c_char * (DSM_MAX_SERVERNAME_LENGTH + 1)),
        ('replServerHost', c_char * (DSM_MAX_SERVERNAME_LENGTH + 1)),
        ('replServerPort', dsInt32_t)
    ]


# noinspection PyPep8Naming
class dsmAppVersion(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('applicationVersion', dsUint16_t),
        ('applicationRelease', dsUint16_t),
        ('applicationLevel', dsUint16_t),
        ('applicationSubLevel', dsUint16_t)
    ]


# noinspection PyPep8Naming
class dsmInitExIn_t(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('apiVersionExP', POINTER(dsmApiVersionEx)),
        ('clientNodeNameP', c_char_p),
        ('clientOwnerNameP', c_char_p),
        ('clientPasswordP', c_char_p),
        ('userNameP', c_char_p),
        ('userPasswordP', c_char_p),
        ('applicationTypeP', c_char_p),
        ('configfile', c_char_p),
        ('options', c_char_p),
        ('dirDelimiter', c_char_p),
        ('useUnicode', c_int),
        ('bCrossPlatform', c_int),
        ('bService', c_int),
        ('bEncryptKeyEnabled', c_int),
        ('useUnicode', c_int),
        ('encryptionPasswordP', c_char_p),
        ('useTsmBuffers', c_int),
        ('numTsmBuffers', dsUint8_t),
        ('appVersionP', dsmAppVersion),
    ]


# noinspection PyPep8Naming
class dsmInitExOut_t(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('userNameAuthorities', dsInt16_t),
        ('infoRC', dsInt16_t),
        ('adsmServerName', c_char * (DSM_MAX_SERVERNAME_LENGTH + 1)),
        ('serverVer', dsUint16_t),
        ('serverRel', dsUint16_t),
        ('serverLev', dsUint16_t),
        ('serverSubLev', dsUint16_t),
        ('bIsFailOverMode', c_int),  # bool
        ('replServerName', c_char * (DSM_MAX_SERVERNAME_LENGTH + 1)),
        ('homeServerName', c_char * (DSM_MAX_SERVERNAME_LENGTH + 1))
    ]


# noinspection PyPep8Naming
class dsmDosFSAttrib(Structure):
    _fields_ = [
        ('driveLetter', c_char),
        ('fsInfoLength', dsUint16_t),
        ('fsInfo', c_char * (DSM_MAX_FSINFO_LENGTH + 1))
    ]


# noinspection PyPep8Naming
class dsmUnixFSAttrib(Structure):
    _fields_ = [
        ('fsInfoLength', dsUint16_t),
        ('fsInfo', c_char * (DSM_MAX_FSINFO_LENGTH + 1))
    ]


dsmNetwareFSAttrib = dsmUnixFSAttrib


# noinspection PyPep8Naming
class dsmFSAttr(Union):
    _fields_ = [
        ('netwareFSAttr', dsmNetwareFSAttrib),
        ('unixFSAttr', dsmUnixFSAttrib),
        ('dsmDosFSAttrib', dsmDosFSAttrib)
    ]


# noinspection PyPep8Naming
class regFSData(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('fsName', c_char_p),
        ('fsType', c_char_p),
        ('occupancy', dsStruct64_t),
        ('capacity', dsStruct64_t),
        ('fsAttr', dsmFSAttr),
    ]


regFSDataVersion = 1


# noinspection PyPep8Naming
class dsmObjName(Structure):
    _fields_ = [
        ('fs', c_char * (DSM_MAX_FSNAME_LENGTH + 1)),
        ('hl', c_char * (DSM_MAX_HL_LENGTH + 1)),
        ('ll', c_char * (DSM_MAX_LL_LENGTH + 1)),
        ('objType', dsUint8_t)
    ]


dsmSendType = c_int  # enum


# noinspection PyPep8Naming
class dsmSendTypeEnum(object):
    stBackup, stArchive, stBackupMountWait, stArchiveMountWait = range(4)


# noinspection PyPep8Naming
class mcBindKey(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('mcName', c_char * (DSM_MAX_MC_NAME_LENGTH + 1)),
        ('backup_cg_exists', dsmBool_t),
        ('archive_cg_exists', dsmBool_t),
        ('backup_copy_dest', c_char * (DSM_MAX_CG_DEST_LENGTH + 1)),
        ('archive_copy_dest', c_char * (DSM_MAX_CG_DEST_LENGTH + 1))
    ]


mcBindKeyVersion = 1


# noinspection PyPep8Naming
class ObjAttr(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('owner', c_char * (DSM_MAX_OWNER_LENGTH + 1)),
        ('sizeEstimate', dsStruct64_t),
        ('objCompressed', dsmBool_t),
        ('objInfoLength', dsUint16_t),
        ('objInfo', c_char_p),
        ('mcNameP', c_char_p),
        ('disableDeduplication', dsmBool_t)
    ]


ObjAttrVersion = 3


# noinspection
#  PyPep8Naming
class DataBlk(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('bufferLen', dsUint32_t),
        ('numBytes', dsUint32_t),
        ('bufferPtr', POINTER(c_char)),  # binary data: https://docs.python.org/2/library/ctypes.html#ctypes.c_char_p
        ('numBytesCompressed', dsUint32_t),
        ('reserved', dsUint16_t)
    ]


DataBlkVersion = 3


# noinspection PyPep8Naming
class sndArchiveData(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('descr', c_char_p)
    ]


sndArchiveDataVersion = 1


# noinspection PyPep8Naming
class dsmEndSendObjExIn_t(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('dsmHandle', dsUint32_t)
    ]


dsmEndSendObjExInVersion = 1


# noinspection PyPep8Naming
class dsmEndSendObjExOut_t(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('totalBytesSent', dsStruct64_t),
        ('objCompressed', dsmBool_t),
        ('totalCompressSize', dsStruct64_t),
        ('totalLFBytesSent', dsStruct64_t),
        ('encryptionType', dsUint8_t),
        ('objDeduplicated', dsmBool_t),
        ('totalDedupSize', dsStruct64_t)
    ]


dsmQueryType = c_int  # enum


# noinspection PyPep8Naming
class dsmQueryTypeEnum(object):
    qtArchive, qtBackup, qtBackupActive, qtFilespace, qtMC = range(5)


# noinspection PyPep8Naming
class qryArchiveData(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('objName', POINTER(dsmObjName)),
        ('owner', c_char_p),
        ('insDateLowerBound', dsmDate),
        ('insDateUpperBound', dsmDate),
        ('expDateLowerBound', dsmDate),
        ('expDateUpperBound', dsmDate),
        ('descr', c_char_p)
    ]


# noinspection PyPep8Naming
class dsUint160_t(Structure):
    _fields_ = [
        ('top', dsUint32_t),
        ('hi_hi', dsUint32_t),
        ('hi_lo', dsUint32_t),
        ('lo_hi', dsUint32_t),
        ('lo_lo', dsUint32_t),
    ]


# noinspection PyPep8Naming
class qryRespArchiveData(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('objName', dsmObjName),
        ('copyGroup', dsUint32_t),
        ('mcName', c_char * (DSM_MAX_MC_NAME_LENGTH + 1)),
        ('owner', c_char * (DSM_MAX_OWNER_LENGTH + 1)),
        ('objId', dsStruct64_t),
        ('reserved', dsStruct64_t),
        ('mediaClass', dsUint8_t),
        ('insDate', dsmDate),
        ('expDate', dsmDate),
        ('descr', c_char * (DSM_MAX_DESCR_LENGTH + 1)),
        ('objInfolen', dsUint16_t),
        ('objInfo', c_char * (DSM_MAX_OBJINFO_LENGTH)),
        ('restoreOrderExt', dsUint160_t),
        ('sizeEstimate', dsStruct64_t),
        ('compressType', dsUint8_t),
        ('retentionInitiated', dsUint8_t),
        ('objHeld', dsUint8_t),
        ('encryptionType', dsUint8_t),
        ('clientDeduplicated', dsmBool_t),
    ]


qryRespArchiveDataVersion = 6
qryArchiveDataVersion = 1
dsmEndSendObjExOutVersion = 3

ObjID = dsStruct64_t


# noinspection PyPep8Naming
class PartialObjData(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('partialObjOffset', dsStruct64_t),
        ('partialObjLength', dsStruct64_t)
    ]


PartialObjDataVersion = 1


# noinspection PyPep8Naming
class dsmGetList(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('numObjId', dsUint32_t),
        ('objId', POINTER(ObjID)),
        ('partialObjData', POINTER(PartialObjData))
    ]


# noinspection PyPep8Naming
class dsmGetTypeEnum(object):
    gtBackup, gtArchive = 0, 1


dsmGetListVersion = 2
dsmGetListPORVersion = 3


# noinspection PyPep8Naming
class dsmDelTypeEnum(object):
    dtArchive, dtBackup, dtBackupID = range(3)


# noinspection PyPep8Naming
class delBack(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('objNameP', POINTER(dsmObjName)),
        ('copyGroup', dsUint32_t)
    ]

delBackVersion = 1


# noinspection PyPep8Naming
class delArch(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('objId', dsStruct64_t)
    ]

delArchVersion = 1


# noinspection PyPep8Naming
class delBackID(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('objId', dsStruct64_t)
    ]

delBackIDVersion = 1


# noinspection PyPep8Naming
class dsmDelInfo(Union):
    _fields_ = [
        ('backInfo', delBack),
        ('archInfo', delArch),
        ('backIDInfo', delBackID)
    ]
