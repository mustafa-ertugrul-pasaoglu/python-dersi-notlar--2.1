
from tkinter import *
master = Tk()

canvas = Canvas(master , height=450 , width=750)
canvas.pack()

frame_ust = Frame(master , bg="#eab676")
frame_ust.place(relx=0.1 , rely=0.1 , relheight=0.1 , relwidth=0.74)

frame_altsol = Frame(master , bg="#eab676")
frame_altsol.place(relx=0.1 , rely=0.21 , relheight=0.56 , relwidth=0.23)

frame_altsağ = Frame(master , bg="#eab676")
frame_altsağ.place(relx=0.34 , rely=0.21 , relheight=0.56 , relwidth=0.5)



master.mainloop()

