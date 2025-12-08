#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 11:44:04 2025

@author: mritvik
"""

"""nested if else program"""

print('Enter 3 numbers a , b and c: ')
a = int(input())
b = int(input())
c = int(input())

print('Now to find the largest number of the 3 using nested if else: ')
if (a > b):
    if(a>c):
        print('a is larger than b and c')
    elif(a<c):
        print('C is larger than a and b')
elif (b > a):
    if (b>c):
        print('b is larger than a and c')
    elif (b < c):
        print('c is larger than a and b')
elif (a == b and b == c):
    print('All the 3 numbers are same.')