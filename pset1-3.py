# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 22:47:17 2016

Assume s is a cadeia of lower case characters.

Write a program that prints the maior subcadeia of s in which the letters
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your 
program should print

maior subcadeia in alphabetical order is: beggh
In the case of ties, print the first subcadeia. For example, if s = 'abcbcd', 
then your program should print

maior subcadeia in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. 
If you've spent more than a few hours on this problem, we suggest that you move 
on to a different part of the course. If you have time, come back to this 
problem after you've had a break and cleared your head.

@author: leonardofsales
"""

s = 'abcbcd'

cadeia = ""
contagem = 0
maiorcontagem = 0
maiorcadeia = ""

for i in range(len(s)):
    if i == 0:
        cadeia += s[i]
        contagem += 1
    elif s[i] >= s[i - 1]:
        cadeia += s[i]
        contagem += 1
    elif s[i] < s[i - 1]:
        if contagem > maiorcontagem:
            maiorcontagem = contagem
            maiorcadeia = cadeia
#        contagem = 0
        contagem = 1
        cadeia = ""
        cadeia += s[i]
    if i == len(s) - 1:
        if contagem > 1:
            if contagem > maiorcontagem:
                maiorcontagem = contagem
                maiorcadeia = cadeia
                
print("Longest substring in alphabetical order is: " + maiorcadeia)