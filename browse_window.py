# Author: Ben Prince
# Version: 1.2
# Description: Window used to browse for a file

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import xlwt
import patient_main as pm
import pathlib


class Window(Tk):

    filename = ""

    def __init__(self):
        super(Window, self).__init__()
        self.run = ttk.Button(self)
        self.browse = ttk.Button(self)
        self.title("Test Patient Generator")
        self.minsize(430, 300)
        self.add_buttons()

    def add_buttons(self):
        self.run["text"] = "run"
        self.run["command"] = self.run_program
        self.run.pack(side="top")
        self.browse["text"] = "Browse"
        self.browse["command"] = self.browse_files
        self.browse.pack(side="top")

    @staticmethod
    def run_program():
        print("Hello World")
        global filename
        try:
            new_file = pm.patients(filename)
            folder_select = filedialog.askdirectory()
            num = ""
            save_path = folder_select + '/patients' + num + '.xls'

            while pathlib.Path(save_path).is_file():
                if num == "":
                    num = 0
                num = str(int(num) + 1)
                save_path = folder_select + '/patients' + num + '.xls'

            new_file.save(save_path)

        except NameError:
            print("No File Selected")

    @staticmethod
    def browse_files():
        global filename
        filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("Excel Files", "*.xlsx *.xls *.xlsm *.xlsb *.csv"), ("all files", "*.*")))
        print(filename)



window = Window()
window.mainloop()
