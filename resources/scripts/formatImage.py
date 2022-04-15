#!/tool/pandora64/bin/python3.6
import os
from PIL import Image, ImageTk


def loadImage(imgPath, imageSize = (24, 24)):
    curDir = os.path.dirname(__file__)
    imgSaveDir = f"{imgPath}".replace("\\", "/")
    imgSave =ImageTk.PhotoImage(Image.open(imgSaveDir).resize(imageSize, Image.ANTIALIAS))
    return imgSave