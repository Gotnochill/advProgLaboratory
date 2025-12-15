#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 12:53:02 2025

@author: mritvik
"""

n = int(input("Enter number of rows: "))

print("\nTriangle Pattern:")
for i in range(1, n + 1):
    print("*" * i)

print("\nInverted Triangle Pattern:")
for i in range(n, 0, -1):
    print("*" * i)
