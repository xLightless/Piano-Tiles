import pygame
from game.graphics.components import Background, Button

class Screen(object):
    def __init__(
        self,
        display
    ):
        self.display:pygame.Surface = display
        self.disabled = True
        self.x:float = 0
        self.y:float = 0
        self.width:float = 0
        self.height:float = 0
        
        
class Main(Screen):
    def __init__(
        self,
        display
    ):
        Screen.__init__(self, display)
    
    def render(self, event:pygame.event.Event = None):
        """ Renders screen data to the display if not disabled """
        Background.fill_gradient(self.display, (236, 0, 140), (252, 103, 103))
        
        # Add some buttons to the main menu interface if not disabled
        if not self.disabled:
            play_button = Button(self.display, text = "Play Game", font_size = 32)
            play_button.render()
            if play_button.is_clicked: GameScreen(self.display)
            
            
class GameScreen(Screen):
    def __init__(
        self,
        display
    ):
        Screen.__init__(self, display)

