from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.configure(bg='black')

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'black',
            foreground = 'white',
            padx=10,
            pady=10,
            borderwidth=0,
            highlightthickness=0)

lbl.pack(anchor = 'center')
time()

def toggle_theme():
    if root.cget('bg') == 'black':
        root.configure(bg='white')
        lbl.configure(bg='white', fg='black')
    else:
        root.configure(bg='black')
        lbl.configure(bg='black', fg='white')

btn = Button(root, text="Toggle Theme", command=toggle_theme)
btn.pack(side=BOTTOM)

mainloop()
