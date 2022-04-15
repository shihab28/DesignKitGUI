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

colorMainBg = "#F6F9F9" # Gray
colorMainBg1 = "#FFF6E9" # Ghiya
colorMainFg = "Black"


# defining the main window 
root = Tk()
root.title("Design Kit")
root.geometry("800x550")
root.resizable(False, False)
rootIcon = loadImage(f"{imageDir}/rootIcon.png", (32, 32))
root.iconphoto(False, rootIcon)


# defining the fonts
fontEntry = font.Font(family="MS Serif", size=12)
fontLabel = font.Font(family="Helvetica", size=12,  slant=font.ITALIC)
fontButton = font.Font(family="Arial", size=12, weight=font.BOLD)
fontTextBox = font.Font(family="Times New Roman", size=11)


canvasMain = Canvas(root, background=colorMainBg)
canvasMain.pack(expand=True, fill="both", anchor=CENTER)

startingWindowBg = loadImage(f"{imageDir}/startingWindowBg.png", (800, 550))
canvasMain.create_image(0, 0, image=startingWindowBg)

frameLeft = Frame(canvasMain, background=colorMainBg1, width=100, height=550)
frameLeft.pack(expand=True, fill="both", side=LEFT)

# frameMain = Frame(canvasMain, bg=colorMainBg, width=600, height=550, \
#     highlightbackground=colorMainBg, highlightcolor=colorMainBg, bd=0, highlightthickness=0)
# frameMain.pack(expand=True, fill="both", side=LEFT)

frameRight = Frame(canvasMain, background=colorMainBg1, width=100, height=550)
frameRight.pack(expand=True, fill="both", side=LEFT)




# defining the main frame





root.mainloop()