# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 16:32:22 2016

@author: lms_user
"""

# Socket server
import socket
s = socket.soket()
host = socket.gethostname()
port = 12345

s.bind((host,port))
s.listen(5)
while True:
    c, addr = s.accept()
    