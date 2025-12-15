#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 13:28:49 2025

@author: mritvik
"""

#print fibo series of n terms
nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0


print("Fibonacci sequence:")
while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1