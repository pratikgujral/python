# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 19:02:20 2016

@author: lms_user
"""

# API
import requests

resp = requests.get('https://todolist.example.com/tasks/')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))

