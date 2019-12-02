def mac_conv(mac, sep=':'):
	#split mac address into 3 groups
	mac = mac.lower()
	mac_parts = mac.split(sep)
	return "{0[0]}{0[1]}.{0[2]}{0[3]}.{0[4]}{0[5]}".format(mac_parts)

	#join groups into a single MAC
	final_mac = '.'.join([gr1, gr2, gr3])

	#print final MAC address
	return(final_mac)

print('=' * 80)
print("[<Interesting MACs Listed>]".center(60,' '))
print('=' * 80)

#Open file with MAC addresses and convert them
with open('mac.txt', 'r') as f:
	for mac in f.readlines():
		print("{} {}".format("sh mac address-table | i",mac_conv(mac)))

print('=' * 80)
print('[<END>]'.center(60,' '))
print('=' * 80)