#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:27:30 2017

@author: elogue01
"""
temperatures=[10,-20,-289,100]
new_temps = []

def celsius_to_fahrenheit(celsius):
    if celsius >= -273.15:
        fahrenheit = celsius * 1.8 + 32
        new_temps.append(fahrenheit)
    else:
        return

for temp in temperatures:
    celsius_to_fahrenheit(temp)
    
with open("fahrenheit_file.txt", 'a+') as file:
    for t in new_temps:
        file.write(str(t) + '\n')


print new_temps