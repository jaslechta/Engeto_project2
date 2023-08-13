"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jan Slechta
email: janslechta31@gmail.com
discord: honzas0100
"""
import os
import random

separator = 90*"-"


def valid_input(num):
    message = ""
    if str(num).isdigit() == False:
        message = "Input has to be only digits!!!"
        return False, message
    elif str(num)[0] == "0":
        message = "First digit can't be zero!!!"
        return False, message
    elif len(str(num)) != 4:
        message = "digits has to contain from 4 digits!!!"
        return False, message
    elif len(str(num)) != len(set(str(num))):
        message = "Use digits without duplicitas!!!"
        return False, message
    return True, message

def generate_random_number():
    number = str(random.randint(1000,9999))
    while valid_input(number) is False:
        number = str(random.randint(1000,9999))
    number_list = []
    for digit in number:
        number_list.append(digit)
    print (number_list)
    return number_list

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
