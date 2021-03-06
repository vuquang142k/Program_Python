from tkinter import *
window=Tk()
window.title('Example')
window.geometry('600x400+100+200')
import tkinter.messagebox as box
def dialog():
    print(chint)
    if chint.get()==1:
        box.showinfo('Sun','Today it is sunny')
    else:
        box.showwarning('Cloud','Today it is cloudy')
chint=IntVar()
ch1=Checkbutton(window,text='Sun?',variable=chint)
ch1.pack()
btn=Button(window,text='An nut',command=dialog)
btn.pack(padx=150,pady=50)
window.mainloop()
