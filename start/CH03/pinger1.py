#!/usr/bin/env python3
# First example of pinging from Python
# By 
import os

ip = "127.0.0.1"
ping_cmd = f"ping -c 1 -w 2 {ip} ; echo$?"
exit_code = os.system(ping_cmd)
print(exit_code)