from pytube import YouTube
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
import tkinter.messagebox
from pathlib import Path

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
    top = Tk()
    top.title("Youtube Downloader")
    top.geometry("500x400")
    L1 = Label(top, text="URL OF VIDEO", fg = "red", font = "Times 20 bold")
    L1.pack( side = TOP , pady = (100,10))
    e = Entry(top,  width = 70)
    e.pack(pady = 10)
    e.focus_set()
    b = Button(top, text='DOWNLOAD VIDEO', command=video)
    b.pack()
    top.mainloop()

downloads_path = str(Path.home() / "Downloads")

path = filedialog.askdirectory(title="Choose directory in which you want to save your video",
                                   initialdir= downloads_path,
                                   mustexist=True)
if path == "":
    path = downloads_path

print("path: " , path)
downloader()