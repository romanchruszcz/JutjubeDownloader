
from tkinter import *
import pytube
import requests
# =========================================================================================================================================
root = Tk()
root.geometry("600x310")
root.config(background="#D4D3D2")
root.title("JuTjube Downloader 1.0 (byR.Ch)")
# =========================================================================================================================================


def Clear():
    link_entry.delete(0, END)
    status_label.configure(text="")


def Download():

    x = link_entry.get()
    a = pytube.YouTube(x)
    r = requests.get(x)
    r2 = r.status_code

    try:
        if status.get() == 1 and r2 == 200:
            print(1)
            status_label.configure(text="LINK LOOKS FINE!")
        elif status.get() == 2 and r2 == 200:
            print(2)
            status_label.configure(text="LINK LOOKS FINE!")
    #   else:
    #       pass

        print("titile: ", a.views)
    except:
        pass
# =========================================================================================================================================


upper_frame = Frame(root, width=580, height=200, highlightbackground="#000000",
                    highlightthickness=1, background="#D4D3D2")
upper_frame.place(x=10, y=10)

lower_frame = Frame(root, width=340, height=80, highlightbackground="#000000",
                    highlightthickness=1, background="#D4D3D2")
lower_frame.place(x=250, y=220)

link_entry = Entry(upper_frame, width=80)
link_entry.place(x=45, y=50)

label1 = Label(upper_frame, width=20,
               text="Paste link above", background="#D4D3D2")
label1.place(x=220, y=70)

status_label = Label(upper_frame, width=20,
                     text="", background="#D4D3D2", foreground="#3210c9")
status_label.place(x=220, y=100)
status = IntVar()

radio_high_res = Radiobutton(upper_frame, text="Download High Resolution Video",
                             background="#D4D3D2", variable=status, value=1)
radio_high_res.place(x=45, y=140)

radio_mp3 = Radiobutton(upper_frame, text="Download Mp3 Music File",
                        background="#D4D3D2", variable=status, value=2)
radio_mp3.place(x=360, y=140)


button_clear = Button(lower_frame, width=20, height=3,
                      text="Clear", command=Clear)
button_clear.place(x=10, y=10)

button_download = Button(lower_frame, width=20, height=3,
                         text="Download", command=Download)
button_download.place(x=180, y=10)


canvas = Canvas(root, width=200, height=80, background="#D4D3D2",
                borderwidth=0, highlightthickness=0)
canvas.place(x=20, y=220)
picture = PhotoImage(file="logo.png")
canvas.create_image(0, 0, anchor=NW, image=picture)


# ==========================================================================================================================================
link_entry.focus()
root.mainloop()
