#! /usr/bin/env python3

import os
import requests

feedback_path = '/data/feedback/'
files = os.listdir(feedback_path)

keys = ["title", "name", "date", "feedback"]
dictionary = {}
for file in files:
    f = open(feedback_path + file, 'r') 
    for key in keys:
        dictionary[key] = f.readline()
    f.close()
    #print(dictionary)
    response = requests.post('http://<corpweb-external-IP>/feedback', data=dictionary)
    print("Status code: ", response.status_code)
