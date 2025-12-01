#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 12:15:56 2025

@author: mritvik
"""

print("Enter two values a and b: ")
a = int(input())
b = int(input())

print("Enter 1. Using temp and Enter 2. Using temp")
x = int(input())

if (x == 1):
        temp = a
        a = b
        b = temp
        print("now a and b are: ", a, b)
        
elif x == 2 :
            a,b = b,a
            print("Now a and b are: ", a,b);
else:
        print("invalid")