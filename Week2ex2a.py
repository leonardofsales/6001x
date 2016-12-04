# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 01:41:39 2016

@author: leonardofsales
"""

low = 0
high = 100
guess = int((low + high) / 2)

print("Please think of a number between 0 and 100!")

while True:
    print("Is your secret number " + str(guess) + "? ")
    
    resposta = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if resposta == "h":
        high = guess
    elif resposta == "l":
        low = guess
    elif resposta == "c":
        break
    else:
        print("Sorry, I did not understand your input.")
        
    guess = int((low + high) / 2)

print("Game over. Your secret number was: " + str(int(guess)))