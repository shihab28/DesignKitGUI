import os, json
from datetime import datetime
from tkinter import *
from tkinter import ttk, font, filedialog

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
        self.libraryPathFileTypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
        )

        self.switchSettings = ''
        self.switchSettingsFileTypes = (
        ('excels files', '*.xlsx'),
        ('csv files', '*.csv'),
        ('excel files', '*.xls'),
        ('All files', '*.*')
        )

        self.outputFileName = ''
        self.configFilePath = ''
        self.configFilePathFileTypes = (
        ('configuration files', '*.config'),
        ('All files', '*.*')
        )



        self.colorMainBg = "#F6F9F9"
        self.colorFrameBg = "#FFF6E9"
        self.colorHighlight = "#2A7FFF"
        self.colorActiveBg = "#FFF6E9"
        self.colorInactiveBg = "#F6F9F9"
        self.colorActibeButtonBg = "#99FF99"
        self.colorActibeButtonFg = "Black"
        self.colorActibeEntryBg = "#CCFFCC"
        self.colorActibeEntryFg = "Black"
        self.colorActiveFg = "Black"
        self.colorInactiveFg = "Gray"

        self.iconOpenFile = loadImage(f"{imageDir}/folderOpenGreen.png", (20,20))
        self.mainFrameList = []
        
        self.buttonFBDimension = (64, 64)

        self.navigationButtonSeq = ['load', 'create']
        self.currentFrame = self.navigationButtonSeq[0]
        self.navigationButtonSeq = ['create', 'load']


        self.createButtons()
        self.createFrame()

        # self.createRunFrame()


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
        self.checkCreateConfigBoxes()
        self.currentFrame = 'create'

    def buttonLoadConfigClicked(self):
        self.dehighlightNavigationButton()
        self.buttonLoadConfig.configure(bg=self.colorActiveBg, highlightbackground=self.colorActiveBg, font=fontButtonBold)
        self.canvasFrame.itemconfigure(self.frameLoadConfigID, state="normal")
        self.checkLoadConfigBoxes()
        self.currentFrame = 'load'

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
        relx=700; rely=225; relwidth=96; relheight=200; pad = 0
        self.frameForwardID = self.canvasFrame.create_window((relx+pad, rely+pad), anchor=NW, window=self.frameForward, tags="self.frameForward", width=relwidth-pad, height=relheight-pad)
        self.mainFrameList.append(self.frameLoadConfigID)

    def placeFrameBackward(self):
        relx=5; rely=225; relwidth=70; relheight=200; pad = 0
        self.frameBackwardID = self.canvasFrame.create_window((relx+pad, rely+pad), anchor=NW, window=self.frameBackward, tags="self.frameBackward", width=relwidth-pad, height=relheight-pad)
        self.mainFrameList.append(self.frameLoadConfigID)

    def checkExtension(self, tempName=None):
        nameExt = None
        nameName, nameExt = self.checkNameExtension(tempName)
        return nameExt

    def checkNameExtension(self, tempName=None):
        nameList = tempName.split(".")
        nameName = tempName
        nameExt = None
        if len(nameList) > 2:
            nameName = '.'.join(nameList[0:-1])
            nameExt = nameList[-1]
        return nameName, nameExt

    


    def makeOutputFileName(self):
        tempName = self.libraryPath
        nameList = tempName.split("/")
        prevName = self.entryOutputFileName.get()
        try:
            tempNam = nameList[-2]
            self.entryOutputFileName.delete(0, END)
            self.entryOutputFileName.insert(END, tempNam)

        except:
            self.entryOutputFileName.delete(0, END)
            self.entryOutputFileName.insert(END, prevName)
        

    def openLibraryPath(self, eve=None):
        self.entryLibraryPath.delete(0, END)
        try:
            temPath = filedialog.askdirectory()
            temPath =  temPath.replace("\\", "/")
            print(temPath)
            self.entryLibraryPath.insert(END, temPath)
            self.libraryPath = temPath
            self.makeOutputFileName()
        except:
            self.entryLibraryPath.insert(END, self.libraryPath)


    def openSwitchSettings(self, eve=None):
        self.entrySwitchSettings.delete(0, END)
        try:
            temPath = filedialog.askopenfilename(filetypes=self.switchSettingsFileTypes)
            temPath =  temPath.replace("\\", "/")
            self.entrySwitchSettings.insert(END, temPath)
            self.switchSettings = temPath
        except:
            self.entrySwitchSettings.insert(END, self.switchSettings)

    def openOutputFileName(self, eve=None):
        pass

    def openConfigFilePath(self, eve=None):
        self.entryConfigFilePath.delete(0, END)
        try:
            temPath = filedialog.askopenfilename(filetypes=self.configFilePathFileTypes)
            temPath =  temPath.replace("\\", "/")
            self.entryConfigFilePath.insert(END, temPath)
            self.configFilePath = temPath
        except:
            self.entryConfigFilePath.insert(END, self.configFilePath)







    def checkCreateConfigBoxes(self, eve=None):
        self.libraryPath = self.entryLibraryPath.get().replace("\\", "/").strip('\"')
        self.switchSettings = self.entrySwitchSettings.get().replace("\\", "/").strip('\"')
        self.outputFileName = self.entryOutputFileName.get().replace("\\", "/").strip('\"')

        # print(self.libraryPath, self.switchSettings, self.outputFileName)
        if os.path.isdir(self.libraryPath):
            self.entryLibraryPath.configure(bg=self.colorActibeEntryBg)
        else:
            self.entryLibraryPath.configure(bg="white")
        
        if os.path.isfile(self.switchSettings):
            self.entrySwitchSettings.configure(bg=self.colorActibeEntryBg)
        else:
            self.entrySwitchSettings.configure(bg="white")
        
        if self.outputFileName != '':
            self.entryOutputFileName.configure(bg=self.colorActibeEntryBg)
        else:
            self.entryOutputFileName.configure(bg="white")
        
        if os.path.isdir(self.libraryPath) and os.path.isfile(self.switchSettings) and self.outputFileName != '':
            self.forwardLabel.pack_forget()
            self.forwardButton.config(image=self.iconForwardActive, state='normal')
            self.forwardButton.pack(anchor=CENTER)
        else:
            self.forwardButton.pack_forget()
            self.forwardButton.config(image=self.iconForwardInactive, state='disabled')
            self.forwardLabel.pack(anchor=CENTER)  
        

    def checkLoadConfigBoxes(self, eve=None):
        self.configFilePath = self.entryConfigFilePath.get().replace("\\", "/").strip('\"')
        # print(self.configFilePath)
        if os.path.isfile(self.configFilePath):
            self.entryConfigFilePath.configure(bg=self.colorActibeEntryBg)
            self.forwardLabel.pack_forget()
            self.forwardButton.config(image=self.iconForwardActive, state='normal')
            self.forwardButton.pack(anchor=CENTER)
        else:        
            self.forwardButton.pack_forget()
            self.forwardButton.config(image=self.iconForwardInactive, state='disabled')
            self.forwardLabel.pack(anchor=CENTER)
            self.entryConfigFilePath.configure(bg="white") 

    
    def checkBothBoxes(self, eve=None):
        if self.currentFrame == 'load':
            self.checkLoadConfigBoxes()
        elif self.currentFrame == 'create':
            self.checkCreateConfigBoxes()

    def forwardButtonCLicked(self, eve=None):
        self.checkBothBoxes()
        print(f"Forward from  {self.currentFrame}")
    
    def backwardButtonClicked(self, eve=None):
        self.checkBothBoxes()
        print(f"Backward from  {self.currentFrame}")


    def createFrame(self):

        self.canvasFrame.bind("<Motion>", lambda eve : self.checkBothBoxes())

        self.frameCreateConfig = Frame(self.canvasFrame, bg=self.colorFrameBg)
        self.placeFrameCreateConfig()
        self.frameCreateConfig.bind("<Motion>", lambda eve : self.checkCreateConfigBoxes())
        

        self.frameLoadConfig = Frame(self.canvasFrame, bg=self.colorFrameBg)
        self.placeFrameLoadConfig()
        self.frameLoadConfig.bind("<Motion>", lambda eve : self.checkLoadConfigBoxes())
        
        # colorMainBg
        self.frameForward = Frame(self.canvasFrame, bg=self.colorMainBg)
        self.placeFrameForward()
        self.iconForwardActive = loadImage(f"{imageDir}/forward_green_1024.png", self.buttonFBDimension)
        self.iconForwardInactive = loadImage(f"{imageDir}/forward_gray_1024.png", self.buttonFBDimension)
        self.forwardButton = Button(self.frameForward, bg = self.colorMainBg, command= lambda eve  = self : self.forwardButtonCLicked(), \
             highlightthickness=0, highlightbackground=self.colorMainBg, border=0, borderwidth=0)
        self.forwardButton.config(image=self.iconForwardActive, state='normal')
        self.forwardButton.config(image=self.iconForwardInactive, state='disabled')
        self.forwardButton.pack(anchor=CENTER)  
        self.forwardButton.pack_forget()
        self.forwardLabel = Label(self.frameForward, bg = self.colorMainBg, image=self.iconForwardInactive, \
             highlightthickness=0, highlightbackground=self.colorMainBg, border=0, borderwidth=0)
        self.forwardLabel.pack(anchor=CENTER)  


        self.frameBackward = Frame(self.canvasFrame, bg=self.colorMainBg)
        self.placeFrameBackward()
        self.iconBackwardActive = loadImage(f"{imageDir}/backward_green_1024.png", self.buttonFBDimension)
        self.iconBackwardInactive = loadImage(f"{imageDir}/backward_gray_1024.png", self.buttonFBDimension)
        self.backwardButton = Button(self.frameBackward, bg = self.colorMainBg, command= lambda eve = self : self.backwardButtonCLicked(), \
             highlightthickness=0, highlightbackground=self.colorMainBg, border=0, borderwidth=0, disabledforeground=self.colorMainBg)
        self.backwardButton.config(image=self.iconBackwardInactive, state='disabled')
        # self.backwardButton.config(image=self.iconBackwardActive, state='normal')
        self.backwardButton.pack(anchor=CENTER)
        self.backwardButton.pack_forget()
        self.backwardLabel = Label(self.frameBackward, bg = self.colorMainBg, image=self.iconBackwardInactive, \
             highlightthickness=0, highlightbackground=self.colorMainBg, border=0, borderwidth=0)
        self.backwardLabel.pack(anchor=CENTER) 
        self.backwardLabel.pack_forget() 
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
        self.entryLibraryPath.bind("<Return>", lambda eve : self.checkCreateConfigBoxes()())
        self.entryLibraryPath.bind("<Leave>", lambda eve : self.checkCreateConfigBoxes())
        self.entryLibraryPath.bind("<Enter>", lambda eve : self.checkCreateConfigBoxes())
        self.entryLibraryPath.bind("<Key>", lambda eve : self.checkCreateConfigBoxes())
        self.buttonLibraryPath = Button(self.frameLabelEntry, image=self.iconOpenFile, command= lambda eve = self : self.openLibraryPath(), \
            highlightthickness=0, highlightbackground=self.colorActiveBg, border=0, borderwidth=0)
        self.buttonLibraryPath.grid(row=0, column=2, sticky=W, pady=(20, 0))

        self.labelSwitchSettings = Label(self.frameLabelEntry, text='Switch Settings', bg=self.colorFrameBg,  \
            highlightthickness=0, highlightbackground=self.colorFrameBg, border=0, borderwidth=0)
        self.labelSwitchSettings.grid(row=1, column=0, sticky=E, pady=(20, 0))
        self.entrySwitchSettings = Entry(self.frameLabelEntry, width=70, highlightcolor=self.colorHighlight, highlightthickness=1)
        self.entrySwitchSettings.grid(row=1, column=1, padx=(5, 2),sticky=EW, pady=(20, 0))
        self.entrySwitchSettings.bind("<Return>", lambda eve : self.checkCreateConfigBoxes())
        self.entrySwitchSettings.bind("<Leave>", lambda eve : self.checkCreateConfigBoxes())
        self.entrySwitchSettings.bind("<Enter>", lambda eve : self.checkCreateConfigBoxes())
        self.entrySwitchSettings.bind("<Key>", lambda eve : self.checkCreateConfigBoxes())
        self.buttonSwitchSettings = Button(self.frameLabelEntry, image=self.iconOpenFile, command= lambda eve = self : self.openSwitchSettings(), \
            highlightthickness=0, highlightbackground=self.colorActiveBg, border=0, borderwidth=0)
        self.buttonSwitchSettings.grid(row=1, column=2, sticky=W, pady=(20, 0))

        self.labelOutputFileName = Label(self.frameLabelEntry, text='Output File Name', bg=self.colorFrameBg, \
            highlightthickness=0, highlightbackground=self.colorFrameBg, border=0, borderwidth=0)
        self.labelOutputFileName.grid(row=2, column=0, sticky=E, pady=(20, 0))
        self.entryOutputFileName = Entry(self.frameLabelEntry, width=7, highlightcolor=self.colorHighlight, highlightthickness=1)
        self.entryOutputFileName.grid(row=2, column=1, columnspan=2, padx=(5, 2), sticky=EW, pady=(20, 0))
        self.entryOutputFileName.bind("<Return>", lambda eve : self.checkCreateConfigBoxes())
        self.entryOutputFileName.bind("<Leave>", lambda eve : self.checkCreateConfigBoxes())
        self.entryOutputFileName.bind("<Enter>", lambda eve : self.checkCreateConfigBoxes())
        self.entryOutputFileName.bind("<Key>", lambda eve : self.checkCreateConfigBoxes())

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

        self.labelConfigFilePath = Label(self.frameLabelEntryLoadOnly, text='Config File Path', bg=self.colorFrameBg, \
            highlightthickness=0, highlightbackground=self.colorActiveBg, border=0, borderwidth=0)
        self.labelConfigFilePath.grid(row=0, column=0, sticky=E, pady=10, padx=(12, 0))
        self.entryConfigFilePath = Entry(self.frameLabelEntryLoadOnly, width=71, highlightcolor=self.colorHighlight, highlightthickness=1)
        self.entryConfigFilePath.grid(row=0, column=1, padx=(5, 2),sticky=EW, pady=10)
        self.entryConfigFilePath.bind("<Return>", lambda eve : self.checkLoadConfigBoxes())
        self.entryConfigFilePath.bind("<Leave>", lambda eve : self.checkLoadConfigBoxes())
        self.entryConfigFilePath.bind("<Enter>", lambda eve : self.checkLoadConfigBoxes())
        self.entryConfigFilePath.bind("<Key>", lambda eve : self.checkLoadConfigBoxes())
        self.buttonConfigFilePath = Button(self.frameLabelEntryLoadOnly, image=self.iconOpenFile, command= lambda eve = self : self.openConfigFilePath(), \
            highlightthickness=0, highlightbackground=self.colorActiveBg, border=0, borderwidth=0)
        self.buttonConfigFilePath.grid(row=0, column=2, sticky=W, pady=10)


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


    def placeFrameRunModule(self):
        relx=72; rely=7; relwidth=709; relheight=540; pad = 10
        self.frameLoadConfigID = self.canvasFrame.create_window((relx+pad, rely+pad), anchor=NW, window=self.frameLoadConfig, tags="self.frameLoadConfig", width=relwidth-pad, height=relheight-pad)
        self.mainFrameList.append(self.frameLoadConfigID)
    
    def createRunFrame(self):
        self.frameRunModule = Frame(self.canvasFrame, bg=self.colorFrameBg)
        self.placeFrameRunModule()
        # self.frameRunModule.bind("<Motion>", lambda eve : self.checkCreateConfigBoxes())
        pass
        

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
root.config(bg="#F6F9F9")


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