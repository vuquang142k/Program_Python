#На плоскости задано множество точек. Найти треугольник, построенный на этих
#точках, в котором самый большой угол.
#Дать графическое изображение результатов.

#Программа сделана Ву Минь Куанг ИУ7-24Б

from tkinter import *
from tkinter import messagebox
from math import *
from itertools import *

def trian_side1(a, b, c):
    ab_side = sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    bc_side = sqrt((c[0]-b[0])**2+(c[1]-b[1])**2)
    ca_side = sqrt((a[0]-c[0])**2+(a[1]-c[1])**2)
    return ab_side, bc_side, ca_side

def is_trian(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        return True
    else:
        return False

def list_get(rang):
    try:
        list_a_b = [float(x) for x in rang.get().strip().split()]
        
        if len(list_a_b) == 0 or isinstance(list_a_b, (str, type(None))):
            messagebox.showerror('Ошибка ввода данных','Проверьте введенные данные')
        return list_a_b
    except:
        messagebox.showerror('Ошибка ввода данных','Проверьте введенные данные')

def draw(entry_1, roots):
    window = Toplevel(roots)
    window['bg'] = '#d0f0c0'
    window.grab_set()
    window.geometry('600x750+500+0')
    window.title('Triangle visualization')

    C = Canvas(window, width=800, height=800, bg='white')
    if ((len(entry_1) % 2)):
        messagebox.showerror('Ошибка ввода данных','Проверьте введенные данные')
        return False

    list_x = entry_1[::2]
    list_y = entry_1[1::2]
    
    entry_xy = [ (list_x[i], list_y[i])
                    for i in range (len(list_x))]
    x_min=min(list_x)
    x_max=max(list_x)
    y_min=min(list_y)
    y_max=max(list_y)

    inter_x = (600 - 50)/(x_max - x_min)
    inter_y = (600 - 50)/(y_max - y_min)
    o_x = -x_min * inter_x + 25
    o_y = -y_min * inter_y + 25

    for i in range(len(list_x)):
        x = list_x[i] * inter_x + o_x
        y = (list_y[i] * inter_y + o_y)
        C.create_oval(x-6,y-6,x+6,y+6,fill='#b3007d')

    min_trial = 2
    list_trial=[]
    for i in range(len(entry_xy)):
        for j in range(len(entry_xy)):
            for k in range(len(entry_xy)):
                ab, bc, ca =trian_side1(entry_xy[i], entry_xy[j], entry_xy[k])
                if is_trian(ab, bc, ca):
                    cos_A = (ab**2+ca**2-bc**2)/(ab*ca*2)
                    cos_B = (bc**2+ab**2-ca**2)/(ab*bc*2)
                    cos_C = (bc**2+ca**2-ab**2)/(bc*ca*2)
                    min_coner = min(cos_A,cos_B,cos_C)
                    if min_coner < min_trial:
                        min_trial = min_coner
                        list_trial = [entry_xy[i], entry_xy[j], entry_xy[k]]

    rez_draw_xy = list()
    for i in range(len(list_trial)):
        rez_draw_xy.append(list_trial[i][0]*inter_x + o_x) 
        rez_draw_xy.append((list_trial[i][1]*inter_y + o_y))
            
    C.create_line(rez_draw_xy[0], rez_draw_xy[1],
                    rez_draw_xy[2], rez_draw_xy[3], width = 3,
                    fill = 'green')

    C.create_line(rez_draw_xy[2], rez_draw_xy[3], rez_draw_xy[4],
                    rez_draw_xy[5], width = 3, fill = 'green')
                    
    C.create_line(rez_draw_xy[4], rez_draw_xy[5], rez_draw_xy[0],
                    rez_draw_xy[1], width = 3, fill = 'green')

    C.pack()

def find():
    entry_1 = list_get(set_entry)
    try:
        kol = int (kol_entry.get())
        if (len(entry_1) != kol * 2):
            messagebox.showerror('Ошибка ввода данных','Проверьте введенные данные')
            return False
    except:
        messagebox.showerror('Ошибка ввода данных','Проверьте введенные данные')
        return False
    draw(entry_1, roots)

def debug():
    global root, c, xy
    root = 0
    c1 = 0     
    xy = list()

def paint_points(event):
    global xy,c1
    x1, y1 = (event.x - 6), (event.y - 6)
    x2, y2 = (event.x + 6), (event.y + 6)
    if str(event.widget) != ".!canvas":
        return event
    xy.append(event.x)
    xy.append(event.y)
    c1.create_oval(x1, y1, x2, y2, fill="orange")
    return event
  
def check_points():
    global xy, c1,root
    root = Tk()
    root['bg'] = '#f50'
    root.geometry('600x600')
    root.title("Geometric task")
    c1 = Canvas(root, width=400, height=400, bg="white")
    width = 400
    height = 400
    for line in range(0, width, 20):
        c1.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')
    for line in range(0, height, 20):
        c1.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')
    c1.pack()
    root.bind('<Button-1>', paint_points)
    e_but =  Button(root, text='Найти треугольник',
        font='consolas 12', command = lambda: draw(xy, root))
    e_but.pack()
    exit_but =  Button(root, text='Exit',
            font='consolas 12', command=root.destroy)
    exit_but.pack()
    root.mainloop()

def draw_point():
    debug()
    check_points()

def showinfo1():
    messagebox.showinfo('Info', 'Программа сделана Ву Минь Куанг.')

roots = Tk()
roots.geometry('800x600+400+100')
roots.title('Example')

roots_label = Label(roots,text = 'Нахождение треугольника по условию',font = 'consolas 14',fg = 'black')
roots_label.place(x = 250, y = 0)

kol_label = Label(roots,text = 'Введите количество точек',font = 'consolas 12',fg = 'black')
kol_label.place(x = 200, y = 70)

kol_entry = Entry(roots, width = 100)
kol_entry.place(x = 60, y = 100)

set_label = Label(roots,text = 'Введите координаты точек множества',font = 'consolas 12',fg = 'black')
set_label.place(x = 200, y = 150)

set_entry = Entry(roots, width = 100)
set_entry.place(x = 60, y = 180)

vis_button = Button(roots,text = 'Найти треугольник',font = 'consolas 12',bg = 'white',fg = 'black',command=find)
vis_button.place(x = 300, y = 250)

paintButton = Button(roots,text = 'Paint points',font = 'consolas 12',bg = 'white',fg = 'black', command=draw_point)
paintButton.place(x = 300, y = 300)

exit_button =  Button(roots,text='Exit',font='consolas 12',bg = 'white',fg = 'black',command = lambda: roots.destroy())
exit_button.place(x = 345, y = 350)

menubar = Menu(roots)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=roots.destroy)
menubar.add_cascade(label='File', menu = filemenu)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu = editmenu)

infomenu = Menu(menubar, tearoff=0)
infomenu.add_command(label='О авторе', command=showinfo1)
menubar.add_cascade(label='Info', menu = infomenu)

roots.config(menu=menubar)

roots.mainloop()