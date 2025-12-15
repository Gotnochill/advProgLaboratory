#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 13:08:14 2025

@author: mritvik
"""

def encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            result += ch
    return result


def decrypt(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base - key) % 26 + base)
        else:
            result += ch
    return result


text = input("Enter text: ")
key = int(input("Enter key: "))

encrypted = encrypt(text, key)
decrypted = decrypt(encrypted, key)

print("Encrypted text:", encrypted)
print("Decrypted text:", decrypted)
