# CopyRight @hejhdiss(Muhammed Shafin P)
# Licensed under Apache 2.0.

from scapy.all import PcapReader


reader = PcapReader("arp_traffic.pcap")

for pkt in reader:
	print(pkt.summary())
