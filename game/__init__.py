from logs import Logger
from datetime import datetime
from game.graphics import Mouse, MainScreen, GameScreen, fill_gradient
import pygame

log = Logger()

class App(object):
    TITLE = ""
    FPS = 120
    
    def __init__(self, width:float, height:float, title:str = TITLE, fps:int = FPS):
        # Creates the application window for pygame
        pygame.init()
        
        self.window = pygame.display.set_mode((width, height), flags=(pygame.RESIZABLE))
        pygame.display.set_caption(title)
        
        self.clock = pygame.time.Clock()
        self.fps = fps
        
        self.mouse = Mouse()
        pygame.mouse.set_visible(False)
        self.isMousePressed = False
        
    def run(self, debug = False):
        
        # Runs the application
        terminated:bool = False
        
        while not terminated:
            for event in pygame.event.get():
                
                # Render screens here
                ms = MainScreen(self.window, event)
                
                
                # Other checking measures
                if debug == True:
                    log.log_events(event)
                
                if event.type == pygame.QUIT:
                    terminated = True
            
            self.mouse.update_mouse_pos(self.window)
            self.clock.tick(self.fps)
            pygame.display.update()
                
                    
                    
                    
                
                    
                    