import tkinter as tk
from tkinter import Frame

window = tk.Tk()
window.title('tkinter basic')
window.geometry('600x300')


frame = Frame(window)

#
btnleft = tk.Button(master=frame, text='frame button left', bg='black', fg='white')
btnleft.pack(side=tk.LEFT)

#
btnright = tk.Button(master=frame, text='frame button right', bg='black', fg='white')
btnright.pack(side=tk.RIGHT)


frame.pack()

window.mainloop()