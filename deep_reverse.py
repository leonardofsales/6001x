# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 22:06:12 2016

@author: leonardofsales
"""
def deep_reverse(L):
   """ assumes L is a list of lists whose elements are ints
   Mutates L such that it reverses its elements and also 
   reverses the order of the int elements in every element of L. 
   It does not return anything.
   """
   indice = 0
   L_copy = L[:]
   L_temp = []
   for i in L_copy:
       i.reverse()
       L_temp.insert(indice, i)
       indice = indice + 1
   L_temp.reverse()
   L = L_temp[:]

L = [[1, 2], [3, 4], [5, 6, 7]]

deep_reverse(L)