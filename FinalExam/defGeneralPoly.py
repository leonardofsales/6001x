#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:53:35 2016

@author: leonardofsales
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    def poly(x):
        resultado = 0
        k = len(L) - 1
        for i in L:
            polinomio = i * (x**(k))
            resultado = resultado + polinomio
            k = k - 1
        return resultado

    return poly
    
general_poly([1, 3, 3, 5])(5)
