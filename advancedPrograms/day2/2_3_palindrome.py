#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 12:47:06 2025

@author: mritvik
"""

s = input('Enter the string: ')
rev = ''

for ch in s:
    rev = ch + rev
    
if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")