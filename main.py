from os.path import basename, splitext
import tkinter as tk
from tkinter import HORIZONTAL, Canvas, Entry, StringVar
# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Color Mish Mash"
    length = 333

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self. varR = StringVar()
        self.varR.set(0)
        self.varR.trace("w", self.entryUpdate)
        self.entryR = Entry(textvariable = self.varR)
        self.entryR.pack()
        self.scaleR = tk.Scale (from_=0, to=255, orient=HORIZONTAL,background = "#ff0000",command = self.change ,length=self.length)
        self.scaleR.pack()

        self.scaleG = tk.Scale (from_=0, to=255, orient=HORIZONTAL, background = "#00ff00",command = self.change, length=self.length)
        self.scaleG.pack()

        self.scaleB = tk.Scale (from_=0, to=255, orient=HORIZONTAL, background = "#0000ff", command = self.change,length=self.length)
        self.scaleB.pack()

        self.canvas = Canvas(background = "#000000")
        self.canvas.pack()

        self.varColor = StringVar()
        self.entryColor = Entry(textvariable = self.varColor, width = 7)
        self.entryColor.pack()

    
    
    def entryUpdate(self, name, index, operations):
        r = self.varR.get()
        if r.isdigit():
            r = int(r)
        else:
            self.varR.set(0)
            r =0
        self.scaleR.set(r)
    
        
    
    
    def change(self , event):
        r = self.scaleR.get()
        self.varR.set(r)
        g = self.scaleG.get()
        b = self.scaleB.get()
        hashcolor = "#%02x%02x%02x" % (r, g, b)
        print(hashcolor) 
        self.canvas.config(background = hashcolor)
        self.varColor.set(hashcolor)



    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
