# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 11:45:11 2016

@author: lms_user
"""

# Json dump
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def print_details(self):
        print "Name:", self.name
        print "Salary:", self.salary

def Manager(Employee):
    def __init__(self, portal_username, *args):
        super.init
        self.portal_username = portal_username
    
    def print_details(self):
        print "Name:", self.name
        print "Salary:", self.salary
        print "Portal Username:", self.portal_username

m1 = Manager("pratikgujral")