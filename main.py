from tkinter import *
from app_constants import Constants
import Sidebar

Window = Tk()
Window.geometry("%dx%d+0+0" % (Constants.app_window_width, Constants.app_window_height))
Window['bg'] = Constants.app_window_bg_colors['dark']

side = Sidebar.Sidebar(Window)

Window.mainloop()
