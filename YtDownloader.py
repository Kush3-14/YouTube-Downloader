from tkinter import *
from pytube import YouTube


root = Tk()
root.geometry('1090x600')
root.configure(bg='Red')
root.resizable(0,0)
root.title("YouTube video Downloader")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold',bg='Red').pack()
link = StringVar()
Label(root, text = 'Paste Link Here :', font = 'arial 15 bold',bg='#80d414').place(x= 175 , y = 140)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 360, y = 145)

def download():
    yt = YouTube(str(link.get()))

    Label(root, text=("Title:",yt.title), pady=10, bg='Red').place(x=300 ,y = 250)
    Label(root, text=("Number of views: ",yt.views), pady=10, bg='Red').place(x=300 ,y =290)
    Label(root, text=("Length: ",yt.length,"seconds"), pady=10, bg='Red').place(x=300 ,y = 320)
    Label(root, text=("Channel: ",yt.author), pady=10, bg='Red').place(x=300 ,y = 350)

    ys = yt.streams.get_highest_resolution() 

    ys.download()
    Label(root, text="Download completed!", pady=20, bg='Red').place(x=500 ,y = 400)

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'light Green', padx = 2, command = download).place(x=500 ,y = 200)
root.mainloop()
