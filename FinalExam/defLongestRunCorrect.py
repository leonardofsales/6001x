#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:35:49 2016

@author: leonardofsales
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    numbers = L[:]
    kn = 1
    in_run = []
    in_run_temp = []
    de_run = []
    de_run_temp = []
    in_index = 0
    de_index = 0

    resultado = 0
    
    for i in L:

        if L[kn] >= i:
            in_run.append(i)
            in_run.append(L[kn])
            if len(in_run) > len(in_run_temp): 
                in_run_temp = in_run[:]
            in_run.remove(L[kn])

        if L[kn] < i:
            in_run = []


        kn += 1

        if kn == len(numbers):
            break

    kn = 1

    for i in L:

        if L[kn] <= i:
            de_run.append(i)
            de_run.append(L[kn])
            if len(de_run) > len(de_run_temp): 
                de_run_temp = de_run[:]
            de_run.remove(L[kn])

        if L[kn] > i:
            de_run = []

        kn += 1

        if kn == len(numbers):
            break
        
    if len(in_run_temp) > len(de_run_temp):
        resultado = sum(in_run_temp)
    elif len(in_run_temp) < len(de_run_temp):
        resultado = sum(de_run_temp)
    else:
        in_index = L.index(in_run_temp[0])
        de_index = L.index(de_run_temp[0])
        if in_index > de_index:
            resultado = sum(de_run_temp)
        else:
            resultado = sum(in_run_temp)
        
    return resultado