from pytube import YouTube
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
import tkinter.messagebox

def video():
    try:
        string = e.get()
        print(string)
        YouTube(string).streams.first().download(path)
        downloaded()
    except Exception:
        answer()

def answer():
    mb.showerror("Error", "Wrong Youtube URL")

def downloaded():
    tkinter.messagebox.showinfo("Downloaded", "Your Video has been downloaded")

def downloader():
    global e
    global path
    top = Tk()
    top.title("Youtube Downloader")
    top.geometry("500x400")
    L1 = Label(top, text="URL OF VIDEO")
    L1.pack( side = TOP)
    e = Entry(top)
    e.pack()
    e.focus_set()
    b = Button(top, text='DOWNLOAD VIDEO', command=video)
    b.pack()
    path = filedialog.askdirectory(title="Choose directory",
                                   initialdir="/home",
                                   mustexist=True)
    top.mainloop()



downloader()