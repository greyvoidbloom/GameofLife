import pygame
import pygame_widgets
import sys

import pygame_widgets.button
class DashBoard():
    def __init__(self,x,y,size,color) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.workplace = pygame.Rect((self.x,self.y),self.size)
    def spawn_dashboard(self,screen):
        pygame.draw.rect(screen,self.color,self.workplace,width=1)
    def spawn_button(self,screen,text):
        button = pygame_widgets.button.Button(
        # Mandatory Parameters
        screen,  # Surface to place button on
        550,  # X-coordinate of top left corner
        550,  # Y-coordinate of top left corner
        50,  # Width
        50,  # Height

        # Optional Parameters
        text=text,  # Text to display
        fontSize=20,  # Size of font
        margin=10,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=lambda: print('Click')  # Function to call when clicked on
)
        
        
if __name__ == "__main__":
    SCREEN_WIDTH = SCREEN_HEIGHT = 400
    PANEL_HEIGHT = 100
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT+PANEL_HEIGHT))
    clock = pygame.time.Clock()
    
    ## DASHBOARD BOILER CODE###
    game_dashboard = DashBoard(0,SCREEN_HEIGHT,(SCREEN_WIDTH,PANEL_HEIGHT),'white')
    game_dashboard.spawn_button(screen=screen,text='hilo')
    
    run = True
    while run:
        screen.fill('black')
        clock.tick(30)
        #game_dashboard.spawn_dashboard(screen)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
            if event.type == pygame.FINGERDOWN:
                touch_pos = event.x,event.y
        pygame_widgets.update(events)
        pygame.display.update()
    pygame.quit()