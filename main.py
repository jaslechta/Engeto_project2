"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jan Slechta
email: janslechta31@gmail.com
discord: honzas0100
"""
import os
import random

separator = 90*"-"

"""
This function checks the validity of the input number
    Args:
        num (str): The input number to be validated

    Returns:
        True/False and if the number is invalid, return error message
"""
def valid_input(num):
    if str(num).isdigit() == False:
        return False,"Input has to be only digits!!!"
    elif str(num)[0] == "0":
        return False, "First digit can't be zero!!!"
    elif len(str(num)) != 4:
        return False, "digits has to contain from 4 digits!!!"
    elif len(str(num)) != len(set(str(num))):
        return False, "Use digits without duplicitas!!!"
    return True, ""

"""
This function generate random number in range from 1000 to 9999. Number is checked for valid format.
    
    Returns:
        number_list : list of digits from generated number
"""
def generate_random_number():
    number = str(random.randint(1000,9999))
    check_result, _ = valid_input(number)
    while check_result is False:
        number = str(random.randint(1000,9999))
        check_result, _ = valid_input(number)
    number_list = []
    for digit in number:
        number_list.append(digit)
    print (number_list)
    return number_list

"""
This function get guess from user. Input is checked for valid format

    Returns:
        guess : list of digits from input
"""
def get_guess():
    number = input("Enter a number: ")
    check_result, message = valid_input(number)
    while  check_result is False:
        print(message)
        number = input("Wrong input. Enter a number: ")
        check_result, message = valid_input(number)
    guess = []
    for digit in str(number):
        guess.append(digit)
    print(guess)
    return guess

"""
This function evaluate user's input against guessed number and returns number of cows (correct numbers, wrong position) 
and bulls (corect digits, correct position)
    Args:
        guess (list): list of digits
        guessed_number (list) : list of digits

    Returns:
        bulls, cows (int) : number  
"""
def guess_result(guess, guessed_number):
    bulls = 0
    cows = 0
    for i in range(len(guessed_number)):
        if guess[i] == guessed_number[i]:
            bulls += 1
        if guess[i] in guessed_number:
            cows += 1           
    cows = cows - bulls
    return bulls, cows

"""
    This is the main function of the program.

    It initializes the game, interacts with the user, and manages the game loop.
    The game is a Bulls and Cows guessing game, where the player tries to guess
    a 4-digit number with unique digits.

    Usage:
    - Run this function to start the game.

"""         
def main():
    game_is_on = True
    os.system("clear")
    print("Hi there!\n",separator,"\nI've generated a random 4 digit number for you. Let's play a bulls and cows game.\n",separator)
    guessed_number = generate_random_number()

    while game_is_on:
        guess = get_guess()
        bulls,cows = guess_result(guess,guessed_number)
        if bulls == 4:
            game_is_on = False
        print(bulls, "bulls", cows, "cows")
        print(separator)
    else:
        print("Congratulation, you guessed the right number")

if __name__ == "__main__":
    main()
