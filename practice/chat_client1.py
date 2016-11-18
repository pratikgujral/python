# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 16:11:53 2016

@author: lms_user
"""

import socket
s = socket.socket()
host = socket.gethostname()
print "Host:", host
port = 12345
s.connect((host, port))
print s.recv()
s.close()