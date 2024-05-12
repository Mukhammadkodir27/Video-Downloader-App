from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from pytube import YouTube
from moviepy.editor import *
import shutil


def download():
    video_path = url_entry.get()
    file_path = path_label.cget("text")

    if not video_path:
        status_label.config(text="Please, provide the video URL.", fg='red')
        return
    if file_path == "Select path to download":
        status_label.config(text="Please select the download path.", fg='red')
        return

    status_label.config(text="Downloading...", fg='black')
    root.update_idletasks()
    try:
        mp4 = YouTube(video_path).streams.get_highest_resolution().download()
        video_clip = VideoFileClip(mp4)
        video_clip.close()
        shutil.move(mp4, file_path)
        status_label.config(text="Successfully downloaded!", fg='green')
    except Exception as e:
        status_label.config(text="Error: " + str(e), fg='red')


def get_path():
    path = filedialog.askdirectory()
    if path:
        path_label.config(text=path)


root = Tk()
root.title("Video Downloader")
root.geometry("600x500")
root.resizable(False, False)

# Load and set the background image using Pillow
image = Image.open('background4.png')
bg_image = ImageTk.PhotoImage(image)
background_label = Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# App label
app_label = Label(root, text="Video Downloader", fg="white",
                  bg="#BE0000", font=("Arial", 18))
app_label.place(x=300, y=70, anchor="center")

# Entry to accept video URL
url_label = Label(root, text="Enter video URL",
                  font=("Arial", 10), fg="white", bg="#BE0000")
url_entry = Entry(root, font=("Arial", 10), width=40)
url_label.place(x=300, y=140, anchor="center")
url_entry.place(x=300, y=170, anchor="center")

# Path to download videos
path_label = Label(root, text="Select path to download",
                   font=("Arial", 10), fg="white", bg="#BE0000")
path_button = Button(root, text="Select", command=get_path,
                     font=("Arial", 10), fg="blue")
path_label.place(x=300, y=210, anchor="center")
path_button.place(x=300, y=250, anchor="center")

# Download button
download_button = Button(root, text="Download",
                         command=download, font=("Arial", 12), fg="blue")
download_button.place(x=300, y=300, anchor="center")

# Status label
status_label = Label(root, text="", font=(
    "Arial", 10), fg="red", bg="white")
status_label.place(x=300, y=340, anchor="center")

# Footer label
footer_label = Label(root, text="Created by Mukhammadkodir",
                     font=("Arial", 8), fg="black", bg="#dedede")
footer_label.pack(side=BOTTOM, fill=X)

root.mainloop()
