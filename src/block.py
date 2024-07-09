import pygame 
import sys

class Block:
    def __init__(self,x,y,side,isAlive):
        self.x = x
        self.y = y
        self.side = side
        self.alive = isAlive
        self.width = 1
        self.id = (int(x/side),int(y/side))
        
    def spawn(self,screen,color):
        self.entity = pygame.Rect((self.x,self.y),(self.side,self.side))
        pygame.draw.rect(screen,color,self.entity,self.width)
    def is_clicked(self, mouse_pos):
        return self.entity.collidepoint(mouse_pos)
    def make_alive(self):
        self.alive = True
        self.width = 0
    def kill(self):
        self.alive = False
        self.width = 1 
if __name__ == "__main__":
    BLOCK_SIDE = 20
    SCREEN_WIDTH = SCREEN_HEIGHT = 400
    PANEL_HEIGHT = 100
    players = []
    alive_players=[]
    #fuctions galore 
    def playground():
        for i in range(0,SCREEN_WIDTH,BLOCK_SIDE):
            for j in range (0,SCREEN_HEIGHT,BLOCK_SIDE):
                player = Block(i,j,BLOCK_SIDE,False)
                players.append(player)
    pygame.init()
    playground()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT+PANEL_HEIGHT))
    clock = pygame.time.Clock()
    run = True
    """
    for i in players:
        print(i.id)
    """
    while run:
        screen.fill('black')
        clock.tick(30)
        for player in players:
            player.spawn(screen=screen,color=(200,200,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(alive_players)
                run = False
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for player in players:
                    if player.is_clicked(mouse_pos):
                        #print(f"touched cell x,y {player.x}{player.y}")
                        player.make_alive()
                        if player not in alive_players:
                            alive_players.append(player)
                        
                        #print(f"cell width = {player.width}")
            if event.type == pygame.FINGERDOWN:
                touch_pos = event.x,event.y
                if player.is_clicked(mouse_pos):
                        player.make_alive()
                        if player not in alive_players:
                            alive_players.append(player)
                
        pygame.display.update()
    pygame.quit()