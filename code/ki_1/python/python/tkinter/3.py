from tkinter import *
window=Tk()
window.title('Example')
window.geometry('600x400+100+200')
import tkinter.messagebox as box
def show():
    box.showinfo('Sun','You like'+var.get())
var=StringVar()
R1=Radiobutton(window,text='Pascal',variable=var,value='Pascal',command=show)
R1.pack(anchor=W)
R2=Radiobutton(window,text='C',variable=var,value='C',command=show)
R2.pack(anchor=W)
R3=Radiobutton(window,text='Python',variable=var,value='Python',command=show)
R3.pack(anchor=W)

window.mainloop()
