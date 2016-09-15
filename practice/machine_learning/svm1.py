# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 09:06:56 2016

@author: prati
"""

# Support Vector Machine

import numpy
X = numpy.array([[-1,-1], [-2,-1], [1,1], [2,1]]) # Training Features
y = numpy.array([1,1,2,2]) # Training Labels

from sklearn.svm import SVC

clf  = SVC() # Prepare the classifier
clf.fit(X,y) # Fit the training data

print clf.predict([[-0.8,-1]]) # Test data