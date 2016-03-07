from __future__ import (absolute_import, unicode_literals)

import ctypes
import logging
import os

from tsm.tsm_definitions import *

__author__ = 'bbrauns'


class TSMApiMethodProxy(object):
    def __init__(self):
        dsmi_config = '/opt/tivoli/tsm/client/ba/bin/dsm.opt'
        logging.info('setting env:DSMI_CONFIG={0}'.format(dsmi_config))
        os.environ['DSMI_CONFIG'] = dsmi_config

        dsmi_dir = '/opt/tivoli/tsm/client/ba/bin'
        os.environ['DSMI_DIR'] = dsmi_dir
        logging.info('setting env:DSMI_DIR={0}'.format(dsmi_dir))

        lib_path = '/opt/tivoli/tsm/client/api/bin64/libApiTSM64.so'
        logging.info('loading tsm api library from: {0}'.format(lib_path))

        lib_api_tsm_64 = ctypes.cdll.LoadLibrary(lib_path)

        self.dsmGetObj = lib_api_tsm_64.dsmGetObj
        self.dsmGetObj.argtypes = [dsUint32_t, POINTER(ObjID), POINTER(DataBlk)]
        self.dsmGetObj.restype = dsInt16_t

        self.dsmGetData = lib_api_tsm_64.dsmGetData
        self.dsmGetData.argtypes = [dsUint32_t, POINTER(DataBlk)]
        self.dsmGetData.restype = dsInt16_t

        self.dsmRCMsg = lib_api_tsm_64.dsmRCMsg
        self.dsmRCMsg.argtypes = [dsUint32_t, dsInt16_t, ctypes.c_char_p]
        self.dsmRCMsg.restype = dsInt16_t

        self.dsmQueryApiVersionEx = lib_api_tsm_64.dsmQueryApiVersionEx
        self.dsmQueryApiVersionEx.argtypes = [POINTER(dsmApiVersionEx)]
        self.dsmQueryApiVersionEx.restype = None

        self.dsmInitEx = lib_api_tsm_64.dsmInitEx
        self.dsmInitEx.argtypes = [POINTER(dsUint32_t), POINTER(dsmInitExIn_t), POINTER(dsmInitExOut_t)]
        self.dsmInitEx.restype = dsInt16_t

        self.dsmQuerySessInfo = lib_api_tsm_64.dsmQuerySessInfo
        self.dsmQuerySessInfo.argtypes = [dsUint32_t, POINTER(ApiSessInfo)]
        self.dsmQuerySessInfo.restype = dsInt16_t

        self.dsmRegisterFS = lib_api_tsm_64.dsmRegisterFS
        self.dsmRegisterFS.argtypes = [dsUint32_t, POINTER(regFSData)]
        self.dsmRegisterFS.restype = dsInt16_t

        self.dsmBeginTxn = lib_api_tsm_64.dsmBeginTxn
        self.dsmBeginTxn.argtypes = [dsUint32_t]
        self.dsmBeginTxn.restype = dsInt16_t

        self.dsmBindMC = lib_api_tsm_64.dsmBindMC
        self.dsmBindMC.argtypes = [dsUint32_t, POINTER(dsmObjName), ctypes.c_int, POINTER(mcBindKey)]
        self.dsmBindMC.restype = dsInt16_t

        self.dsmSendObj = lib_api_tsm_64.dsmSendObj
        #                                                         objName of BindMC
        self.dsmSendObj.argtypes = [dsUint32_t, dsmSendType, ctypes.c_void_p, POINTER(dsmObjName),
                                    POINTER(ObjAttr), POINTER(DataBlk)]
        self.dsmSendObj.restype = dsInt16_t

        self.dsmSendData = lib_api_tsm_64.dsmSendData
        self.dsmSendData.argtypes = [dsUint32_t, POINTER(DataBlk)]
        self.dsmSendData.restype = dsInt16_t

        self.dsmEndSendObjEx = lib_api_tsm_64.dsmEndSendObjEx
        self.dsmEndSendObjEx.argtypes = [POINTER(dsmEndSendObjExIn_t), POINTER(dsmEndSendObjExOut_t)]
        self.dsmEndSendObjEx.restype = dsInt16_t

        self.dsmTerminate = lib_api_tsm_64.dsmTerminate
        self.dsmTerminate.argtypes = [dsUint32_t]
        self.dsmTerminate.restype = dsInt16_t

        self.dsmEndTxn = lib_api_tsm_64.dsmEndTxn
        self.dsmEndTxn.argtypes = [dsUint32_t, dsUint8_t, POINTER(dsUint16_t)]
        self.dsmEndTxn.restype = dsInt16_t

        self.dsmBeginQuery = lib_api_tsm_64.dsmBeginQuery
        #                                                   normal: dsmQueryBuff
        self.dsmBeginQuery.argtypes = [dsUint32_t, dsmQueryType, POINTER(qryArchiveData)]
        self.dsmBeginQuery.restype = dsInt16_t

        self.dsmGetNextQObj = lib_api_tsm_64.dsmGetNextQObj
        self.dsmGetNextQObj.argtypes = [dsUint32_t, POINTER(DataBlk)]
        self.dsmGetNextQObj.restype = dsInt16_t

        self.dsmEndQuery = lib_api_tsm_64.dsmEndQuery
        self.dsmEndQuery.argtypes = [dsUint32_t]
        self.dsmEndQuery.restype = dsInt16_t

        self.dsmBeginGetData = lib_api_tsm_64.dsmBeginGetData
        self.dsmBeginGetData.argtypes = [dsUint32_t, ctypes.c_int, ctypes.c_int, POINTER(dsmGetList)]
        self.dsmBeginGetData.restype = dsInt16_t

        self.dsmGetObj = lib_api_tsm_64.dsmGetObj
        self.dsmGetObj.argtypes = [dsUint32_t, POINTER(ObjID), POINTER(DataBlk)]
        self.dsmGetObj.restype = dsInt16_t

        self.dsmGetData = lib_api_tsm_64.dsmGetData
        self.dsmGetData.argtypes = [dsUint32_t, POINTER(DataBlk)]
        self.dsmGetData.restype = dsInt16_t

        self.dsmEndGetObj = lib_api_tsm_64.dsmEndGetObj
        self.dsmEndGetObj.argtypes = [dsUint32_t]
        self.dsmEndGetObj.restype = dsInt16_t

        self.dsmEndGetData = lib_api_tsm_64.dsmEndGetData
        self.dsmEndGetData.argtypes = [dsUint32_t]
        self.dsmEndGetData.restype = dsInt16_t

        self.dsmDeleteObj = lib_api_tsm_64.dsmDeleteObj
        self.dsmDeleteObj.argtypes = [dsUint32_t, ctypes.c_int, dsmDelInfo]
        self.dsmDeleteObj.restype = dsInt16_t
