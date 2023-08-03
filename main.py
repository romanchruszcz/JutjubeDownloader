
# all libraries used
import os                       # standard library
from tkinter import *           # standard library
from tkinter import messagebox  # standard library
import pytube                   # pip install pytube
import requests                 # pip install requests
from moviepy.editor import *    # pip install moviepy

# ==================================================     TKINTER GUI    =====================================================================
# Creating window of Jutjube Downloader
root = Tk()
root.geometry("600x310")
root.config(background="#D4D3D2")
root.title("Jutjube Downloader 1.0 (by Roman Chruszcz)")

# ===================================================     FUNCTIONS     =====================================================================

# function to create folder in same place where is located main.py file You're currently using


def folder_creation():
    # os.getcwd() means get current working directory - means giving filepath
    current_directory = os.getcwd()

    x = os.path.exists(current_directory + "\Downloads")
    if x != True:
        os.makedirs(current_directory + "\Downloads")

# function to remove strings from labels used in window


def Clear():
    link_entry.delete(0, END)
    status_label.configure(text="")
    title_label.configure(text="")

# function to gets link from entry box then checking connection status with youtube's link provided using in this case library requests


def Download():
    # trying to get link and connection status code
    try:
        x = link_entry.get()
        a = pytube.YouTube(x)
        r = requests.get(x)
        r2 = r.status_code


# giving and error msg if something is wrong
    except:
        messagebox.showinfo(
            "Error", "Error occured. \nProbably reasons are: \n-no internet \n-wrong link \n-empty link box\nCheck all above and try again.")
        status_label.configure(text="ERROR", foreground="#ff0000")

# checking  which option user chose (1 - high video  or 2 - mp3 file) abd checking if connection status code = 200 (available) and
# checking  if link provided is to youtube service - if its fine then giving labels update
    if status.get() == 1 or status.get() == 2 and r2 == 200 and x[0:20] == "https://www.youtube.":
        # print(status.get())
        status_label.configure(text="LINK LOOKS FINE!")
        title_label.configure(text="Title: " + a.title[0:60])

# once again checking which option is chosen by user (high reso. video mp4  for 1 ) then downloads the file
        try:
            if status.get() == 1:
                youtube_file = a.streams.get_highest_resolution()
                youtube_file.download(os.getcwd() + "\Downloads")
                status_label.configure(text="FILE DOWNLOADED!")
# once again checking which option is chosen by user (mp3  for 2) then downloads the file

            elif status.get() == 2:
                ascii = a.title.isascii()
                if ascii == False:
                    youtube_file = a.streams.get_highest_resolution()
                    youtube_file.download(
                        os.getcwd() + "\Downloads", filename="Your file - please rename.mp4")
                    location = os.getcwd() + "\Downloads\\" + "Your file - please rename" + ".mp4"
# converting file from native mp4 to mp3 extension
                    mp3_file = VideoFileClip(location)
                    mp3_file.audio.write_audiofile(location[:-4] + ".mp3")
                    mp3_file.close()
                    os.remove(location)
                    status_label.configure(text="FILE DOWNLOADED!")
                else:
                    location = os.getcwd() + "\Downloads\\" + a.title + ".mp4"
# converting file from native mp4 to mp3 extension
                    mp3_file = VideoFileClip(location)
                    mp3_file.audio.write_audiofile(location[:-4] + ".mp3")
                    mp3_file.close()
                    os.remove(location)
                    status_label.configure(text="FILE DOWNLOADED!")

# error handling if something is wrong
        except:
            messagebox.showinfo("showinfo", "ERROR")
            status_label.configure(text="ERROR", foreground="#ff0000")
# error handling if something is wrong
    else:
        status_label.configure(text="ERROR", foreground="#ff0000")


# ===================================================     VISUAL PART - GUI     =============================================================

# upper frame creating for the  entry box also for radio buttons and labels
upper_frame = Frame(root, width=580, height=200, highlightbackground="#000000",
                    highlightthickness=1, background="#D4D3D2")
upper_frame.place(x=10, y=10)

# lower frame creating fot the buttons  clear and download
lower_frame = Frame(root, width=340, height=80, highlightbackground="#000000",
                    highlightthickness=1, background="#D4D3D2")
lower_frame.place(x=250, y=220)

# entry box for link
link_entry = Entry(upper_frame, width=80)
link_entry.place(x=45, y=50)

# label under entry box
label1 = Label(upper_frame, width=20,
               text="Paste link above", background="#D4D3D2")
label1.place(x=220, y=70)

# label with status - giving output if everything is fine or there is error
status_label = Label(upper_frame, width=20, text="",
                     background="#D4D3D2", foreground="#3210c9")
status_label.place(x=220, y=20)

# label under entry box and label1  - this one giving title of the downloaded file
title_label = Label(upper_frame, width=50, text="",
                    background="#D4D3D2", foreground="#3210c9", wraplength=400)
title_label.place(x=120, y=100)

# handling chosen option for downloading file
status = IntVar()

# radiobutton for choice nr 1  - high reso. mp4 file
radio_high_res = Radiobutton(upper_frame, text="Download High Resolution MP4 Video File",
                             background="#D4D3D2", variable=status, value=1)
radio_high_res.place(x=45, y=140)

# radiobutton for choice nr 1  - audio only mp4 file
radio_mp3 = Radiobutton(upper_frame, text="Download Mp3 Audio File",
                        background="#D4D3D2", variable=status, value=2)
radio_mp3.place(x=360, y=140)

# button in lower frame thats running function to clear labels texts and entrybox for link
button_clear = Button(lower_frame, width=20, height=3,
                      text="Clear", command=Clear)
button_clear.place(x=10, y=10)

# button in lower frame thats running downloading function
button_download = Button(lower_frame, width=20, height=3,
                         text="Download", command=Download)
button_download.place(x=180, y=10)

# canvas box with my logo
canvas = Canvas(root, width=200, height=80, background="#D4D3D2",
                borderwidth=0, highlightthickness=0)
canvas.place(x=20, y=220)
picture = PhotoImage(file="logo.png")
canvas.create_image(0, 0, anchor=NW, image=picture)


# ===================================================            END            =============================================================
# sets focus on link entry box
link_entry.focus()
# when this program is opened it runs below function (on the beginning of the file) - checking if folder "Downloads" exists in the same file directory as this program
folder_creation()
# keeps this program opened - otherwise it would instantly close after openening this program
root.mainloop()
