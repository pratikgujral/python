# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 16:04:21 2016

@author: lms_user
"""

# Chat server
import socket

host = socket.gethostname()
print "Server host:", host

# Monitor client1 on a port
s1 = socket.socket()
port1 = 12345
s1.bind((host,port1))
s1.listen(5)

#Monitor client2 on another port
s2 = socket.socket()
port2 = 12346
s2.bind((host,port2))
s2.listen(5)

while True:
    print "\n\n*** RUN CLIENT 1 ***"
    c1,addr1 = s1.accept(msg1)
    print "Client1 connected", c1
    print "Client's address", addr1

    print "\n\n*** RUN CLIENT 2 ***"
    c2, addr2 = s2.accept(msg2)
    print "Client2 connected", c2
    print "Client's address", addr2

    if s1.accept(msg1):
        
