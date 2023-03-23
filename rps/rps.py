# File created by: Zydaan Khan
# 
 
# import libraries

from time import sleep

from random import randint 

import pygame as pg

import os

game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 1600
HEIGHT = 1000
FPS = 30

# define colors
# tuples are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# the choices
choices = ["rock", "paper", "scissors"]
# all the options for the text
def draw_text(text, size, color, x, y):
    # which font
    font_name = pg.font.match_font('arial')
    # size of the font
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

def cpu_randchoice():
    # random choice
    choice = choices[randint(0,2)]
    # prints computer randomly decides...
    print("computer randomly decides..." + choice)
    return choice

pg.init()
pg.mixer.init()
# where the caption will go
screen = pg.display.set_mode((WIDTH, HEIGHT))
# displays the caption
pg.display.set_caption("Rock, Paper, Scissors...")
clock = pg.time.Clock()
# gets the picture from the folder
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()
cpu_rock_image_rect = rock_image.get_rect()
# gets the picture from the folder
paper_image = pg.image.load(os.path.join(game_folder, 'paper.png')).convert()
paper_image_rect = paper_image.get_rect()
# gets the picture from the folder
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.png')).convert()
scissors_image_rect = scissors_image.get_rect()
# starts
start_screen = True

player_choice = ""
cpu_choice = ""
running = True

while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # ########## input ###########
        # HCI - human computer interaction...
        # keyboard, mouse, controller, vr headset
        # checks for keyboard
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                print("game on!!!!")
                start_screen = False
        
        if event.type == pg.MOUSEBUTTONUP:
            # gets the mouses position
            print(pg.mouse.get_pos()[0])
            # gets the mouse position
            print(pg.mouse.get_pos()[1])
            # get the mouse coordinates
            mouse_coords = pg.mouse.get_pos()
            # prints the mouse coordinates
            print(rock_image_rect.collidepoint(mouse_coords))
            if rock_image_rect.collidepoint(mouse_coords):
                # prints you clicked on rock...
                print("you clicked on rock..")
                # the players choice of rock
                player_choice = "rock"
                # randomizes and does a random choice
                cpu_choice = cpu_randchoice()
            # call a function that gets the cpu choice...
            elif paper_image_rect.collidepoint(mouse_coords):
                # prints you clicked on paper...
                print("you clicked on paper...")
                # the players choice of paper
                player_choice = "paper"
                # randomizes and does a random choice
                cpu_choice = cpu_randchoice()
            # uses the coords to answer with the print
            elif scissors_image_rect.collidepoint(mouse_coords):
                # prints you clicked on scissors...
                print("you clicked on scissors...")
                # the players choice of scissors
                player_choice = "scissors"
                # randomizes and does a random choice
                cpu_choice = cpu_randchoice()    
            # if player clicked on nothing, print you didn't click on anything...
            else:
                print("you didn't click on anything...")
    
    
    

    ############ draw ###################
    screen.fill(BLACK)

    # waits for player to hit space bar
    if start_screen == True:
        draw_text("Press space to play rock paper scissors", 22, WHITE, WIDTH/2, HEIGHT/10)
        rock_image_rect.x = 2000
        paper_image_rect.x = 2000
        scissors_image_rect.x = 2000

    # allows player to choose rock paper or scissors
    if not start_screen and player_choice == "":
        # where the rock image goes on the x-axis
        rock_image_rect.x = 50
        # where the paper image goes on the x-axis
        paper_image_rect.x = 600
        # where the scissors image goes on the x-axis
        scissors_image_rect.x = 1200
        screen.blit(scissors_image, scissors_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(rock_image, rock_image_rect)


    if player_choice == "rock":
        if cpu_choice == "rock":
            cpu_rock_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You tied!!!", 22, WHITE, WIDTH/2, HEIGHT/10)
    
    if player_choice == "paper":
        if cpu_choice == "paper":
            cpu_rock_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You tied!!!", 22, WHITE, WIDTH/2, HEIGHT/10)

    if player_choice == "scissors":
        if cpu_choice == "scissors":
            cpu_rock_image_rect.x = 500
            screen.blit(rock_image, rock_image_rect)
            screen.blit(rock_image, cpu_rock_image_rect)
            draw_text("You tied!!!", 22, WHITE, WIDTH/2, HEIGHT/10)



    pg.display.flip()

pg.quit()