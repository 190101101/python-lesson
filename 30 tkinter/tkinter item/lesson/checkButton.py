import tkinter as tk

window = tk.Tk()
window.title('tkinter basic')
window.geometry('600x300')

btn1 = tk.Checkbutton(master=window, text='yes')
btn1.grid(row=0, column=0)

btn2 = tk.Checkbutton(master=window, text='no')
btn2.grid(row=0, column=1)


window.mainloop()