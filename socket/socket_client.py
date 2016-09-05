# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 10:21:07 2016

@author: lms_user
"""

# Socket client
import socket
s = socket.socket()
host = socket.gethostname()
print type(host)
print "Client's hostname", host
port = 12345 # Have to be the same as the listening  port of the server
s.connect((host, port))
print s.recv(1024)
s.close()