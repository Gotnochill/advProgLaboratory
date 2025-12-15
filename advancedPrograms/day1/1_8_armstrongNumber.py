#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 12:11:57 2025

@author: mritvik
"""

n = int(input("Enter the number: "))
temp = n 
count = 0
while(temp > 0):
    count = count+1
    temp = temp // 10

arm_sum = 0 
temp = n
while(temp > 0):
    lastDigit = temp % 10
    arm_sum = arm_sum + pow(lastDigit, count)
    temp = temp // 10
    
if (arm_sum == n):
    print('Armstrong number!')
else :
    print('Not an Armstrong Number!')