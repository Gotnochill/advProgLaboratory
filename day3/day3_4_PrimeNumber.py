#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 13:29:38 2025

@author: mritvik
"""


#check if num is prime
print("Enter number")
x=int(input())
count=0
for i in (2,x):
    if(x%i==0):
        count+=1
if(count>1):
    print(x," is not a prime number")
else:
    print(x," is a prime num")