# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:51:37 2016

@author: leonardofsales
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    soma = 0
    indice = 0
    for n in listA:
        multi = n*listB[indice]
        soma = soma + multi
        indice += indice
    return soma
        