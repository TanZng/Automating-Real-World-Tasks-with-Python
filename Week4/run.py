#!/usr/bin/env python3
import os
import requests
import glob

linux_instance_external_IP = ''
keys = ["name", "weight", "description"]
PATH_TXT = 'supplier-data/descriptions/'
PATH_IMG = 'supplier-data/images/'

def image_name(filename):
    temp = filename.split("/")
    temp = temp[-1:][0]
    temp = temp.split(".")
    name = temp[0]
    return name + ".jpeg"


my_json = {}
for filename in os.listdir(PATH_TXT + "*.txt"):
    f = open( PATH_TXT + filename, 'r')
    my_json = { "name":f.readline().rstrip("\n"),
                "weight":int(f.readline().rstrip("\n").split(' ')[0]),
                "description":f.readline().rstrip("\n")}
    name = image_name(filename)
    my_json["image_name"] = name # ex 001.jpge
    
    resp = requests.post('http://127.0.0.1:80/fruits/', json=my_json)
    print ("Status code: {} for {}".format(resp.status_code, name))