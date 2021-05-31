from tkinter import *
import os
import pygame
from mutagen.mp3 import MP3
from tkinter import filedialog
import tkinter.messagebox as tmsg
import time
import eyed3

pygame.init()

root = Tk()
root.title('MUSIC PLAYER BY AK')
root.geometry("830x220")

starting = StringVar()
ending = StringVar()

info_getter = StringVar()

starting.set('--:--')
ending.set('--:--')

def emp(text):
    Label(f1,text=text,bg="black").pack(side=LEFT)

def start_music():

    music_file_dir = filedialog.askopenfilename(initialdir="")

    try:

        pygame.mixer.music.load(music_file_dir)

        pygame.mixer.music.play()

        button1.config(image=photo2,command=stop_music)

        sound = MP3(music_file_dir)

        timing = "%.0f"%sound.info.length

        ending.set(eval(timing))

        starting.set('0')

        button3.config(state=NORMAL)

        l22.config(text="Start: ")

        l33.config(text="End: ")

        title = eyed3.load(music_file_dir)

        titttle = title.tag.title

        if titttle == "":

            lll.config(text="<Untitled>")

        else:

            lll.config(text=titttle)

        player()

    except:

        tmsg.showwarning('Warning','This media file is not supported')

def player():

    try:

        while (True):

            root.update()

            if (info_getter.get())=="None":

                info_getter.set('')

                break

            if eval((starting.get())) >= eval((ending.get())):

                pygame.mixer.music.stop()

                pygame.mixer.music.unload()

                button1.config(image=photo1,command=start_music)

                l22.config(text="")
        
                l33.config(text="")

                break

            else:

                one = eval((starting.get()))
                two = eval((ending.get()))

                three = (one/two)*100

                calc1 = "%.0f"%three

                l1.config(text="   "+calc1+" %",width=calc1,bg="red",justify=CENTER)

                music_gett = pygame.mixer.music.get_pos()

                music_get = music_gett/1000

                music_final = "%.0f"%music_get

                starting.set(str(music_final))

                root.after(1000)
    except:

        pass    

def stop_music():

    ah = pygame.mixer.music.pause()

    info_getter.set(ah)

    button1.config(image=photo1,command=unpause_music)

def unpause_music():

    pygame.mixer.music.unpause()

    button1.config(image=photo2, command=stop_music)

    player()

def reset():

    pygame.mixer.music.stop()

    pygame.mixer.music.unload()

    l1.config(width=0,bg="black")

    starting.set('--:--')
    ending.set('--:--')

    button3.config(state=DISABLED)

    button1.config(image=photo1,command=start_music)

    l22.config(text="")
        
    l33.config(text="")


lll = Label(text="",bg="black",fg="white",font="comicsansms 16 bold",padx=4,pady=5)
lll.pack()

f2 = Frame(borderwidth=10, bg="black")


Label(f2, text="",bg="black").pack()    

l22 = Label(f2, text="",bg="black",fg="white")
l22.pack(side=LEFT)

l2 = Label(f2, textvariable=starting,bg="black",fg="white")
l2.pack(side=LEFT)

l1 = Label(f2,bg="black",width=0)
l1.pack(side=LEFT)

l33 = Label(f2, text="",bg="black",fg="white")
l33.pack(side=LEFT)

l3 = Label(f2, textvariable=ending,bg="black",fg="white")
l3.pack(side=LEFT)


f2.pack(anchor='s')


f1 = Frame(borderwidth=10,bg="black")

emp(" ")

photo1 = PhotoImage(file="Python\\1.png")
photo2 = PhotoImage(file="Python\\2.png")

button1 = Button(f1,image=photo1,command=start_music)

button1.pack(side=LEFT)

emp(" ")

button3 = Button(f1,text="Reset",bg="black",fg="white",font="comicsansms 12 bold",width=6,command=reset,state=DISABLED)

button3.pack(side=LEFT)

f1.pack(anchor="s")


root.config(bg="black")
root.mainloop()