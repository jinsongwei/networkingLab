'''
    udp socket client
    Silver Moon
'''

import socket   #for sockets
import sys  #for exit
from check import ip_checksum

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

host = 'localhost';
port = 4510;

#intialization
windowSize = 4
base = 0
nextseqnum = 0

msgList = []
n = 0
while(n < 10) :
    msgList.append(n)
    n = n + 1


old_msg = ''
resend = 0
count = 1
while(1) :

    msg = str(msgList[nextseqnum])
    try :

        s.settimeout(3)
        d = ip_checksum(msg)
        msg_d = d + msg
        msg_seq_d = str(nextseqnum) + msg_d
# check corrupted msg
#    msg_d = 'll' + msg
        if nextseqnum < base + windowSize :
            print 'sending... ' + msg_seq_d
            s.sendto(msg_seq_d, (host, port))
            nextseqnum = nextseqnum + 1


        # receive data from client (data, addr)
        try:
            data = s.recvfrom(1024)
            reply = data[0]
            addr = data[1]
            print 'Server reply : ' + reply
        except : #s.Timeouterror:
            print 'time out!!!'
            nextseqnum = base
            continue

        if reply == str(base) :
            base = base + 1
#        elif :
#            nextseqnum = base


    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

