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

playing = True
choices = ["rock","paper","scissors"]

# print("Let's play: " + str(choices))
#print("Let's play: ", choices[0], choices[2], choices[3])

def get_userchoice():
    global user_choice
    user_choice = input("Choose rock paper or scissors...")

def cpu_choice():
    return choices[randint(0,2)]
# defines wanna play
def wanna_play():
    response = input("do you want to play rock paper scissors?")
    if response == "no":
        return False
    elif response == "yes":
        print("attaboy!!!")
        return True
    else:
        print("need more input....")
# game, catdog, battle, start, rock_paper_scissors
def rps():
    wanna_play()
    get_userchoice()
    cpu = cpu_choice()
    print("The computer chose", cpu)
    if user_choice == cpu:
        print("Tie!!")
    elif user_choice == "rock":
        if cpu == "scissors":
            print("You win!")
        elif cpu == "paper":
            print("You lose!")
    else:
        print("this is the last thing that will happen if nothing else is true")

# while True:
#     playing = wanna_play()
#     print("playing is", playing)
#     if playing == False:
#         break
#     else:
#         get_userchoice()
#         compare()
rps()