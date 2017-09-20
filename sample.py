from datetime import datetime, time, date
from meraki_api import MerakiAPI
# snmp_helper functions courtesy of Kirk Byers: https://github.com/ktbyers/pynet/blob/master/snmp/snmp_helper.py
import requests
import json
import re

KEY = "e3c703d01c11e77217198699d9f181d8aa5ac01c"
ORG_INDEX = 0
NET_INDEX = 0
SSID_INDEX = 1
meraki = MerakiAPI(KEY)

def _localGetSSID(orgid_index, netid_index, ssid_index):
    orgs = meraki.organizations().index().json();
    ORGID= orgs[orgid_index]['id'];
    nets = meraki.organizations(ORGID).networks().index().json();
    NETWORKID = nets[netid_index]['id'];
    ssids = meraki.organizations(ORGID).networks(NETWORKID).ssids().index().json();
    SSID = ssids[ssid_index]
    return SSID



SSID = _localGetSSID(ORG_INDEX, NET_INDEX, SSID_INDEX);
print(SSID)
