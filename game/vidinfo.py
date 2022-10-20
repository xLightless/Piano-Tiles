import pygame

class Display(object):
    FPS:int = 120
    TITLE:str = "Piano Tiles v1.0.0"
    
    def __init__(self, width = float, height = float, title:str = TITLE):
        self.get_display = pygame.display.set_mode((width, height), flags = pygame.RESIZABLE, vsync=1)
        self.set_caption = pygame.display.set_caption(title)
        self.info = pygame.display.Info()
        self.clock = pygame.time.Clock()
    
display = Display(412, 915)
# print(display.info)
        
        
# This is an abstract class file to help class objects and functions use the correct display information