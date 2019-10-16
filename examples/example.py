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
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        print ("Missing required argument 'host IP'")
        print ("Usage: $ python3 example.py [host IP]")
        return 1

    if not quantastor_sdk_enabled():
        print('QuantaStor python SDK is required for this module.')

    client = QuantastorClient(host,'admin','password')

    try:
        system = client.storage_system_get()
        print (json.dumps(system.exportJson(), sort_keys=True,  indent=4, separators=(',', ': ')))
    except:
        print ("No storage system at IP: '" + host + "'.")

main()