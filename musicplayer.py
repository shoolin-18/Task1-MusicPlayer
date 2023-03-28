import tkinter as tk
import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory

from mutagen.id3 import ID3

root = Tk()


root.minsize(500, 500)

listofsongs = []
real_names = []

v = StringVar()

index = 0




def directorychooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            real_names.append(audio['TIT2'].text[0])

            listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])


directorychooser()



def updatelabel():
    global index
    v.set(real_names[index])


def nextsong():
    global index
    index += 1
    updatelabel()


def prevsong():
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def unpausesong():
    pygame.mixer.music.unpause()

    updatelabel()


def pausesong():
    pygame.mixer.music.pause()
    v.set("Song Paused")


def stopsong():
    pygame.mixer.music.stop()
    v.set("")


def play():
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()




listbox_frame = LabelFrame(root, text='Music Player@CodeClause', bg="DodgerBlue2", padx=5)
listbox_frame.place(x=360, y=0, height=715, width=300)

listbox = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='Gold')


scroll_bar = Scrollbar(listbox, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)


listbox.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=listbox.yview)

listbox.pack(fill=BOTH, padx=0, pady=0)




real_names.reverse()

for items in real_names:
    listbox.insert(0, items)

real_names.reverse()



song_frame = LabelFrame(root, text='Current Song Playing', bg='Gold', width=400, height=200, fg="Black", pady=75)
song_frame.place(x=0, y=0)

songlabel = tk.Label(song_frame, textvariable=v, width=50, bg="Black", height=5, fg="White")

button_frame = LabelFrame(root, text='Control Buttons', bg='Turquoise', width=400, height=120, padx=115)
button_frame.place(y=250)

nextbutton = Button(button_frame, text='Next Song', command=nextsong, padx=30, pady=25, bg="Black", fg="White")
nextbutton.place(x=350, y=10)
nextbutton.pack()

previousbutton = Button(button_frame, text='Previous Song', command=prevsong, padx=20, pady=25, bg="Black", fg="White")
previousbutton.place(x=300, y=10)
previousbutton.pack()

pausebutton = Button(button_frame, text='Pause Song', command=pausesong, padx=27, pady=25, bg="Black", fg="White")
pausebutton.place(x=290, y=10)
pausebutton.pack()

unpausebutton = Button(button_frame, text='Resume Song', command=unpausesong, padx=22, pady=25, bg="Black", fg="White")
unpausebutton.place(x=250, y=10)
unpausebutton.pack()

stopbutton = Button(button_frame, text='Stop Music', command=stopsong, padx=29, pady=25, bg="Black", fg="White")
stopbutton.place(x=150, y=10)
stopbutton.pack()

playbutton = Button(button_frame, text='Play Music', command=play, padx=29, pady=25, bg="Black", fg="White")
playbutton.place(x=190, y=10)
playbutton.pack()

songlabel.pack()
root.mainloop()
