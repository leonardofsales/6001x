#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:34:38 2016

@author: leonardofsales
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    soma = 0
    for word in aDict.values():
        if len(word) == 1:
            soma = soma + 1
        else:
            for i in word:
                soma = soma + 1
    return soma