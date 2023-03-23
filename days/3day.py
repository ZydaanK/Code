# file created by Zydaan Khan
'''
IPOS: Inpt, process, output, (store)

To install oygame on 3.11

Pygame isn't updated for python 3.11, but you can still instal a pre-version with pi
'''
# print is a built in funtion, displays words in between parenthesis
# hello there is a string
# hello there argument
# print("Hello there...")
# variable, string value

import pygame as pg

WIDTH = 800
HEIGHT = 600
vec = pg.math.Vector2

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()

greeting = "Hello there..."

x = True
y = "False"

print(greeting)
#
# storing a value that is returned from the input function that you type in the terminal
user_input = input("Please enter your name")
# 
print(greeting + user_input)

print(type(x))

print(x+y)