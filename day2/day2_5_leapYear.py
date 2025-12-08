#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 12:00:49 2025

@author: mritvik
"""

year = int(input("Enter the year: "))
if (year % 400==0):
    print("Is a leap year")
elif (year % 100==0):
    print("Not a leap year")
elif (year % 4 == 0):
    print("Is a leap year")
else:
    print('Not a leap year')
    