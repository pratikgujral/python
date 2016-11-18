# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 12:16:10 2016

@author: lms_user
"""

# Inheritance
class Employee:
    def __init__(self, name, salary):
        print "Employee class constructor called"
        self.name = name
        self.__salary = salary # __salary is hidden.
        self.salary = salary
        
    def print_details(self):
        print "Method of Employee class called"
        print "Name:", self.name
        print "Salary:", self.__salary # Salary is accessible to class members but not outside the class
        
def Manager(Employee): # Inheritance
    def __init__(self, portal_username, *args):
        print "Manager class constructor called"
        super(Manager, self, *args).__init__()
        self.portal_username = portal_username
    
    def print_details(self):
        print "Method of Employee class called"
        print "Name:", self.name
        print "Portal Username:", self.portal_username


e1 = Employee("Shubham", 25000) # Instance created

e1.print_details() # Calling a method

print e1.name # Should work

## print e1.__salary # Will not work as it is hidden
print e1._Employee__salary # But hidden attributes are accessible in this way

# Creating instance of Manager
m1 = Manager("pratikgujral", "Pratik Gujral", 40000)