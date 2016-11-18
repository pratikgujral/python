# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 11:26:02 2016

@author: lms_user
"""

import urllib

AppId = '402b04269f2fc8b4d339d6427f529f19'
url = "http://api.openweathermap.org/data/2.5/forecast/city?id=524901&APPID="

print "Connecting to url"
url  = urllib.urlopen(url + AppId)
print "Got the data from url"
print url.info()

html =  url.read()
fo = open("testFile.txt", mode = 'w+')
fo.write(html)
fo.close()


fo = open("testFile.txt", "r")

import json
