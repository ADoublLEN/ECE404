#! /bin/bash

# Author: Alex Dunker
# ECN: adunker
# HW: 9
# Filename: Dunker_hw09.sh
# Due Date: 03/29/2015

#PLACE NO RESTRICTION ON OUTBOUND PACKETS
iptables -I OUTPUT 1 -j ACCEPT

#BLOCK A LIST OF SPECIFIC IP ADDRESSES FOR ALL INCOMING CONNECTIONS
iptables -A INPUT -s 48.0.0.0/64.255.255.255 -j DROP

#BLOCK YOUR COMPUTER FROM BEING PINGED BY ALL OTHER HOSTS
iptables -A INPUT -p icmp --icmp-type echo-request -j REJECT

#SETUP PORT FORWARDING FROM AN UNUSED PORT OF CHOICE TO PORT 22
iptables -t nat -A PREROUTING -p tcp --dport 7800 -j DNAT --to 128.46.4.85:22
iptables -A INPUT -p tcp --dport 7800 -j ACCEPT
iptables -A FORWARD -p tcp --dport 22 -j ACCEPT

#ALLOW FOR SSH ACCES TO YOUR MACHINE FROM ONLY ECN
iptables -A INPUT -p tcp --dport 22 -j REJECT
iptables -A INPUT -s ecn.purdue.edu -p tcp --dport 22 -j ACCEPT

#HTTP ONLY ALLOWS A SINGLE IP ADDRESS
iptables -A INPUT -p tcp --dport 80 -j REJECT
iptables -A INPUT -p tcp -s 128.46.4.85 --dport 80 -j ACCEPT

#PERMIT AUTH/IDENT ON PORT 113
iptables -A INPUT -p tcp -m tcp --syn --dport 113 -j ACCEPT
