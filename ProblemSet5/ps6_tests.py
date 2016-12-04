#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 22:34:56 2016

@author: leonardofsales
"""
import string

def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        

    shift (integer): the amount by which to shift every letter of the 
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to 
             another letter (string). 
    '''
    low_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase

    shift_val = shift

    all_casesShift = {}

    if shift == 26:
        raise IndexError('Shift value must be under 26')

    for i in low_case:
        all_casesShift[i] = low_case[shift_val]
        shift_val = shift_val + 1
        if shift_val == 26:
            shift_val = 0

    shift_val = shift

    for i in upper_case:
        all_casesShift[i] = upper_case[shift_val]
        shift_val = shift_val + 1
        if shift_val == 26:
            shift_val = 0

    return all_casesShift

def apply_shift(shift):
    '''
    Applies the Caesar Cipher to self.message_text with the input shift.
    Creates a new string that is self.message_text shifted down the
    alphabet by some number of characters determined by the input shift        
    
    shift (integer): the shift with which to encrypt the message.
    0 <= shift < 26

    Returns: the message text (string) in which every character is shifted
         down the alphabet by the input shift
    '''
    
    message_text = "hello"
    
    ignored = ' ' + string.punctuation + string.digits
    
    dicShift = build_shift_dict(shift)
    
    shifted_message = ''
    
    for i in message_text:
        if i in ignored:
            shifted_message = shifted_message + i
        elif i in dicShift:
            shifted_message = shifted_message + dicShift[i]
            
    return shifted_message
            
    
    