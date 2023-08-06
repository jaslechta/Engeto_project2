"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jan Slechta
email: janslechta31@gmail.com
discord: honzas0100
"""
import random

separator = 90*"-"

def without_duplicates(num):     
    return len(str(num)) == len(set(str(num)))

def generate_random_number():
    number = random.randint(1000,9999)
    while without_duplicates(number) is False:
        number = random.randint(1000,9999)
    number = str(number)
    number_list = []
    for digit in number:
        number_list.append(digit)
    print (number_list)
    return number_list

def get_guess():
    number = input("Enter a number: ")
    guess = []
    for digit in number:
        guess.append(digit)
    print(guess)
    return guess

def guess_result(guess, guessed_number):
    bulls = 0
    cows = 0
    for i in range(len(guessed_number)):
        if guess[i] == guessed_number[i]:
            cows += 1
        if guess[i] in guessed_number:
            bulls += 1           
    bulls = bulls - cows
    return bulls, cows
         


print("Hi there!\n",separator,"\nI've generated a random 4 digit number for you. Let's play a bulls and cows game.\n",separator)
guessed_number = generate_random_number()
guess = get_guess()
bulls,cows = guess_result(guess,guessed_number)
print(bulls, cows)



