#!/usr/bin/env python3
# Fourth example of pinging from Python
# By 

import platform
import os

def ping_add(ip_add):
    current_os = platform.system().lower()
    if (current_os == "windows"):
        ping_cmd = f"ping -n 1 -w 2 {ip_add} > nul"
    else:
        ping_cmd = f"ping -c 1 -w 2 {ip_add} > /dev/null 2>&1"
    
    exit_code = os.system(ping_cmd)
    return exit_code

for octet in range(254):
    ip = "192.168.0.{0}".format(octet + 1)
    exit_code = ping_add(ip)
    print("{0}: {1}".format(ip, exit_code))

