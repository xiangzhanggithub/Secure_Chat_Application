##  features.py for final project
##  Course: CS6740 Network Security
##
##  By: Xiang Zhang, Yunfan Tian

import zmq
import sys
import time
import base64
import argparse
import protobuf_pb2
import getpass
import threading

# check repeat in file (if repeat, delete the repeat item)
def check_repeat(file_name, username):
    f = open(file_name, "r")
    lines = f.readlines()
    f.close()
    f = open(file_name, "w")
    for line in lines:
        log = line.split("  ")
        name = log[0]
        if name != username:
            f.write(line)
    f.close()

# delete the item 
def delete_from_file(file_name, username):
    check_repeat(file_name, username)

# check the repeat item in sign up
def check_repeat_in_sign_up(file_name, username):
    with open("sign_up.txt", 'r') as f: 
        for line in f:
            log = line.split("  ")
            name = log[0]
            Hash_password = log[1]
            if name == username:
                return 1
    return 0
        

# check the time stamp (if timeout, return 0)
def check_time_stamp(time1, time2):
    if time2 - time1 > 100:
        print 'Receive message time out'
        return 0
    else:
        return 1

# print prompt
def print_prompt(c):
    sys.stdout.write(c)
    sys.stdout.flush()
                

