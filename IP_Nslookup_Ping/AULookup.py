import os
import subprocess

base_cmd_windows_nslookup = 'nslookup'
base_cmd_windows_ping = 'ping -n 2'

print('=' * 80)
print("[<Interesting IPs Listed>]")
print('=' * 80)

#TO-DO: Write contents to a file
#file = open('myfile.txt', 'w+')

with open(os.devnull, "wb") as limbo:
        for n in range(0, 255):
                ip="192.168.101.{0}".format(n)
                result=subprocess.Popen(["ping", "-n", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        #print(ip + " : inactive")
                        #print('-' * 80)
                        continue
                else:
                        print(ip + " : active")
                        return_code = os.system("{} {}".format(base_cmd_windows_nslookup, ip))
                        #return_code = os.system("{} {}".format(base_cmd_windows_ping, ip))
                        print('-' * 80)
print('*' * 80)
print("Operation Complete")