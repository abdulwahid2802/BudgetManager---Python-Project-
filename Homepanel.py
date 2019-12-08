from tkinter import *
from tkinter.font import Font
from app_constants import Constants

# home panel - main frame

class Homepanel:
    def __init__(self, root):
        main_frame = Frame(master=root, height = Constants.app_window_height, width = Constants.app_window_width * .75, bg = Constants.app_window_bg_colors['light'])
        main_frame.pack(side="right")