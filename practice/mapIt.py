# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 10:10:29 2016

@author: lms_user
"""

## https://automatetheboringstuff.com/chapter11/
import webbrowser, sys

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

# TODO: Get address from clipboard.