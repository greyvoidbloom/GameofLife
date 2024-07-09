import pygame
import sys
class DashBoard():
    def __init__(self,x,y,size,color) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.workplace = pygame.Rect((self.x,self.y),self.size)
    def spawn_dashboard(self,screen):
        pygame.draw.rect(screen,self.color,self.workplace)
    def spawn_button(self,screen,text):
        pass
if __name__ == "__main__":
    SCREEN_WIDTH = SCREEN_HEIGHT = 400
    PANEL_HEIGHT = 100
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT+PANEL_HEIGHT))
    clock = pygame.time.Clock()
    
    ## DASHBOARD BOILER CODE###
    game_dashboard = DashBoard(0,SCREEN_HEIGHT,(SCREEN_WIDTH,PANEL_HEIGHT),'white')
    #game_dashboard.spawn_button(screen=screen,text='hilo')
    
    run = True
    while run:
        screen.fill('black')
        clock.tick(30)
        game_dashboard.spawn_dashboard(screen)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
            if event.type == pygame.FINGERDOWN:
                touch_pos = event.x,event.y
        pygame.display.update()
    pygame.quit()