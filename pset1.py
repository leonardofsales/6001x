# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:50:37 2016

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if
s = 'azcbobobegghakl', your program should print:

@author: leonardofsales
"""

s = "aaaaaaaaaa"

vowels = 0

for n in s:
    if n == "a" or n=="e" or n=="i" or n=="o" or n=="u":
        vowels += 1
print("Number of vowels: " + str(vowels))