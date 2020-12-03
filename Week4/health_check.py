#!/usr/bin/env python3
import shutil
import psutil
import socket
import emails
import os

def cpu_ussage():
    err = "OK"
    if psutil.cpu_percent(1) >= 80:
        err = "Error - CPU usage is over 80%"
    print("CPU: {} %, {}".format(psutil.cpu_percent(1), err))
    return err

def mem_available():
    err = "OK"
    mem = psutil.virtual_memory()
    THRESHOLD = 500 * 1024 * 1024  # 500MB
    if mem.available <= THRESHOLD:
        err = "Error - Available memory is less than 500MB"
    print("MEMORY: {} bytes, {} ".format(mem.available, err))
    return err

def disc_space():
    err = "OK"
    du = shutil.disk_usage('/')
    free = du.free / du.total * 100
    if obj_Disk.percent >= 20:
        err = "Error - Available disk space is less than 20%"
    print("DISC SPACE: {} %, {}".format(free, err))
    return err

def resolve_localhost():
    err = "OK"
    ip = socket.gethostbyname('localhost')
    if ip != '127.0.0.1':
        err = "Error - localhost cannot be resolved to 127.0.0.1"
    print("LOCAL HOST: {}, {}".format(ip ,err))
    return err

def main():
    functions = [cpu_ussage, mem_available, disc_space, resolve_localhost]
    issue = "OK"
    for function in functions:
        issue = function()
        if issue != "OK":
            send_report(issue)
    
def send_report(title):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = title
    body = "Please check your system and resolve the issue as soon as possible"
    message = emails.generate(sender, receiver, subject, body, None)
    emails.send(message)

if __name__ == "__main__":
    main()