#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 13:03:04 2025

@author: mritvik
"""

import re

email = input("Enter email address: ")

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")
