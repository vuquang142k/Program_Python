from tkinter import *
root = Tk()

C = Canvas(root, width=800, height=800, bg='white')

#bg--цвет фона
#bd--границы (толщина)
#height--высота холста
#width--ширина
#cursor--типа курсора мыши

#Линии
C.create_line(10, 610, 190, 650)

C.create_line(500,580, 500, 460, fill='green',width=5, dash=(10, 2),activefill='lightgreen',arrowshape="10 20 10")

#Прямоугольник
x=600
y=120
C.create_rectangle(x,y,x+80,y+50,fill='chocolate',outline='violet')

#окружности, овалов
C.create_oval([20,200],[150,300],fill='gray50') #elip
C.create_oval(550, 610, 650, 710, width=2)
C.create_oval(510, 720, 690, 790,fill='grey70', outline='white')

#секторы
coord=310,350,540,510
arc=C.create_arc(coord,start=0,extent=150,fill='red')
#extend--размер угла
#start--угол начала рисования дуги
#style--по умолчанию сектор, ARC--дуга, CHORD--сегмент
#fill,outline

#Текст
C.create_text(20,330,text='Опыты с графическими примитивами\nна холсте',font='Verdana 12',anchor='w',justify=CENTER ,fill='red')
#Многоугольник
C.create_polygon([250,100],[200,150],[300,150],fill='yellow')
C.create_polygon([300,80],[400,80],[450,75],[450,200],[300,180],[330,160],outline='orange',smooth=1)
C.create_polygon((40, 710), (160, 710), (190, 780), (10, 780),fill='orange', outline='black')

C.create_oval(10, 10, 190, 190,fill='lightgrey',outline='white')
C.create_arc(10, 10, 190, 190, start=0, extent=45, fill='red')
C.create_arc(10, 10, 190, 190, start=180, extent=25, fill='orange')
C.create_arc(10, 10, 190, 190, start=240, extent=100, style=CHORD, fill='green')
C.create_arc(10, 10, 190, 190, start=160, extent=-70, style=ARC, outline='darkblue', width=5)

C.pack()

root.mainloop()
