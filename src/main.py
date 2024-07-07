import pygame
import sys
from dashboard import DashBoard
from block import Block


BLOCK_SIDE = 20
SCREEN_WIDTH = SCREEN_HEIGHT = 400
PANEL_HEIGHT = 100
ALIVE_PLAYER_COLOR = (255,182,193)
players = {}
alive_players=[]
neighbour_counter={}

generation = 1
#fuctions galore 
def playground():
    for i in range(0,SCREEN_WIDTH,BLOCK_SIDE):
        for j in range (0,SCREEN_HEIGHT,BLOCK_SIDE):
            player = Block(i,j,BLOCK_SIDE,False)
            players[player.id] = player
def append_child(child,parent):
    if child not in parent:
        parent.append(child)
def update_alive(alive_players,population):
    alive_players = []
    for player in population.values():
        if player.alive == True:
            #print(f"alive players: {player.id}")
            append_child(player,alive_players)
    return alive_players
    
def neighbour_tracker(alive_population,max_x,max_y):
    trackable_candidates=[] 
    #print(f"alive populaton: {alive_population}")
    for cell in alive_population:
        for i in range(-1,2,1):
            for j in range(-1,2,1):
                check_x = i+cell.id[0]
                check_y = j+cell.id[1]
                if(0<=check_x<max_x) and (0<=check_y<max_y) and ((check_x,check_y) not in trackable_candidates):
                    trackable_candidates.append((check_x,check_y))
    #print(f"trackable candidates: {trackable_candidates}")
    return trackable_candidates
def alive_neighbour_count(total_population,cell,max_x,max_y):
    neighbour_count=0 
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            check_x = i+cell[0]
            check_y = j+cell[1]
            if((i,j) != (0,0)) and (0<=check_x<max_x) and (0<=check_y<max_y) and (total_population[check_x,check_y].alive == True):
                neighbour_count+=1
    return neighbour_count
def neighbour_count_logic(total_population,neighbourstorage, max_x,max_y,tracked_candidates):
    #print(candidates)
    neighbours = tracked_candidates
    for candidate in neighbours:
        neighbour_count = alive_neighbour_count(total_population=total_population,cell=candidate,max_x=max_x,max_y=max_y)
        #print(f"{candidate} is {total_population[candidate].alive} and has {neighbour_count} alive neighburs")
        neighbourstorage[candidate] = neighbour_count
        
def neighbour_decision_logic(total_population,neighbourlist):
    
    for cell in neighbourlist:
        candidate = cell
        neighbour_count = neighbourlist[cell]
        #print(candidate,neighbour_count)
        
        if (total_population[candidate].alive == True) and (neighbour_count < 2 or neighbour_count > 3):
            total_population[candidate].kill()
        elif (total_population[candidate].alive == True) and (neighbour_count == 2 or neighbour_count == 3):
            total_population[candidate].make_alive()
        elif (total_population[candidate].alive == False) and (neighbour_count == 3):
            total_population[candidate].make_alive()
def game_logic_compacted(alive_players,players,neighbour_counter):
    new_members = update_alive(alive_players,players)
    tracking=neighbour_tracker(alive_population=new_members,max_x=SCREEN_WIDTH/BLOCK_SIDE,max_y=SCREEN_HEIGHT/BLOCK_SIDE)
    neighbour_count_logic(  players,
                            neighbourstorage=neighbour_counter,
                            max_x=SCREEN_WIDTH/BLOCK_SIDE,
                            max_y=SCREEN_HEIGHT/BLOCK_SIDE,
                            tracked_candidates=tracking)
    neighbour_decision_logic(   total_population= players,
                                neighbourlist= neighbour_counter)
    
pygame.init()
playground()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT+PANEL_HEIGHT))
clock = pygame.time.Clock()
run = True
while run:
    screen.fill('black')
    clock.tick(30)
    for player in players.values():
        player.spawn(screen=screen,color=ALIVE_PLAYER_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_logic_compacted(alive_players=alive_players,players=players,neighbour_counter=neighbour_counter)
                generation+=1
                new_members=update_alive(alive_players,players)
                print(f"generation: {generation} and alive players: {len(new_members)}")
            """
            if event.key == pygame.K_w:
                players[(5,7)].make_alive()
            if event.key == pygame.K_a:
                players[(5,7)].kill() 
            """
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