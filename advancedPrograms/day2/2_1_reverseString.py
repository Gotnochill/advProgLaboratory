#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 12:23:12 2025

@author: mritvik
"""

s = input("Enter the string: ")
temp = ""

while s != "":
    lastLetter = s[-1]
    temp += lastLetter
    s = s[:-1]

print('Reversed string is: ' , temp)
    