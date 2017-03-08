#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 22:38:45 2017

@author: elogue01
"""
import datetime
import glob2

sample_files = glob2.glob("*.txt")

now = datetime.datetime.now()


with open(now.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", 'w') as merge_file:
    for item in sample_files:
        file = open(item, 'r')
        text = file.read()
        merge_file.write(text  + '\n')
        