# -*- coding: utf-8 -*-
"""
Created on Fri Sep 09 13:27:45 2016

@author: lms_user
"""

# Multiple Arguments to a function
def add(a1, a2):
    return a1+a2

def add2(*args):
    print len(args)
    print type(args)
    
    total = 0    
    for number in args:
       total += number
    return total
    
print add(2,1)
print add2(2,3,4,5)