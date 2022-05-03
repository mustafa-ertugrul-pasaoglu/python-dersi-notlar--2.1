
from tkinter import *
master = Tk()

canvas = Canvas(master , height=450 , width=750)
canvas.pack()

frame_ust = Frame(master , bg="#eab676")
frame_ust.place(relx=0.1 , rely=0.1 , relheight=0.1 , relwidth=0.75)


master.mainloop()

