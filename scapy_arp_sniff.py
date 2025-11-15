# CopyRight @hejhdiss(Muhammed Shafin P)
# Licensed under Apache 2.0.

from scapy.all import sniff

sniff(store=False,iface='wlo1',filter='arp',prn=lambda x: x.summary())
