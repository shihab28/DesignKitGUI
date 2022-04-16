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



class CREATE_CONFIG():
    def __init__(self, canvasFrame):
        self.canvasFrame = canvasFrame
        self.libraryPath = ''
        self.switchSettings = ''
        self.outputFileName = ''

        self.colorFrameBg = "#FFF6E9"

        self.colorActiveBg = "#FFF6E9"
        self.colorInactiveBg = "#F6F9F9"
        self.colorActiveFg = "Black"
        self.colorInactiveFg = "Gray"

        self.iconOpenFile = loadImage(f"{imageDir}/folderOpenGreen.png", (24,24))



        self.createButtons()
        self.createFrame()

        

    

    def createButtons(self):
        self.buttonCreateConfig = Button(self.canvasFrame, text="Create Config", bg=self.colorActiveBg, command= lambda eve = self : self.buttonCreateConfigClicked(), \
            highlightthickness=0, highlightbackground=self.colorActiveBg, border=0, borderwidth=0, font=fontButton)
        relx=122; rely=151; relwidth=135; relheight=33; pad=-1
        self.canvasFrame.create_window((relx, rely), anchor=NW, window=self.buttonCreateConfig, tags="self.buttonCreateConfig", width=relwidth, height=relheight)

        self.buttonLoadConfig = Button(self.canvasFrame, text="Load Config", bg=self.colorInactiveBg, command= lambda eve = self : self.buttonLoadConfigClicked(), \
            highlightthickness=0, highlightbackground=self.colorInactiveBg, border=0, borderwidth=0, font=fontButton)
        relx=relx+relwidth+pad; 
        self.canvasFrame.create_window((relx, rely), anchor=NW, window=self.buttonLoadConfig, tags="self.buttonLoadConfig", width=relwidth, height=relheight)

    def buttonCreateConfigClicked(self):
        self.dehighlightButton()
        self.buttonCreateConfig.configure(bg=self.colorActiveBg, highlightbackground=self.colorActiveBg)
        self.placeFrameCreateConfig()

    def buttonLoadConfigClicked(self):
        self.dehighlightButton()
        self.buttonLoadConfig.configure(bg=self.colorActiveBg, highlightbackground=self.colorActiveBg)
        self.placeFrameLoadConfig()

    def dehighlightButton(self):
        self.frameCreateConfig.place_forget()
        self.frameLoadConfig.place_forget()
        self.buttonCreateConfig.configure(bg=self.colorInactiveBg, highlightbackground=self.colorInactiveBg)
        self.buttonLoadConfig.configure(bg=self.colorInactiveBg, highlightbackground=self.colorInactiveBg)
        


    def placeFrameCreateConfig(self):
        relx=111; rely=181; relheight=180; relwidth=570; pad = 10
        self.canvasFrame.create_window((relx+pad, rely+pad), anchor=NW, window=self.frameCreateConfig, tags="self.frameCreateConfig", width=relwidth-pad, height=relheight-pad)
    
    def placeFrameLoadConfig(self):
        relx=111; rely=181; relheight=180; relwidth=570; pad = 10
        self.canvasFrame.create_window((relx+pad, rely+pad), anchor=NW, window=self.frameLoadConfig, tags="self.frameLoadConfig", width=relwidth-pad, height=relheight-pad)


    def createFrame(self):

        self.frameLoadConfig = Frame(self.canvasFrame, bg=self.colorFrameBg)
        self.placeFrameLoadConfig()
        self.frameLoadConfig.place_forget()

        self.frameCreateConfig = Frame(self.canvasFrame, bg=self.colorFrameBg)
        relx=111; rely=181; relheight=180; relwidth=570; pad = 10
        self.placeFrameCreateConfig()

        self.frameLabelEntry = Frame(self.frameCreateConfig, bg=self.colorFrameBg, \
            highlightthickness=0, highlightbackground=self.colorFrameBg, border=0, borderwidth=0)
        self.frameLabelEntry.pack(expand=True, fill="both")
        self.frameButtonConfig = Frame(self.frameCreateConfig, bg=self.colorFrameBg, \
            highlightthickness=0, highlightbackground=self.colorFrameBg, border=0, borderwidth=0)
        self.frameButtonConfig.pack(expand=True, fill="both")


        self.labelLibraryPath = Label(self.frameLabelEntry, text='Library Path', bg=self.colorFrameBg, \
            highlightthickness=0, highlightbackground=self.colorActiveBg, border=0, borderwidth=0)
        self.labelLibraryPath.grid(row=0, column=0, sticky=E, pady=10)
        self.entryLibraryPath = Entry(self.frameLabelEntry, width=70)
        self.entryLibraryPath.grid(row=0, column=1, padx=(5, 2),sticky=EW, pady=10)
        self.buttonLibraryPath = Button(self.frameLabelEntry, image=self.iconOpenFile, \
            highlightthickness=0, highlightbackground=self.colorActiveBg, border=0, borderwidth=0)
        self.buttonLibraryPath.grid(row=0, column=2, sticky=W, pady=10)


        self.labelSwitchSettings = Label(self.frameLabelEntry, text='Switch Settings', bg=self.colorFrameBg,  \
            highlightthickness=0, highlightbackground=self.colorFrameBg, border=0, borderwidth=0)
        self.labelSwitchSettings.grid(row=1, column=0, sticky=E, pady=10)
        self.entrySwitchSettings = Entry(self.frameLabelEntry, width=70)
        self.entrySwitchSettings.grid(row=1, column=1, padx=(5, 2),sticky=EW, pady=10)
        self.buttonSwitchSettings = Button(self.frameLabelEntry, image=self.iconOpenFile, \
            highlightthickness=0, highlightbackground=self.colorActiveBg, border=0, borderwidth=0)
        self.buttonSwitchSettings.grid(row=1, column=2, sticky=W, pady=10)


        self.labelOutputFileName = Label(self.frameLabelEntry, text='Output File Name', bg=self.colorFrameBg, \
            highlightthickness=0, highlightbackground=self.colorFrameBg, border=0, borderwidth=0)
        self.labelOutputFileName.grid(row=2, column=0, sticky=E, pady=10)
        self.entryOutputFileName = Entry(self.frameLabelEntry, width=7)
        self.entryOutputFileName.grid(row=2, column=1, columnspan=2, padx=(5, 2), sticky=EW, pady=10)

        self.frameLabelEntry.columnconfigure(0, weight=2)
        self.frameLabelEntry.columnconfigure(1, weight=5)
        self.frameLabelEntry.columnconfigure(2, weight=1)


        self.buttonCreateCreateConfig = Button(self.frameButtonConfig, text="Create", bg=self.colorInactiveBg, state='disabled', \
             highlightthickness=0, highlightbackground=self.colorActiveBg, border=0, borderwidth=0, font=("Helvetica", 12, font.BOLD))
        self.buttonCreateCreateConfig.pack(expand=True, fill="x")













# defining color 

colorMainBg = "#F6F9F9" # Gray
colorMainBg1 = "#FFF6E9" # Ghiya
colorMainFg = "Black"


# defining the main window 
root = Tk()
root.title("Design Kit")
rootWidth = 800
rootHight = 550
root.geometry(f"{rootWidth}x{rootHight}")
root.resizable(False, False)
rootIcon = loadImage(f"{imageDir}/rootIcon.png", (32, 32))
root.iconphoto(False, rootIcon)


# defining the fonts
fontEntry = font.Font(family="MS Serif", size=11)
fontLabel = font.Font(family="Helvetica", size=11,  slant=font.ITALIC)
fontButton = font.Font(family="Arial", size=11, weight=font.BOLD)
fontTextBox = font.Font(family="Times New Roman", size=11)


canvasMain = Canvas(root, background=colorMainBg)
canvasMain.pack(expand=True, fill="both", anchor=CENTER)

startingWindowBg = loadImage(f"{imageDir}/startingWindowBg1.png", (800, 550))
canvasMain.create_image(rootWidth//2, rootHight//2, image=startingWindowBg)

# frameLeft = Frame(canvasMain, background=colorMainBg1, width=100, height=550)
# frameLeft.pack(expand=False, fill="y", side=LEFT)

# frameMain = Frame(canvasMain, bg=colorMainBg, width=600, height=550, \
#     highlightbackground=colorMainBg, highlightcolor=colorMainBg, bd=0, highlightthickness=0)
# frameMain.pack(expand=True, fill="both", side=LEFT)

# frameRight = Frame(canvasMain, background=colorMainBg1, width=100, height=550)
# frameRight.pack(expand=False, fill="y", side=RIGHT)


configClass = CREATE_CONFIG(canvasFrame=canvasMain)
# canvasMain.place()




root.mainloop()