###########################################################
#
# udp-client-py2.py
# Modified version of "UDP Client" p. 11 Black Hat Python
# Created: 25 Jan 2019
#
###########################################################

import socket

target_host = "127.0.0.1"
# The book has port 80, but if the port is below 1024, an unprivileged user is not allowed to bind
# https://stackoverflow.com/questions/24001147/python-bind-socket-error-errno-13-permission-denied
target_port = 8000


# create socket object - - AF_INET means IPv4, and SOCK_DGRAM means it's a UDP client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Since the script from the book just hung waiting for a response, I took the advice to
# bind the socket to the target address (host + port)
# https://stackoverflow.com/questions/37191612/issue-with-receiving-response-from-127-0-0-1-with-udp-client-in-python


client.bind((target_host, target_port))

# You don't have to establish a connection because UDP is connectionless
# send data
client.sendto("AAABBBCCC", (target_host, target_port))

# receive data
data, addr = client.recvfrom(4096)

print data