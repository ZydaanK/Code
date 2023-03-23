# This file is created by Zydaan Khan

'''
File created by:  Chris  Cozort

This series of files will include a step by step process for creating a basic pygame-based game in python

PRIMARY RESOURCE: https://www.w3schools.com/python/default.asp 

On installing pygame: 
Pygame isn't updated for python 3.11, but you 
can still install a pre-version with pip install pygame --pre

Scavenger hunt: Comment on the following items as you see them below:
- Variables
- Data Types
- Numbers
- Strings
- Booleans
- Operators
- Tuples
- While loops
- For loops
- If Else Conditional statements
- Functions
- Classes
'''

import pygame as pg

from pygame.sprite import Sprite

from random import *

from math import *

import os

# variable that stores a class...
vec = pg.math.Vector2

"""
From https://www.geeksforgeeks.org/__file__-a-special-variable-in-python/ 
A double underscore variable in Python is usually referred to as a dunder. A dunder variable is a 
variable that Python has defined so that it can use it in a “Special way”. 
This Special way depends on the variable that is being used.
The variable below __file__ is a variable that contains the path to the module that is currently being imported.
"""

# Data Types: Variables can store data of different types/paths, and different types can do different things
# <> will be showing data types
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

# A block of code of which only runs when it is called
# This prints in the terminal "here's the current game folder"
print("here's the current game folder", game_folder)
print("here's the current game folder", img_folder)


# A variable is created the moment you first assign a value to it
# This variable determines the size of the screen
WIDTH = 800
HEIGHT = 600
# FPS determines the speed in which the square goes
FPS = 30
# tuple that creates an RGB value that pygame uses
# tuple is variable 
# <>
BLACK = (0,0,0)
WHITE = (255,255,255)
TILESIZE = 64
# Determines where the square starst on the screen
# both are int
x = 0
y = 0

# <>
pg.init()
# <>
screen = pg.display.set_mode((WIDTH, HEIGHT))
# <>
# Strings in python are surrounded by either single quotation marks, or double quotation marks
# This string is saying "My First Pygame..."
pg.display.set_caption("My First Pygame...")
clock = pg.time.Clock()

# boolean value that determines if the game is running
running = True
# This is also a Number
speed = 5

# With the while loop we can execute a set of statements as long as a condition is true
# Saying when it is turned on
while running:
    clock.tick(FPS)
# A for loop is used for iterating over a sequence
# When closing out of the application, it stops running
    for event in pg.event.get():
# Seeing if the statement is true or false
        if event.type == pg.QUIT:

            running = False
    
    ##### UPDATE #####
    # Operators are used to perform operations on variables and values
    x += speed * FPS/1000
    # y += speed * FPS/1000
    rect = pg.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
    
    #####  DRAW  #####
    screen.fill(BLACK)
    pg.draw.rect(screen, WHITE, rect)

    pg.display.flip()

pg.quit()