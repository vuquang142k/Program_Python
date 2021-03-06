from tkinter import *

def changeanswer():
    if etime.get()=='':
        pass
    else:
        if measure.get()=='kmh':
            t,m=etime.get().split()
            if m=='s':
                tm=str(float(t)/3600)+' h'
                etime.delete(0,END)
                etime.insert(0,tm)
        else:
            t,m=etime.get().split()
            if m=='h':
                tm=str(float(t)*3600)+' s'
                etime.delete(0, END)
                etime.insert(0, tm)

def timecalc():
    v=float(ebspeed.get())-float(ewspeed.get()) if curvar.get()\
        else float(ebspeed.get())+float(ewspeed.get())
    t=float(edist.get())/v
    ans=str(t)+' '+measure.get()[-1]
    etime.delete(0,END)
    etime.insert(0,ans)

window=Tk()

#label and entry for ship and water speeds
lbspeed=Label(window,text='Скорость лодки')
ebspeed=Entry(window)
lwspeed=Label(window,text='Скорость воды')
ewspeed=Entry(window)

lbspeed.grid(row=0,column=0)
ebspeed.grid(row=0,column=1)
lwspeed.grid(row=1,column=0)
ewspeed.grid(row=1,column=1)

#ship direction
curvar=BooleanVar()
cbcurrent=Checkbutton(window,text='Против течения?',variable=curvar)
cbcurrent.grid(row=2,column=0,columnspan=2)

#dist
lsidt=Label(window,text='Длина маршрута')
edist=Entry(window)
lsidt.grid(row=3,column=0)
edist.grid(row=3,column=1)

#measure of speed
measure=StringVar()
rbmeasure1=Radiobutton(window,text='km/h',variable=measure,value='kmh',command=changeanswer)
rbmeasure2=Radiobutton(window,text='m/s',variable=measure,value='ms',command=changeanswer)
rbmeasure1.grid(row=4,column=0,sticky=N+W)
rbmeasure2.grid(row=5,column=0,sticky=N+W)

#button
btnanswer=Button(window,text='Вычислить',command=timecalc)
btnanswer.grid(row=6,column=1)

#answer
ltime=Label(window,text='Время движения')
etime=Entry(window)
ltime.grid(row=7,column=0)
etime.grid(row=7,column=1)


window.mainloop()
