#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:59:00 2016

@author: leonardofsales
"""

#def biggest(aDict):
#    '''
#    aDict: A dictionary, where all the values are lists.
#
#    returns: The key with the largest number of values associated with it
#    '''

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    y = 0
    n = ''
    for i in aDict:
        x = len(aDict[i])
        if x >= y:
            y = x
            n = i
    return n
        
print(biggest(animals))