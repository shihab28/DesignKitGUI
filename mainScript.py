import os, json
from datetime import datetime
from tkinter import *
from tkinter import ttk, font

from resources.scripts.formatImage import loadImage

# getting the staring time
time_load = datetime.now()
print("Starting at : ", time_load)


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

        self.colorMainBg = "#F6F9F9"
        self.colorFrameBg = "#FFF6E9"
        self.colorHighlight = "#2A7FFF"
        self.colorActiveBg = "#FFF6E9"
        self.colorInactiveBg = "#F6F9F9"
        self.colorActibeButtonBg = "#AAFFAA"
        self.colorActibeButtonFg = "Black"
        self.colorActiveFg = "Black"
        self.colorInactiveFg = "Gray"

        self.iconOpenFile = loadImage(f"{imageDir}/folderOpenGreen.png", (20,20))
        self.mainFrameList = []

        self.navigationButtonSeq = ['load', 'create']
        # self.navigationButtonSeq = ['create', 'load']

        self.createButtons()
        self.createFrame()


    def createButtons(self):
        
        if  self.navigationButtonSeq == ['load', 'create']:
            self.buttonLoadConfig = Button(self.canvasFrame, text="Load Config", bg=self.colorInactiveBg, command= lambda eve = self : self.buttonLoadConfigClicked(), \
                highlightthickness=0, highlightbackground=self.colorInactiveBg, border=0, borderwidth=0, font=fontButtonNormal)
            relx=122; rely=151; relwidth=135; relheight=33; pad=-1        
            self.canvasFrame.create_window((relx, rely), anchor=NW, window=self.buttonLoadConfig, tags="self.buttonLoadConfig", width=relwidth, height=relheight)

            self.buttonCreateConfig = Button(self.canvasFrame, text="Create Config", bg=self.colorActiveBg, command= lambda eve = self : self.buttonCreateConfigClicked(), \
                highlightthickness=0, highlightbackground=self.colorActiveBg, border=0, borderwidth=0, font=fontButtonNormal)
            relx=relx+relwidth+pad; 
            self.canvasFrame.create_window((relx, rely), anchor=NW, window=self.buttonCreateConfig, tags="self.buttonCreateConfig", width=relwidth, height=relheight)
        
        else:
            self.buttonCreateConfig = Button(self.canvasFrame, text="Create Config", bg=self.colorActiveBg, command= lambda eve = self : self.buttonCreateConfigClicked(), \
                highlightthickness=0, highlightbackground=self.colorActiveBg, border=0, borderwidth=0, font=fontButtonNormal)
            relx=122; rely=151; relwidth=135; relheight=33; pad=-1          
            self.canvasFrame.create_window((relx, rely), anchor=NW, window=self.buttonCreateConfig, tags="self.buttonCreateConfig", width=relwidth, height=relheight)

            self.buttonLoadConfig = Button(self.canvasFrame, text="Load Config", bg=self.colorInactiveBg, command= lambda eve = self : self.buttonLoadConfigClicked(), \
                highlightthickness=0, highlightbackground=self.colorInactiveBg, border=0, borderwidth=0, font=fontButtonNormal)
            relx=relx+relwidth+pad;       
            self.canvasFrame.create_window((relx, rely), anchor=NW, window=self.buttonLoadConfig, tags="self.buttonLoadConfig", width=relwidth, height=relheight)

            

        
        

    def buttonCreateConfigClicked(self):
        self.dehighlightNavigationButton()
        self.buttonCreateConfig.configure(bg=self.colorActiveBg, highlightbackground=self.colorActiveBg, font=fontButtonBold)
        self.canvasFrame.itemconfigure(self.frameCreateConfigID, state="normal")

    def buttonLoadConfigClicked(self):
        self.dehighlightNavigationButton()
        self.buttonLoadConfig.configure(bg=self.colorActiveBg, highlightbackground=self.colorActiveBg, font=fontButtonBold)
        self.canvasFrame.itemconfigure(self.frameLoadConfigID, state="normal")

    def dehighlightNavigationButton(self):
        self.buttonCreateConfig.configure(bg=self.colorInactiveBg, highlightbackground=self.colorInactiveBg, font=fontButtonNormal)
        self.buttonLoadConfig.configure(bg=self.colorInactiveBg, highlightbackground=self.colorInactiveBg, font=fontButtonNormal)
        for frm in self.mainFrameList:
            self.canvasFrame.itemconfigure(frm, state="hidden")
        

    def placeFrameCreateConfig(self):
        relx=111; rely=181; relwidth=570; relheight=180; pad = 10
        self.frameCreateConfigID = self.canvasFrame.create_window((relx+pad, rely+pad), anchor=NW, window=self.frameCreateConfig, tags="self.frameCreateConfig", width=relwidth-pad, height=relheight-pad)
        self.mainFrameList.append(self.frameCreateConfigID)
        
    
    def placeFrameLoadConfig(self):
        relx=111; rely=181; relwidth=570; relheight=180; pad = 10
        self.frameLoadConfigID = self.canvasFrame.create_window((relx+pad, rely+pad), anchor=NW, window=self.frameLoadConfig, tags="self.frameLoadConfig", width=relwidth-pad, height=relheight-pad)
        self.mainFrameList.append(self.frameLoadConfigID)

    def placeFrameForward(self):
        relx=700; rely=225; relwidth=100; relheight=200; pad = 0
        self.frameForwardID = self.canvasFrame.create_window((relx+pad, rely+pad), anchor=NW, window=self.frameForward, tags="self.frameForward", width=relwidth-pad, height=relheight-pad)
        self.mainFrameList.append(self.frameLoadConfigID)

    def placeFrameBackward(self):
        relx=0; rely=225; relwidth=100; relheight=200; pad = 0
        self.frameBackwardID = self.canvasFrame.create_window((relx+pad, rely+pad), anchor=NW, window=self.frameBackward, tags="self.frameBackward", width=relwidth-pad, height=relheight-pad)
        self.mainFrameList.append(self.frameLoadConfigID)
        

    def createFrame(self):

        self.frameCreateConfig = Frame(self.canvasFrame, bg=self.colorFrameBg)
        self.placeFrameCreateConfig()

        self.frameLoadConfig = Frame(self.canvasFrame, bg=self.colorFrameBg)
        self.placeFrameLoadConfig()

        # colorMainBg
        self.frameForward = Frame(self.canvasFrame, bg=self.colorMainBg)
        self.placeFrameForward()

        self.iconForwardActive = loadImage(f"{imageDir}/forward_green_1024.png", (64,128))
        self.iconForwardInactive = loadImage(f"{imageDir}/forward_gray_1024.png", (64,128))
        self.forwardButton = Button(self.frameForward, bg = self.colorMainBg, \
             highlightthickness=0, highlightbackground=self.colorMainBg, border=0, borderwidth=0)
        self.forwardButton.config(image=self.iconForwardActive, state='normal')
        self.forwardButton.config(image=self.iconForwardInactive, state='disabled')
        self.forwardButton.pack(anchor=CENTER)  

        self.frameBackward = Frame(self.canvasFrame, bg=self.colorMainBg)
        self.placeFrameBackward()
        self.iconBackwardActive = loadImage(f"{imageDir}/backward_green_1024.png", (64,128))
        self.iconBackwardInactive = loadImage(f"{imageDir}/backward_gray_1024.png", (64,128))
        self.backwardButton = Button(self.frameBackward, bg = self.colorMainBg, \
             highlightthickness=0, highlightbackground=self.colorMainBg, border=0, borderwidth=0, disabledforeground=self.colorMainBg)
        self.backwardButton.config(image=self.iconBackwardInactive, state='disabled')
        # self.backwardButton.config(image=self.iconBackwardActive, state='normal')
        self.backwardButton.pack(anchor=CENTER)
        self.backwardButton.pack_forget()
        # self.colorFrameBg = "Yellow"


        self.frameLabelEntry = Frame(self.frameCreateConfig, bg=self.colorFrameBg, \
            highlightthickness=0, highlightbackground=self.colorFrameBg, border=0, borderwidth=0)
        self.frameLabelEntry.pack(expand=True, fill="both")
        self.frameButtonConfig = Frame(self.frameCreateConfig, bg=self.colorFrameBg, \
            highlightthickness=0, highlightbackground=self.colorFrameBg, border=0, borderwidth=0)
        self.frameButtonConfig.pack(expand=False, fill="x")

        self.frameLabelEntry.columnconfigure(0, weight=2)
        self.frameLabelEntry.columnconfigure(1, weight=5)
        self.frameLabelEntry.columnconfigure(2, weight=1)
        self.frameLabelEntry.rowconfigure(0, weight=1)
        self.frameLabelEntry.rowconfigure(1, weight=1)
        self.frameLabelEntry.rowconfigure(2, weight=1)


        self.labelLibraryPath = Label(self.frameLabelEntry, text='Library Path', bg=self.colorFrameBg, \
            highlightthickness=0, highlightbackground=self.colorActiveBg, border=0, borderwidth=0)
        self.labelLibraryPath.grid(row=0, column=0, sticky=E, pady=(20, 0))
        self.entryLibraryPath = Entry(self.frameLabelEntry, width=70, highlightcolor=self.colorHighlight, highlightthickness=1)
        self.entryLibraryPath.grid(row=0, column=1, padx=(5, 2),sticky=EW, pady=(20, 0))
        self.buttonLibraryPath = Button(self.frameLabelEntry, image=self.iconOpenFile, \
            highlightthickness=0, highlightbackground=self.colorActiveBg, border=0, borderwidth=0)
        self.buttonLibraryPath.grid(row=0, column=2, sticky=W, pady=(20, 0))


        self.labelSwitchSettings = Label(self.frameLabelEntry, text='Switch Settings', bg=self.colorFrameBg,  \
            highlightthickness=0, highlightbackground=self.colorFrameBg, border=0, borderwidth=0)
        self.labelSwitchSettings.grid(row=1, column=0, sticky=E, pady=(20, 0))
        self.entrySwitchSettings = Entry(self.frameLabelEntry, width=70, highlightcolor=self.colorHighlight, highlightthickness=1)
        self.entrySwitchSettings.grid(row=1, column=1, padx=(5, 2),sticky=EW, pady=(20, 0))
        self.buttonSwitchSettings = Button(self.frameLabelEntry, image=self.iconOpenFile, \
            highlightthickness=0, highlightbackground=self.colorActiveBg, border=0, borderwidth=0)
        self.buttonSwitchSettings.grid(row=1, column=2, sticky=W, pady=(20, 0))


        self.labelOutputFileName = Label(self.frameLabelEntry, text='Output File Name', bg=self.colorFrameBg, \
            highlightthickness=0, highlightbackground=self.colorFrameBg, border=0, borderwidth=0)
        self.labelOutputFileName.grid(row=2, column=0, sticky=E, pady=(20, 0))
        self.entryOutputFileName = Entry(self.frameLabelEntry, width=7, highlightcolor=self.colorHighlight, highlightthickness=1)
        self.entryOutputFileName.grid(row=2, column=1, columnspan=2, padx=(5, 2), sticky=EW, pady=(20, 0))


        self.buttonCreateCreateConfig = Button(self.frameButtonConfig, text="Create", bg=self.colorActibeButtonBg, fg=self.colorActibeButtonFg,  state='normal', \
             highlightthickness=0, highlightbackground=self.colorActibeButtonBg, border=0, borderwidth=0, font=("Helvetica", 12, font.BOLD))
        self.buttonCreateCreateConfig.pack(expand=False, fill="x", pady=(20, 0))
        

        
        self.frameLabelEntryLoad = Frame(self.frameLoadConfig, bg=self.colorFrameBg, \
            highlightthickness=0, highlightbackground=self.colorFrameBg, border=0, borderwidth=0)
        self.frameLabelEntryLoad.pack(expand=True, fill="both", side=TOP)
        self.frameButtonLoad = Frame(self.frameLoadConfig, bg=self.colorFrameBg, \
            highlightthickness=0, highlightbackground=self.colorFrameBg, border=0, borderwidth=0)
        self.frameButtonLoad.pack(expand=False, fill="x", side=BOTTOM)

        self.frameLabelEntry.columnconfigure(0, weight=2)
        self.frameLabelEntry.columnconfigure(1, weight=5)
        self.frameLabelEntry.columnconfigure(2, weight=1)
        self.frameLabelEntry.rowconfigure(0, weight=10)
        
        self.frameLabelEntryLoadOnly = Frame(self.frameLabelEntryLoad, bg=self.colorFrameBg, \
            highlightthickness=0, highlightbackground=self.colorFrameBg, border=0, borderwidth=0)
        self.frameLabelEntryLoadOnly.pack(expand=True, fill="x")

        self.labelConfigPath = Label(self.frameLabelEntryLoadOnly, text='Library Path', bg=self.colorFrameBg, \
            highlightthickness=0, highlightbackground=self.colorActiveBg, border=0, borderwidth=0)
        self.labelConfigPath.grid(row=0, column=0, sticky=E, pady=10, padx=(33, 0))
        self.entryConfigPath = Entry(self.frameLabelEntryLoadOnly, width=71, highlightcolor=self.colorHighlight, highlightthickness=1)
        self.entryConfigPath.grid(row=0, column=1, padx=(5, 2),sticky=EW, pady=10)
        self.buttonConfigPath = Button(self.frameLabelEntryLoadOnly, image=self.iconOpenFile, \
            highlightthickness=0, highlightbackground=self.colorActiveBg, border=0, borderwidth=0)
        self.buttonConfigPath.grid(row=0, column=2, sticky=W, pady=10)

        self.buttonLoadLoadConfig = Button(self.frameButtonLoad, text="Load", bg=self.colorActibeButtonBg, fg=self.colorActibeButtonFg,  state='normal', \
             highlightthickness=0, highlightbackground=self.colorActibeButtonBg, border=0, borderwidth=0, font=("Helvetica", 12, font.BOLD))
        self.buttonLoadLoadConfig.pack(expand=False, fill="x")
        

        self.dehighlightNavigationButton()
        if self.navigationButtonSeq == ['load', 'create']:
            self.buttonLoadConfigClicked()
            self.canvasFrame.itemconfigure(self.frameCreateConfigID, state="hidden")
            self.canvasFrame.itemconfigure(self.frameLoadConfigID, state="normal")
        else:
            self.buttonCreateConfigClicked()
            self.canvasFrame.itemconfigure(self.frameCreateConfigID, state="normal")
            self.canvasFrame.itemconfigure(self.frameLoadConfigID, state="hidden")
        

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
fontButtonBold = font.Font(family="Arial", size=11, weight=font.BOLD)
fontButtonNormal = font.Font(family="Arial", size=11)
fontTextBox = font.Font(family="Times New Roman", size=11)

canvasMain = Canvas(root, background=colorMainBg)
canvasMain.pack(expand=True, fill="both", anchor=CENTER)

startingWindowBg = loadImage(f"{imageDir}/startingWindowBg1.png", (800, 550))
canvasMain.create_image(rootWidth//2, rootHight//2, image=startingWindowBg)

configClass = CREATE_CONFIG(canvasFrame=canvasMain)


time_end = datetime.now()
print("Now         : ", time_end, f"\nTime Needed :  {(time_end - time_load)}")
root.mainloop()