# QuantaStor
## OSNEXUS QuantaStor Python Client Library

---

The python library for QuantaStor simplifies the process of automating QuantaStor management operations via python scripts.  All of the published QuantaStor REST APIs as documented on the OSNEXUS documentation [wiki](https://wiki.osnexus.com/index.php?title=REST_API_Reference_Guide) are callable via the python client.

---
## System Requirements

The minimum requirements for your storage system vary based on the workload. Use our [Solution Design Tools](https://www.osnexus.com/design) to help you find the solution that best fits your use-case and budget. The minimum requirements provided in this documentation serves as the bare minimum to explore using the software and its capabilities.

* Intel Xeon or AMD x64 bit server (or virtual server) 
* 16GB RAM 
* 2x SSDs for system/boot drives
    - Boot drives should be hardware mirrored and should be atleast 64GB in size.
* One or more disks per system for storage pools. (SSD/NVMe/PCI SSD/SATA/SAS/FC/iSCSI/AoE)
* Download [QuantaStor USB/ISO Installation Media](https://www.osnexus.com/downloads) for installation.
---
## Installation

### Install Quantastor

To use the QuantaStor Python Client Library, you must first install QuantaStor on your server hardware or use a QuantaStor virtual system. Installation of QuantaStor will also include python3. QuantaStor ISO files are created as hybrid ISO files which can be written to DVD media with DVD writting software or directly copied to a USB flash drive using `dd`. Follow the [installation guide](https://wiki.osnexus.com/index.php?title=%2B_Installation_Guide_Overview) on our support wiki to get started. The installation guide provides instructions for installation and configuration on both server hardware and virtual machines.

---
## Examples

See the `./examples/` directory for examples:

1. **Basic Example**

The basic example for the QuantaStor Python Client Library (`example.py`) does one operation to get information about the storage system that is specified from the command line and dumps the response data in JSON format. You can use this Python script as a basic template to build off of for QuantaStor automation.

2. **StorageVolume**

The file `example_sv.sh` is a bash script that utilizes two python scripts, `vol_setup.py` and `acl_attach.py`, to create an example storage volume and host. It then utilizes the `qs-util` QuantaStor tool-set to add a host initiator and login to an ISCSI session with the example storage volume.

3. **NetworkShare**

The file `example_ns.sh` is a bash script that utilizes the `shr_setup.py` python script to create an example network share. Then using the zfs `mount` command, mounts the network share to the local mount directory `/mnt/testMount`.