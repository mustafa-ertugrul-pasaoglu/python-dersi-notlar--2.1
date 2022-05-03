
from cProfile import label
from tkinter import *
from tkinter.font import BOLD
from turtle import left
master = Tk()
canvas = Canvas(master , height=450 , width=750)
canvas.pack()

frame_ust = Frame(master , bg="#eab676")
frame_ust.place(relx=0.1 , rely=0.1 , relheight=0.1 , relwidth=0.75)

frame_alt = Frame(master , bg="#eab676")
frame_alt.place(relx=0.1 , rely=0.21 , relheight=0.56 , relwidth=0.75)

giris_etiketi = Label(frame_ust, bg ="#eab676", text ="Uludağ banka hoşgeldiniz.", font="Verdana 12 bold")
giris_etiketi.pack(padx=10 , pady=10 , side=TOP)

#giris_etiketi_opsiyon = StringVar(frame_ust)
#giris_etiketi_opsiyon.set = ("\t")

#giris_etiketi_opsiyon_açılır_menü = OptionMenu(
 #   frame_ust,
  #  giris_etiketi_opsiyon,
   # "E posta  ",
    #"Banka şifresi ",
    #"Hesap numarası")
#giris_etiketi_opsiyon_açılır_menü.pack(padx=10 , pady=10 , side=RIGHT)
sifre_yazısı = Label(frame_alt, bg="#eab676", text ="Lütfen şifrenizi giriniz" , font="Verdana 12 bold")
sifre_yazısı.pack(padx=10 , pady=50 , side=TOP)

metin_alanı = Text(frame_alt , height=2 , width=30)
metin_alanı.tag_configure("style", foreground ="#eab676", font=("Verdana" , "12" , "bold" ))
metin_alanı.pack()


karşılama_metni = "şifrenizi buraya giriniz..."
metin_alanı.insert(END , karşılama_metni , "style")

giriş_butonu = Button(frame_alt, text="Giriş", command=master.destroy)
giriş_butonu.pack(anchor=S)

master.mainloop()
print("yazdım oldumu")


