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
    print(numbers)
    k = 0
    kn = 1
    x = 0
    xx = 0
    in_run = []
    in_run_temp = []
    de_run = []
    de_run_temp = []

    resultado = 0
    
    for i in range(0, len(numbers)):
        if L[kn] >= L[k]:
#            x = k
            xx = kn
            in_run = L[x:xx]
            print(in_run)
            k += 1
            kn += 1
            

        if len(in_run) > len(in_run_temp):
            in_run_temp = in_run[:]
        
    # termina execução para evitar out of range
        if kn == len(numbers):
            break
        
    # compara o tamanho das duas sequências
    if len(in_run_temp) > len(de_run_temp):
        resultado = in_run_temp[:]
    elif len(in_run_temp) < len(de_run_temp):
        resultado = de_run_temp[:]
        
    # retorna resultado
    return resultado
            
    
L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
longest_run(L)