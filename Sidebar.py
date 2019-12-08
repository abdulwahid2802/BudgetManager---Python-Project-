from tkinter import *
from app_constants import Constants

class Sidebar:
    def __init__(self, root):
        side_frame = Frame(root, height = Constants.app_window_height, width = Constants.app_window_width / 4 , bg = "#554F4C", relief="raised")
        side_frame.pack(side="left")