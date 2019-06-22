#!/usr/bin/python

from rdms.rdms import RdmsClient

if __name__ == "__main__":
    rdms = RdmsClient('111.231.138.146', 2333, 'lixisverygay', 1)
    rdms.connect()
