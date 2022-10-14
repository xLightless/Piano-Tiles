from logs import Logger
from datetime import datetime
import pygame

class App(object):
    title = ""
    
    def __init__(self, width, height, title=title):
        # Creates the application window for pygame
        pygame.init()
        
        self.window = pygame.display.set_mode((width, height), flags=(pygame.RESIZABLE))
        self.title = title
        pygame.display.set_caption(title)
        
    def run(self, debug = False):
        terminated = False
        keys = pygame.key.get_pressed()
        
        while not terminated:
            for event in pygame.event.get():
                if debug == True:
                    if pygame.event.event_name(event.type) == "MouseMotion": pass
                    else: print(pygame.event.event_name(event.type))
                
                if event.type == pygame.QUIT:
                    terminated = True
                
                
                    
                    
                    
                
                    
                    