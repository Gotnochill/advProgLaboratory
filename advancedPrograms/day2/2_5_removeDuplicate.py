#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 12:55:49 2025

@author: mritvik
"""

s = input("Enter a string: ")
result = ""

for ch in s:
    if ch not in result:
        result += ch

print("String without duplicates:", result)
