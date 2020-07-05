#!/usr/bin/env python3
from network import *
import shutil
import psutil
import requests
import socket
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75
def check_localhost():
   localhost = socket.gethostbyname('localhost')

def check_connectivity():
   request = requests.get("http://www.google.com")


# If there's not enough disk, or not enough CPU, print an error
if  check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() or check_connectivity():
    print("Everything ok")
else:
    print("Network checks failed")
