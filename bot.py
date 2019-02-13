from PIL import ImageGrab,ImageOps
import pyautogui
import time
import numpy as np

class Cordinates():
    replayBtn = (340,390)
    dinosaur = (171,395)
    #240 = x to check for trees
    #420 = y for the height of tree


def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    pyautogui.keyUp('space')

def imageGrab():
    box = (240,Cordinates.dinosaur[1],280,Cordinates.dinosaur[1]+30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = np.array(grayImage.getcolors())
    return a.sum()

def main():
    restartGame()
    while True:
        if(imageGrab()!=1447):
            pressSpace()
            time.sleep(0.1)

main()
