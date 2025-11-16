## Here contents are something related to my own learning,since  i learning something .i happened to upload to this public repo.dont misuse.only for  learning purpose.
## No warranty 
## No guarranty that this will be updated always or any thing ,since if i think ,i will upload.but may be better for incomers or beginners for this fields.
- **mac_generator.py**: its random mac generator,but may craete valid one with valid oui(organizationally unique identifier -as prefix) - have only one function,it is - random_mac()
- **scapy_flood_arp_reply.py**: flooding using arp reply.
- **scapy_flood_arp_request.py**: flooding using arp request.
- **scapy_arp_probe.py**: probing using arp.
- **scapy_arp_sniff.py**: this is sniffing may be equals to tcpdump with filtered of arp.uses store=False ,so no saving in memory(means after  performing function based prn keyword input on each packet ,it doesnt save in its internal python list (scapy's) -never stop nic,kernel,.. buffering .print in terminal.
- **scapy_arp_sniff_pcap_save.py**: this is sniffing as mentioned above but with saving as pcap file.uses sync=True which will not buffer ,direct write for each package to disk immediatly.
- **scapy_pcap_reader.py**: pcap reader.
- **scapy_get_cidr.py**: getting cidr using scapy.
