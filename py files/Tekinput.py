# Copyright 2020 by Chua Teck Lee.
# All rights reserved.

import tkinter as tk
from tkinter import *
#from tkinter import filedialog
#from tkinter import font as tkFont  # for convenience

from tkinter import ttk
from tkinter.ttk import *

import PIL
from PIL import ImageTk,Image

import pathlib
import copy
import webbrowser

import Data

#INIT

#set current file directory
directory = pathlib.Path(__file__).parent.absolute()

def makePath(relative_path) :
    #try:
        #base_path = sys._MEIPASS # pylint: disable=no-member
        #base_path = directory.absolute()
    #except Exception:
    #    base_path = os.path.abspath(".")

    #return os.path.join(base_path, relative_path)
    return r"{}{}".format(directory.absolute(), relative_path)

#Centralizing Window to middle of one Screen
def centraliseWindow(window):
    window.update_idletasks()

    # Tkinter way to find the screen resolution
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # PyQt way to find the screen resolution
    #app = QtGui.QApplication([])
    #screen_width = app.desktop().screenGeometry().width()
    #screen_height = app.desktop().screenGeometry().height()

    size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
    x = screen_width/2 - size[0]/2
    y = screen_height/2 - size[1]/2

    window.geometry("+%d+%d" % (x, y))

#TK GUI
root = Tk()
root.title("Tekinput Generator BETA V1.2")
root.geometry("900x600")
centraliseWindow(root)
root.iconbitmap(makePath(r'\..\Images\Logo\tkig.ico'))

#ttk style
style = ttk.Style()

#Various GUI Frames
DisplayFrame = ttk.LabelFrame(root, text = "Display")
DisplayFrame.pack(pady = 10)

InputFrame = ttk.LabelFrame(root, text = "Inputs", padding = 50)
InputFrame.pack(pady = 10)

# MovementLabel = ttk.Label(InputFrame, text = "Movement")
# MovementLabel.grid()

# AttackLabel = ttk.Label(InputFrame, text = "Attack")
# AttackLabel.grid()

# StateLabel = ttk.Label(InputFrame, text = "State")
# StateLabel.grid()

# SpecialLabel = ttk.Label(InputFrame, text = "Special")
# SpecialLabel.grid()


ButtonsFrame = ttk.Frame(root, padding = 10)
ButtonsFrame.pack()

SupportFrame = ttk.LabelFrame(root, text = "Credits", padding = 20)
SupportFrame.pack(pady = 30,side = BOTTOM)

########################VARIABLES###############################

save_path = r"\..\Images\Output"

preview_size = 32

inputBuffer = []

buttons = []

final_Images = {}

preview_Images = {}

#Preload all Images Resized.
for element in Data.Inputs:
    f_im = Image.open(makePath(element.filepath))
    final_Images[element.name] = f_im
    #Here I make a deepcopy, resize my opened image to preview_size and save into preview images
    p_im = copy.deepcopy(f_im)
    p_im.thumbnail((preview_size, preview_size))
    preview_Images[element.name] = p_im

comboText = tk.StringVar()
comboText.set("Combo Output")

displayFinalOutput = BooleanVar()
displayFinalOutput.set(TRUE)

#FUNCTIONS

def generateImage() :

    if(len(inputBuffer) == 0) :
        return
   
    totalLength = 0

    for i in range(0, len(inputBuffer), 1):
        totalLength += final_Images[inputBuffer[i].name].size[0]

    #creates a new empty image, RGB mode, and size
    new_im = Image.new('RGBA', (totalLength, final_Images[inputBuffer[0].name].size[1]))
    
    currentLength = 0
    for i in range(0, len(inputBuffer), 1):
        new_im.paste(final_Images[inputBuffer[i].name], (currentLength, 0))
        currentLength += final_Images[inputBuffer[i].name].size[0]

    #saves the image onto the selected path
    new_im.save(makePath(save_path + '\\' + generateFilename() + '.png'))

    #display the finished product if bool is true
    if(displayFinalOutput.get()):
        new_im.show()

def generateFilename():

    text = ""
    for input in inputBuffer :
        text += input.fileDisplay

    return text

def generateText():
    
    if(len(inputBuffer) == 0):
         comboText.set("Combo Output")
    else:
        text = ""
    
        for input in inputBuffer :
            text += input.display

        comboText.set(text)

def generatePreview() :

    if(len(inputBuffer) == 0) :
        comboPreview.configure(image = None)
        comboPreview.image = None
        return

    lengthX = preview_size * len(inputBuffer)
    lengthY = preview_size

    #creates a new empty image, RGB mode, and size.
    new_im = Image.new('RGBA', (lengthX, lengthY))
    
    for i in range(0, len(inputBuffer), 1):
        new_im.paste(preview_Images[inputBuffer[i].name], (i * preview_size, 0))
    
    photo = ImageTk.PhotoImage(new_im)
    comboPreview.configure(image = photo)
    comboPreview.image = photo

def addInput(input) :
    inputBuffer.append(input)
    generateText()
    generatePreview()

def clear():
    
    if(len(inputBuffer) == 0) : 
        return None

    inputBuffer.clear()
    generateText()
    generatePreview()

def erase():

    if(len(inputBuffer) == 0) : 
        return None

    inputBuffer.pop()
    generateText()
    generatePreview()


#UI
style.configure('InputButton.TButton', background = 'black', borderwidth = 10)
class inputButton():
    def __init__ (self, root, element):
        #PHOTO OUTPUT
        self.photo = ImageTk.PhotoImage(preview_Images[element.name])
        #BUTTON CREATION
        self.btn = ttk.Button(root, text = element.name, image = self.photo
        , command = lambda : addInput(element), style = 'InputButton.TButton'
        )
        self.btn.grid(
            row = element.buttonLayout[0],
            column = element.buttonLayout[1],
            padx = 3,
            pady = 10)
        
for element in Data.Inputs:
    #if(element.character == "None") : 
    buttons.append(inputButton(InputFrame, element))

#unique button widget

#combo image preview label


# characterList = [
#     "Choose your character",
#     "Akuma",
#     "Alisa",
#     "Claudio",
#     "Eliza",
# ]
# v = tk.StringVar()
# v.set(characterList[0])
# om = tk.OptionMenu(InputFrame, v, *characterList)
# om.grid(row = 0, column = 20)

#v = tk.StringVar()
#v.set(characterList[0])


#def updateSelect(event):
#   if(charSelectLabel == ):
#        charSelectLabel = ttk.Label(InputFrame, text = characterList[0]).grid(row = 0, column = 20)

#def updateSelect(event):
    #myLabel = Label(InputFrame, text = myCombo.get()).grid(row = 0, column = 20)

myCombo = ttk.Combobox(InputFrame, value = Data.characters)
myCombo.current(0)

charSelectLabel = ttk.Label(InputFrame, text = "Choose your character").grid(row = 0, column = 20)
#def updateSelect(event):
#    charSelectLabel.text = myCombo.get()
#myCombo.bind("<<ComboBoxSelected>>", updateSelect)
myCombo.grid(row = 1, column = 20)




style.configure('comboPreviewLabel.TLabel', width = 100, height = 50)
comboPreview = ttk.Label(DisplayFrame, 
style = 'comboPreviewLabel.TLabel')
comboPreview.pack()

#combo letters display label
style.configure('comboDisplayLabel.TLabel', width = 100, relief = SUNKEN, borderwidth = 200,)
comboDisplay = ttk.Label(DisplayFrame, textvariable = comboText,
style = 'comboDisplayLabel.TLabel')
comboDisplay.pack()

#print toggle
toggle = ttk.Checkbutton(DisplayFrame,
text = "Display Final Output", variable = displayFinalOutput)
toggle.pack()



#GENERATE, CLEAR, ERASE Buttons
style.configure('generateBtn.TButton', 
font = ("Helvetica", 24, "bold"), background = 'green', foreground = 'green')
style.configure('clearBtn.TButton', 
font = ("Helvetica", 24, "bold"), background = 'red', foreground = 'red')
style.configure('eraseBtn.TButton', 
font = ("Helvetica", 24, "bold"), background = 'orange', foreground = 'orange')

generateBtn = ttk.Button(ButtonsFrame, text = "Generate", 
command = generateImage, style = 'generateBtn.TButton')
clearBtn = ttk.Button(ButtonsFrame, text = "Clear",
command = clear, style = 'clearBtn.TButton')
eraseBtn = ttk.Button(ButtonsFrame, text = "Erase",
command = erase, style = 'eraseBtn.TButton')

generateBtn.grid(row = 0, column = 0, padx = 0)
clearBtn.grid(row = 0, column = 1, padx = 100)
eraseBtn.grid(row = 0, column = 2, padx = 0)

#credits
photo = ImageTk.PhotoImage(Image.open(makePath(r'\..\Images\Logo\TKIG.png')).resize((192, 100)))
label = ttk.Label(SupportFrame, image = photo)
label.grid(row = 1, column = 1)

chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def callback(url):
    webbrowser.get(using = 'chrome').open(url,new = 2)

link = ttk.Label(SupportFrame, text="Buy me tea", foreground ="blue", cursor="hand2")
link.grid(row = 0, column = 0)
link.bind("<Button-1>", lambda e: callback("paypal.me/chuatecklee"))

CopyrightNotice = ttk.Label(SupportFrame, 
text="(C)Product of Chua Teck Lee, all rights reserved", foreground="black")
CopyrightNotice.grid(row = 1, column = 0)

root.mainloop()














'''
def setImage(name):
    #filedialog
    filepath = filedialog.askopenfilename(
        initialdir = "",
        title = "Select file for" + name,
        filetypes = (("png files", "*.png"),("jpg files", "*.jpg"),("svg files", "*.svg"), ("all files", "*.*"))
        )
    Data.Inputs[name].filepath = filepath


def setSaveFileDir(name):
    #filedialog
    filepath = filedialog.askopenfilename(
        initialdir = "",
        title = "Select file for" + name,
        filetypes = (("png files", "*.png"),("jpg files", "*.jpg"),("svg files", "*.svg"), ("all files", "*.*"))
        )
    Data.Inputs[name].filepath = filepath


e = Entry(root, width = 50, borderwidth = 5)
e.pack()
e.insert(0, "Enter Your Name")

def myClick() :
   myLabel = Label(root, text = e.get())
   myLabel.pack()

'''
