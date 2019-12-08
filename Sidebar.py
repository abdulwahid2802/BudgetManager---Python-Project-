from tkinter import *

class Sidebar:
    def __init__(self, root):
        side_frame = Frame(root, height = 300, width = 100 , bg = "#554F4C", relief="raised")
        print(root.winfo_reqheight)
        side_frame.pack(side="left")