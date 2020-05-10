
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

#TK GUI
root = Tk()
root.title("TTK Styling")
root.geometry("900x600+600+150")


style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")

l1.pack()
l2.pack()



root.mainloop()