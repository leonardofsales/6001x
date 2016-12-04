# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 22:27:37 2016

@author: leonardofsales
"""

numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))