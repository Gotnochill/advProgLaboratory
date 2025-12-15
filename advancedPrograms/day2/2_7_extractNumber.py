#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 13:07:05 2025

@author: mritvik
"""

import re

s = input("Enter a string: ")

numbers = re.findall(r'\d+', s)

print("Extracted numbers:", numbers)
