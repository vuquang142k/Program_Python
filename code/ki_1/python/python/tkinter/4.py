from tkinter import *
window=Tk()
window.title('Example')
window.geometry('600x400+100+200')
import tkinter.messagebox as box
def helloinfo():
    box.showinfo('Sun',"Hello!")
def byeinfo():
    box.showinfo('Sun','Good bye!')
def dayinfo():
    box.showinfo('Sun','9!')
def monthinfo():
    box.showinfo('Sun','December!')
def yearinfo():
    box.showinfo('Sun',str(2019+offset))
mmenu=Menu(window)

fmenu=Menu(mmenu)
fmenu.add_command(label='Hi!',command=helloinfo)
fmenu.add_command(label='Bye!',command=byeinfo)
fmenu.add_separator()
fmenu.add_command(label='Exit!',command=exit)
mmenu.add_cascade(label='File',menu=fmenu)

emenu=Menu(mmenu)
emenu.add_command(label='Day!',command=dayinfo)
emenu.add_command(label='Month!',command=monthinfo)

eymenu=Menu(emenu)
eymenu.add_command(label='Last',command=lambda:yearinfo(0))
eymenu.add_command(label='Now!',command=lambda:yearinfo(1))
eymenu.add_command(label='Next!',command=lambda:yearinfo(2))
emenu.add_cascade(label='Year!',menu=eymenu)

mmenu.add_cascade(label='Edit',menu=emenu)
window.config(menu=mmenu)
window.mainloop()
