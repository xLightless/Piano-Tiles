# This file is designed to handle game events and not logs or some arbitrary actions

import pygame

class ButtonEvent(object):
    """ Handles user interaction with Button objects """
    
    def _is_clicked(self, btn_obj, pos):
        # Checks if mouse is ontop of a Button object
        return True if btn_obj.collidepoint(pos[0], pos[1]) else False
    
    def target(self, event, action):
        # Targets the action of the button when interacted with
        """
            event (int): type of event to check for,
            action (Any): the target action of the object interaction
        """
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self._is_clicked() == True:
                    return action