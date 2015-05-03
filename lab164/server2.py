'''
    Simple udp socket server
    Silver Moon (m00n.silv3r@gmail.com)
'''
 
import socket
import sys
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5410 # Arbitrary non-privileged port
 
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

myList = []
#now keep talking with the client
while 1:
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
    
    checker = 0
    for member in myList:
        if str(member) == str(addr): 
            checker = 1    

    if checker == 0:
        myList.append(addr)
    checker = 0;
     
    if not data: 
        break

    prefix = data[0:12]
#    if(data == 'Send to all:'  
    reply = 'OK...' + prefix
#    for member in myList:
#        ips += ' ' + str(member) 

    if prefix == 'Send to all:': 
        reply = data[12:len(data)] 
        for member in myList:
            s.sendto(reply, member)
    else:
        s.sendto(reply, addr)
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
     
s.close()
