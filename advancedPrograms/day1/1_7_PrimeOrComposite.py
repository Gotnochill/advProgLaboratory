#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 12:03:39 2025

@author: mritvik
"""
import math as mt

n = int(input('Enter the number to check for prime: '))
isPrime = 1 

if ( n < 2):
    isPrime = 0
elif ( n == 2 ):
    isPrime = 1
else:
    for i in range ( 2 , int(mt.sqrt(n))+1):
        if( n % i == 0):
            isPrime = 0
            break
        else :
            isPrime = 1

if(isPrime == 1):
    print(n , ' is a prime number')
else :
    print(n , " is a composite number")