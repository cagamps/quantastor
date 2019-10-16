# This is an example file for using the Quantastor Python Client (qs_client.py).
# for a simple demo:
# > create a symbolic link to qs_client.py in the python3.x dist-packages directory
# cmd: sudo ln -s  /full/path/to/qs_client.py /usr/local/lib/python3.6/dist-packages/qs_client.py
# > once the symlink has been created, you can run this program using the following command:
# cmd: python3 example.py [host IP]
# RESULTS: if the host IP exists

from qs_client import QuantastorClient
from qs_client import quantastor_sdk_enabled
from qs_client import StorageSystem
import requests
import json
import sys
from requests.auth import HTTPBasicAuth

def main():
    if len(sys.argv) == 3:
        host = sys.argv[1]
        initator = sys.argv[2]
    else:
        print ("Missing required argument 'host IP'")
        print ("Usage: $ python3 acl_attach.py [host IP] [iqn]")
        return 1

    if not quantastor_sdk_enabled():
        print('QuantaStor python SDK is required for this module.')

    client = QuantastorClient(host,'admin','password')

    #create a host_initator
    try:
        task, obj = client.host_initiator_add(host='testHost',iqn=initator)
    except Exception as e:
        print ("EXCEPTION CAUGHT: " + str(e))

main()