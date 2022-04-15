from msilib.schema import Font
import os, json
from datetime import datetime
from tkinter import *
from tkinter import ttk, font

from resources.scripts.formatImage import loadImage

# getting the staring time
time_load = datetime.now()
print(time_load)


# defining the directory path
curScriptDir = os.path.dirname(__file__).replace("\\", "/")
resourceDir = f"{curScriptDir}/resources"
imageDir = f"{resourceDir}/images"
dataDir = f"{resourceDir}/data"
scriptResourceDir = f"{resourceDir}/scripts"


# defining color 
colorMainBg = "White"
colorMainFg = "Black"


# defining the main window 
root = Tk()
root.title("Design Kit")
root.geometry("600x400")
rootIcon = loadImage(f"{imageDir}/rootIcon.png", (32, 32))
root.iconphoto(False, rootIcon)


# defining the fonts
fontEntry = font.Font(family="MS Serif", size=12)
fontLabel = font.Font(family="Helvetica", size=12,  slant=font.ITALIC)
fontButton = font.Font(family="Arial", size=12, weight=font.BOLD)
fontTextBox = font.Font(family="Times New Roman", size=11)


# defining the main frame
colorMainFrameBg = "#dddddd"
colorMainFrameFg = "#111111"
frameMain = Frame(root, bg=colorMainFrameBg, \
    highlightbackground=colorMainFrameBg, highlightcolor=colorMainFrameBg, bd=0, highlightthickness=0)
frameMain.pack(expand=True, fill="both", anchor=CENTER )


#defing the configuration frame
colorFrameConfigBg = "#eeeeee"
colorFrameConfigFg = "#111111"
frameConfig = Frame(root, bg=colorFrameConfigBg, \
    highlightbackground=colorFrameConfigBg, highlightcolor=colorFrameConfigBg, bd=0, highlightthickness=0)
frameConfig.pack(expand=True, fill="both", anchor=CENTER)



root.mainloop()