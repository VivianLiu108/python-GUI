from tkinter import *
import time

class change_title:
    def __init__(self, name):
        self.counter = 0
        self.__name__ = name
    def __call__(self):
        global label
        label.config(text = str(self.counter))
        self.counter = (self.counter + 1)
        label.after(1000, self)
f = change_title("f")  #self.__name__ = f

root = Tk()
root.title("init")
label = Label(root, text = "origine")
label.pack()
label.after(1000, f)

root.mainloop()