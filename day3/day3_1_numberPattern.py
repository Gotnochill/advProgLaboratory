#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 13:11:43 2025

@author: mritvik
"""

#3 number printing patterns
def pattern1(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def pattern2(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):  
            print(j, end=" ")
        print()

def pattern3(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

pattern1(5)
print("\n")
pattern2(5)
pattern3(5)