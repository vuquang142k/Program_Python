#Уточнение корней
#Определить корни заданной функции методом простых итераций

# Переменные:
# a,b - общий рассматриваемый участок функции
# h - шаг локального участка функции
# eps - точность эпсилон
# n_max - максимальное число итераций
# a_cur - конечная точка рассматриваемого участка
# x_cur - текущий корень локального участка функции
# x_prev - предыдущий корень локального участка
# error - возможная ошибка
# n - промежуточная переменная
# root - окно таблицы
# window - окно таблицы ввода
# entry_a, entry_b, entry_eps - поля ввода начальных значений
# hg - начальное приближение к корню
# frame1..7 - место размещение виджетов в окне ввода значений
# label_ - метки, поясняющие определенные места в окне программы
# entry_ - поля ввода значений
# root - окно таблицы нахождения корней
# peregib - существование точки перегиба на рассматриваемом участке


from math import sin, fabs

from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np



def Table_creator():
    root = Tk()
    try:
        root.close()
    except:
        pass
    treeview = ttk.Treeview(root)
    treeview.pack()
    root.title('Таблица')
    treeview["columns"]=("one","two","three","four","five","six")
        
    treeview.column("#0", width=50, minwidth=50, stretch=tk.NO)
    treeview.column("one", width=80, minwidth=80, stretch=tk.NO)
    treeview.column("two", width=80, minwidth=80)
    treeview.column("three", width=100, minwidth=50, stretch=tk.NO)
    treeview.column("four", width=80, minwidth=50, stretch=tk.NO)
    treeview.column("five", width=80, minwidth=50, stretch=tk.NO)
    treeview.column("six", width=300, minwidth=100, stretch=tk.NO)

    treeview.heading("#0",text="Номер корня",anchor=tk.W)
    treeview.heading("one",text="Левая граница",anchor=tk.W)
    treeview.heading("two",text="Правая граница",anchor=tk.W)
    treeview.heading("three",text="Значение корня",anchor=tk.W)
    treeview.heading("four",text="Значение функции",anchor=tk.W)
    treeview.heading("five",text="Число итераций",anchor=tk.W)
    treeview.heading("six",text="Код ошибки",anchor=tk.W)
    return(treeview)



def g(x, x0): # Функция вида x = fi(x)
    try:
        y = x - (f(x) / x0)
    except:
        
        return(x - f(x))
    return (x - (f(x) / x0))

def df(x):
    try:
        y = 2 * x
    except:
        return(False)
    return(2 * x)

def f(x): # Исходная функция
    try:
        y = x * x - 4
    except:
        return(False)
    return(x * x - 4)

def ddf(x): # Вторая производная от исходной функции
    try:
        y = 2
    except:
        return(False)
    return(2)

def ddg1(x): # Функция вида x = fi(x) на отрезке возрастания
    try:
        y = x - 2
    except:
        return(False)
    return (x - 2)

def ddg2(x): # Функция вида x = fi(x) на отрезке убывания
    try:
        y = x + 2
    except:
        return(False)
    return (x + 2)

def Errorvalue(entry_a,entry_b, entry_h,entry_eps,entry_n):
    t=0
    a = float(entry_a.get())
    b = float(entry_b.get())
    if a >= b:
        t=1

    shag = float(entry_h.get().strip())
    if shag < 0:
        t=1

    eps = float(entry_eps.get().strip())
    if not (0 < eps < shag / 2):
        t=1

    iterr = int(entry_n.get().strip())
    if iterr < 0:
        t=1
    return t

def graph(a,b): # график рассматриваемой функции
    x_graph = np.linspace(a,b,500000)
    y_graph = []
    for i in x_graph:
        y_graph.append(f(i))
    plt.title('$x^2-4$')
    plt.plot(x_graph, y_graph)
    plt.grid(True)
    extr_list_x = list()
    extr_list_y = list()
    for i in range(1,499999):
        if abs(df(x_graph[i]))<= 0.0001 and df(x_graph[i-1])*df(x_graph[i+1])<0:
            extr_list_x.append(x_graph[i])
            extr_list_y.append(f(x_graph[i]))


    plt.scatter(extr_list_x,extr_list_y,color = 'red',label='Extremums')
    plt.show()

def graph_p(arr1, arr2):
    #fig, ax = plt.subplots()
    plt.scatter(arr1,arr2, c = 'red')
    

def insert_data():
    if plt:
        plt.close()
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        h = float(entry_h.get())
        eps = float(entry_eps.get())
        n_max = int(entry_n.get())
    except:
        messagebox.showerror('Ошибка ввода данных','Проверьте введенные данные')
    if Errorvalue(entry_a,entry_b, entry_h,entry_eps,entry_n) == 1:
        messagebox.showerror('Error','Input Error')
    else:
        treeview1 = Table_creator()
        a1 = a
        b1 = b
        #print(a)
        a_cur = a + h
        #print(a_cur)
        x_num = 0
        arg_exist = False
        processing(a,b,h,eps,n_max,a_cur,x_num,arg_exist, treeview1)
        graph(a1,b1)



def processing(a,b,h,eps,n_max,a_cur,x_num,arg_exist,treeview):
    peregib = False
    x_peregib = []
    y_peregib = []
    if h <= 1:
        hg = 10
    else:
        hg = abs(a - b) / h
    treeview.config(height = int(hg + 1))
        
    while (a_cur <= b):
        #print(a_cur)
        check = True
        error = 0
        if (ddf(a) * ddf(a_cur)) <= 0:
            x_prev = (a + a_cur) / 2
            minus = False
            if ddf(x_prev) > ddf(x_prev + 1e-3):
                 x_cur = ddg2(x_prev)
                 minus = True
            else:
                 x_cur = ddg1(x_prev)
            if check == False:
                error = 3
                break
            while fabs(x_cur - x_prev) > eps:
                 x_prev = x_cur
                 if minus == True:
                     x_cur = ddg2(x_prev)
                 else:        
                     x_cur = ddg1(x_prev)
                 if check == False:
                     error = 3
                     break
            if error != 0:
                error = 0
            else:
                peregib = True
                x_peregib.append(x_cur)
                y_peregib.append(ddf(x_cur))

                
        if (f(a) * f(a_cur)) <= 0:
            x_num += 1
            if (f(a) * f(a_cur)) == 0:
                n = 1
                if (f(a) == 0):
                    x_cur = a
                else:
                    x_cur = a_cur
            else:    
                x_prev = (a + a_cur) / 2
                x0 = df(x_prev)
                x_cur = g(x_prev, x0)
                print(x_cur)
                n = 1
                while fabs(x_cur - x_prev) > eps:
                     n += 1
                     if n > n_max:
                         error = 2
                         break
                     x_prev = x_cur
                     x_cur = g(x_prev, x0)
                     print(x_cur)
                     if check == False:
                         error = 3
                         break
            if arg_exist == True:
                if abs(x_cur - x_last) < 1e-5:
                    error = 4
                    x_num -= 1
        else:
            error = 1   
        if error == 0:
            arg_exist = True
            x_last = x_cur
            plt.scatter(x_cur,f(x_cur), c = 'orange')
            treeview.insert('','end', text = x_num, \
                        values = ('{:^11.0f}'.format(a),\
                        '{:^12.0f}'.format(a_cur),\
                        '{:^12.9f}'.format(x_cur),\
                        '{:^14.2}'.format(f(x_cur)),\
                        '{:^12d}'.format(n),'{:^10s}'.format('-')))
        elif error == 1:
            pass
        elif error == 2:
            treeview.insert('','end', text = '{:^10s}'.format('-'),\
                        values = ('{:^11.0f}'.format(a),\
                        '{:^12.0f}'.format(a_cur),\
                        '{:^12s}'.format('-'),\
                        '{:^14s}'.format('-'),\
                        '{:^10s}'.format('-'),\
                        '{:^10s}'.format\
                        ('2 - Превышено максимальное число итераций')))
        elif error == 3:
            treeview.insert('','end', text = '{:^10s}'.format('-'),\
                        values = ('{:^11.0f}'.format(a),\
                                  '{:^12.0f}'.format(a_cur),\
                                  '{:^12s}'.format('-'),'{:^14s}'.format('-'),\
                                  '{:^10s}'.format('-'),\
                                  '{:^10s}'.format('3 - Деление на ноль')))
        elif error == 4:
            pass
        if (abs(b - a_cur) < h):
            if (abs(b - a_cur) < 1e-5):
                break
            a = a_cur
            a_cur = b
        else:
            a = a_cur  
            a_cur += h
    if peregib == True:
        graph_p(x_peregib,y_peregib)

    

# Ввод значений:


window = Tk()
window.title('Ввод значений')
frame1 = Frame(window)
frame2 = Frame(window)
frame3 = Frame(window)
frame4 = Frame(window)
frame5 = Frame(window)
frame6 = Frame(window)
frame7 = Frame(window)

entry_a = Entry(frame1)
entry_b = Entry(frame2)
entry_h = Entry(frame3)
entry_eps = Entry(frame4)
entry_n = Entry(frame5)

label_f = Label(frame6, text = 'Уточнение корней методом простых итераций; \
y = x^2-4')
label_a = Label(frame1, text = 'Введите левую границу')
label_b = Label(frame2, text = 'Введите правую границу')
label_h = Label(frame3, text = 'Введите шаг')
label_eps = Label(frame4, text = 'Введите точность epsilon')
label_n = Label(frame5, text = 'Введите максимальное число итераций')



label_f.pack(side = 'left', padx = 10)

label_a.pack(side = 'left', padx = 10)
entry_a.pack(side = 'left')

label_b.pack(side = 'left', padx = 8)
entry_b.pack(side = 'left', padx = 2)

label_h.pack(side = 'left', padx = 10)
entry_h.pack(side = 'left')

label_eps.pack(side = 'left', padx = 10)
entry_eps.pack(side = 'left')

label_n.pack(side = 'left', padx = 10)
entry_n.pack(side = 'left')

frame6.pack(padx = 10, pady = 10)
frame1.pack(padx = 10, pady = 10)
frame2.pack(padx = 10, pady = 10)
frame3.pack(padx = 10, pady = 10)
frame4.pack(padx = 10, pady = 10)
frame5.pack(padx = 10, pady = 10)

btn_entry = Button(window, text = 'Ввод данных', command = insert_data)
btn_entry.pack(side = 'right')


window.mainloop()


