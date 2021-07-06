from tkinter import *
import matplotlib.pyplot as plt
from tkinter import messagebox
from math import exp
import numpy as np

def f(x):
    return x**3-3*x**2+2*x-5

def f1(x):
    return 3+5/x**2-2/x

def df1(x):
    return -10/x**3+2/x**2

def df(x):
    return 3*x**2-6*x+2

def list_get(rang):
    try:
        list_a_b = [float(x) for x in rang.get().strip().split()]

        if len(list_a_b) == 0 or len(list_a_b) > 2:
            raise ValueError
        return list_a_b

    except ValueError:
        messagebox.showerror('Ошибка ввода данных',
                             'Проверьте введенные данные')

def iteration(a1,b1,max_iter,eps):
    error =0
    iter_n = 0
    x0=a1
    x1=f1(x0)
    if abs(df1(a1))>abs(df1(b1)):
        q=abs(df1(a1))
    else:
        q=abs(df1(b1))
    if q>=1:
        return 0
    else:
        while q*abs(x1-x0)/(1-q) >= eps:
            x0=x1
            x1=f1(x0)
        iter_n += 1
        if iter_n > max_iter:
            error =1
        return x1,iter_n,error

def Errorvalue(range_, shag_,eps_,iter_):
    a=0
    range_list = list_get(range_)
    a=range_list[0]
    b = range_list[1]
    if a >= b:
        a=1

    shag = float(shag_.get().strip())
    if shag < 0:
        a=1

    eps = float(eps_.get().strip())
    if not (0 < eps < shag / 2):
        a=1

    iterr = int(iter_.get().strip())
    if iterr < 0:
        a=1
    return a

def calc_roots(range_, shag_,eps_,iter_):
    range_list = list_get(range_)
    a=range_list[0]
    b = range_list[1]
    shag = float(shag_.get().strip())
    eps = float(eps_.get().strip())
    iterr = int(iter_.get().strip())
    if Errorvalue(range_, shag_,eps_,iter_) == 1:
        messagebox.showerror('Error','Input Error')
    else:
        try:
            n=1
            it = 0
            err = 0
            n_list = []
            x_list = []
            fx_list = []
            left_l = []
            right_l = []
            iter_list = []
            error_list = []

            while a+shag*(n-1)<b:
                left = a+shag*(n-1)
                right = a+shag*(n) if a+shag*(n)<b else b
                if f(left)*f(right) <= 0:
                    if iteration(left,right,iterr,eps)!= 0:
                        x,it,err = iteration(left,right,iterr,eps)
                    else:
                        n += 1
                        continue
                else:
                    n += 1
                    continue

                if (err == 0 or err==1) and (len(x_list) == 0 or abs(x - x_list[-1]) > 2 * eps):
                    n_list.append(n)
                    x_list.append(x)
                    fx_list.append(f(x))
                    left_l.append(left)
                    right_l.append(right)
                    iter_list.append(it)
                    error_list.append(err)                
                n+=1
            return n_list, x_list, fx_list, left_l, right_l, iter_list, error_list
        except:
            messagebox.showerror('Error','Input Error')

def find_root(range_, shag_,eps_,iter_):
    all_roots = calc_roots(range_, shag_,eps_,iter_)
    if all_roots:
        if not len(all_roots[0]):
            messagebox.showinfo('Корни не найдены',
                                'Корни не найдены на заданном интервале')
        else:
            window = Toplevel(windows)
            window.grab_set()
            window.focus_set()
            window.geometry('600x500+700+100')
            window.title('Таблица')
            window['bg'] = '#c4adf0'
            w_window_l = Label(window,text = 'Таблица приближенных корней, найденных на интервале',
                               font = 'consolas 14',bg='#f0ade2',fg = 'black')
            w_window_l.place(x=300,y=25,anchor ='center')

            n_label = Label(window, text = ' № ',font = 'consolas 9',
                            fg = 'black')
            n_label.place(x=5,y=50)

            a_b_label = Label(window, text = '       [a,b]       ',
                              font = 'consolas 9',fg = 'black')
            a_b_label.place(x=35,y=50)

            x_label = Label(window, text = '     x      ',
                            font = 'consolas 9',fg = 'black')
            x_label.place(x=180,y=50)
            
            fx_label = Label(window, text = '      F(x)     ',
                             font = 'consolas 9',fg = 'black')
            fx_label.place(x=275,y=50)

            iter_label = Label(window, text = 'Кол-во итераций',
                               font = 'consolas 9',fg = 'black')
            iter_label.place(x=390,y=50)              

            err_label = Label(window, text = 'Код ошибки',
                              font = 'consolas 9',fg = 'black')
            err_label.place(x=505,y=50)

            n = len(all_roots[0])


            for i in range (n):
                if all_roots[6][i]==1:
                    print('SOS')
                    n_label = Label(window, text = '{:3d}'.format(i+1),
                                    font = 'consolas 9',fg = 'black')
                    n_label.place(x=5,y=50+30*(i+1))

                    a_b_label = Label(window, text = '[{:8.4f};{:8.4f}]'\
                                      .format(all_roots[3][i],all_roots[4][i]),
                                      font = 'consolas 9',fg = 'black')
                    a_b_label.place(x=35,y=50+30*(i+1))

                    x_label = Label(window, text = '              -          ',
                                    fg = 'black')
                    x_label.place(x=180,y=50+30*(i+1))
                    
                    fx_label = Label(window, text = '                -        ',
                                     fg = 'black')
                    fx_label.place(x=275,y=50+30*(i+1))

                    iter_label = Label(window, text = '{:15.0f}'.format\
                                       (all_roots[5][i]),
                                       font = 'consolas 9',fg = 'black')
                    iter_label.place(x=390,y=50+30*(i+1))              

                    err_label = Label(window, text = '{:10.0f}'.format\
                                      (all_roots[6][i]),
                                      font = 'consolas 9',fg = 'black')
                    err_label.place(x=505,y=50+30*(i+1))
                else:
                   
                    n_label = Label(window, text = '{:3d}'.format(i+1),
                                    font = 'consolas 9',fg = 'black')
                    n_label.place(x=5,y=50+30*(i+1))

                    a_b_label = Label(window, text = '[{:8.4f};{:8.4f}]'.format\
                                        (all_roots[3][i],all_roots[4][i]),
                                          font = 'consolas 9',fg = 'black')
                    a_b_label.place(x=35,y=50+30*(i+1))

                    x_label = Label(window, text = '{:12.5f}'.format\
                                        (all_roots[1][i]),
                                        font = 'consolas 9',fg = 'black')
                    x_label.place(x=180,y=50+30*(i+1))
                        
                    fx_label = Label(window, text = '{:15.0e}'.format\
                                         (all_roots[2][i]),
                                         font = 'consolas 9',fg = 'black')
                    fx_label.place(x=275,y=50+30*(i+1))

                    iter_label = Label(window, text = '{:15.0f}'.format\
                                           (all_roots[5][i]),
                                           font = 'consolas 9',fg = 'black')
                    iter_label.place(x=390,y=50+30*(i+1))              

                    err_label = Label(window, text = '{:10.0f}'.format\
                                          (all_roots[6][i]),
                                          font = 'consolas 9',fg = 'black')
                    err_label.place(x=505,y=50+30*(i+1))



            error_code_j = Button(window, text='Код ошибки',
                                  width = 15,height = 1,
                                  bg = 'white',fg = 'black',
                                  command=lambda:messagebox.showinfo\
                                  ('Код ошибки','0 - нет ошибки\n\
1 - кол-во итераций больше максимального'))
            error_code_j.place(x=10,y = 70+45*n)

def draw(range_, shag_,eps_,iter_):
    all_roots = calc_roots(range_, shag_,eps_,iter_)
    d = list_get(range_)
    x = np.linspace(d[0],d[1],500000)
    y = []
    for i in x:
        y.append(f(i))
    plt.cla()
    plt.title('$x^3-3*x^2+2*x-5$')
    plt.grid(True)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    
    plt.plot(x,y,'b')
    
    extr_list_x = list()
    extr_list_y = list()
    for i in range(1,499999):
        if abs(df(x[i]))<= 0.0001 and df(x[i-1])*df(x[i+1]):
            extr_list_x.append(x[i])
            extr_list_y.append(f(x[i]))


    plt.scatter(extr_list_x,extr_list_y,color = 'red',label='Extremums')
    plt.scatter(all_roots[1],all_roots[2],color = 'green',label='Roots')


    plt.legend(loc = 'lower left')
    plt.show()

windows = Tk()
windows['bg'] = '#fff'
windows.geometry('500x280+500+200')
windows.title('Simple iteration method')

start_label = Label(windows, text = 'Нахождниe корней функции (x^3-3*x^2+2*x-5) с помощью метода простой итерации',font = 'consolas 13',fg = 'black')
start_label.grid(row = 1,column =0,columnspan = 3)

start_label1 = Label(windows, text = '',font = 'consolas',
                     bg = '#fff',fg = 'black')
start_label1.grid(row = 2,column =0,columnspan = 3)

range_label = Label(windows, text = 'Правая и левая граница\n \
(через пробел)',font = 'consolas 10',
                    bg = '#fff',fg = 'black')
range_label.grid(row = 3,column = 0)

range_entry = Entry(windows, width=20)
range_entry.grid(row=3, column=1, rowspan=2)



shag_label = Label(windows, text = 'Шаг',
                    font = 'consolas 10',bg = '#fff',fg = 'black')
shag_label.grid(row = 7,column = 0,rowspan = 2)


shag_entry = Entry(windows, width=20)
shag_entry.grid(row=7, column=1, rowspan=2)


eps_label = Label(windows, text = 'Точность измерений',
                    font = 'consolas 10',bg = '#fff',fg = 'black')
eps_label.grid(row = 10,column = 0,rowspan = 2)


eps_entry = Entry(windows, width=20)
eps_entry.grid(row=10, column=1, rowspan=2)




iter_label = Label(windows, text = 'Максимальное количество итераций',
                    font = 'consolas 10',bg = '#fff',fg = 'black')
iter_label.grid(row = 13,column = 0,rowspan = 2)



iter_entry = Entry(windows, width=20)
iter_entry.grid(row=13, column=1, rowspan=2)


#Кнопки(Найти корни, построить график, выход)
find_roote = Button(windows, text='Найти корни',width = 15,height = 1,
                   bg = 'white',fg = 'black',
                   command=lambda: find_root(range_entry,shag_entry,
                                             eps_entry,iter_entry))
find_roote.place(anchor = 'center',x=100, y=200)

draw_graf = Button(windows, text='Построить график',width = 15,height = 1,
                   bg = 'white',fg = 'black',
                   command = lambda: draw(range_entry,shag_entry,eps_entry,iter_entry))
draw_graf.place(anchor = 'center',x=250, y=200)

exit_but =  Button(windows, text='Выход',width = 15,height = 1,
                   bg = 'white',fg = 'black',
                   command = lambda: windows.destroy())
exit_but.place(anchor = 'center',x=400, y=200)

windows.mainloop()