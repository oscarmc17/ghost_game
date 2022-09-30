from curses.ascii import isdigit
import random
import string
from word_list import letters
from random import randint

# Opens up the list.txt file.
with open('list.txt') as search:
    for line in search:
        line = line.strip()
        # print(line)


# Play function that takes all inputs and return specific outputs.
def play():

    word = []
    strikes = 0
    current_word = ""
    current_player = random.choice([0, 1])

# How many players are playing? If int break, else pick a number.
    while True:
        player_count = input("1 or 2 players? ")
        if player_count.isdigit():
            players = int(player_count)
            if players <= 2:
                break
        else:
            print("Please pick between 1 or 2.")

# Player 1 starts, ints not allowed (try again), added strikes counter,
# append the letter that Player 1 entered into word list so it can be
# compared to overall words.
    while True:
        player1 = input("Player 1 please provide a letter: ")
        try:
            player1 = int(player1)
            print('Sorry, no numbers allowed. Try again: ')
            strikes += 1
            print("Strikes: ", strikes)
            if strikes == 3:
                print("Game Over. Player 2 wins.")
                break
        except ValueError:
            word.append(player1)
            break
    print("Player 1 selected: ", word)


# Player 2 starts, ints not allowed (try again), added strikes counter,
# append the letter that Player 2 entered into word list so it can be
# compared to overall words.
    while True:
        player2 = input("Player 2 please provide a letter: ")
        try:
            player2 = int(player2)
            print('Sorry, no numbers allowed. Try again: ')
            strikes += 1
            print("Strikes: ", strikes)
            if strikes == 3:
                print("Game Over. Player 1 wins.")
                break
        except ValueError:
            word.append(player2)
            break
        print(strikes)
    print("Player 2 selected: ", word)

# If letters entered by user match overall words, print them out.
    if word == letters:
        print(word)


# Play function gets called.
play()


# Here I was trying to loop through the letters,
# and have the respective player enter another one until condition is met.

# while True:
#     try:
#         if word == letters:
#             print(word)
#     except ValueError:
#         print("Loop through it again?")
#         break

# print(player2)
# print(word)
# if word == letters:
#     print("You lost. Sorry.")

# Here I was trying to randomly assign a player and have it loop through the game.

# round_number = 0
# player_list = [player1, player2]
# while True:
#     round_number += 1
#     # print("ROUND: ", round_number)
#     if round_number%2:
#         print(player_list[1], "GETS TO PLAY")
#         input("Press a key: \n\n")
