# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:19:30 2016

@author: prati
"""

# Decision Trees

from sklearn import tree
X = [[0,0],[1,1]]
y = [0,1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)

print clf.predict([[2.,2,]])