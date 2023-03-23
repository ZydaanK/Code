# This file is created by: Zydaan Khan

'''
Step by step process for playing rock paper scissors
Algorithms - step by step process

1. Challenge the opponent and determine wthe rules by which you are going to play by
2. Mentally choose your option
        - Scissor
        - Paper
        - Rock
3. Count down from 3 to 1 and on "Shoot" make a rock, paper, or scissor.
4. Compare what each players get
5. Last step: Win lose or tie

Goals:
    - To win the matchup
Rules
    - You have to pick 1 of the 3 different objects
    - Have to both draw at the same time
Feedback
    - Whether you win or not
Freedom
    - To pick rock paper or scissors
    - How may games you can play

Nouns and verbs in RPS

Nouns:
    - Rock Paper and Scissors
    - Win or Lose or Tie
    - Input
    - Opponent
 Verbs:
    - Print
    - Number Generator
    - Countdown to decide
    - Play Again
    - Choose (input)
    - Display (print)
    - Compare (win or lose?)
  
Variables and function

'''

# Libraries
# Imports sleep function for suspense
from time import sleep
# Imports function of randint: Choose a random integer from set perameters (random pseudo random)
from random import randint

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

#print("Let's play:" + str(choices))
print("Let's play:")
#print(choices[0])
#print(choices[1])
#print(choices[2])
catdog = 9
for catdog in choices0:
    print(catdog)
# wait 3 seconds
#sleep(3)
print(catdog)

for i in range(len(choices0)):
    print("this is the index" + str(i))
    # oliver is working too hard
    # my least favorite thing
    j = choices0[i]
    print("This is the value in the list " + j)

# Allows us to choose what option we want
user_choice = input("Choose rock paper or scissors")

# prints you choose
print("You chose" + user_choice)

# What the computer chooses
def cpu_choice():
    # The final sentence to this game
    return "The computer has chosen something..." + choices0[randint(0,2)] 
    # return "The computer has chosen something..." + choices0[randint(0,2)]
#print(choices[randint(0,2)])
# Prints in the terminal
print(cpu_choice())

def cpu_choice():
    return choices0[randint(0,2)]
    # return "The computer has chosen" + choics[radint(0,2)]
# print(choices[radint(0,2)])

def compare(x,y):
    if x == y:
        print("Samesies")
    else:
        print("not samesies...")
    if x == "rock" and y == "scissors":
        print("you win!!!!!!!")

compare(user_choice,"scissors")