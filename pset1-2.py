# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:56:21 2016

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

@author: leonardofsales
"""

s = 'bob bob bob bobob'

bobs = 0

palavra = "bob"

for n in range(len(s)):
    if s[n:n+len(palavra)] == palavra:
        bobs += 1
        
print("Number of times bob occurs is: " + str(bobs))
