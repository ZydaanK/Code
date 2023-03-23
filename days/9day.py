# this file was created by: Zydaan Khan

'''
Step by step process for playing rock paper scissors
Algorithms - step by step process

Choose
Choose
Pick rock paper or scissors (skillfully analyzing opponent)
Last step: win lose or tie
Play again

Goals
Rules
Feedback 
Freedom

nouns and verbs in RPS
variables and function
Nouns:
Rock
Input
Win
opponent
lose
tie
paper
scissors

Verbs:
play again
count down to decide
choose (input)
challenging the adversary (do you want to play a game..)
display (print)
compare (win or lose?)

'''

# libraries
# suspense
from time import sleep
# random pseudo random
from random import randint

import pygame as pg
from os import path

#choices = [0,1,2]
choices0 = ["rock","paper","scissors"]
choices1 = ["Wizard","Theives","Fighter"]
games = [choices0, choices1]
# This prints ["rock","paper","scissors"] ["Wizard","Theives","Fighter"]
print(games)
# This prints ["rock","paper","scissors"]
print(games[0])
# This prints rock
print(games[0][0])
# This prints the letter r
print(games[0][0][0])
# this will cause a bug becasue the computer will be looking for something that is not there
#print(games[0][0][10])

# sleep(10)

# print("Let's play: " + str(choices))
print("Let's play: ", choices0[0], choices0[2], choices0[3])
# print(choices0[0])
# print(choices0[1])
# print(choices0[2])
catdog = 9
for i in choices0:
    print(i, "", end="")
# sleep(3)


# for i in range(len(choices0)):
#     print("this is the index " + str(i))
#     # oliver is working too hard
#     # my least favorite thing 
#     j = choices0[i]
#     print("This is the value in the list " + j)
def get_userchoice():
    global user_choice
    user_choice = input("Choose rock paper or scissors...")


def cpu_choice():
    return choices0[randint(0,2)]
    # return "The computer has chosen " + choices0[randint(0,2)]
# print(choices[randint(0,2)])
# defines wanna play
def wanna_play():
    # responds to the input
    response = input("do you want to play?")
    # if  command if no
    if response == "no":
        # goes false if no
        return False
    # if this is true it will say yes
    elif response == "yes":
        # prints attaboy!!!
        print("attaboy!!!")
    else:
        print("")
# defines the compare function
def compare():
    # what the computer choses
    cpu = cpu_choice()
    #prints the computer chose
    print("The computer chose", cpu)
    if user_choice == cpu:
        print("Tie!!")
    # if this is true
    elif user_choice == "rock":
        # if  command if scissors
        if cpu == "scissors":
            # prints You win!
            print("You win!")
        # if this is true
         # if this is true it will say paper
        elif cpu == "paper":
            # prints You lose!
            print("You lose!")
    # if this is not true
    else:
        # prints this is the last thing that will happen if nothing else is true
        print("this is the last thing that will happen if nothing else is true")
        # if true
while True:
    # makes playing equal to function
    playing = wanna_play()
    # prints playing is
    print("playing is", playing)
    # if playing then it equal to false
    if playing == False:
        # takes a break/stops
        break
    # if this is not true
    else:
        get_userchoice()
        compare()