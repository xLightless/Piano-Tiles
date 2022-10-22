from logs import Logger
from datetime import datetime
from game.graphics.components import mouse
from game.graphics.screens import GameScreen, Main
from game.vidinfo import display
import pygame

log = Logger()

class App(object):
    
    def __init__(self):
        # Creates the application window for pygame
        pygame.init()
        
        self.window = display.get_display
        self.display = display
        self.clock = display.clock
        self.fps = self.clock.get_fps()
        
        self.mouse = mouse
        self.isMousePressed = False
        
    def run(self, debug = False):
        
        # Runs the application
        terminated:bool = False
        
        # Initialise screens
        ms = Main(display = self.window)
        ms.disabled = False
        
        gs = GameScreen(display = self.window)
        
        while not terminated:
            
            for event in pygame.event.get():
                
                # Render Screens here
                if ms.disabled == False:
                    ms.render(event)
                # elif gs.disabled == False:
                #     gs.render(event)
                
                if debug == True:
                    log.log_events(event)
                
                if event.type == pygame.QUIT:
                    terminated = True

            self.mouse.set_mouse_pointer(self.window)
            pygame.display.update()