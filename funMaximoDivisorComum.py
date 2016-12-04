# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 21:15:06 2016

Função de cálculo para máximo divisor comum

@author: leonardofsales
"""

def gcdRecur(a, b):
    if (a % b == 0):
        return b
    return gcdRecur(b, a%b)
    