# Author: Ben Prince
# Version: 1.2
# Description: Window used to browse for a file

from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class Window(Tk):

    def __init__(self):
        super(Window, self).__init__()
        self.hello = ttk.Button(self)
        self.title("Test Patient Generator")
        self.minsize(640, 400)
        self.add_buttons()

    def add_buttons(self):
        self.hello["text"] = "Hello World"
        self.hello["command"] = self.say_hi
        self.hello.pack(side="top")

    @staticmethod
    def say_hi():
        print("Hello World")


window = Window()
window.mainloop()
