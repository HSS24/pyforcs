#!/usr/bin/env python3
# Sixth example of pinging from Python
# Writing log messages to a file
# By 

import platform
import os
from datetime import datetime

def import_add():
    lines = []
    script_path = os.path.realpath(__file__)
    script_folder = os.path.split(script_path)
    f = open(script_folder[0] + "/ips.txt", "r")
    for line in f:
        line = line.strip()
        lines.append(line)

    return lines

def write_log(message):
    now = str(datetime.now() + "\t")
    message = now + str(message) + "\n"
    script_path = os.path.realpath(__file__)
    script_folder = os.path.split(script_path)
    f = open(script_folder[0] + "/pinger.log", "a")
    f.write(message)
    f.close()

def ping_add(ip_add):
    current_os = platform.system().lower()
    if (current_os == "windows"):
        ping_cmd = f"ping -n 1 -w 2 {ip_add} > nul"
    else:
        ping_cmd = f"ping -c 1 -w 2 {ip_add} > /dev/null 2>&1"
    
    exit_code = os.system(ping_cmd)
    return exit_code

for ip in ip_add: 
    exit_code = ping_add(ip)
    if exit_code == 0:
        write_log("{0} is online".format(ip))
        print("{0} is online".format(ip))
    else:
        write_log("{0} is offline".format(ip))
        
        