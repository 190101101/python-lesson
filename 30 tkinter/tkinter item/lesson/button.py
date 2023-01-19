import tkinter as tk

window = tk.Tk()
window.title('tkinter basic')
window.geometry('600x300')

btn = tk.Button(master=window,
			 text='close',
			 width=25,
			 height=5,
			 bg='green',
			 fg='white', 
			 command=window.destroy)
btn.pack()

window.mainloop()