
from cProfile import label
from tkinter import *
from turtle import left
master = Tk()

canvas = Canvas(master , height=450 , width=750)
canvas.pack()

frame_ust = Frame(master , bg="#eab676")
frame_ust.place(relx=0.1 , rely=0.1 , relheight=0.1 , relwidth=0.75)

frame_alt = Frame(master , bg="#eab676")
frame_alt.place(relx=0.1 , rely=0.21 , relheight=0.56 , relwidth=0.75)

giris_etiketi = Label(frame_ust, bg ="#eab676", text ="Giriş yapmak için şifrenizi aşağı giriniz", font="Verdana 12 bold")
giris_etiketi.pack(padx=5 , pady=5 , side=LEFT)

giris_etiketi_opsiyon = StringVar(frame_ust)
giris_etiketi_opsiyon.set = ("\t")

#giris_etiketi_opsiyon_açılır_menü = OptionMenu(
 #   frame_ust,
  #  giris_etiketi_opsiyon,
   # "E posta  ",
    #"Banka şifresi ",
    #"Hesap numarası")
#giris_etiketi_opsiyon_açılır_menü.pack(padx=10 , pady=10 , side=RIGHT)



master.mainloop()

