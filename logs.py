from datetime import datetime
import os

dt = datetime.now().strftime("%d.%m.%y-%H.%M.%S")

SAVE_PATH = os.path.abspath("logs") + '\\'
file_name = f"{dt}.txt"

class Logger(object):
    def __init__(self, save_path = SAVE_PATH, file_name = file_name):
        self.save_path = save_path
        self.file = open(save_path+file_name, "w")