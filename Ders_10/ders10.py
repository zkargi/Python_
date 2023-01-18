"""
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
global secilen,baslangictarihi,bitistariH
ekran =tk.Tk()
ekran.resizable(width=True,height=True)
ekran.geometry("800x800")
pariteler=["ust","asd","asd","asd"]
parite_sec = tk.Label(ekran, text="parite seciniz")
parite_sec.pack(padx=10,pady=10)
combo = ttk.Combobox(ekran, values=pariteler)
combo.pack()
baslangic_sec = tk.Label(ekran, text="baslangic tarihi giriniz")
baslangic_sec.pack(padx=10,pady=10)
date_entry1 = DateEntry(ekran)
date_entry1.pack(padx=10,pady=10)

bitis_sec = tk.Label(ekran, text="bitis tarihi giriniz")
bitis_sec.pack(padx=10,pady=10)
date_entry2 = DateEntry(ekran)
date_entry2.pack(padx=10,pady=10)

def kaydet():
    secilen=combo.get()
    baslangictarih=date_entry1.get()
    bitistariH=date_entry2.get()
    print(secilen)
    print(baslangictarih)
    print(bitistariH)

kaydet=tk.Button(ekran,text="kaydet",bg="blue",width=20,height=3,command=kaydet)
kaydet.pack(padx=10,pady=10)

ekran.update()
ekran.mainloop()"""

from tkinter import *


# Pencere oluşturma
from tkcalendar import DateEntry

pencere = Tk()



pencere.geometry('500x400')

lbl = Label(pencere, text="Parite")
lbl.grid(column=0, row=0)

tarih_bas = StringVar()
tarih_bit = StringVar()

lbl22 = Label(pencere, text="Başlangıç Tarihi")
lbl22.grid(column=0, row=1)

cal=DateEntry(pencere, selectmode='day', textvariable=tarih_bas)
cal.grid(row=1, column=1, padx=15)

lbl33 = Label(pencere, text="Bitiş Tarihi")
lbl33.grid(column=0, row=2)

cal2=DateEntry(pencere, selectmode='day', textvariable=tarih_bit)
cal2.grid(row=2, column=1, padx=15)

def tiklandi():
    parite = variable.get()
    tarih_baslangic = tarih_bas.get()
    tarih_bitis = tarih_bit.get()

    pass

btn2 = Button(pencere, text="Grafik Çiz",
              bg="orange", fg="red",
              command=tiklandi
              )

btn2.grid(column=1, row=3)

variable = StringVar(pencere)
variable.set("BTCUSDT") # default value



# Seçenek kutusu oluşturma
secenekler = ["BTCUSDT", "ETHUSDT", "ADAUSDT"]
secenek_kutusu = OptionMenu(pencere,
                            variable,
                            *secenekler)

secenek_kutusu.grid(column=1, row=0)



# Seçenek kutusunu pencereye ekleme

# Pencereyi ekranda gösterme
pencere.mainloop()