import tkinter as tk
from tkinter import Text

window = tk.Tk()
window.title('tkinter basic')
window.geometry('600x300')


txt = Text(window, height=2, width=40)

txt.pack()


window.mainloop()