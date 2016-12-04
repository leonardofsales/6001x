# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 23:29:58 2016

@author: leonardofsales
"""

guess = 50
guessWhat = guess

print("Please think of a number between 0 and 100!")

while True:
    guess = guess/2
    print("Is your secret number " + str(int(guessWhat)) + "? ")
    
    resposta = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if resposta == "h":
        guessWhat = guessWhat - guess
    elif resposta == "l":
        guessWhat = guessWhat + guess
    elif resposta == "c":
        break
    else:
        print("Sorry, I did not understand your input.")

<<<<<<< HEAD
print("Game over. Your secret number was: " + str(int(guessWhat)))
=======
print("Game over. Your secret number was: " + str(int(guessWhat)))
>>>>>>> 07b5099b9e95df5981abd2315dafd1fe4c13ae6f
