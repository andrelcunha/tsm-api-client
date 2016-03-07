from __future__ import (absolute_import, unicode_literals, division)

import collections
import ctypes
import datetime
import logging
import os

from tsm import tsm_helper
from tsm.tsm_definitions import *
from tsm.tsm_helper import convert_size_to_hi_lo, convert_hi_lo_to_size, convert_tsm_structure_to_str
from tsm.tsm_method_proxy import TSMApiMethodProxy
from tsm.tsm_rc_codes import *

__author__ = 'bbrauns'


class TSMError(Exception):
    def __init__(self, msg, rc):
        self.rc = rc
        super(TSMError, self).__init__(msg)


class TSMNotFoundError(TSMError):
    def __init__(self, msg):
        super(TSMNotFoundError, self).__init__(msg, rc=None)


class TSMApiClient(object):
    """
    A TSMApiClient instance is capable to archive and retrieve arbitrary sized files
    in combination with a TSM Server.

    More information:
    http://publib.boulder.ibm.com/tividd/td/TSMC/GC32-0793-02/en_US/HTML/ansa000064.htm
    """

    def __init__(self):
        self.dsm_handle = None
        self.send_buffer_len = 1024 * 1024  # 1 MB
        self.receive_buffer_len = 1024 * 1024  # 1 MB
        self.filespace_type = 'UNIX'
        self.filespace_info = 'test-api'
        self.method_proxy = TSMApiMethodProxy()

    def connect(self):
        if not self.dsm_handle:
            logging.info('establishing connection to tsm server.')
            self._check_api_version()
            self.dsm_handle = self._init_session()
            info = self.query_session_info()
            logging.info('session info:')
            info_str = tsm_helper.convert_tsm_structure_to_str(info)
            logging.info(info_str)
        else:
            logging.info('using session with handle: {0}'.format(self.dsm_handle))

    def close(self):
        if self.dsm_handle:
            logging.info('terminating handle')
            self.method_proxy.dsmTerminate(self.dsm_handle)

    def _raise_err(self, rc):
        if self.dsm_handle:
            msg = ctypes.create_string_buffer(128)
            self.method_proxy.dsmRCMsg(self.dsm_handle, rc, msg)
            raise TSMError(msg.value, rc)
        else:
            raise TSMError('unknown error, rc={0}'.format(rc), rc)

    def _raise_err_on_rc(self, rc):
        if rc != DSM_RC_OK:
            self._raise_err(rc)

    def log_dsm_rc_msg(self):
        def err_check(rc, func, funcargs):
            logging.info('dsm func call: {0}, rc={1}'.format(func.__name__, rc))
            if self.dsm_handle is not None and rc != DSM_RC_OK:
                msg = ctypes.create_string_buffer(128)
                self.method_proxy.dsmRCMsg(self.dsm_handle, rc, msg)
                logging.info('dsm API msg: {0}'.format(msg.value))
            return rc

        return err_check

    @staticmethod
    def _normalize_input(filename, filespace, highlevel, lowlevel):
        if lowlevel is None:
            lowlevel = '/' + os.path.basename(filename)
        if not lowlevel.startswith('/'):
            lowlevel = '/' + lowlevel
        if not highlevel.startswith('/'):
            highlevel = '/' + highlevel
        if not filespace.startswith('/'):
            filespace = '/' + filespace
        return filespace, highlevel, lowlevel

    def archive(self, filename, filespace, highlevel, lowlevel=None):
        """
        Archive a file to TSM.
        :param filename: source file
        :param filespace: TSM filespace
        :param highlevel: TSM highlevel name
        :param lowlevel: TSM lowlevel name
        :return:
        """
        assert filename
        assert os.path.exists(filename)
        assert filespace
        assert highlevel

        fs, hl, ll = self._normalize_input(filename, filespace, highlevel, lowlevel)
        self._register_fs(fs, self.filespace_type, self.filespace_info)
        self._begin_tx()
        logging.info('starting to archive filename={0} to filespace={1}, highlevel={2}, lowlevel={3}'.format(
            filename, fs, hl, ll))
        dsm_obj_name = self._bind_mc(fs, hl, ll)
        self._send_obj(dsm_obj_name, filename)
        self._send_data(filename)
        self._end_send_obj()
        self._end_tx()

    def retrieve(self, dest_file, filespace, highlevel, lowlevel=None):
        """
        Retrieve an archived file.
        :param dest_file: destination file
        :param filespace: TSM filespace
        :param highlevel: TSM highlevel name
        :param lowlevel: TSM lowlevel name. If lowlevel name is None
        the basename of dest_file is used.
        :return:
        """
        assert dest_file
        assert filespace
        assert highlevel

        fs, hl, ll = self._normalize_input(dest_file, filespace, highlevel, lowlevel)
        self._begin_query(fs, hl, ll)
        found_objs = self._get_next_query_obj()
        if len(found_objs) == 1:
            self._end_query()
            self._begin_get_data(found_objs[0].obj_id)
            data_blk, buff = self._get_obj(found_objs[0].obj_id)
            self._get_data(dest_file, data_blk, buff, found_objs[0].size_estimate)
            self._end_get_obj()
            self._end_get_data()
        elif len(found_objs) > 1:
            raise TSMError('{0} objects found, but 1 was expected.'.format(len(found_objs)), rc=None)
        else:
            raise TSMNotFoundError('object can not be found.'
                                   ' filespace:{0}, highlevel:{1}, lowlevel:{2}'.format(fs,
                                                                                        hl,
                                                                                        ll))

    def delete(self, filespace, highlevel, lowlevel=None):
        """
        Delete an archived file.
        :param filespace: TSM filespace
        :param highlevel: TSM highlevel name
        :param lowlevel: TSM lowlevel name. If lowlevel name is None
        all objects under highlevel name are deleted.
        :return:
        """
        assert filespace
        assert highlevel

        if lowlevel is None:
            lowlevel = '/*'
        fs, hl, ll = self._normalize_input(None, filespace, highlevel, lowlevel)
        self._begin_query(fs, hl, ll)
        found_objs = self._get_next_query_obj()
        self._end_query()
        if not found_objs:
            raise TSMNotFoundError('object can not be found.'
                                   ' filespace:{0}, highlevel:{1}, lowlevel:{2}'.format(fs,
                                                                                        hl,
                                                                                        ll))
        assert len(found_objs) < 5, 'sanity check for _delete_obj failed.'
        logging.info('found {0} objects.'.format(len(found_objs)))
        self._begin_tx()
        for obj in found_objs:
            self._delete_obj(obj.obj_id)
        self._end_tx()

    def _delete_obj(self, obj_id):
        assert obj_id

        del_info = dsmDelInfo()
        del_info.archInfo.stVersion = delArchVersion
        del_info.archInfo.objId = obj_id

        logging.info('deleting: objId.lo={0}, objId.hi={1}'.format(obj_id.lo, obj_id.hi))

        self.method_proxy.dsmDeleteObj.errcheck = self.log_dsm_rc_msg()
        rc = self.method_proxy.dsmDeleteObj(self.dsm_handle, dsmDelTypeEnum.dtArchive, del_info)
        self._raise_err_on_rc(rc)

    def _check_api_version(self):
        """
        Check if this application client is compatible with the available api libraries.
        """
        apiversionex = dsmApiVersionEx()
        self.method_proxy.dsmQueryApiVersionEx(ctypes.byref(apiversionex))
        logging.info('API Version: {version}.{release}.{level}.{subLevel}'.format(
            version=apiversionex.version, release=apiversionex.release,
            level=apiversionex.level, subLevel=apiversionex.subLevel))
        applversion = (10000 * DSM_API_VERSION) + \
                      (1000 * DSM_API_RELEASE) + \
                      (100 * DSM_API_LEVEL) + DSM_API_SUBLEVEL
        apiversion = (10000 * apiversionex.version) + \
                     (1000 * apiversionex.release) + \
                     (100 * apiversionex.level) + apiversionex.subLevel

        # check for compatibility problems
        if apiversion < applversion:
            msg = 'The Tivoli Storage Manager API library Version = {0}.{1}.{2}.{3} is at a lower version\n'.format(
                apiversionex.version,
                apiversionex.release,
                apiversionex.level,
                apiversionex.subLevel)
            msg += ' than the application version = {0}.{1}.{2}.{3}\n'.format(
                DSM_API_VERSION,
                DSM_API_RELEASE,
                DSM_API_LEVEL,
                DSM_API_SUBLEVEL)
            msg += 'Please upgrade the API accordingly.'
            raise TSMError(msg, rc=None)

    def _init_session(self):
        """
        Starts an API session using the additional parameters that permit extended verification.
        """
        api_appl_ver = dsmApiVersionEx()
        api_appl_ver.stVersion = apiVersionExVer
        api_appl_ver.version = DSM_API_VERSION
        api_appl_ver.release = DSM_API_RELEASE
        api_appl_ver.level = DSM_API_LEVEL
        api_appl_ver.subLevel = DSM_API_SUBLEVEL
        api_appl_ver_p = ctypes.pointer(api_appl_ver)

        app_ver = dsmAppVersion()
        app_ver.applicationVersion = DSM_API_VERSION
        app_ver.applicationRelease = DSM_API_RELEASE
        app_ver.applicationLevel = DSM_API_LEVEL
        app_ver.applicationSubLevel = DSM_API_SUBLEVEL

        init_in = dsmInitExIn_t()
        init_in.stVersion = dsmInitExInVersion
        init_in.apiVersionExP = api_appl_ver_p
        # Es wird die dsm.sys verwendet, gesetzt durch env variablen DSM_DIR usw.
        # initIn.clientNodeNameP     = ''
        # initIn.clientOwnerNameP    = ''
        # initIn.clientPasswordP     = ''
        init_in.applicationTypeP = self.filespace_type
        # init_in.configfile = ''
        # initIn.options             = ''

        # initIn.userNameP           = 'KOPAL-TEST'
        # initIn.userPasswordP       = ''
        # initIn.dirDelimiter        = '\0'
        # initIn.useUnicode          = dsmFalse
        # initIn.bEncryptKeyEnabled  = dsmFalse
        # initIn.encryptionPasswordP = ''
        # initIn.appVersionP         = appVer

        initout = dsmInitExOut_t()
        initout.stVersion = dsmInitExOutVersion

        local_handle = dsUint32_t()
        self.method_proxy.dsmInitEx.errcheck = self.log_dsm_rc_msg()
        rc = self.method_proxy.dsmInitEx(ctypes.byref(local_handle), ctypes.byref(init_in), ctypes.byref(initout))
        self._raise_err_on_rc(rc)
        logging.info('dsmInitEx')
        logging.info(
            'Connected to server: {server}, ver/rel/lev {ver}/{rel}/{lev}'.format(server=initout.adsmServerName,
                                                                                  ver=initout.serverVer,
                                                                                  rel=initout.serverRel,
                                                                                  lev=initout.serverLev))
        return local_handle

    def query_session_info(self):
        """
        The dsmQuerySessInfo function call starts a query request to Tivoli Storage Manager for information
        related to the operation of the specified session in dsmHandle.
        A structure of type ApiSessInfo is passed in the call,
        with all available session related information entered.
        This call is started after a successful dsmInitEx call.
        """
        dsm_sess_info = ApiSessInfo()
        dsm_sess_info.stVersion = ApiSessInfoVersion
        self.method_proxy.dsmQuerySessInfo.errcheck = self.log_dsm_rc_msg()
        rc = self.method_proxy.dsmQuerySessInfo(self.dsm_handle, ctypes.byref(dsm_sess_info))
        self._raise_err_on_rc(rc)
        return dsm_sess_info

    def _register_fs(self, fs_name, fs_type, fs_info):
        """
        The dsmRegisterFS function call registers a new file space with the Tivoli Storage Manager server.
        Register a file space first before you can back up any data to it.
        :param fs_name: Filespace name to create
        :param fs_type: Filespace type: eg. UNIX
        :param fs_info: Descriptive info data
        """
        assert fs_name
        assert fs_type
        assert fs_info
        dsm_reg_fs_data = regFSData()
        dsm_reg_fs_data.stVersion = regFSDataVersion
        dsm_reg_fs_data.fsName = fs_name  # '/api1'
        dsm_reg_fs_data.fsType = fs_type  # 'smp'
        dsm_reg_fs_data.fsAttr.unixFSAttr.fsInfo = fs_info  # '123'
        dsm_reg_fs_data.fsAttr.unixFSAttr.fsInfoLength = len(dsm_reg_fs_data.fsAttr.unixFSAttr.fsInfo)

        self.method_proxy.dsmRegisterFS.errcheck = self.log_dsm_rc_msg()
        rc = self.method_proxy.dsmRegisterFS(self.dsm_handle, dsm_reg_fs_data)
        if rc == DSM_RC_FS_ALREADY_REGED:
            logging.info('filespace: {0} is already registered'.format(fs_name))
        else:
            self._raise_err_on_rc(rc)

    def _begin_tx(self):
        """
        The dsmBeginTxn function call begins one or more Tivoli Storage Manager transactions
        that begin a complete action; either all the actions succeed or none succeed.
        An action can be either a single call or a series of calls. For example,
        a dsmSendObj call that is followed by a number of dsmSendData calls can be considered a single action.
        Similarly, a dsmSendObj call with a dataBlkPtr that indicates a data area containing the object
        to back up is also considered a single action.
        """
        self.method_proxy.dsmBeginTxn.errcheck = self.log_dsm_rc_msg()
        rc = self.method_proxy.dsmBeginTxn(self.dsm_handle)
        self._raise_err_on_rc(rc)

    def _bind_mc(self, filespace, highlevel, lowlevel):
        """
        The dsmBindMC function call associates, or binds, a management class to the passed object.
        The object is passed through the Include-Exclude list that is pointed to in the options file.
        If a match is not found in the Include list for a specific management class,
        the default management class is assigned.
        The Exclude list can prevent objects from a backup but not from an archive.
        :param filespace: The filespace name associated for this object
        :param highlevel: The highlevel name associated for this object
        :param lowlevel: The lowlevel name associated for this object
        """
        assert filespace
        assert highlevel
        assert lowlevel

        dsm_obj_name = dsmObjName()
        dsm_obj_name.fs = filespace
        dsm_obj_name.hl = highlevel
        dsm_obj_name.ll = lowlevel
        dsm_obj_name.objType = DSM_OBJ_FILE
        mc_bind_key = mcBindKey()
        mc_bind_key.stVersion = mcBindKeyVersion

        self.method_proxy.dsmBindMC.errcheck = self.log_dsm_rc_msg()
        rc = self.method_proxy.dsmBindMC(self.dsm_handle, ctypes.byref(dsm_obj_name), dsmSendTypeEnum.stArchive,
                                         ctypes.byref(mc_bind_key))
        self._raise_err_on_rc(rc)
        return dsm_obj_name

    def _send_obj(self, dsm_obj_name, filename):
        """
        The dsmSendObj function call starts a request to send a single object to storage. +Multiple dsmSendObj calls
        and associated dsmSendData calls can be made within the bounds of a transaction for performance reasons.

        :param dsm_obj_name: Object returned from bind_mc function
        :param filename: The file to be sent
        """
        assert dsm_obj_name
        assert os.path.exists(filename)

        obj_attr = ObjAttr()
        obj_attr.stVersion = ObjAttrVersion

        size = os.path.getsize(filename)
        if size == 0:
            raise TSMError('size of: {0} is 0 bytes.'.format(filename), rc=None)

        hi, lo = convert_size_to_hi_lo(size)
        logging.info('obj size={0} => hi={1}, low={2}'.format(size, hi, lo))
        obj_attr.sizeEstimate.hi = hi
        obj_attr.sizeEstimate.lo = lo
        obj_attr.objCompressed = dsmFalse
        obj_attr.objInfoLength = 17  # todo
        obj_attr.objInfo = 'test-api-objinfo'

        snd_arch_data = sndArchiveData()
        snd_arch_data.stVersion = sndArchiveDataVersion

        data_blk = DataBlk()
        data_blk.stVersion = DataBlkVersion

        self.method_proxy.dsmSendObj.errcheck = self.log_dsm_rc_msg()
        rc = self.method_proxy.dsmSendObj(self.dsm_handle,
                                          dsmSendTypeEnum.stArchive,
                                          ctypes.byref(snd_arch_data),
                                          ctypes.byref(dsm_obj_name),
                                          ctypes.byref(obj_attr),
                                          ctypes.byref(data_blk))
        if rc == DSM_RC_WILL_ABORT:
            self._end_send_obj()
            self._end_tx()
        else:
            self._raise_err_on_rc(rc)

    def _send_data(self, filename):
        """
        The dsmSendData function call sends a byte stream of data to Tivoli Storage Manager through a buffer.
        The application client can pass any type of data for storage on the server.
        Usually, this data is file data, but it is not limited to such.
        You can call dsmSendData several times, if the byte stream of data that you want to send is large.
        :param filename: Path to file being sent.
        
        """
        assert filename
        assert os.path.exists(filename)

        logging.info('using send_buffer_len={0} bytes'.format(self.send_buffer_len))

        size = os.path.getsize(filename)
        if size == 0:
            raise TSMError('size of: {0} is 0 bytes.'.format(filename), rc=None)
        logging.info('size of file={0} is: {1} bytes'.format(filename, size))
        bytes_left = size
        start = datetime.datetime.now()

        data_blk = DataBlk()
        data_blk.stVersion = DataBlkVersion
        buff = ctypes.create_string_buffer(self.send_buffer_len)
        data_blk.bufferPtr = ctypes.cast(buff, ctypes.POINTER(ctypes.c_char))

        done = False
        self.method_proxy.dsmSendData.errcheck = self.log_dsm_rc_msg()
        with open(filename, 'rb') as f:
            while not done:
                if bytes_left < self.send_buffer_len:
                    send_amount = bytes_left
                else:
                    send_amount = self.send_buffer_len

                data_blk.bufferLen = send_amount
                data_blk.numBytes = 0  # changed, when send is done
                data = f.read(send_amount)  # str
                logging.info('read {0} bytes from file'.format(send_amount))
                buff.raw = data
                rc = self.method_proxy.dsmSendData(self.dsm_handle, ctypes.byref(data_blk))
                if rc == DSM_RC_WILL_ABORT:
                    self._end_send_obj()
                    self._end_tx()
                else:
                    self._raise_err_on_rc(rc)

                logging.info('{0} bytes of {1} bytes remaining, {2}%...'.format(
                    bytes_left, size, round((100.0 / float(size)) * (size - bytes_left), 2)))

                if send_amount < self.send_buffer_len:  # todo: raussprung muss geprueft werden
                    done = True
                bytes_left = bytes_left - send_amount
        end = datetime.datetime.now()
        elapsed = end - start
        logging.info('sending took: {0} s'.format(elapsed.total_seconds()))

    def _end_send_obj(self):
        """
        The dsmEndSendObj function call indicates the end of data that is sent to storage.

        Enter the dsmEndSendObj function call to indicate the end of data from the dsmSendObj and dsmSendData calls.
        A protocol violation occurs if this is not performed.
        The exception to this rule is if you call dsmEndTxn to end the transaction.
        Doing this discards all data that was sent for the transaction.
        """
        end_send_obj_ex_out = dsmEndSendObjExOut_t()
        end_send_obj_ex_out.stVersion = dsmEndSendObjExOutVersion

        end_send_obj_ex_in = dsmEndSendObjExIn_t()
        end_send_obj_ex_in.stVersion = dsmEndSendObjExInVersion
        end_send_obj_ex_in.dsmHandle = self.dsm_handle

        self.method_proxy.dsmEndSendObjEx.errcheck = self.log_dsm_rc_msg()
        self.method_proxy.dsmEndSendObjEx(ctypes.byref(end_send_obj_ex_in), ctypes.byref(end_send_obj_ex_out))
        return convert_hi_lo_to_size(hi=end_send_obj_ex_out.totalBytesSent.hi,
                                     lo=end_send_obj_ex_out.totalBytesSent.lo)

    def _end_tx(self, vote=DSM_VOTE_COMMIT):
        """
        The dsmEndTxn function call ends a Tivoli Storage Manager transaction.
        Pair the dsmEndTxn function call with dsmBeginTxn to identify the call or
        set of calls that are considered a transaction.
        The application client can specify on the dsmEndTxn call whether or not
        the transaction should be committed or ended.

        Perform all of the following calls within the bounds of a transaction:

        dsmSendObj
        dsmSendData
        dsmEndSendObj
        dsmDeleteObj
        """
        txn_reason = dsUint16_t(0)
        txn_reason_p = ctypes.pointer(txn_reason)

        self.method_proxy.dsmEndTxn.errcheck = self.log_dsm_rc_msg()
        rc = self.method_proxy.dsmEndTxn(self.dsm_handle, vote, txn_reason_p)
        self._raise_err_on_rc(rc)

    def _begin_query(self, filespace, highlevel, lowlevel):
        """
        The dsmBeginQuery function call starts a query request to the server for information
        about one of the following items:

        Archived data
        Backed-up data
        Active backed-up data
        File spaces
        Management classes.
        :param filespace: The filespace name associated for this object
        :param highlevel: The highlevel name associated for this object
        :param lowlevel: The lowlevel name associated for this object
        """
        assert filespace
        assert highlevel
        assert lowlevel

        obj_name = dsmObjName()
        obj_name.fs = filespace
        obj_name.hl = highlevel
        obj_name.ll = lowlevel
        obj_name.objType = DSM_OBJ_FILE

        archive_data = qryArchiveData()
        archive_data.stVersion = qryArchiveDataVersion
        archive_data.objName = ctypes.pointer(obj_name)
        archive_data.insDateLowerBound.year = DATE_MINUS_INFINITE
        archive_data.insDateUpperBound.year = DATE_PLUS_INFINITE
        archive_data.expDateLowerBound.year = DATE_MINUS_INFINITE
        archive_data.expDateUpperBound.year = DATE_PLUS_INFINITE
        archive_data_p = ctypes.pointer(archive_data)

        logging.info('querying for DSM_OBJ_FILE, DATE_MINUS_INFINITE - DATE_PLUS_INFINITE: fs={0}, hl={1}, '
                     'll={2}...'.format(filespace,
                                        highlevel, lowlevel))

        self.method_proxy.dsmBeginQuery.errcheck = self.log_dsm_rc_msg()
        rc = self.method_proxy.dsmBeginQuery(self.dsm_handle, dsmQueryTypeEnum.qtArchive, archive_data_p)
        self._raise_err_on_rc(rc)

    def _get_next_query_obj(self):
        """
        The dsmGetNextQObj function call gets the next query response from a previous dsmBeginQuery
        call and places it in the caller's buffer.
        The dsmGetNextQObj call is called one or more times.
        Each time it is called, a single query record is retrieved.
        If the application client needs to end the query before retrieving all of the data,
        you can send a dsmEndQuery call.
        :return: Returns namedtuple of type (obj_id, size_estimate)
        """
        query_result_tuple = collections.namedtuple('query_result_tuple', 'obj_id size_estimate')

        resp_archive = qryRespArchiveData()
        resp_archive.stVersion = qryRespArchiveDataVersion

        data_blk = DataBlk()
        data_blk.stVersion = DataBlkVersion
        data_blk.bufferLen = ctypes.sizeof(qryRespArchiveData)

        # pointer
        resp_archive_p = ctypes.pointer(resp_archive)
        data_blk.bufferPtr = ctypes.cast(resp_archive_p, ctypes.POINTER(ctypes.c_char))

        found_objs = []
        done = False

        self.method_proxy.dsmGetNextQObj.errcheck = self.log_dsm_rc_msg()

        logging.info('begin query')
        while not done:
            rc = self.method_proxy.dsmGetNextQObj(self.dsm_handle, ctypes.byref(data_blk))
            if rc == DSM_RC_ABORT_NO_MATCH:
                return None
            if rc != DSM_RC_MORE_DATA and rc != DSM_RC_FINISHED:
                self._raise_err_on_rc(rc)
            if (rc == DSM_RC_MORE_DATA or rc == DSM_RC_FINISHED) and data_blk.numBytes:
                logging.info('# found object:')
                logging.info('objId.lo: ' + str(resp_archive.objId.lo))
                logging.info('objId.hi: ' + str(resp_archive.objId.hi))
                logging.info('objName fs/hl/ll: ' + resp_archive.objName.fs + resp_archive.objName.hl +
                             resp_archive.objName.ll)
                logging.info('mediaClass: ' + str(resp_archive.mediaClass))
                logging.info('sizeEstimate.lo: ' + str(resp_archive.sizeEstimate.lo))
                logging.info('sizeEstimate.hi: ' + str(resp_archive.sizeEstimate.hi))

                obj_id = dsStruct64_t()
                obj_id.hi = resp_archive.objId.hi
                obj_id.lo = resp_archive.objId.lo

                size_estimate = dsStruct64_t()
                size_estimate.hi = resp_archive.sizeEstimate.hi
                size_estimate.lo = resp_archive.sizeEstimate.lo

                result = query_result_tuple(obj_id=obj_id, size_estimate=size_estimate)
                found_objs.append(result)
            if rc == DSM_RC_FINISHED:
                logging.info('end query')
                done = True
        assert len(found_objs) < 10  # sanity check

        return found_objs

    def _end_query(self):
        self.method_proxy.dsmEndQuery.errcheck = self.log_dsm_rc_msg()
        rc = self.method_proxy.dsmEndQuery(self.dsm_handle)
        self._raise_err_on_rc(rc)

    def _begin_get_data(self, obj_id):
        """
        The dsmBeginGetData function call starts a restore or retrieve operation on a list of objects in storage.
        This list of objects is contained in the dsmGetList structure.
        The application creates this list with values from the query that preceded a call to dsmBeginGetData.
        :param obj_id:
        :return:
        """
        assert obj_id

        mount_wait = 1  # wait for mounting device

        get_list = dsmGetList()
        get_list.stVersion = dsmGetListVersion
        get_list.numObjId = dsUint32_t(1)  # number of items
        get_list.objId = ctypes.pointer(obj_id)  # (ObjID *)rest_ibuff;

        self.method_proxy.dsmBeginGetData.errcheck = self.log_dsm_rc_msg()
        rc = self.method_proxy.dsmBeginGetData(self.dsm_handle, mount_wait, dsmGetTypeEnum.gtArchive,
                                               ctypes.byref(get_list))
        self._raise_err_on_rc(rc)

    def _get_obj(self, obj_id):
        """
        The dsmGetObj function call obtains the requested object data from the Tivoli Storage Manager
        data stream and places it in the caller's buffer.
        The dsmGetObj call uses the object ID to obtain the next object or partial object from the data stream.
        :param obj_id:
        :return:
        """
        assert obj_id

        data_blk = DataBlk()
        data_blk.stVersion = DataBlkVersion
        logging.info('using receive_buffer_len={0} bytes'.format(self.receive_buffer_len))
        data_blk.bufferLen = self.receive_buffer_len
        data_blk.numBytes = 0

        buff = ctypes.create_string_buffer(self.receive_buffer_len)
        data_blk.bufferPtr = ctypes.cast(buff, ctypes.POINTER(ctypes.c_char))

        self.method_proxy.dsmGetObj.errcheck = self.log_dsm_rc_msg()
        logging.info('requesting object data. this could take a while...')
        rc = self.method_proxy.dsmGetObj(self.dsm_handle, ctypes.pointer(obj_id), ctypes.byref(data_blk))
        if rc != DSM_RC_MORE_DATA and rc != DSM_RC_FINISHED:
            self._raise_err_on_rc(rc)
        return data_blk, buff

    def _get_data(self, dest_file, data_blk, buff, size_estimate):
        """
        The dsmGetData function call obtains a byte stream of data from Tivoli Storage Manager
        and place it in the caller's buffer. The application client calls dsmGetData when there
        is more data to receive from a previous dsmGetObj or dsmGetData call.
        :param dest_file: file to save data
        :param data_blk: infos about received data
        :param buff: buffer to hold received bytes
        :param size_estimate: estimated size
        :return:
        """
        assert dest_file
        assert data_blk
        assert buff

        size_estimate64 = convert_hi_lo_to_size(size_estimate.hi, size_estimate.lo)
        sum_bytes = 0
        logging.info('saving data from server to file: {0}'.format(dest_file))
        done = False
        rc = DSM_RC_MORE_DATA  # rc from dsmGetObj
        self.method_proxy.dsmGetData.errcheck = self.log_dsm_rc_msg()
        start = datetime.datetime.now()
        with open(dest_file, 'wb') as f:
            while not done:
                if rc != DSM_RC_MORE_DATA and rc != DSM_RC_FINISHED:
                    self._raise_err_on_rc(rc)
                if rc == DSM_RC_MORE_DATA:
                    f.write(buff.raw[:data_blk.numBytes])
                    logging.debug('DSM_RC_MORE_DATA wrote {0} bytes to file'.format(data_blk.numBytes))
                    sum_bytes += data_blk.numBytes

                    # gets new data and sets data_blk.numBytes
                    rc = self.method_proxy.dsmGetData(self.dsm_handle, ctypes.byref(data_blk))

                    logging.info('{0} bytes of {1} bytes received, {2}%...'.format(
                        sum_bytes, size_estimate64, round((float(sum_bytes) / float(size_estimate64)) * 100, 2)))
                if rc == DSM_RC_FINISHED:
                    if data_blk.numBytes:
                        f.write(buff.raw[:data_blk.numBytes])
                        logging.debug('DSM_RC_FINISHED wrote {0} bytes to file'.format(data_blk.numBytes))
                        sum_bytes += data_blk.numBytes
                    logging.info('loop done')
                    done = True
        end = datetime.datetime.now()
        elapsed = end - start
        logging.info('-- wrote {0} bytes'.format(sum_bytes))
        logging.info('receiving took: {0} s'.format(elapsed.total_seconds()))

    def _end_get_obj(self):
        """
        The dsmEndGetObj function call ends a dsmGetObj session that obtains data for a specified object.
        :return:
        """
        self.method_proxy.dsmEndGetObj.errcheck = self.log_dsm_rc_msg()
        rc = self.method_proxy.dsmEndGetObj(self.dsm_handle)
        self._raise_err_on_rc(rc)

    def _end_get_data(self):
        """
        The dsmEndGetData function call ends a dsmBeginGetData session that obtains objects from storage.
        :return:
        """
        self.method_proxy.dsmEndGetData.errcheck = self.log_dsm_rc_msg()
        rc = self.method_proxy.dsmEndGetData(self.dsm_handle)
        self._raise_err_on_rc(rc)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='archive or delete via the tsm api.')
    parser.add_argument('mode', help='archive or retrieve')
    parser.add_argument('file', help='path to src or dest file')
    parser.add_argument('fs', help='filespace')
    parser.add_argument('hl', help='highlevel')
    parser.add_argument('ll', help='lowlevel')
    args = parser.parse_args()

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    tsm_api_client = TSMApiClient()
    try:

        tsm_api_client.connect()
        session_info = tsm_api_client.query_session_info()
        logging.info('session info:')
        session_info_str = convert_tsm_structure_to_str(session_info)
        logging.info(session_info_str)
        if args.mode == 'a' or args.mode == 'archive':
            tsm_api_client.archive(filename=args.file,
                                   filespace=args.fs,
                                   highlevel=args.hl,
                                   lowlevel=args.ll)
        if args.mode == 'r' or args.mode == 'retrieve':
            tsm_api_client.retrieve(dest_file=args.file,
                                    filespace=args.fs,
                                    highlevel=args.hl,
                                    lowlevel=args.ll)
    except Exception as err:
        tsm_api_client.close()
        logging.exception(err.message)
        logging.error(err.message)
    finally:
        tsm_api_client.close()
