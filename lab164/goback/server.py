'''
    Simple udp socket server
    Silver Moon (m00n.silv3r@gmail.com)
'''

import socket
import sys
import time
from check import ip_checksum

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 4510 # Arbitrary non-privileged port

# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()


# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print 'Socket bind complete'

#now keep talking with the client


#initialization

while 1:
    # receive data from client (data, addr)
#    s.settimeout(10)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]

    seq = data[0:1]
    msg_sum = data[1:3]
    msg = data[3:len(data)]
    #sleep_here = 0
    msg_checksum = ip_checksum(msg)

    if msg_sum != msg_checksum:
        reply = seq + 1
    else:
        reply = seq
    #checksum = 0
    if not data:
        break

    s.sendto(reply, addr)
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()

s.close()

