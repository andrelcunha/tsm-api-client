from __future__ import (absolute_import, unicode_literals)

__author__ = 'bbrauns'

DSM_RC_SUCCESSFUL = 0  # successful = completion
DSM_RC_OK = 0  # successful = completion

DSM_RC_UNSUCCESSFUL = -1  # unsuccessful = completion

# dsmEndTxn = reason code 
DSM_RS_ABORT_SYSTEM_ERROR = 1
DSM_RS_ABORT_NO_MATCH = 2
DSM_RS_ABORT_BY_CLIENT = 3
DSM_RS_ABORT_ACTIVE_NOT_FOUND = 4
DSM_RS_ABORT_NO_DATA = 5
DSM_RS_ABORT_BAD_VERIFIER = 6
DSM_RS_ABORT_NODE_IN_USE = 7
DSM_RS_ABORT_EXPDATE_TOO_LOW = 8
DSM_RS_ABORT_DATA_OFFLINE = 9
DSM_RS_ABORT_EXCLUDED_BY_SIZE = 10
DSM_RS_ABORT_NO_STO_SPACE_SKIP = 11
DSM_RS_ABORT_NO_REPOSIT_SPACE = DSM_RS_ABORT_NO_STO_SPACE_SKIP
DSM_RS_ABORT_MOUNT_NOT_POSSIBLE = 12
DSM_RS_ABORT_SIZESTIMATE_EXCEED = 13
DSM_RS_ABORT_DATA_UNAVAILABLE = 14
DSM_RS_ABORT_RETRY = 15
DSM_RS_ABORT_NO_LOG_SPACE = 16
DSM_RS_ABORT_NO_DB_SPACE = 17
DSM_RS_ABORT_NO_MEMORY = 18

DSM_RS_ABORT_FS_NOT_DEFINED = 20
DSM_RS_ABORT_NODE_ALREADY_DEFED = 21
DSM_RS_ABORT_NO_DEFAULT_DOMAIN = 22
DSM_RS_ABORT_INVALID_NODENAME = 23
DSM_RS_ABORT_INVALID_POL_BIND = 24
DSM_RS_ABORT_DEST_NOT_DEFINED = 25
DSM_RS_ABORT_WAIT_FOR_SPACE = 26
DSM_RS_ABORT_NOT_AUTHORIZED = 27
DSM_RS_ABORT_RULE_ALREADY_DEFED = 28
DSM_RS_ABORT_NO_STOR_SPACE_STOP = 29

DSM_RS_ABORT_LICENSE_VIOLATION = 30
DSM_RS_ABORT_EXTOBJID_ALREADY_EXISTS = 31
DSM_RS_ABORT_DUPLICATE_OBJECT = 32

DSM_RS_ABORT_INVALID_OFFSET = 33  # Partial = Object Retrieve
DSM_RS_ABORT_INVALID_LENGTH = 34  # Partial = Object Retrieve
DSM_RS_ABORT_STRING_ERROR = 35
DSM_RS_ABORT_NODE_NOT_AUTHORIZED = 36
DSM_RS_ABORT_RESTART_NOT_POSSIBLE = 37
DSM_RS_ABORT_RESTORE_IN_PROGRESS = 38
DSM_RS_ABORT_SYNTAX_ERROR = 39

DSM_RS_ABORT_DATA_SKIPPED = 40
DSM_RS_ABORT_EXCEED_MAX_MP = 41
DSM_RS_ABORT_NO_OBJSET_MATCH = 42
DSM_RS_ABORT_PVR_ERROR = 43
DSM_RS_ABORT_BAD_RECOGTOKEN = 44
DSM_RS_ABORT_MERGE_ERROR = 45
DSM_RS_ABORT_FSRENAME_ERROR = 46
DSM_RS_ABORT_INVALID_OPERATION = 47
DSM_RS_ABORT_STGPOOL_UNDEFINED = 48
DSM_RS_ABORT_INVALID_DATA_FORMAT = 49
DSM_RS_ABORT_DATAMOVER_UNDEFINED = 50

DSM_RS_ABORT_INVALID_MOVER_TYPE = 231
DSM_RS_ABORT_ITEM_IN_USE = 232
DSM_RS_ABORT_LOCK_CONFLICT = 233
DSM_RS_ABORT_SRV_PLUGIN_COMM_ERROR = 234
DSM_RS_ABORT_SRV_PLUGIN_OS_ERROR = 235
DSM_RS_ABORT_CRC_FAILED = 236
DSM_RS_ABORT_INVALID_GROUP_ACTION = 237
DSM_RS_ABORT_DISK_UNDEFINED = 238
DSM_RS_ABORT_BAD_DESTINATION = 239
DSM_RS_ABORT_DATAMOVER_NOT_AVAILABLE = 240
DSM_RS_ABORT_STGPOOL_COPY_CONT_NO = 241
DSM_RS_ABORT_RETRY_SINGLE_TXN = 242
DSM_RS_ABORT_TOC_CREATION_FAIL = 243
DSM_RS_ABORT_TOC_LOAD_FAIL = 244
DSM_RS_ABORT_PATH_RESTRICTED = 245
DSM_RS_ABORT_NO_LANFREE_SCRATCH = 246
DSM_RS_ABORT_INSERT_NOT_ALLOWED = 247
DSM_RS_ABORT_DELETE_NOT_ALLOWED = 248
DSM_RS_ABORT_TXN_LIMIT_EXCEEDED = 249
DSM_RS_ABORT_OBJECT_ALREADY_HELD = 250
DSM_RS_ABORT_INVALID_CHUNK_REFERENCE = 254
DSM_RS_ABORT_DESTINATION_NOT_DEDUP = 255
DSM_RS_ABORT_DESTINATION_POOL_CHANGED = 257
DSM_RS_ABORT_NOT_ROOT = 258


# RETURN = CODE 

DSM_RC_ABORT_SYSTEM_ERROR = DSM_RS_ABORT_SYSTEM_ERROR
DSM_RC_ABORT_NO_MATCH = DSM_RS_ABORT_NO_MATCH
DSM_RC_ABORT_BY_CLIENT = DSM_RS_ABORT_BY_CLIENT
DSM_RC_ABORT_ACTIVE_NOT_FOUND = DSM_RS_ABORT_ACTIVE_NOT_FOUND
DSM_RC_ABORT_NO_DATA = DSM_RS_ABORT_NO_DATA
DSM_RC_ABORT_BAD_VERIFIER = DSM_RS_ABORT_BAD_VERIFIER
DSM_RC_ABORT_NODE_IN_USE = DSM_RS_ABORT_NODE_IN_USE
DSM_RC_ABORT_EXPDATE_TOO_LOW = DSM_RS_ABORT_EXPDATE_TOO_LOW
DSM_RC_ABORT_DATA_OFFLINE = DSM_RS_ABORT_DATA_OFFLINE
DSM_RC_ABORT_EXCLUDED_BY_SIZE = DSM_RS_ABORT_EXCLUDED_BY_SIZE

DSM_RC_ABORT_NO_REPOSIT_SPACE = DSM_RS_ABORT_NO_STO_SPACE_SKIP
DSM_RC_ABORT_NO_STO_SPACE_SKIP = DSM_RS_ABORT_NO_STO_SPACE_SKIP

DSM_RC_ABORT_MOUNT_NOT_POSSIBLE = DSM_RS_ABORT_MOUNT_NOT_POSSIBLE
DSM_RC_ABORT_SIZESTIMATE_EXCEED = DSM_RS_ABORT_SIZESTIMATE_EXCEED
DSM_RC_ABORT_DATA_UNAVAILABLE = DSM_RS_ABORT_DATA_UNAVAILABLE
DSM_RC_ABORT_RETRY = DSM_RS_ABORT_RETRY
DSM_RC_ABORT_NO_LOG_SPACE = DSM_RS_ABORT_NO_LOG_SPACE
DSM_RC_ABORT_NO_DB_SPACE = DSM_RS_ABORT_NO_DB_SPACE
DSM_RC_ABORT_NO_MEMORY = DSM_RS_ABORT_NO_MEMORY

DSM_RC_ABORT_FS_NOT_DEFINED = DSM_RS_ABORT_FS_NOT_DEFINED
DSM_RC_ABORT_NODE_ALREADY_DEFED = DSM_RS_ABORT_NODE_ALREADY_DEFED
DSM_RC_ABORT_NO_DEFAULT_DOMAIN = DSM_RS_ABORT_NO_DEFAULT_DOMAIN
DSM_RC_ABORT_INVALID_NODENAME = DSM_RS_ABORT_INVALID_NODENAME
DSM_RC_ABORT_INVALID_POL_BIND = DSM_RS_ABORT_INVALID_POL_BIND
DSM_RC_ABORT_DEST_NOT_DEFINED = DSM_RS_ABORT_DEST_NOT_DEFINED
DSM_RC_ABORT_WAIT_FOR_SPACE = DSM_RS_ABORT_WAIT_FOR_SPACE
DSM_RC_ABORT_NOT_AUTHORIZED = DSM_RS_ABORT_NOT_AUTHORIZED
DSM_RC_ABORT_RULE_ALREADY_DEFED = DSM_RS_ABORT_RULE_ALREADY_DEFED
DSM_RC_ABORT_NO_STOR_SPACE_STOP = DSM_RS_ABORT_NO_STOR_SPACE_STOP

DSM_RC_ABORT_LICENSE_VIOLATION = DSM_RS_ABORT_LICENSE_VIOLATION
DSM_RC_ABORT_EXTOBJID_ALREADY_EXISTS = DSM_RS_ABORT_EXTOBJID_ALREADY_EXISTS
DSM_RC_ABORT_DUPLICATE_OBJECT = DSM_RS_ABORT_DUPLICATE_OBJECT

DSM_RC_ABORT_INVALID_OFFSET = DSM_RS_ABORT_INVALID_OFFSET
DSM_RC_ABORT_INVALID_LENGTH = DSM_RS_ABORT_INVALID_LENGTH

DSM_RC_ABORT_STRING_ERROR = DSM_RS_ABORT_STRING_ERROR
DSM_RC_ABORT_NODE_NOT_AUTHORIZED = DSM_RS_ABORT_NODE_NOT_AUTHORIZED
DSM_RC_ABORT_RESTART_NOT_POSSIBLE = DSM_RS_ABORT_RESTART_NOT_POSSIBLE
DSM_RC_ABORT_RESTORE_IN_PROGRESS = DSM_RS_ABORT_RESTORE_IN_PROGRESS
DSM_RC_ABORT_SYNTAX_ERROR = DSM_RS_ABORT_SYNTAX_ERROR

DSM_RC_ABORT_DATA_SKIPPED = DSM_RS_ABORT_DATA_SKIPPED
DSM_RC_ABORT_EXCEED_MAX_MP = DSM_RS_ABORT_EXCEED_MAX_MP
DSM_RC_ABORT_NO_OBJSET_MATCH = DSM_RS_ABORT_NO_OBJSET_MATCH
DSM_RC_ABORT_PVR_ERROR = DSM_RS_ABORT_PVR_ERROR
DSM_RC_ABORT_BAD_RECOGTOKEN = DSM_RS_ABORT_BAD_RECOGTOKEN
DSM_RC_ABORT_MERGE_ERROR = DSM_RS_ABORT_MERGE_ERROR
DSM_RC_ABORT_FSRENAME_ERROR = DSM_RS_ABORT_FSRENAME_ERROR
DSM_RC_ABORT_INVALID_OPERATION = DSM_RS_ABORT_INVALID_OPERATION
DSM_RC_ABORT_STGPOOL_UNDEFINED = DSM_RS_ABORT_STGPOOL_UNDEFINED
DSM_RC_ABORT_INVALID_DATA_FORMAT = DSM_RS_ABORT_INVALID_DATA_FORMAT
DSM_RC_ABORT_DATAMOVER_UNDEFINED = DSM_RS_ABORT_DATAMOVER_UNDEFINED

DSM_RC_ABORT_INVALID_MOVER_TYPE = DSM_RS_ABORT_INVALID_MOVER_TYPE
DSM_RC_ABORT_ITEM_IN_USE = DSM_RS_ABORT_ITEM_IN_USE
DSM_RC_ABORT_LOCK_CONFLICT = DSM_RS_ABORT_LOCK_CONFLICT
DSM_RC_ABORT_SRV_PLUGIN_COMM_ERROR = DSM_RS_ABORT_SRV_PLUGIN_COMM_ERROR
DSM_RC_ABORT_SRV_PLUGIN_OS_ERROR = DSM_RS_ABORT_SRV_PLUGIN_OS_ERROR
DSM_RC_ABORT_CRC_FAILED = DSM_RS_ABORT_CRC_FAILED
DSM_RC_ABORT_INVALID_GROUP_ACTION = DSM_RS_ABORT_INVALID_GROUP_ACTION
DSM_RC_ABORT_DISK_UNDEFINED = DSM_RS_ABORT_DISK_UNDEFINED
DSM_RC_ABORT_BAD_DESTINATION = DSM_RS_ABORT_BAD_DESTINATION
DSM_RC_ABORT_DATAMOVER_NOT_AVAILABLE = DSM_RS_ABORT_DATAMOVER_NOT_AVAILABLE
DSM_RC_ABORT_STGPOOL_COPY_CONT_NO = DSM_RS_ABORT_STGPOOL_COPY_CONT_NO
DSM_RC_ABORT_RETRY_SINGLE_TXN = DSM_RS_ABORT_RETRY_SINGLE_TXN
DSM_RC_ABORT_TOC_CREATION_FAIL = DSM_RS_ABORT_TOC_CREATION_FAIL
DSM_RC_ABORT_TOC_LOAD_FAIL = DSM_RS_ABORT_TOC_LOAD_FAIL
DSM_RC_ABORT_PATH_RESTRICTED = DSM_RS_ABORT_PATH_RESTRICTED
DSM_RC_ABORT_NO_LANFREE_SCRATCH = DSM_RS_ABORT_NO_LANFREE_SCRATCH
DSM_RC_ABORT_INSERT_NOT_ALLOWED = DSM_RS_ABORT_INSERT_NOT_ALLOWED
DSM_RC_ABORT_DELETE_NOT_ALLOWED = DSM_RS_ABORT_DELETE_NOT_ALLOWED
DSM_RC_ABORT_TXN_LIMIT_EXCEEDED = DSM_RS_ABORT_TXN_LIMIT_EXCEEDED
DSM_RC_ABORT_OBJECT_ALREADY_HELD = DSM_RS_ABORT_OBJECT_ALREADY_HELD
DSM_RC_ABORT_INVALID_CHUNK_REFERENCE = DSM_RS_ABORT_INVALID_CHUNK_REFERENCE
DSM_RC_ABORT_DESTINATION_NOT_DEDUP = DSM_RS_ABORT_DESTINATION_NOT_DEDUP
DSM_RC_ABORT_DESTINATION_POOL_CHANGED = DSM_RS_ABORT_DESTINATION_POOL_CHANGED
DSM_RC_ABORT_NOT_ROOT = DSM_RS_ABORT_NOT_ROOT


# Definitions = for server = signon reject = codes                          
# These = error codes = are in = the range (51 to = 99) inclusive.            
DSM_RC_REJECT_NO_RESOURCES = 51
DSM_RC_REJECT_VERIFIER_EXPIRED = 52
DSM_RC_REJECT_ID_UNKNOWN = 53
DSM_RC_REJECT_DUPLICATE_ID = 54
DSM_RC_REJECT_SERVER_DISABLED = 55
DSM_RC_REJECT_CLOSED_REGISTER = 56
DSM_RC_REJECT_CLIENT_DOWNLEVEL = 57
DSM_RC_REJECT_SERVER_DOWNLEVEL = 58
DSM_RC_REJECT_ID_IN_USE = 59
DSM_RC_REJECT_ID_LOCKED = 61
DSM_RC_SIGNONREJECT_LICENSE_MAX = 62
DSM_RC_REJECT_NO_MEMORY = 63
DSM_RC_REJECT_NO_DB_SPACE = 64
DSM_RC_REJECT_NO_LOG_SPACE = 65
DSM_RC_REJECT_INTERNAL_ERROR = 66
DSM_RC_SIGNONREJECT_INVALID_CLI = 67  # client = type not = licensed
DSM_RC_CLIENT_NOT_ARCHRETPROT = 68
DSM_RC_REJECT_LASTSESS_CANCELED = 69
DSM_RC_REJECT_UNICODE_NOT_ALLOWED = 70
DSM_RC_REJECT_NOT_AUTHORIZED = 71
DSM_RC_REJECT_TOKEN_TIMEOUT = 72
DSM_RC_REJECT_INVALID_NODE_TYPE = 73
DSM_RC_REJECT_INVALID_SESSIONINIT = 74
DSM_RC_REJECT_WRONG_PORT = 75
DSM_RC_CLIENT_NOT_SPMRETPROT = 79

DSM_RC_USER_ABORT = 101  # processing = aborted by = user
DSM_RC_NO_MEMORY = 102  # no = RAM left = to complete = request
DSM_RC_TA_COMM_DOWN = 2021  # no = longer used
DSM_RC_FILE_NOT_FOUND = 104  # specified = file not = found
DSM_RC_PATH_NOT_FOUND = 105  # specified = path doesn't = exist
DSM_RC_ACCESS_DENIED = 106  # denied = due to = improper permission
DSM_RC_NO_HANDLES = 107  # no = more file = handles available
DSM_RC_FILE_EXISTS = 108  # file = already exists
DSM_RC_INVALID_PARM = 109  # invalid = parameter passed. CRITICAL
DSM_RC_INVALID_HANDLE = 110  # invalid = file handle = passed
DSM_RC_DISK_FULL = 111  # out = of disk = space
DSM_RC_PROTOCOL_VIOLATION = 113  # call = protocol violation. CRITICAL
DSM_RC_UNKNOWN_ERROR = 114  # unknown = system error. CRITICAL
DSM_RC_UNEXPECTED_ERROR = 115  # unexpected = error. CRITICAL
DSM_RC_FILE_BEING_EXECUTED = 116  # No = write is = allowed
DSM_RC_DIR_NO_SPACE = 117  # directory = can't = be expanded
DSM_RC_LOOPED_SYM_LINK = 118  # too = many symbolic = links were
# encountered = in translating = path.
DSM_RC_FILE_NAME_TOO_LONG = 119  # file = name too = long
DSM_RC_FILE_SPACE_LOCKED = 120  # filespace = is locked = by the = system
DSM_RC_FINISHED = 121  # finished = processing
DSM_RC_UNKNOWN_FORMAT = 122  # unknown = format
DSM_RC_NO_AUTHORIZATION = 123  # server = response when = the client = has
# no = authorization to = read another
# host's = owner backup/archive = data
DSM_RC_FILE_SPACE_NOT_FOUND = 124  # specified = file space = not found
DSM_RC_TXN_ABORTED = 125  # transaction = aborted
DSM_RC_SUBDIR_AS_FILE = 126  # Subdirectory = name exists = as file
DSM_RC_PROCESS_NO_SPACE = 127  # process = has no = more disk = space.
DSM_RC_PATH_TOO_LONG = 128  # a = directory path = being build = became
# too = long
DSM_RC_NOT_COMPRESSED = 129  # file = thought to = be compressed = is
# actually = not
DSM_RC_TOO_MANY_BITS = 130  # file = was compressed = using more = bits
# then = the expander = can handle
DSM_RC_SYSTEM_ERROR = 131  # internal = system error
DSM_RC_NO_SERVER_RESOURCES = 132  # server = out of = resources.
DSM_RC_FS_NOT_KNOWN = 133  # the = file space = is not = known by = the
# server
DSM_RC_NO_LEADING_DIRSEP = 134  # no = leading directory = separator
DSM_RC_WILDCARD_DIR = 135  # wildcard = character in = directory
# path = when not = allowed
DSM_RC_COMM_PROTOCOL_ERROR = 136  # communications = protocol error
DSM_RC_AUTH_FAILURE = 137  # authentication = failure
DSM_RC_TA_NOT_VALID = 138  # TA = not a = root and/or = SUID program
DSM_RC_KILLED = 139  # process = killed.

DSM_RC_RETRY = 143  # retry = same operation = again

DSM_RC_WOULD_BLOCK = 145  # operation = would cause = the system = to
# block = waiting for = input.
DSM_RC_TOO_SMALL = 146  # area = for compiled = pattern small
DSM_RC_UNCLOSED = 147  # no = closing bracket = in pattern
DSM_RC_NO_STARTING_DELIMITER = 148  # pattern = has to = start with
# directory = delimiter
DSM_RC_NEEDED_DIR_DELIMITER = 149  # a = directory delimiter = is needed
# immediately = before and = after the
# "match = directories" metastring
# ("...") and = one wasn't = found
DSM_RC_UNKNOWN_FILE_DATA_TYPE = 150  # structured = file data = type is
# unknown
DSM_RC_BUFFER_OVERFLOW = 151  # data = buffer overflow

DSM_RC_NO_COMPRESS_MEMORY = 154  # Compress/Expand = out of = memory
DSM_RC_COMPRESS_GREW = 155  # Compression = grew
DSM_RC_INV_COMM_METHOD = 156  # Invalid = comm method = specified
DSM_RC_WILL_ABORT = 157  # Transaction = will be = aborted
DSM_RC_FS_WRITE_LOCKED = 158  # File = space is = write locked
DSM_RC_SKIPPED_BY_USER = 159  # User = wanted file = skipped in = the
# case = of ABORT_DATA_OFFLINE
DSM_RC_TA_NOT_FOUND = 160  # TA = not found = in it's = directory
DSM_RC_TA_ACCESS_DENIED = 161  # Access = to TA = is denied
DSM_RC_FS_NOT_READY = 162  # File = space not = ready
DSM_RC_FS_IS_BAD = 163  # File = space is = bad
DSM_RC_FIO_ERROR = 164  # File = input/output = error
DSM_RC_WRITE_FAILURE = 165  # Error = writing to = file
DSM_RC_OVER_FILE_SIZE_LIMIT = 166  # File = over system/user = limit
DSM_RC_CANNOT_MAKE = 167  # Could = not create = file/directory,
# could = be a = bad name
DSM_RC_NO_PASS_FILE = 168  # password = file needed = and user = is
# not = root
DSM_RC_VERFILE_OLD = 169  # password = stored locally = doesn't
# match = the one = at the = host
DSM_RC_INPUT_ERROR = 173  # unable = to read = keyboard input
DSM_RC_REJECT_PLATFORM_MISMATCH = 174  # Platform = name doesn't = match
# up = with what = the server = says
# is = the platform = for the = client
DSM_RC_TL_NOT_FILE_OWNER = 175  # User = trying to = backup a = file is = not
# the = file's = owner.
DSM_RC_COMPRESSED_DATA_CORRUPTED = 176  # Compressed = data is = corrupted
DSM_RC_UNMATCHED_QUOTE = 177  # missing = starting or = ending quote

DSM_RC_SIGNON_FAILOVER_MODE = 178  # Failed = over to = the replication = server,
# running = in failover = mode
DSM_RC_FAILOVER_MODE_FUNC_BLOCKED = 179  # function = is blocked = because
# session = is in = failover mode

# ---------------------------------------------------------------------------
# Return = codes = 180-199 are = reserved for = Policy Set = handling                 
# ---------------------------------------------------------------------------
DSM_RC_PS_MULTBCG = 181  # Multiple = backup copy = groups in = 1 MC
DSM_RC_PS_MULTACG = 182  # Multiple = arch.  copy = groups in = 1 MC
DSM_RC_PS_NODFLTMC = 183  # Default = MC name = not in = policy set
DSM_RC_TL_NOBCG = 184  # Backup = req, no = backup copy = group
DSM_RC_TL_EXCLUDED = 185  # Backup = req, excl. by = in/ex = filter
DSM_RC_TL_NOACG = 186  # Archive = req, no = archive copy = group
DSM_RC_PS_INVALID_ARCHMC = 187  # Invalid = MC name = in archive = override
DSM_RC_NO_PS_DATA = 188  # No = policy set = data on = the server
DSM_RC_PS_INVALID_DIRMC = 189  # Invalid = directory MC = specified in
# the = options file.
DSM_RC_PS_NO_CG_IN_DIR_MC = 190  # No = backup copy = group in = directory MC.
# Must = specify an = MC using = DirMC
# option.

DSM_RC_WIN32_UNSUPPORTED_FILE_TYPE = 280  # File = is not = of
# Win32 type = FILE_TYPE_DISK

# ---------------------------------------------------------------------------
# Return = codes for = the Trusted = Communication Agent                          
# ---------------------------------------------------------------------------
DSM_RC_TCA_NOT_ROOT = 161  # Access = to TA = is denied
DSM_RC_TCA_ATTACH_SHR_MEM_ERR = 200  # Error = attaching shared = memory
DSM_RC_TCA_SHR_MEM_BLOCK_ERR = 200  # Shared = memory block = error
DSM_RC_TCA_SHR_MEM_IN_USE = 200  # Shared = memory block = error
DSM_RC_TCA_SHARED_MEMORY_ERROR = 200  # Shared = memory block = error
DSM_RC_TCA_SEGMENT_MISMATCH = 200  # Shared = memory block = error
DSM_RC_TCA_FORK_FAILED = 292  # Error = forking off = TCA process
DSM_RC_TCA_DIED = 294  # TCA = died unexpectedly
DSM_RC_TCA_INVALID_REQUEST = 295  # Invalid = request sent = to TCA
DSM_RC_TCA_SEMGET_ERROR = 297  # Error = getting semaphores
DSM_RC_TCA_SEM_OP_ERROR = 298  # Error = in semaphore = set or = wait
DSM_RC_TCA_NOT_ALLOWED = 299  # TCA = not allowed (multi = thread)

# ---------------------------------------------------------------------------
# 400-430  for = options                                                      
# ---------------------------------------------------------------------------
DSM_RC_INVALID_OPT = 400  # invalid = option
DSM_RC_NO_HOST_ADDR = 405  # Not = enuf info = to connect = server
DSM_RC_NO_OPT_FILE = 406  # No = default user = configuration file
DSM_RC_MACHINE_SAME = 408  # -MACHINENAME = same as = real name
DSM_RC_INVALID_SERVER = 409  # Invalid = server name = from client
DSM_RC_INVALID_KEYWORD = 410  # Invalid = option keyword
DSM_RC_PATTERN_TOO_COMPLEX = 411  # Can't = match Include/Exclude = entry
DSM_RC_NO_CLOSING_BRACKET = 412  # Missing = closing bracket = inc/excl
DSM_RC_OPT_CLIENT_NOT_ACCEPTING = 417  # Client = doesn't = accept this = option from = the server
DSM_RC_OPT_CLIENT_DOES_NOT_WANT = 418  # Client = doesn't = want this = value from = the server
DSM_RC_OPT_NO_INCLEXCL_FILE = 419  # inclexcl = file not = found
DSM_RC_OPT_OPEN_FAILURE = 420  # can't = open file
DSM_RC_OPT_INV_NODENAME = 421  # used = for Windows = if nodename=local machine = when CLUSTERNODE=YES
DSM_RC_OPT_NODENAME_INVALID = 423  # generic = invalid nodename
DSM_RC_OPT_ERRORLOG_CONFLICT = 424  # both = logmax & retention = specified
DSM_RC_OPT_SCHEDLOG_CONFLICT = 425  # both = logmax & retention = specified
DSM_RC_CANNOT_OPEN_TRACEFILE = 426  # cannot = open trace = file
DSM_RC_CANNOT_OPEN_LOGFILE = 427  # cannot = open error = log file
DSM_RC_OPT_SESSINIT_LF_CONFLICT = 428  # both = sessioninit=server = and  enablelanfree=yes = are specified
DSM_RC_OPT_OPTION_IGNORE = 429  # option = will be = ignored
DSM_RC_OPT_DEDUP_CONFLICT = 430  # cannot = open error = log file
DSM_RC_OPT_HSMLOG_CONFLICT = 431  # both = logmax & retention = specified


# ---------------------------------------------------------------------------
# 600 to = 610 for = volume label = codes                                         
# ---------------------------------------------------------------------------
DSM_RC_DUP_LABEL = 600  # duplicate = volume label = found
DSM_RC_NO_LABEL = 601  # drive = has no = label

# ---------------------------------------------------------------------------
# Return = codes for = message file = processing                                  
# ---------------------------------------------------------------------------
DSM_RC_NLS_CANT_OPEN_TXT = 610  # error = trying to = open msg = txt file
DSM_RC_NLS_CANT_READ_HDR = 611  # error = trying to = read header
DSM_RC_NLS_INVALID_CNTL_REC = 612  # invalid = control record
DSM_RC_NLS_INVALID_DATE_FMT = 613  # invalid = default date = format
DSM_RC_NLS_INVALID_TIME_FMT = 614  # invalid = default time = format
DSM_RC_NLS_INVALID_NUM_FMT = 615  # invalid = default number = format

# ---------------------------------------------------------------------------
# Return = codes = 620-630 are = reserved for = log message = return codes            
# ---------------------------------------------------------------------------
DSM_RC_LOG_CANT_BE_OPENED = 620  # error = trying to = open error = log
DSM_RC_LOG_ERROR_WRITING_TO_LOG = 621  # error = occurred writing = to log = file
DSM_RC_LOG_NOT_SPECIFIED = 622  # no = error log = file was = specified


# ---------------------------------------------------------------------------
# Return = codes = 900-999 TSM = CLIENT ONLY                                      
# ---------------------------------------------------------------------------
DSM_RC_NOT_ADSM_AUTHORIZED = 927  # Must = be ADSM = authorized to = perform
# action : root = user or = pwd auth
DSM_RC_REJECT_USERID_UNKNOWN = 940  # userid = unknown on = server
DSM_RC_FILE_IS_SYMLINK = 959  # errorlog = or trace = is a = symbolic link
#

DSM_RC_DIRECT_STORAGE_AGENT_UNSUPPORTED = 961  # Direct = connection to = SA not = supported
DSM_RC_FS_NAMESPACE_DOWNLEVEL = 963  # Long = namespace has = been removed = from from = the Netware = volume
DSM_RC_CONTINUE_NEW_CONSUMER = 972  # Continue = processing using = a new = consumer
DSM_RC_CONTINUE_NEW_CONSUMER_NODEDUP = 973  # Continue = processing using = a new = consumer no = dedup

DSM_RC_SERVER_SUPPORTS_FUNC = 994  # the = server supports = this function
DSM_RC_SERVER_AND_SA_SUPPORT_FUNC = 995  # Both = server and = SA support = func
DSM_RC_SERVER_DOWNLEVEL_FUNC = 996  # The = server is = downlevel for = func
DSM_RC_STORAGEAGENT_DOWNLEVEL = 997  # the = storage agent = is downlevel
DSM_RC_SERVER_AND_SA_DOWNLEVEL = 998  # both = server and = SA downlevel


# TCP/IP = error codes 
DSM_RC_TCPIP_FAILURE = -50  # TCP/IP = communications failure
DSM_RC_CONN_TIMEDOUT = -51  # TCP/IP = connection attempt = timedout
DSM_RC_CONN_REFUSED = -52  # TCP/IP = connection refused = by host
DSM_RC_BAD_HOST_NAME = -53  # TCP/IP = invalid host = name specified
DSM_RC_NETWORK_UNREACHABLE = -54  # TCP/IP = host name = unreachable
DSM_RC_WINSOCK_MISSING = -55  # TCP/IP = WINSOCK.DLL = missing
DSM_RC_TCPIP_DLL_LOADFAILURE = -56  # Error = from LoadLibrary
DSM_RC_TCPIP_LOADFAILURE = -57  # Error = from GetProcAddress
DSM_RC_TCPIP_USER_ABORT = -58  # User = aborted while = in TCP/IP = layer

# ---------------------------------------------------------------------------
# Return = codes (-71)-(-90) are = reserved for = CommTSM error = codes             
# ---------------------------------------------------------------------------
DSM_RC_TSM_FAILURE = -71  # TSM = communications failure
DSM_RC_TSM_ABORT = -72  # Session = aborted abnormally

# comm3270 error = codes - no = longer used
DSM_RC_COMM_TIMEOUT = 2021  # no = longer used
DSM_RC_EMULATOR_INACTIVE = 2021  # no = longer used
DSM_RC_BAD_HOST_ID = 2021  # no = longer used
DSM_RC_HOST_SESS_BUSY = 2021  # no = longer used
DSM_RC_3270_CONNECT_FAILURE = 2021  # no = longer used
DSM_RC_NO_ACS3ELKE_DLL = 2021  # no = longer used
DSM_RC_EMULATOR_ERROR = 2021  # no = longer used
DSM_RC_EMULATOR_BACKLEVEL = 2021  # no = longer used
DSM_RC_CKSUM_FAILURE = 2021  # no = longer used
#

# The = following Return = codes are = for EHLLAPI = for Windows                    
DSM_RC_3270COMMError_DLL = 2021  # no = longer used
DSM_RC_3270COMMError_GetProc = 2021  # no = longer used
DSM_RC_EHLLAPIError_DLL = 2021  # no = longer used
DSM_RC_EHLLAPIError_GetProc = 2021  # no = longer used
DSM_RC_EHLLAPIError_HostConnect = 2021  # no = longer used
DSM_RC_EHLLAPIError_AllocBuff = 2021  # no = longer used
DSM_RC_EHLLAPIError_SendKey = 2021  # no = longer used
DSM_RC_EHLLAPIError_PacketChk = 2021  # no = longer used
DSM_RC_EHLLAPIError_ChkSum = 2021  # no = longer used
DSM_RC_EHLLAPIError_HostTimeOut = 2021  # no = longer used
DSM_RC_EHLLAPIError_Send = 2021  # no = longer used
DSM_RC_EHLLAPIError_Recv = 2021  # no = longer used
DSM_RC_EHLLAPIError_General = 2021  # no = longer used
DSM_RC_PC3270_MISSING_DLL = 2021  # no = longer used
DSM_RC_3270COMM_MISSING_DLL = 2021  # no = longer used


# NETBIOS = error codes 
DSM_RC_NETB_ERROR = -151  # Could = not add = node to = LAN
DSM_RC_NETB_NO_DLL = -152  # The = ACSNETB.DLL = could not = be loaded
DSM_RC_NETB_LAN_ERR = -155  # LAN = error detected
DSM_RC_NETB_NAME_ERR = -158  # Netbios = error on = Add Name
DSM_RC_NETB_TIMEOUT = -159  # Netbios = send timeout
DSM_RC_NETB_NOTINST = -160  # Netbios = not installed - DOS
DSM_RC_NETB_REBOOT = -161  # Netbios = config err - reboot = DOS

# Named = Pipe error = codes 
DSM_RC_NP_ERROR = -190

# CPIC = error codes 
DSM_RC_CPIC_ALLOCATE_FAILURE = 2021  # no = longer used
DSM_RC_CPIC_TYPE_MISMATCH = 2021  # no = longer used
DSM_RC_CPIC_PIP_NOT_SPECIFY_ERR = 2021  # no = longer used
DSM_RC_CPIC_SECURITY_NOT_VALID = 2021  # no = longer used
DSM_RC_CPIC_SYNC_LVL_NO_SUPPORT = 2021  # no = longer used
DSM_RC_CPIC_TPN_NOT_RECOGNIZED = 2021  # no = longer used
DSM_RC_CPIC_TP_ERROR = 2021  # no = longer used
DSM_RC_CPIC_PARAMETER_ERROR = 2021  # no = longer used
DSM_RC_CPIC_PROD_SPECIFIC_ERR = 2021  # no = longer used
DSM_RC_CPIC_PROGRAM_ERROR = 2021  # no = longer used
DSM_RC_CPIC_RESOURCE_ERROR = 2021  # no = longer used
DSM_RC_CPIC_DEALLOCATE_ERROR = 2021  # no = longer used
DSM_RC_CPIC_SVC_ERROR = 2021  # no = longer used
DSM_RC_CPIC_PROGRAM_STATE_CHECK = 2021  # no = longer used
DSM_RC_CPIC_PROGRAM_PARAM_CHECK = 2021  # no = longer used
DSM_RC_CPIC_UNSUCCESSFUL = 2021  # no = longer used
DSM_RC_UNKNOWN_CPIC_PROBLEM = 2021  # no = longer used
DSM_RC_CPIC_MISSING_LU = 2021  # no = longer used
DSM_RC_CPIC_MISSING_TP = 2021  # no = longer used
DSM_RC_CPIC_SNA6000_LOAD_FAIL = 2021  # no = longer used
DSM_RC_CPIC_STARTUP_FAILURE = 2021  # no = longer used

# ---------------------------------------------------------------------------
# Return = codes -300 to -307 are = reserved for = IPX/SPX = communications         
# ---------------------------------------------------------------------------
DSM_RC_TLI_ERROR = 2021  # no = longer used
DSM_RC_IPXSPX_FAILURE = 2021  # no = longer used
DSM_RC_TLI_DLL_MISSING = 2021  # no = longer used
DSM_RC_DLL_LOADFAILURE = 2021  # no = longer used
DSM_RC_DLL_FUNCTION_LOADFAILURE = 2021  # no = longer used
DSM_RC_IPXCONN_REFUSED = 2021  # no = longer used
DSM_RC_IPXCONN_TIMEDOUT = 2021  # no = longer used
DSM_RC_IPXADDR_UNREACHABLE = 2021  # no = longer used
DSM_RC_CPIC_MISSING_DLL = 2021  # no = longer used
DSM_RC_CPIC_DLL_LOADFAILURE = 2021  # no = longer used
DSM_RC_CPIC_FUNC_LOADFAILURE = 2021  # no = longer used

# === Shared = Memory Protocol = error codes   ===
DSM_RC_SHM_TCPIP_FAILURE = -450
DSM_RC_SHM_FAILURE = -451
DSM_RC_SHM_NOTAUTH = -452

DSM_RC_NULL_OBJNAME = 2000  # Object = name pointer = is NULL
DSM_RC_NULL_DATABLKPTR = 2001  # dataBlkPtr = is NULL
DSM_RC_NULL_MSG = 2002  # msg = parm in = dsmRCMsg is = NULL

DSM_RC_NULL_OBJATTRPTR = 2004  # Object = Attr Pointer = is NULL

DSM_RC_NO_SESS_BLK = 2006  # no = server session = info
DSM_RC_NO_POLICY_BLK = 2007  # no = policy hdr = info
DSM_RC_ZERO_BUFLEN = 2008  # bufferLen = is zero = for dataBlkPtr
DSM_RC_NULL_BUFPTR = 2009  # bufferPtr = is NULL = for dataBlkPtr

DSM_RC_INVALID_OBJTYPE = 2010  # invalid = object type
DSM_RC_INVALID_VOTE = 2011  # invalid = vote
DSM_RC_INVALID_ACTION = 2012  # invalid = action
DSM_RC_INVALID_DS_HANDLE = 2014  # invalid = ADSM handle
DSM_RC_INVALID_REPOS = 2015  # invalid = value for = repository
DSM_RC_INVALID_FSNAME = 2016  # fs = should start = with dir = delim
DSM_RC_INVALID_OBJNAME = 2017  # invalid = full path = name
DSM_RC_INVALID_LLNAME = 2018  # ll = should start = with dir = delim
DSM_RC_INVALID_OBJOWNER = 2019  # invalid = object owner = name
DSM_RC_INVALID_ACTYPE = 2020  # invalid = action type
DSM_RC_INVALID_RETCODE = 2021  # dsmRC = in dsmRCMsg = is invalid
DSM_RC_INVALID_SENDTYPE = 2022  # invalid = send type
DSM_RC_INVALID_PARAMETER = 2023  # invalid = parameter
DSM_RC_INVALID_OBJSTATE = 2024  # active, inactive, or = any match?
DSM_RC_INVALID_MCNAME = 2025  # Mgmt = class name = not found
DSM_RC_INVALID_DRIVE_CHAR = 2026  # Drive = letter is = not alphabet
DSM_RC_NULL_FSNAME = 2027  # Filespace = name is = NULL
DSM_RC_INVALID_HLNAME = 2028  # hl = should start = with dir = delim

DSM_RC_NUMOBJ_EXCEED = 2029  # BeginGetData = num objs = exceeded

DSM_RC_NEWPW_REQD = 2030  # new = password is = required
DSM_RC_OLDPW_REQD = 2031  # old = password is = required
DSM_RC_NO_OWNER_REQD = 2032  # owner = not allowed. Allow = default
DSM_RC_NO_NODE_REQD = 2033  # node = not allowed = w/ pw=generate
DSM_RC_KEY_MISSING = 2034  # key = file can't = be found
DSM_RC_KEY_BAD = 2035  # content = of key = file is = bad

DSM_RC_BAD_CALL_SEQUENCE = 2041  # Sequence = of DSM = calls not = allowed
DSM_RC_INVALID_TSMBUFFER = 2042  # invalid = value for = tsmbuffhandle or = dataPtr
DSM_RC_TOO_MANY_BYTES = 2043  # too = many bytes = copied to = buffer
DSM_RC_MUST_RELEASE_BUFFER = 2044  # cant = exit app = needs to = release buffers
DSM_RC_BUFF_ARRAY_ERROR = 2045  # internal = buff array = error
DSM_RC_INVALID_DATABLK = 2046  # using = tsmbuff datablk = should be = null
DSM_RC_ENCR_NOT_ALLOWED = 2047  # when = using tsmbuffers = encription not = allowed
DSM_RC_OBJ_COMPRESSED = 2048  # Can't = restore using = tsmBuff on = compressed object
DSM_RC_OBJ_ENCRYPTED = 2049  # Cant = restore using = tsmbuff an = encr obj
DSM_RC_WILDCHAR_NOTALLOWED = 2050  # Wild = card not = allowed for = hl,ll
DSM_RC_POR_NOT_ALLOWED = 2051  # Can't = use partial = object restore = with tsmBuffers
DSM_RC_NO_ENCRYPTION_KEY = 2052  # Encryption = key not = found
DSM_RC_ENCR_CONFLICT = 2053  # mutually = exclusive options

DSM_RC_FSNAME_NOTFOUND = 2060  # Filespace = name not = found
DSM_RC_FS_NOT_REGISTERED = 2061  # Filespace = name not = registered
DSM_RC_FS_ALREADY_REGED = 2062  # Filespace = already registered
DSM_RC_OBJID_NOTFOUND = 2063  # No = object id = to restore
DSM_RC_WRONG_VERSION = 2064  # Wrong = level of = code
DSM_RC_WRONG_VERSION_PARM = 2065  # Wrong = level of = parameter struct

DSM_RC_NEEDTO_ENDTXN = 2070  # Need = to call = dsmEndTxn

DSM_RC_OBJ_EXCLUDED = 2080  # Object = is excluded = by MC
DSM_RC_OBJ_NOBCG = 2081  # Object = has no = backup copy = group
DSM_RC_OBJ_NOACG = 2082  # Object = has no = archive copy = group

DSM_RC_APISYSTEM_ERROR = 2090  # API = internal error

DSM_RC_DESC_TOOLONG = 2100  # description = is too = long
DSM_RC_OBJINFO_TOOLONG = 2101  # object = attr objinfo = too long
DSM_RC_HL_TOOLONG = 2102  # High = level qualifier = is too = long
DSM_RC_PASSWD_TOOLONG = 2103  # password = is too = long
DSM_RC_FILESPACE_TOOLONG = 2104  # filespace = name is = too long
DSM_RC_LL_TOOLONG = 2105  # Low = level qualifier = is too = long
DSM_RC_FSINFO_TOOLONG = 2106  # filespace = length is = too big
DSM_RC_SENDDATA_WITH_ZERO_SIZE = 2107  # send = data w/ zero = est

# === new = return codes = for dsmaccess ===
DSM_RC_INVALID_ACCESS_TYPE = 2110  # invalid = access type
DSM_RC_QUERY_COMM_FAILURE = 2111  # communication = error during = query
DSM_RC_NO_FILES_BACKUP = 2112  # No = backed up = files for = this fs
DSM_RC_NO_FILES_ARCHIVE = 2113  # No = archived files = for this = fs
DSM_RC_INVALID_SETACCESS = 2114  # invalid = set access = format

# === new = return codes = for dsmaccess ===
DSM_RC_STRING_TOO_LONG = 2120  # String = parameter too = long

DSM_RC_MORE_DATA = 2200  # There = are more = data to = restore

DSM_RC_BUFF_TOO_SMALL = 2210  # DataBlk = buffer too = small for = qry

DSM_RC_NO_API_CONFIGFILE = 2228  # specified = API confg = file not = found
DSM_RC_NO_INCLEXCL_FILE = 2229  # specified = inclexcl file = not found
DSM_RC_NO_SYS_OR_INCLEXCL = 2230  # either = dsm.sys = or inclexcl = file
# specified = in dsm.sys = not found
DSM_RC_REJECT_NO_POR_SUPPORT = 2231  # server = doesn't = have POR = support

DSM_RC_NEED_ROOT = 2300  # API = caller must = be root
DSM_RC_NEEDTO_CALL_BINDMC = 2301  # dsmBindMC = must be = called first
DSM_RC_CHECK_REASON_CODE = 2302  # check = reason code = from dsmEndTxn
DSM_RC_NEEDTO_ENDTXN_DEDUP_SIZE_EXCEEDED = 2303  # max = dedup bytes = exceeded

# === return = codes = 2400 - 2410 used = by lic = file see = agentrc.h ===

# === return = codes = 2410 - 2430 used = by Oracle = agent see = agentrc.h ===

DSM_RC_ENC_WRONG_KEY = 4580  # the = key provided = is incorrect
DSM_RC_ENC_NOT_AUTHORIZED = 4582  # user = is not = allowed to = decrypt
DSM_RC_ENC_TYPE_UNKNOWN = 4584  # encryption = type unknown

# =============================================================================
#   Return = codes (4600)-(4624) are = reserved for = clustering
# =============================================================================
DSM_RC_CLUSTER_INFO_LIBRARY_NOT_LOADED = 4600
DSM_RC_CLUSTER_LIBRARY_INVALID = 4601
DSM_RC_CLUSTER_LIBRARY_NOT_LOADED = 4602
DSM_RC_CLUSTER_NOT_MEMBER_OF_CLUSTER = 4603
DSM_RC_CLUSTER_NOT_ENABLED = 4604
DSM_RC_CLUSTER_NOT_SUPPORTED = 4605
DSM_RC_CLUSTER_UNKNOWN_ERROR = 4606


# =============================================================================
#   Return = codes (5701)-(5749) are = reserved for = proxy
# =============================================================================
DSM_RC_PROXY_REJECT_NO_RESOURCES = 5702
DSM_RC_PROXY_REJECT_DUPLICATE_ID = 5705
DSM_RC_PROXY_REJECT_ID_IN_USE = 5710
DSM_RC_PROXY_REJECT_INTERNAL_ERROR = 5717
DSM_RC_PROXY_REJECT_NOT_AUTHORIZED = 5722
DSM_RC_PROXY_INVALID_FROMNODE = 5746
DSM_RC_PROXY_INVALID_SERVERFREE = 5747
DSM_RC_PROXY_INVALID_CLUSTER = 5748
DSM_RC_PROXY_INVALID_FUNCTION = 5749

# =============================================================================
#   Return = codes = 5801 - 5849 are = reserved for = cryptography/security
# =============================================================================

DSM_RC_CRYPTO_ICC_ERROR = 5801
DSM_RC_CRYPTO_ICC_CANNOT_LOAD = 5802
DSM_RC_SSL_NOT_SUPPORTED = 5803
DSM_RC_SSL_INIT_FAILED = 5804
DSM_RC_SSL_KEYFILE_OPEN_FAILED = 5805
DSM_RC_SSL_KEYFILE_BAD_PASSWORD = 5806
DSM_RC_SSL_BAD_CERTIFICATE = 5807

# =============================================================================
#   Return = codes = 6300 - 6399 are = reserved for = client-side = deduplication
# =============================================================================
DSM_RC_DIGEST_VALIDATION_ERROR = 6300  # End-to-end = digest validation = err  
DSM_RC_DATA_FINGERPRINT_ERROR = 6301  # Failure = in Rabin = fingeprinting
DSM_RC_DATA_DEDUP_ERROR = 6302  # Error = converting data = into chunks
