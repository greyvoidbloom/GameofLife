import pygame
import sys
import time
from GameButtons import ControlButton

from GameLogic import *

BLOCK_SIDE = 10
SCREEN_WIDTH = SCREEN_HEIGHT = 800
PANEL_HEIGHT = 200
ALIVE_PLAYER_COLOR = (253, 93, 168)
players = {}
alive_players=[]
neighbour_counter={}
global auto_generation_propagation
auto_generation_propagation = False
global run
run = True
pygame.init()

playground(screen_width=SCREEN_WIDTH,screen_height=SCREEN_HEIGHT,block_side=BLOCK_SIDE,population=players)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT+PANEL_HEIGHT))
pygame.display.set_caption("Conway's game of life")
clock = pygame.time.Clock()

#DASHBOARD SETUP 
quitBtn = ControlButton('./assets/quit.png',2,100)
sinleGenPropBtn = ControlButton('./assets/manual_generation_propagation.png',2,100)
autoGenPropBtn = ControlButton('./assets/auto_generation_propagation.png',2,100)

def quitSim():
    print("Quitting program ...")
    run = False
    sys.exit()
while run:
    screen.fill('black')
    clock.tick(30)
    quitBtn.spawn(screen=screen,x=50,y=SCREEN_HEIGHT+50)
    sinleGenPropBtn.spawn(screen=screen,x=300,y=SCREEN_HEIGHT+50)
    autoGenPropBtn.spawn(screen=screen, x= 550 , y= SCREEN_HEIGHT + 50)
        

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
            quitSim()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quitSim()
            elif event.key == pygame.K_SPACE:
                game_logic_compacted(alive_players=alive_players,
                                        players=players,
                                        neighbour_counter=neighbour_counter,
                                        screen_width=SCREEN_WIDTH,
                                        screen_height=SCREEN_HEIGHT,
                                        block_side=BLOCK_SIDE)   
            elif event.key == pygame.K_RETURN:
                auto_generation_propagation = not auto_generation_propagation
            elif event.key == pygame.K_c:
                cleanSlate(players=players)
                alive_players = []
                neighbour_counter={}
                print("board cleared!")
            elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                print("saving to file ...")
                save_to_file(savefile="saved.json",alive_players=alive_players,players=players,block_side=BLOCK_SIDE)
            elif event.key == pygame.K_l and pygame.key.get_mods() & pygame.KMOD_CTRL:
                print("loading data ...")
                alive_players = []
                neighbour_counter={}
                load_data(savefile="saved.json",players=players,block_size=BLOCK_SIDE,alive_players=alive_players,population=players)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if sinleGenPropBtn.isClicked(mouse_pos=mouse_pos):
                game_logic_compacted(alive_players=alive_players,
                                        players=players,
                                        neighbour_counter=neighbour_counter,
                                        screen_width=SCREEN_WIDTH,
                                        screen_height=SCREEN_HEIGHT,
                                        block_side=BLOCK_SIDE) 
            if quitBtn.isClicked(mouse_pos=mouse_pos):
                quitSim()
            if autoGenPropBtn.isClicked(mouse_pos=mouse_pos):
                auto_generation_propagation = not auto_generation_propagation 
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
    pygame.display.flip() 
    pygame.display.update()
pygame.quit()