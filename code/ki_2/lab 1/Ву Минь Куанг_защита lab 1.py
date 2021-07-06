#Программа сделана Ву Минь Куанг, ИУ7-24Б

from tkinter import *
import tkinter.messagebox as box

key=['1','0']
def donothing():
    pass

def calc():
    t1=innumEntry.get()
    t=list(t1)
    for i in range(len(t)):
        if t[1] not in key:
            box.showinfo('Error','Ввод error')
            return
    if t1[0]=='0':
        t2=''.join(t)
        t3=''.join(t)
    else:
        for i in range(1,len(t)):
            if t[i]=='0':
                t[i]='1'
            else:
                t[i]='0'
        t2=''.join(t)
        i=len(t)-1
        k=0
        while k==0:
            if t[i]=='0':
                t[i]='1'
                k=1
            else:
                t[i]='0'
                k=0
            i -=1
        t3=''.join(t)
    ansEntry1.delete(0,END)
    ansEntry1.insert(0,t1)
    ansEntry2.delete(0,END)
    ansEntry2.insert(0,t2)
    ansEntry3.delete(0,END)
    ansEntry3.insert(0,t3)

def showinfo1():
    box.showinfo('Info', 'Программа сделана Ву Минь Куанг.')

def showinfo2():
    box.showinfo('Info', 'Перевод заданного числа из 10-й сс в 5-ю и обратно')

window = Tk()
window.geometry("600x400+150+150")

innumLabel = Label(window, text = 'Ввод')
innumEntry = Entry(window, width= 50)
innumLabel.place(x = 50, y = 0)
innumEntry.place(x = 100, y = 0)

calcButton=Button(window,text='Вычислить',command=calc)
calcButton.place(x = 200, y = 100)

ansLabel1=Label(window,text='прямой')
ansEntry1=Entry(window, width = 40)
ansLabel1.place(x = 50, y = 150)
ansEntry1.place(x = 150, y = 150)

ansLabel2=Label(window,text='обратный')
ansEntry2=Entry(window, width = 40)
ansLabel2.place(x = 50, y = 250)
ansEntry2.place(x = 150, y = 250)

ansLabel3=Label(window,text='дополнительный')
ansEntry3=Entry(window, width = 40)
ansLabel3.place(x = 50, y = 350)
ansEntry3.place(x = 150, y = 350)

menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=window.destroy)
menubar.add_cascade(label='File', menu = filemenu)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu = editmenu)

infomenu = Menu(menubar, tearoff=0)
infomenu.add_command(label='О авторе', command=showinfo1)
infomenu.add_command(label='О программе', command=showinfo2)
menubar.add_cascade(label='Info', menu = infomenu)

window.config(menu=menubar)
window.mainloop()
