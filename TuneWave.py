from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root = Tk()
root.title("TuneWave")
root.geometry("920x670+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False,False)

mixer.init()

def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
#        print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def play_song():
    music_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    Music.config(text=music_name[0:-4])


#icon
image_icon=PhotoImage(file="img/logo.png")
root.iconphoto(False,image_icon)


Top = PhotoImage(file="img/top.png")
Label(root,image=Top,bg="#0f1a2b").pack()
B = Label(root, text="TuneWave",font=("Arial",50),fg="White",bg="#0767ed")
B.place(x=570,y=100)
A = Label(root, text="Copyright@SasinduRashmika2023",font=("Arial",7),fg="White",bg="#0f1a2b")
A.place(x=735,y=640)


#logo
Logo=PhotoImage(file="img/logo.png")
Label(root,image=Logo,bg="#0f1a2b").place(x=47,y=105)

#button
play_button=PhotoImage(file="img/play.png")
Button(root,image=play_button,bg="#0f1a2b",bd=0,command=play_song).place(x=120,y=350)

stop_button=PhotoImage(file="img/stop.png")
Button(root,image=stop_button,bg="#0f1a2b",bd=0,command=mixer.music.stop).place(x=20,y=400)

resume_button=PhotoImage(file="img/resume.png")
Button(root,image=resume_button,bg="#0f1a2b",bd=0,command=mixer.music.unpause).place(x=80,y=500)

pause_button=PhotoImage(file="img/pause.png")
Button(root,image=pause_button,bg="#0f1a2b",bd=0,command=mixer.music.pause).place(x=200,y=500)

#label
Music=Label(root,text="",font=("arial",15),fg="White",bg="#0f1a2b")
Music.place(x=240,y=280,anchor="center")

#Music
menu = PhotoImage(file="img/menu.png")
Label(root,image=menu,bg="#0f1a2b").pack(padx=10,pady=50,side=RIGHT)

music_frame=Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=330,y=350,width=560,height=250)

Button(root,text="Open Folder",width=15,height=2,font=("arial",10,"bold"),fg="white",bg="#21b3de",command=open_folder).place(x=330,y=300)

scroll=Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,font=("arial",10),bg="#333333",fg="gray",selectbackground="lightblue",
                 cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)
root.mainloop()
