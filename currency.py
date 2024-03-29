# -*- coding: utf-8 -*-
"""Atakan_Çiçek_Final_Projesi

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g8t418e2BNU-1rindz2xPMPczAielbEf

#UYGULAMANIN YERELDE ÇALIŞTIRILMASI GEREKİYOR.
"""

#Basit bir döviz çevirme uygulaması yaptım.
#İlk fonksiyonda uygulamanın arayüzünü oluşturdum.
#Tkinter kullanarak bir arayüz oluşturdum ve uygulamamın içinde olmasını istediğim para birimlerini (CAD, CHF, CZK, EUR, USD ve TRY) ekledim.
#İkinci fonksiyonda seçilen para birimleri arasında gerçekleşecek işlemlerin nasıl olması gerektiğini yazdım.
#“Alphavantage” isimli siteden veri çekebilmek için bir api key ve base url aldım. Ardından “url” isimli değişkene elde etmek istediğim linki atadım.
#“Alphavantage” sitesinden para birimlerinin anlık değerlerini çekebilmek ve bu verileri uygulamama yansıtabilmek için requests ve json modüllerini kullandım.
#Son olarak da “Miktar Giriniz” kısmına istenilmeyen bir değer girildiğinde ve internet bağlantısı olmadığında
#“alphavantage” sitesinden veri çekilemediği için “messagebox” kullanarak birer mesaj kutusu yazdım.



import requests, json
import tkinter as tk
from tkinter import messagebox
from tkinter import *
    
def createWidgets():

    paraBirimleri = ["CAD","CHF", "CZK", "EUR", "USD", "TRY"]

    baslik = Label(root, text="Döviz Çevirme Uygulamasına Hoşgeldiniz", bg="#FFFF8C")
    baslik.grid(row=1, column=1, pady=10)

    miktar = Label(root, text="Miktar Giriniz:", bg="#81D68B")
    miktar.grid(row=2, column=0, padx=20, pady=10)

    global miktarGir
    miktarGir = Entry(root, width=40, textvariable=miktar1)
    miktarGir.grid(row=2, column=1, padx=20, pady=10)

    paraBiriminden = Label(root, text="Şu Para Biriminden:", bg="#81D68B")
    paraBiriminden.grid(row=3, column=0, padx=20, pady=10)
    
    paraBiriminden2 = OptionMenu(root, variable1, *paraBirimleri)
    paraBiriminden2.grid(row=3, column=1, padx=20, pady=10)

    paraBirimine = Label(root, text="Şu Para Birimine:", bg="#81D68B")
    paraBirimine.grid(row=4, column=0, padx=20, pady=10)
    
    paraBirimine2 = OptionMenu(root, variable2, *paraBirimleri)
    paraBirimine2.grid(row=4, column=1, padx=20, pady=10)

    donustur = Button(root, width=15, text="Dönüştür", command=islem, bg="#FFFF8C")
    donustur.grid(row=6, columns=4, padx=10, pady=10)

    donusturMetin = Label(root, text="Döviz Miktarı:", bg="#81D68B")
    donusturMetin.grid(row=5, column=0, padx=20, pady=10)
    
    global miktarGir2
    miktarGir2 = Entry(root, width=40)
    miktarGir2.grid(row=5, column=1, pady=10)
    
    sıfırla = Button(root, text="Sıfırla", width=10, command=clear, bg="#A4B8BA")
    sıfırla.grid(row=5, column=2, pady=10)
         

def islem():
    
    apiKey = "VN37DNR2N76KQXDI"
    link = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"   
    var1 = variable1.get()
    var2 = variable2.get()

    url = link+"&from_currency="+var1+"&to_currency="+var2+"&apikey=" + apiKey

    req_ob = requests.get(url)
    sonuc = req_ob.json()
    
    try:
        Exchange_rate = float(sonuc["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    except:
        messagebox.showwarning(title="Hata!", message="Guncel doviz kuru cekilirken hata meydana geldi! Internet baglantinizi kontrol edin.")
        return
    
    try:
        x = float(miktar1.get())
    except:
        messagebox.showwarning(title="Hata!", message="Lütfen Geçerli Bir Değer Giriniz.")
        return
    new_amount = round(x*Exchange_rate, 3)

    miktarGir2.insert(0, str(new_amount))

def clear():

    miktarGir.delete(0, END)
    miktarGir2.delete(0, END)

root = tk.Tk()
root.geometry("550x300")
root.title("Döviz Çevirici")
root.config(background="#43084f")

miktar1 = StringVar()
variable1 = StringVar()
variable2 = StringVar()
variable1.set("seçiniz")
variable2.set("seçiniz")


createWidgets()

root.mainloop()