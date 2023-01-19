import tkinter as tk
from tkinter import Label, Entry

window = tk.Tk()
window.title('tkinter basic')
window.geometry('600x300')

#
lbad = Label(master=window, text='adi')
lbsoyad = Label(master=window, text='soyadi')

#
entad = Entry(window)
entsoyad = Entry(window)

#
lbad.grid(row=0, column=0)
entad.grid(row=0, column=1)

#
lbsoyad.grid(row=1, column=0)
entsoyad.grid(row=1, column=1)


window.mainloop()