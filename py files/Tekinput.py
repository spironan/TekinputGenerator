# Copyright 2020 by Chua Teck Lee.
# All rights reserved.

import tkinter as tk
from tkinter import *

from tkinter import ttk
from tkinter.ttk import *

import copy
import webbrowser

import Utility
import Data


#INIT

#TK GUI
root = Tk()
root.title("Tekinput Generator")
root.geometry("1536x864")
#root.geometry("1280x720")
Utility.CentraliseWindow(root)
root.iconbitmap(Utility.MakePath(r'\..\Images\Logo\tkig.ico'))


#ttk style
style = ttk.Style()


#Various GUI Frames
DisplayFrame = ttk.Frame(root)
DisplayFrame.pack(pady = 10)

InputFrame = ttk.LabelFrame(root, text = "Inputs", padding = 10)
InputFrame.pack(pady = 10)

ButtonsFrame = ttk.Frame(root, padding = 10)
ButtonsFrame.pack()

#SupportFrame = ttk.LabelFrame(root, text = "Credits", padding = 10)
#SupportFrame.pack(pady = 5)
SupportFrame = ttk.LabelFrame(root, text = "Credits", padding = 20)
SupportFrame.pack(pady = 20)

########################VARIABLES###############################

save_path = r"\..\Images\Output"

preview_size = 32

inputBuffer = []

buttons = []

final_Images = {}

preview_Images = {}
proper_previews = {}

#Preload all Images Resized.
for element in Data.Inputs:
    f_im = Utility.MakeImage(element.filepath)
    final_Images[element.name] = f_im
    #Here I make a deepcopy, resize my opened image to preview_size and save into preview images
    p_im = copy.deepcopy(f_im)
    y = p_im.size[1]/preview_size
    x = p_im.size[0] / y
    preview_Images[element.name] = p_im.resize((32,32))
    p_im.thumbnail((x,preview_size))
    proper_previews[element.name] = p_im

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
    new_im = Utility.NewImage('RGBA', totalLength, final_Images[inputBuffer[0].name].size[1])
    
    currentLength = 0
    for i in range(0, len(inputBuffer), 1):
        new_im.paste(final_Images[inputBuffer[i].name], (currentLength, 0))
        currentLength += final_Images[inputBuffer[i].name].size[0]

    #saves the image onto the selected path
    new_im.save(Utility.MakePath(save_path + '\\' + generateFilename() + '.png'))

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

    totalLength = 0

    for i in range(0, len(inputBuffer), 1):
        totalLength += proper_previews[inputBuffer[i].name].size[0]

    #creates a new empty image, RGB mode, and size
    new_im = Utility.NewImage('RGBA', totalLength, preview_size)
    
    currentLength = 0
    for i in range(0, len(inputBuffer), 1):
        new_im.paste(proper_previews[inputBuffer[i].name], (currentLength, 0))
        currentLength += proper_previews[inputBuffer[i].name].size[0]
    
    photo = Utility.MakeTKImageWithImage(new_im)
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

def updateSelection():
   for element in buttons:
        if(element.characterList == None) : 
            continue
        elif(myCombo.get() == None) : 
            s = myCombo.get()
            element.btn.grid_remove()
        elif(myCombo.get() not in element.characterList) : 
            s = myCombo.get()
            element.btn.grid_remove()
        else : 
            element.btn.grid()

def updateSelectionCallback(event):
    updateSelection()

def scrollCanvas(event):
    comboCanvas.configure(scrollregion=comboCanvas.bbox("all"), width=1000, height=40)


#Tekinput Graphic Image Label
photo = Utility.MakeTKImage(r'\..\Images\Logo\TKIG.png',160,90)
label = ttk.Label(DisplayFrame, image = photo)
label.grid(row = 0, column = 0)


comboPreviewFrame = Labelframe(DisplayFrame, text = "Combo Preivew", width = 1000, height = 40)
comboPreviewFrame.grid(row = 0, column = 1)
comboPreviewFrame.grid_propagate(0)

comboCanvas=Canvas(comboPreviewFrame, width = 1000, height = 40)
comboFrame=Frame(comboCanvas)
myscrollbar=Scrollbar(comboPreviewFrame, orient = "horizontal", command=comboCanvas.xview)
comboCanvas.configure(xscrollcommand = myscrollbar.set)
myscrollbar.pack(side="bottom",fill="x")
comboCanvas.pack(side="bottom")
comboCanvas.create_window((0,0),window=comboFrame,anchor='nw')
comboFrame.bind("<Configure>",scrollCanvas)

#combo Preview label
style.configure('comboPreviewLabel.TLabel', width = 100, height = 50)
comboPreview = ttk.Label(comboFrame, 
style = 'comboPreviewLabel.TLabel')
comboPreview.grid(row = 0, column = 1)



#combo letters display label
style.configure('comboDisplayLabel.TLabel', width = 100, relief = SUNKEN, borderwidth = 200,)
comboDisplay = ttk.Label(DisplayFrame, textvariable = comboText,
style = 'comboDisplayLabel.TLabel')
comboDisplay.grid(row = 1, column = 1)

#print toggle
toggle = ttk.Checkbutton(DisplayFrame,
text = "Display Final Output", variable = displayFinalOutput)
toggle.grid(row = 2, column = 1)


#UI
style.configure('InputButton.TButton', background = 'black', borderwidth = 10)
class inputButton():
    def __init__ (self, root, element):
        #PHOTO OUTPUT
        self.photo = Utility.MakeTKImageWithImage(preview_Images[element.name])
        #BUTTON CREATION
        self.btn = ttk.Button(root, text = element.name, image = self.photo
        , command = lambda : addInput(element), style = 'InputButton.TButton'
        )
        
        self.btn.grid(
            row = element.buttonLayout[0],
            column = element.buttonLayout[1],
            padx = 3,
            pady = 10)

        self.characterList = element.characterList
        
for element in Data.Inputs:
    buttons.append(inputButton(InputFrame, element))


#Character Selection widgets and functions
charSelectLabel = ttk.Label(InputFrame, text = "Choose your character").grid(row = 0, column = 20)

myCombo = ttk.Combobox(InputFrame, value = Data.characters)
updateSelection()
myCombo.bind("<<ComboboxSelected>>", updateSelectionCallback)
myCombo.grid(row = 1, column = 20)

###TEMP CODE###
for element in buttons:
        if(element.characterList == None) : 
            continue
        
        element.btn.grid_remove()
###TEMP CODE###

#GENERATE, CLEAR, ERASE Buttons
generatePhoto = Utility.MakeTKImage(r'\..\Images\Logo\Generate.png',162,50)
clearPhoto = Utility.MakeTKImage(r'\..\Images\Logo\Clear.png',125,50)
erasePhoto = Utility.MakeTKImage(r'\..\Images\Logo\Erase.png',125,50)

generateBtn = ttk.Button(ButtonsFrame, text = "Generate", 
command = generateImage
, image = generatePhoto
)

clearBtn = ttk.Button(ButtonsFrame, text = "Clear", 
command = clear
, image = clearPhoto
)
eraseBtn = ttk.Button(ButtonsFrame, text = "Erase",
command = erase
, image = erasePhoto
)

generateBtn.grid(row = 0, column = 0, padx = 0)
clearBtn.grid(row = 0, column = 1, padx = 100)
eraseBtn.grid(row = 0, column = 2, padx = 0)

#credits
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def callback(url):
    webbrowser.get(using = 'chrome').open(url,new = 2)


style.configure('support.TLabel', font = ("Helvetica", 16, "bold"))
link = ttk.Label(SupportFrame, text="Buy me coffee?", foreground ="blue", cursor="hand2", style = 'support.TLabel')
link.grid(row = 0, column = 1)
link.bind("<Button-1>", lambda e: callback("paypal.me/chuatecklee"))


Version = ttk.Label(SupportFrame, 
text="Tekinput Generator Release V1.0", foreground="black")
Version.grid(row = 1, column = 1)

shoutout = ttk.Label(SupportFrame, 
text="Graphics & Images provided by Duke_KC ", foreground="black", cursor="hand2")
shoutout.grid(row = 2, column = 1)
shoutout.bind("<Button-1>", lambda e: callback("https://twitter.com/DukeKC_"))

CopyrightNotice = ttk.Label(SupportFrame, 
text="(C)Product of Chua Teck Lee, all rights reserved", foreground="black", cursor="hand2")
CopyrightNotice.grid(row = 3, column = 1)
CopyrightNotice.bind("<Button-1>", lambda e: callback("https://twitter.com/chuatecklee"))

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
