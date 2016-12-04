# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 21:56:30 2016

@author: leonardofsales
"""

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup. 
    '''
    odd = 0
    oddTuple = ()
    for i in range(0, len(aTup), 2):
        oddTuple = oddTuple + (aTup[i],)
    return print(oddTuple)
    
x = ((15, 10, 1, 8, 2, 4, 6, 8))

oddTuples(x)