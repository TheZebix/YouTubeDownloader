from tkinter.messagebox import showerror, showwarning
from pytube import YouTube
from tkinter import *
from tkinter import filedialog


def chosePath():
    filename = filedialog.askdirectory()
    path_lb.configure(text=filename)
    if path_lb.cget("text") == "":
        path_lb.configure(text="Path where you want to save the file")

def download():
# https://youtu.be/wuJIqmha2Hk
    if link_ent.get() == "" or path_lb.cget("text") == "":
        showwarning(title="Download Error", message="Before you download video you need to chose path and paste link.")
    else:
        try: 
            yt = YouTube(link_ent.get()) 
        except:
            print("Connection Error")
            showerror(title="Conntection Error", message="Sorry, your video is currently unvaliable.")
            return

        resolution = [int(i.split("p")[0]) for i in (list(dict.fromkeys([i.resolution for i in yt.streams if i.resolution])))].sort()
        print(resolution)

        d_video = yt.streams.get_highest_resolution()

        try:
            d_video.download(path_lb.cget("text"))
        except: 
            print("Some Error!") 

        print('Task Completed!') 


HEIGHT = 850
WIDTH = 450

root = Tk()
root.title("Youtube Downloader")
root.geometry(f"{HEIGHT}x{WIDTH}")
root.resizable(False, False)
root.iconbitmap(r"C:\YouTubeDownloader\program files\images\favicon.ico")

logo_img = PhotoImage(file="C:\YouTubeDownloader\program files\images\gear.jpg").subsample(7, 7)

logo_lb = Label(root, image=logo_img)
logo_lb.grid(column=0, row=0, padx=(330, 0))

path_lb = Label(root, text="Path where you want to save the file")
path_lb.grid(column=0, row=1, padx=(300, 0), pady=(30, 15))

path_btn = Button(root, text="Chose Path", command=chosePath)
path_btn.grid(column=1, row=1, pady=(30, 15))
download_btn = Button(root, text="Download", command=download)
download_btn.grid(column=0, row=3, padx=(300, 0))
resolution_btn = Button(root, text="Chose resolution")
resolution_btn.grid(column=1, row=2, padx=(25, 0))

link_ent = Entry(root, width=50)
link_ent.grid(column=0, row=2, padx=(300, 0), pady=15)


root.mainloop()