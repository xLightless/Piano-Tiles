import pygame

class Background(object):
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
    """ Manages mouse graphics and cursor information """

    button_down = False
    button_up = True
    
    def set_mouse_pointer(self, window, color:tuple = (0, 0, 0), x:int = None, y:int = None):
        pygame.mouse.set_visible(False)
        mousepos = pygame.mouse.get_pos()
        outer = pygame.draw.circle(window, color, mousepos, 20, 3)
        inner = pygame.draw.circle(window, color, mousepos, 12, 3)
        return (outer, inner)
    
    def is_over(self, obj):
        """ Used to check if the mouse is over an object """
        mousepos = pygame.mouse.get_pos()
        return True if obj.collidepoint(mousepos[0], mousepos[1]) else False
    
mouse = Mouse()

class Button(object):
    """ Creates a Button on the display """
    def __init__(
        self,
        surface:pygame.Surface,
        x:float = 0,
        y:float = 0,
        text:str = "",
        font:str = 'arial',
        font_size:int = 11
    ):
        # The surface/window of the parent
        self.surface = surface
        
        # Font, text, and color
        self.text = text
        self.font = font
        self.font_size = font_size
        self.text_color:tuple = (255, 255, 255)
        
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
        
        self.btn_color:tuple = (0, 0, 0)
        self.btn_hover_color:tuple = (31, 33, 34)
        self.btn_click_color:tuple = (61, 63, 64)
        self.br:int = 4 # Button Border Radius
        
        # Button display positioning
        self.x:float = self.surface.get_width()/2 + x
        self.y:float = self.surface.get_height()/2 + y
        
        # This parameter helps encourage screen switching rather than using generic callbacks to achieve a goal
        self.is_clicked:bool = False
        """
            Example: if #.clicked == True 'run code' else 'do something'
        """
        
    def render(self, x:float = None, y:float = None):
        """ Renders the Button object to a window or screen """
        
        x = self.x if x is None else x
        y = self.y if y is None else y        
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
        
        # Styles button interactions
        self._hover()
        self._is_clicked()
        
    def _hover(self, hover_color:tuple = None):
        """ Adds style to the Button object when hovered on """
        
        hover_color = self.btn_hover_color if hover_color is None else hover_color
        if self._is_over(self.btn_obj):
            pygame.draw.rect(self.surface, hover_color, self.btn_obj, border_radius = self.br)
            self.surface.blit(
                self.text_obj,
                (self.btn_obj.centerx - (self.text_obj.get_width()/2), 
                (self.btn_obj.centery - (self.text_obj.get_height()/2)))
            )
    def _is_clicked(self, click_color:tuple = None):
        """ Adds style to the Button object when clicked on """
        
        click_color = self.btn_click_color if click_color is None else click_color
        mousepress = pygame.mouse.get_pressed()[0] # Left Click

        if mousepress and self._is_over(self.btn_obj) == True:
            # Styles the button when clicked
            pygame.draw.rect(self.surface, click_color, self.btn_obj, border_radius = self.br)
            self.surface.blit(
                self.text_obj,
                (self.btn_obj.centerx - (self.text_obj.get_width()/2), 
                (self.btn_obj.centery - (self.text_obj.get_height()/2)))
            )
            
            self.is_clicked = True
        
    def _is_over(self, btn_obj = None):
        """ Private function that checks the button a user is interacting with """
        
        if btn_obj is not None:
            pos = pygame.mouse.get_pos()
            return True if btn_obj.collidepoint(pos[0], pos[1]) else False
        else: 
            btn_obj = self.btn_obj