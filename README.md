# tsm-api-client

A ctypes python wrapper for the IBM Spectrum Protect (formerly Tivoli Storage Manager) API. 

Caution: This code is not fully tested.

# Requirements

The API requires a pre installed TSM Client [1] and expects a pre defined dsm.opt file in: /opt/tivoli/tsm/client/ba/bin/dsm.opt

[1] https://www.ibm.com/support/knowledgecenter/SSGSG7_7.1.1/com.ibm.itsm.client.doc/t_inst_linuxx86client.html%23t_inst_linuxx86client

# Sample usage

See also: \__main__ in tsm/tsm_api_client.py

    client = TSMApiClient()
    try:
        filename = '/tmp/test.txt'
        filespace = 'TEST'
        hl = 'abc'
        ll = 'test.txt'
        
        client.connect()
        info = tsm_api_client.query_session_info()
        logging.info('session info: {0}'.format(convert_tsm_structure_to_str(info)))
        tsm_api_client.archive(filename=filename,
                               filespace=filespace,
                               highlevel=hl,
                               lowlevel=ll)
        dest = '/tmp/test_retrieve.txt'
        tsm_api_client.retrieve(dest_file=dest,
                                filespace=filespace,
                                highlevel=hl,
                                lowlevel=ll)
    except Exception as err:
        tsm_api_client.close()
        logging.exception(err.message)
        logging.error(err.message)
    finally:
        tsm_api_client.close()
