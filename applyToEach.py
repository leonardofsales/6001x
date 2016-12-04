#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 16:30:29 2016

@author: leonardofsales
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
def aSquare(a):
    '''
    Retorna o qudradado de a
    '''
    return abs(a)**2

def plusOne(a):
    '''
    Retorna a mais 1
    '''
    return a + 1