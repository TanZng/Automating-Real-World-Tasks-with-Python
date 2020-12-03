#!/usr/bin/env python3
import requests
import glob

url = "http://localhost/upload/"

img_path = 'supplier-data/images/'

for filename in glob.glob(img_path + "*.jpeg"):
    with open(filename, 'rb') as image:
        r = requests.post(url, files={'file': image})
        print("Status code: ", r.status_code)