#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 18:29:16 2016

@author: leonardofsales
"""
def square(x):
    '''
    x: int or float.
    '''
    y = x**2
    
    return y

def fourthPower(x):
    '''
    x: int or float.
    '''
    fourth = square(x) * square(x)
    return fourth
    
print(fourthPower(2))