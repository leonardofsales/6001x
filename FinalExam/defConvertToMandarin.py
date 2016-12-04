#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 14:04:52 2016

@author: leonardofsales
"""

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

    if len(us_num) > 1:
        us_num_str_1 = us_num[0]
        us_num_str_2 = us_num[1]
    
    if int(us_num) >= 0 and int(us_num) <= 10:
        return trans[us_num]
    elif int(us_num) >= 11 and int(us_num) <= 19:
        return trans['10'] + ' ' + trans[us_num_str_2]
    elif int(us_num) >= 20 and int(us_num) <= 99:
        if us_num_str_2 == '0':
            return trans[str(us_num_str_1)] + ' ' + trans['10']
        else:
            return trans[str(us_num_str_1)] + ' ' + trans['10'] + ' ' + trans[str(us_num_str_2)]