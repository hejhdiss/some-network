# CopyRight @hejhdiss(Muhammed Shafin P)
# Licensed under Apache 2.0.

# this is a probe where uses srp which have repluy w8ing and sendp doesnt have -it is send forgotten. verbose =1 is debugginga nd verbose =0 is sil;ent and clean execution
# used 00:00:00:00:00:00 instaed of broadcast (to show that we dont know destination or target mac - becuase ,some routers treats as  probe only if arp destination is that.differ by router. ) which is better and used commonly 
# probe is used to get ip for a diskless server which is replaced by bootp which is replaced by dhcp.
# this isnt unicast ,whiuch means this isnt sending to a specified mac to ask that is this ip available or who has this ip.
# may can use unicast instead of braodcast  in any case if you need to reduce arp cache flooding or congestion porblem in router.



from scapy.all import Ether,ARP,srp,get_if_hwaddr

iface='wlo1'
mac_id=get_if_hwaddr(iface)
for i in range(1,255):
    ip_wanted=f'192.168.0.{i}'
    pkt=Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(hwsrc=mac_id,psrc='0.0.0.0',pdst=ip_wanted,hwdst='00:00:00:00:00:00',op=1)
    print(f'sending as probe for {ip_wanted}')
    ans,unans =srp(pkt,iface=iface,timeout=0.5,verbose=1)

    if ans:
	    for my_send_packet,got_packet in ans:
	        	print('Have in this:',got_packet.psrc,'MAC:',got_packet.hwsrc)
    else:
	    print('nothing')
	
"""
deprecated  thsi after 2.4.x of scapy ,now automated collection.
multi=True means to gets  multiple else stops in first packaes getting ,its for only srp not for sendp and srp is at  layer 2 only and  the another which is at layer 3 which is sr. this srp also have soemthing like this srp1() stop after one reply.
"""
"""
a=my_send_packet
a[Ether].src     → your MAC
a[ARP].psrc      → "0.0.0.0"    (for probe)
a[ARP].pdst      → target IP
"""

"""
b=got_packet
b[Ether].src     → MAC of device replying
b[ARP].hwsrc     → MAC of device replying
b[ARP].psrc      → IP of device replying
"""
"""
coming under says that both ans and unas will be lists of tuples.
unans is contains list of send packets which doesnt get replies.
"""
"""

receiving format in ans 

[(send_packet_1,recieved_packet_1),(send_packet_1,recieved_packet_2).....] ==> packest (two packets) inside tuples inside list

these paxckets are scapy objects not ditcionary which have defiend  may be seen like Ether  | ARP like where it have its value defined  but it can be used or called like  sent_packet[ARP].psrc or sent_packet[Ether].src like taht for all scapy objects getting
"""

"""
unas will be list of tuples  where one  packet

since no reply got .

[(send_packet_1),(send_packet_2)......]
"""
