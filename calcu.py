from tkinter import *
import tkinter.font as font
import math

root =  Tk()
root.title("Simple Calculator")
root.geometry("310x400")
root["bg"] = "#d1d1d1"

myfont = font.Font(size=15)

e = Entry(root,width=23,borderwidth=5)
e["font"] = myfont
e["bg"] = "#fff"
e.grid(row=0,column=0,columnspan=4,padx=20,pady=20)

def angka(nilai):
    sebelum = e.get()
    e.delete(0,END)
    e.insert(0,str(sebelum)+str(nilai))
def tambah():
   no_awal = e.get()
   global n_awal
   global mtk
   mtk = "penjumlahan"
   n_awal = int(no_awal)
   e.delete(0,END)
def kurang():
   no_awal = e.get()
   global n_awal
   global mtk
   mtk = "pengurangan"
   n_awal = int(no_awal)
   e.delete(0,END)
def kali():
   no_awal = e.get()
   global n_awal
   global mtk
   mtk = "perkalian"
   n_awal = int(no_awal)
   e.delete(0,END)
def bagi():
   no_awal = e.get()
   global n_awal
   global mtk
   mtk = "pembagian"
   n_awal = int(no_awal)
   e.delete(0,END)
def akar():
   no_awal = e.get()
   global n_awal
   n_awal = int(no_awal)
   e.delete(0,END)
   e.insert(0,math.sqrt(n_awal))
def sisa():
   no_awal = e.get()
   global n_awal
   global mtk
   mtk = "sisa"
   n_awal = int(no_awal)
   e.delete(0,END)
def pangkat():
   no_awal = e.get()
   global n_awal
   n_awal = int(no_awal)
   e.delete(0,END)
   e.insert(0,n_awal **2)
def hapus():
   e.delete(0,END)
def samadgn():
   no_akhir = e.get()
   e.delete(0,END)
   if mtk =="penjumlahan":
       e.insert(0, n_awal + int(no_akhir))
   elif mtk =="pengurangan":
       e.insert(0, n_awal - int(no_akhir))
   elif mtk =="perkalian":
       e.insert(0, n_awal * int(no_akhir))
   elif mtk =="pembagian":
       try:
           hitung = n_awal / int(no_akhir)
           e.insert(0,hitung)
       except ZeroDivisionError:
           e.insert(0,'ERROR')
   elif mtk =="sisa":
       e.insert(0, n_awal % int(no_akhir))

       


btn1 = Button(root,text="1",padx=30,pady=20,command=lambda:angka(1))
btn2 = Button(root,text="2",padx=30,pady=20,command=lambda:angka(2))
btn3 = Button(root,text="3",padx=30,pady=20,command=lambda:angka(3))
btn4 = Button(root,text="4",padx=30,pady=20,command=lambda:angka(4))
btn5 = Button(root,text="5",padx=30,pady=20,command=lambda:angka(5))
btn6 = Button(root,text="6",padx=30,pady=20,command=lambda:angka(6))
btn7 = Button(root,text="7",padx=30,pady=20,command=lambda:angka(7))
btn8 = Button(root,text="8",padx=30,pady=20,command=lambda:angka(8))
btn9 = Button(root,text="9",padx=30,pady=20,command=lambda:angka(9))
btn0 = Button(root,text="0",padx=30,pady=20,command=lambda:angka(0))
tbh = Button(root,text="+",padx=30,bg="#3d3d3d",fg="#fff",pady=20,command=tambah)
akr = Button(root,text="sq2",padx=30,bg="#3d3d3d",fg="#fff",pady=20,command=akar)
sis = Button(root,text="//2",padx=20,bg="#3d3d3d",fg="#fff",pady=20,command=sisa)
pgk = Button(root,text="x2",padx=30,bg="#3d3d3d",fg="#fff",pady=20,command=pangkat)
krg = Button(root,text="-",padx=30,bg="#3d3d3d",fg="#fff",pady=20,command=kurang)
kli = Button(root,text="x",padx=30,bg="#3d3d3d",fg="#fff",pady=20,command=kali)
bgi = Button(root,text="/",padx=30,bg="#3d3d3d",fg="#fff",pady=20,command=bagi)
hps = Button(root,text="AC",padx=30,bg="#3d3d3d",fg="#fff",pady=20,command=hapus)
sdg = Button(root,text="=",padx=30,bg="#3d3d3d",fg="#fff",pady=20,command=samadgn)

btn1.grid(row=3,column=0,pady=2)
btn2.grid(row=3,column=1,pady=2)
btn3.grid(row=3,column=2,pady=2)
btn4.grid(row=2,column=0,pady=2)
btn5.grid(row=2,column=1,pady=2)
btn6.grid(row=2,column=2,pady=2)
btn7.grid(row=1,column=0,pady=2)
btn8.grid(row=1,column=1,pady=2)
btn9.grid(row=1,column=2,pady=2)
btn0.grid(row=4,column=1,pady=2)
tbh.grid(row=1,column=3,pady=2)
krg.grid(row=2,column=3,pady=2)
kli.grid(row=3,column=3,pady=2)
bgi.grid(row=4,column=3,pady=2)
hps.grid(row=4,column=0,pady=2)
sdg.grid(row=5,column=2,pady=2)
akr.grid(row=5,column=0,pady=2)
sis.grid(row=4,column=2,pady=2)
pgk.grid(row=5,column=1,pady=2)


root.mainloop()