import sys
import os
from time import sleep
from tkinter import *


glowne_okno = Tk()
glowne_okno.title("Wykrywacz mrugnięć")
glowne_okno.geometry("800x500")

litery="abcdefghijklmnoprstuwxyz"

def wyswietlanie_liter():
    while True:
        for i in range(len(litery)):
            label = Label(glowne_okno, text=litery[i], font=30, fg="blue")
            label.pack()
            label.place(x=380, y=200)
            print(litery[i])
            sleep(1)
            label.after(1000, litery[i].destroy)
            i+1
            print(litery[i])
            label.mainloop()

glowne_okno.mainloop()
