import os

WINDOWS = True

base_cmd_windows = 'nslookup'

base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

ip_list = ["172.16.1.70",
"172.16.1.72",
"10.0.106.46",
"172.16.120.19",
"10.0.106.45",
"172.16.1.25",
"172.16.1.122",
"172.16.1.121",
"172.16.1.119",
"172.16.1.118",
"10.1.8.170",
"10.1.8.171",
"10.1.8.168",
"10.1.8.169"]

for i, ip_addr in enumerate(ip_list):
	print("{} ---> {}".format(i, ip_addr))

print()
print('-' * 80)
for ip_addr in ip_list:
	print("IP Addr: ", ip_addr)
	return_code = os.system("{} {}".format(base_cmd, ip_addr))
	print('-' * 80)
print('-' * 80)
print()