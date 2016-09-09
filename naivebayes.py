# -*- coding: utf-8 -*-
"""
Created on Fri Sep 09 20:37:38 2016

@author: pratikgujral
"""

# Naive bayes
import numpy as np
X = np.array([[-1,-1], [-2,-1],[-3,-2],[1,1],[2,1],[3,2]]) # Fetures for training
Y = np.array([1,1,1,2,2,2]) # Labels for training

# Print X and Y
print "X:", X
print "Y:", Y

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB() # Create the classifier

clf.fit(X,Y) # Fit the data using GaussianNB

# Predicting the features for the test data
print clf.predict([[-0.8, -1]])  # New data point