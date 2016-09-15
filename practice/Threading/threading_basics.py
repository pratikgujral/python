# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 07:42:15 2016

@author: lms_user
"""

# threading modulem basics
import threading
import time

exitFlag = 0

class myThread(threading.Thread): # Class being derived from threading.Thread class
    # Overriding the __init__ 
    def __init__(self, threadID, name, counter):
        print "__init__ called"
        print "About to call parent's __init__"
        threading.Thread.__init__(self) # call to parent's constructor
        print "Call to parent's __init__ finished"
        self.threadID = threadID
        self.name = name
        self.counter = counter
        print "Last statement of __init__"
        
    # Run() is the entry point for the thread
    def Run(self):
        print "Entry point for thread- Run() called"
        print "Starting ", self.name
        print "Call to the "
        print_time()
        
        
    def print_time(threadName, delay, counter):
        while counter:
            if exitFlag:
                thread.exit()
            time.sleep(delay)
            print "%s : %s" % (threadName, time.ctime(time.time()))
            counter -= 1
            
# Create new threads
thread1 = myThread(threadID = 1, name = "Thread1", counter = 1)
thread2 = myThread(2, "Thread2", 2)

# Start the threads
thread1.start()
thread2.start()

print "Exiting the main thread"    