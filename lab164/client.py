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
 
ack = '0'
old_msg = ''
resend = 0
msgList = []
msgList.append("hello world!!")
msgList.append("I hate you, package missing!!!")
msgList.append("good bye world!!!")
count = 0
while(1) :
    if resend :
        msg = old_msg
        resend = 0
    else:
        msg = raw_input('Enter message to send : ')
        old_msg = msg
    
    try :
        #Set the whole string
         
        s.settimeout(5) 
        d = ip_checksum(msg) 
        msg_d = d + msg
# check corrupted msg
#    msg_d = 'll' + msg
        if ack == '0':
            msg_ack = '0' + msg_d
          #  ack = '0'
        elif ack == '1':
            msg_ack = '1' + msg_d
         #   ack = '1'
        print msg_ack
        s.sendto(msg_ack, (host, port))

         
        # receive data from client (data, addr)
        try:
            data = s.recvfrom(1024)
            reply = data[0]
            addr = data[1] 
            print 'Server reply : ' + reply
        except : #s.Timeouterror:
            print 'time out!!!'
            resend = 1
            continue

        if  reply == '0':
            if ack == '1':
                resend = 1
                msg = old_msg
                continue
            else:
                resend = 0
            ack = '1'
        else:
            if ack == '0':
                resend = 1
                msg = old_msg
                continue
            else:
                resend = 0
            ack = '0'
     
    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

