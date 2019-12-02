import os

WINDOWS = True

#base_cmd_windows = 'nslookup'
base_cmd_windows_nslookup = 'nslookup'
base_cmd_windows_ping = 'ping -n 2'

#base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

ip_list = []
f = open("ip_addr.txt", "r")
for line in f:
	ip_list.append(line)
f.close

print('=' * 80)
print("[<Interesting IPs Listed>]")
print('=' * 80)
for i, ip_addr in enumerate(ip_list):
	print("{} ---> {}".format(i, ip_addr))

print()
print('-' * 80)
for ip_addr in ip_list:
	print("IP Addr: ", ip_addr)
	return_code = os.system("{} {}".format(base_cmd_windows_nslookup, ip_addr))
	return_code = os.system("{} {}".format(base_cmd_windows_ping, ip_addr))
	print('-' * 80)
print('-' * 80)
print()