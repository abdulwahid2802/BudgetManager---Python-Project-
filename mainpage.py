from tkinter import *
from app_constants import Constants
from PIL import Image, ImageTk

load = Image.open("man.png")
render = ImageTk.PhotoImage(load)


root_bg = {'dark': "#453F3C", 'light': "#D5d5d5"}

root = Tk()
root.geometry("%dx%d+0+0" % (Constants.app_window_width, Constants.app_window_height))
root.configure(background="#453F3C")


# side panel
side_frame = Frame(root, height=Constants.app_window_height, width = Constants.app_window_width/4, bg = "#554F4C", relief="raised")
side_frame.pack(side="left")

load = Image.open("man.png")
render = ImageTk.PhotoImage(load)
img = Label(side_frame, image=render)
img.image = render