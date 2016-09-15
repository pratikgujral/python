# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 07:09:59 2016

@author: lms_user
"""

# Threading basics
import thread
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s:%s" % (threadName, time.ctime(time.time()))
        
# Creating two threads
try:
    # calling thread.start_new_thread and passing in the function name and
    # parameters for the function as a tuple
    thread.start_new_thread(print_time, ("Thread1",2,))
    thread.start_new_thread(print_time, ("Thread2",4,))
except:
    print "Error: unable to start thread"
    
# Keep looping
while 1: pass
