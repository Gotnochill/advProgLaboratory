#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 11:50:29 2025

@author: mritvik
"""

import math as mt

n = int( input('Enter the number: ') )
print('Square , cube and root of the number is : ')
square = mt.pow(n , 2)
cube = mt.pow(n , 3)
sqrt = mt.pow(n, 1/2)
print(square, " " , cube , " " , sqrt )