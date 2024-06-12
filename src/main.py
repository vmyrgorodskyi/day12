# #lesson 114
#
# ################### Scope ####################
#
# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
#
# #local scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

#drink_potion()
#print(potion_strength)

#global scope

# player_health = 10
#
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#     drink_potion()
#
# drink_potion()
# print(player_health)

#lesson 115

# game_level = 3
#
#
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)

#lesson 116

#modifying global scope
#
# enemies = 1
#
# def increase_enemies():
#
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1
#
# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# #lesson 117
#
# #Global constants
# PI = 3.14159
#
# URL = "https://www.google.com"
# TWITTER_HANDLE + "@yu_angla"



#lesson 118

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)

print("Welcom to the guessing game!")
print("I'm thinkning of a number between 1 and 100")
secret_number = random.randint(1, 100)
#print(f"The secret number is {secret_number}")

def game():

    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    attempts_number = 0



    if difficulty_level == 'easy':
        attempts_number = 10
        print("You have 10 attempts")
    elif difficulty_level == 'hard':
        attempts_number = 4
        print("You have 5 attempts")


    is_guessed = False

    def calc(attempts_number):
        print(f"inside attempts number {attempts_number}")
        return attempts_number - 1


    #print(f"outside attempts number {attempts_number}")

    while not is_guessed:
        user_guess = int(input("Make a guess: "))
        if user_guess == secret_number:
            print(f"You guessed the {secret_number} as a secret number")
            is_guessed = True
        elif user_guess < secret_number and attempts_number > 0:
            print("Your guess is too low")
            attempts_number = calc(attempts_number)
        elif user_guess > secret_number and attempts_number > 0:
            print("Your guess is too high")
            attempts_number = calc(attempts_number)
        else:
            print("You lost")
            return

game()
print(f"The secret number was {secret_number}")




