# CopyRight  @hejhdiss(Muhammed Shafin P)
# LIcensed under Apache 2.0.


from scapy.all import conf, get_if_addr, get_if_mask

# 1. Get interface (default interface Scapy uses)
iface = conf.iface

# 2. Get local IP address
ip_addr = get_if_addr(iface)

# 3. Get subnet mask from interface
mask = get_if_mask(iface)

# 4. Convert subnet mask to prefix length (CIDR)
mask_list = mask.split('.')
prefix = sum(bin(int(x)).count("1") for x in mask_list)

# 5. Build CIDR string
cidr_value = f"{ip_addr}/{prefix}"

print("Interface :", iface)
print("IP Address:", ip_addr)
print("Netmask   :", mask)
print("CIDR      :", cidr_value)
