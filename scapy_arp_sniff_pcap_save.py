# CopyRight @hejhdiss(Muhammed Shafin P)
# Licensed under Apache 2.0.

from scapy.all import sniff,PcapWriter

pcap_writer = PcapWriter("arp_traffic.pcap", append=True, sync=True)

sniff(store=False,iface='wlo1',filter='arp',prn=lambda x: [pcap_writer.write(x),print(x.summary())])
