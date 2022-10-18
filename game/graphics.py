import pygame

def fill_gradient(surface, color, gradient, rect=None, vertical=True, forward=True):
    """fill a surface with a gradient pattern
    Parameters:
    color -> starting color
    gradient -> final color
    rect -> area to fill; default is surface's rect
    vertical -> True=vertical; False=horizontal
    forward -> True=forward; False=reverse
    
    Pygame recipe: http://www.pygame.org/wiki/GradientCode
    """
    if rect is None: rect = surface.get_rect()
    x1,x2 = rect.left, rect.right
    y1,y2 = rect.top, rect.bottom
    if vertical: h = y2-y1
    else:        h = x2-x1
    if forward: a, b = color, gradient
    else:       b, a = color, gradient
    rate = (
        float(b[0]-a[0])/h,
        float(b[1]-a[1])/h,
        float(b[2]-a[2])/h
    )
    fn_line = pygame.draw.line
    if vertical:
        for line in range(y1,y2):
            color = (
                min(max(a[0]+(rate[0]*(line-y1)),0),255),
                min(max(a[1]+(rate[1]*(line-y1)),0),255),
                min(max(a[2]+(rate[2]*(line-y1)),0),255)
            )
            fn_line(surface, color, (x1,line), (x2,line))
    else:
        for col in range(x1,x2):
            color = (
                min(max(a[0]+(rate[0]*(col-x1)),0),255),
                min(max(a[1]+(rate[1]*(col-x1)),0),255),
                min(max(a[2]+(rate[2]*(col-x1)),0),255)
            )
            fn_line(surface, color, (col,y1), (col,y2))
            
            
class Mouse(object):
    """ Manages mouse graphics """
    
    def update_mouse_pos(self, window, color:tuple = (255, 255, 255), x:int = None, y:int = None):
        mousepos = pygame.mouse.get_pos()
        cursor_outer = pygame.draw.circle(window, color, mousepos, 20, 3)
        cursor_inner = pygame.draw.circle(window, color, mousepos, 12, 3)
        return (cursor_outer, cursor_inner)

class Button(object):
    """ Creates an interactive button object on a surface 
    
        e.g: menu_screen = Screen()
        e.g: menu_screen.surface.blit(button, x, y)
    
    """
    def __init__(
        self,
        surface,
        text:str,
        font:str = 'arial',
        font_size:int = 11
    ):
        # The surface/window of the parent
        self.surface = surface
        
        # Font, text, and color
        self.text = text
        self.font = font
        self.font_size = font_size
        self.text_color = (255, 255, 255)
        
        # Button dimensions and color
        self.padding = {
            "top":10,
            "bottom":10,
            "left":10,
            "right":10
        }
           
        pt = self.padding["top"]
        pb = self.padding["bottom"]
        pl = self.padding["left"]
        pr = self.padding["right"]
        
        self.margin = {
            
        }
        
        self.btn_color = (50,50,50)
        self.btn_click_color = (124,252,0)
        border_radius = self.br = 4

    def render(self, x:float, y:float):
        font = pygame.font.SysFont(self.font, self.font_size) 
        text_color = self.text_color
        self.text_obj = font.render(self.text, True, text_color)
        
        self.btn_width = self.text_obj.get_width() + self.padding["top"]
        self.btn_height = self.text_obj.get_height() + self.padding["left"]
        
        self.btn_obj = pygame.Rect(x-(self.btn_width/2), y-(self.btn_height/2), self.btn_width, self.btn_height)
        
        # Draws button object to parent surface then draws text object to button
        pygame.draw.rect(self.surface, self.btn_color, self.btn_obj, border_radius = self.br)
        self.surface.blit(
            self.text_obj,
            (self.btn_obj.centerx - (self.text_obj.get_width()/2), 
            (self.btn_obj.centery - (self.text_obj.get_height()/2)))
        )
        
    def _is_over(self, btn_obj):
        # Checks if mouse is ontop of a Button object
        pos = pygame.mouse.get_pos()
        return True if btn_obj.collidepoint(pos[0], pos[1]) else False
    
    def target(self, event, action = None):
        # Targets the action of the button when interacted with
        """
            event (int): type of event to check for,
            action (Any): the target of the object interaction - typically used via a function
        """
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self._is_over(self.btn_obj) == True:
                    # Update the color of the button when clicked and run 'action'
                    pygame.draw.rect(self.surface, self.btn_click_color, self.btn_obj, border_radius = self.br)
                    self.surface.blit(
                        self.text_obj,
                        (self.btn_obj.centerx - (self.text_obj.get_width()/2), 
                        (self.btn_obj.centery - (self.text_obj.get_height()/2)))
                    )
                    
                    action

class Screen(object):
    """ Base class to update new screen (surfaces) to the special pygame.display screen """
    def __init__(
        self,
        display
    ):
        self.display = display # Used to get the top level display of the application
        self.width, self.height = self.display.get_size()
        
    def render(self, obj, x:float, y:float):
        """ Used to render objects to the current screen """
        self.display.blit(obj, (x, y))
        pygame.display.update()
        
class MainScreen(Screen):
    """ Game Menu Screen """
    def __init__(
        self,
        display,
        event_loop
    ):
        self.display = display  # Used to get the top level display of the application
        clear_screen = (255, 255, 255)
        self.display.fill(clear_screen)
        
        # Add some buttons to the main menu interface
        btn_obj = Button(self.display, "Play Game", font_size = 32)
        btn_obj.btn_color = (128, 0, 0)
        btn_obj.btn_click_color = (102, 51, 153)
        btn_obj.render(self.display.get_width()/2, self.display.get_height()/2)
        btn_obj.target(event_loop)
        
class GameScreen(Screen):
    """ Game Screen """
    def __init__(
        self,
        display,
        event_loop
    ):
        self.display = display  # Used to get the top level display of the application
        clear_screen = (255, 255, 255)
        self.display.fill(clear_screen)
        
        # Add some buttons to the main menu interface
        btn_obj = Button(self.display, "Test game screen button", font_size = 32)
        btn_obj.btn_color = (128,0,0)
        btn_obj.btn_click_color = (102, 51, 153)
        btn_obj.render(self.display.get_width()/2, self.display.get_height()/2)
        btn_obj.target(event_loop, action = None)