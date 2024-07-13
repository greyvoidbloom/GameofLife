import pygame
import sys
from GameButtons import ControlButton
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
    DASHBOARD_COMMON_OFFSET = 10
    DASHBOARD_LEFT_OFFSET = 0
    DASHBOARD_TOP_OFFSET = 0
    
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT+PANEL_HEIGHT))
    clock = pygame.time.Clock()
    
    ## DASHBOARD BOILER CODE###
    game_dashboard = DashBoard(0,SCREEN_HEIGHT,(SCREEN_WIDTH,PANEL_HEIGHT),'black')
    quitBtn = ControlButton('./assets/quit.png',2,25)
    genBtn = ControlButton('./assets/manual_generation_propagation.png',2,25)
    run = True
    while run:
        clock.tick(30)
        
        screen.fill('black')  # Clear the screen if needed
        game_dashboard.spawn_dashboard(screen)
        quitBtn.spawn(screen=screen,x=10,y=410)
        genBtn.spawn(screen=screen,x=10,y=450)
        
        pygame.display.flip() 
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if genBtn.isClicked(mouse_pos=mouse_pos):
                    print('prop btn clicked')
                if quitBtn.isClicked(mouse_pos=mouse_pos):
                    print('quit button clicked')
                print(mouse_pos)
                
            if event.type == pygame.FINGERDOWN:
                touch_pos = event.x, event.y
    pygame.quit()
