# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 10:14:39 2016

@author: lms_user
"""

# server
import socket
s = socket.socket()
host = socket.gethostname()
print "Server Host:", host
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    # Open help for s.accept
    help(s.accept)
    print "Client connected", c
    print "Client's address", addr
    c.send("Thank you for connecting")
    c.close()