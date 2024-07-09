import pygame
import sys
import time
from dashboard import DashBoard
from block import Block
from GameLogic import *

BLOCK_SIDE = 10
SCREEN_WIDTH = SCREEN_HEIGHT = 800
PANEL_HEIGHT = 100
ALIVE_PLAYER_COLOR = (240,240,240)
players = {}
alive_players=[]
neighbour_counter={}
global auto_generation_propagation
auto_generation_propagation = False

pygame.init()
playground(screen_width=SCREEN_WIDTH,screen_height=SCREEN_HEIGHT,block_side=BLOCK_SIDE,population=players)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT+PANEL_HEIGHT))
clock = pygame.time.Clock()
run = True

while run:
    screen.fill('black')
    clock.tick(30)
    for player in players.values():
        player.spawn(screen=screen,color=ALIVE_PLAYER_COLOR)
    if auto_generation_propagation:
        game_logic_compacted(alive_players=alive_players,
                                players=players,
                                neighbour_counter=neighbour_counter,
                                screen_width=SCREEN_WIDTH,
                                screen_height=SCREEN_HEIGHT,
                                block_side=BLOCK_SIDE)
        time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
                sys.exit()
            if event.key == pygame.K_SPACE:
                game_logic_compacted(alive_players=alive_players,
                                        players=players,
                                        neighbour_counter=neighbour_counter,
                                        screen_width=SCREEN_WIDTH,
                                        screen_height=SCREEN_HEIGHT,
                                        block_side=BLOCK_SIDE)   
            if event.key == pygame.K_RETURN:
                auto_generation_propagation = not auto_generation_propagation
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for player in players.values():
                if player.is_clicked(mouse_pos):
                    #print(f"touched cell x,y {player.x}{player.y}")
                    player.make_alive()
                    append_child(player,alive_players)
                    #print(f"cell width = {player.width}")
        if event.type == pygame.FINGERDOWN:
            touch_pos = event.x,event.y
            if player.is_clicked(touch_pos):
                    player.make_alive()
                    append_child(player,alive_players)
        
    pygame.display.update()
pygame.quit()