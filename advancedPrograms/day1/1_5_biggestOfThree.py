#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 11:53:57 2025

@author: mritvik
"""

print("Enter the 3 numbers: ")
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
if(a > b):
    if(a>c):
        print(a , " " + "is the greatest number")
    else:
        print(c , " " + "is the greatest number")
elif (b>a):
    if(b>c):
        print(b , ' ' + "is the greatest number")
    else:
        print(c , " " + "is the greatest number")
        