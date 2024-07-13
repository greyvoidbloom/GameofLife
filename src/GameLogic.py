import pygame
from block import Block
global generation
generation = 1
def playground(screen_width,screen_height,block_side,population):
    for i in range(0,screen_width,block_side):
        for j in range (0,screen_height,block_side):
            player = Block(i,j,block_side,False)
            population[player.id] = player
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
def game_logic_compacted(alive_players,players,neighbour_counter,screen_width,screen_height,block_side):
    global generation
    new_members = update_alive(alive_players,players)
    tracking=neighbour_tracker(alive_population=new_members,max_x=screen_width/block_side,max_y=screen_height/block_side)
    neighbour_count_logic(  players,
                            neighbourstorage=neighbour_counter,
                            max_x=screen_width/block_side,
                            max_y=screen_height/block_side,
                            tracked_candidates=tracking)
    neighbour_decision_logic(   total_population= players,
                                neighbourlist= neighbour_counter)
    generation+=1
    print(f"generation: {generation} and alive players: {len(new_members)}")
