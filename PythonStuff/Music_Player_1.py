#This program is a simple music player using python
#User only needs MP3 music folder with MP3 music inside.
#Just select folder to point to MP3 music files when prompted

import os
from tkinter.filedialog import askdirectory


import pygame
from mutagen.id3 import ID3
from tkinter import *

root = Tk()
root.minsize(300, 300)

listofsongs = []

index = 0

def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def stopsong(event):
    pygame.mixer.music.stop()

def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            realdir = os.path.realpath(files)
            audio = ID3()
            listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

directorychooser()

label = Label(root, text='Music Player')
label.pack()

listbox = Listbox(root)
listbox.pack()

reversedlist = listofsongs.reverse()

for items in listofsongs:
    listbox.insert(0,items)

listofsongs.reverse()

nextbutton = Button(root, text='Next Song')
nextbutton.pack()

previousbutton = Button(root, text='Previous Song')
previousbutton.pack()

stopbutton = Button(root, text='Stop Music')
stopbutton.pack()


nextbutton.bind("<Button-1>", nextsong)
previousbutton.bind("<Button-1>", prevsong)
stopbutton.bind("<Button-1>", stopsong)





root.mainloop()
