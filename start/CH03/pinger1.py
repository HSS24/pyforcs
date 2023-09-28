#!/usr/bin/env python3
# First example of pinging from Python
# By hss24

import os
ip = "127.0.0.1"
ping_cmd = f"ping -c 1 -w -2 {ip} > echo $null 2>&1"
exit_code = os.system(ping_cmd)
print(exit_code)
