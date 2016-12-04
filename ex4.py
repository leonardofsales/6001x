# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 22:31:24 2016

@author: leonardofsales
"""

num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')