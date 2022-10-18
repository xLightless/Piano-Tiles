from datetime import datetime
import os
import pygame

dt = datetime.now().strftime("%d.%m.%y-%H.%M.%S")

SAVE_PATH = os.path.abspath("logs") + '\\'
file_name = f"{dt}.txt"

class Logger(object):
    def __init__(self, save_path = SAVE_PATH, file_name = file_name):
        self.save_path = save_path
        self.file = open(save_path+file_name, "w")
        
    def log_events(self, event):
        if pygame.event.event_name(event.type) == "MouseMotion": pass
        elif pygame.event.event_name(event.type) == "Quit": print("Generating console log file now...")
        else: print(datetime.now(), "=>", pygame.event.event_name(event.type)) # Change this to save data to log
        
        # Create a method to saves new logs to latest.txt file
            # On Game close store latest to datetime file and empty latest file for new runtimes
            
    def console(self):
        """ Handles console interactions via the user """
        while True:
            pass
