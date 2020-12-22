# Author: Ben Prince
# Version: 1.2
# Description: Window used to browse for a file

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import xlwt
import patient_main as pm
import pathlib


class Window(Tk):

    filename = ""

    def __init__(self):
        super(Window, self).__init__()
        self.run = ttk.Button(self)
        self.browse = ttk.Button(self)
        self.instruction = ttk.Label(self)
        self.fileLoc = ttk.Label(self)
        self.image = PhotoImage(file="example.png")
        self.examplePic = Label(self, image=self.image)
        self.examplePic.place(x=295, y=40)
        self.exampleInstructions = ttk.Label(self)
        self.title("Test Patient Generator v1.2")
        self.minsize(550, 300)
        self.resizable(0,0)
        self.add_buttons()

    def add_buttons(self):
        self.run["text"] = "run"
        self.run["command"] = lambda: self.run_program()
        self.run.pack(side="bottom")
        self.browse["text"] = "Browse"
        self.browse["command"] = lambda: self.browse_files()
        self.browse.pack(side="bottom")
        self.instruction["text"] = "Welcome!\n"\
                                    "Browse for a file then select Run to\n"\
                                    "generate the test patient file. Select\n"\
                                    "a save location and go there to see the\n"\
                                    "generated file.\n\n"\
                                    "A few things to Note:\n"\
                                    "- Time is currently in minutes (input and output)\n"\
                                    "- Undiffernetiated can be anything (Unknown, etc)\n"\
                                    "- All three sex types need to have normal casing\n"\
                                    "- The first row is skipped, it is assumed to be\n"\
                                    "  a header row for each column."
        self.instruction.place(x=20, y=20)
        self.exampleInstructions["text"] = "Please format data as shown here:"
        self.exampleInstructions.place(x=300, y=20)

    def run_program(self):
        global filename
        try:
            new_file = pm.get_patients_wb(filename)
            folder_select = filedialog.askdirectory()
            num = ""
            save_path = folder_select + '/patients' + num + '.xls'

            while pathlib.Path(save_path).is_file():
                if num == "":
                    num = 0
                num = str(int(num) + 1)
                save_path = folder_select + '/patients' + num + '.xls'

            new_file.save(save_path)
            self.fileLoc["text"] = "Success!"
            self.fileLoc.place(x=20, y=220)
        except NameError:
            self.fileLoc["text"] = "Please Select a File"
            self.fileLoc.place(x=20, y=220)

    def browse_files(self):
        global filename
        filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("Excel Files", "*.xlsx *.xls *.xlsm *.xlsb *.csv"), ("all files", "*.*")))
        self.fileLoc["text"] = filename
        self.fileLoc.place(x=20, y=220)
