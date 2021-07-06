from tkinter import *
import matplotlib.pyplot as plt
from tkinter import messagebox
from math import sin,cos
import numpy as np
def F(x):
    return sin(x)

def Fi(x):
    return cos(x)

def Method_hord2(a1,b1,max_iter,eps1):
    error =0
    iter_n = 0
    f = F(b1)
    x = a1
    rez = b1
    f = F(b1)
    f0 = F(a1)
    rez = rez-f/(f-f0)*(rez-x)
    while (abs(F(rez))>eps1):
        if f!=f0 and F(rez)*F(a1)<0:
            f = F(rez)
            f0 =F(a1)
            x = rez
            b1 = rez
            rez = rez -f/(f-f0)*(rez-a1)
            iter_n += 1
        elif  f!=f0 and F(rez)*F(b1)<0:
            f = F(rez)
            f0 =F(b1)
            a1 = rez
            x = rez
            rez = rez -f/(f0-f)*(b1-rez)
            iter_n += 1
    if iter_n>max_iter:
        error =1
    return rez,iter_n,error

def list_get(rang):
    try:
        list_a_b = [float(x) for x in rang.get().strip().split()]

        if len(list_a_b) == 0 or len(list_a_b) > 2:
            raise ValueError
        return list_a_b

    except ValueError:
        messagebox.showerror('Ошибка ввода данных',
                             'Проверьте введенные данные')

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

def calc_roots(range_, shag_, eps_, iter_):
    try:
        range_list = list_get(range_)
        a=range_list[0]
        b = range_list[1]
        shag = float(shag_.get().strip())
        eps = float(eps_.get().strip())
        iterr = int(iter_.get().strip())
        if Errorvalue(range_, shag_,eps_,iter_) == 1:
            messagebox.showerror('Error','Input Error')
        else:
            n = 1
            n_list = list()
            x_list = list()
            fx_list = list()
            left_l = list()
            right_l = list()
            iter_list = list()
            error_list = list()

            while a+shag*(n-1)<b:
                left = a+shag*(n-1)
                right = a+shag*(n) if a+shag*(n)<b else b
                if F(left)*F(right)<=0:
                    x,it,err = Method_hord2(left,right,iterr,eps)
                else:
                    n+=1
                    continue
                if (err == 0 or err==1) and \
                (len(x_list) == 0 or abs(x - x_list[-1]) > 2 * eps):
                    n_list.append(n)
                    x_list.append(x)
                    fx_list.append(F(x))
                    left_l.append(left)
                    right_l.append(right)
                    iter_list.append(it)
                    error_list.append(err)                    
                n+=1
            return n_list, x_list, fx_list, left_l, right_l, iter_list, error_list
    

    except:
        messagebox.showerror('Ошибка ввода данных',
                             'Проверьте введенные данные')   
                          
def find_root(a,s,eps,f):
    all_roots = calc_roots(a,s,eps,f)
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
            w_window_l = Label(window,text = 'Таблица приближенных корней, \
найденных на интервале',
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

                    x_label = Label(window, text = '              -          \
  ',
                                    fg = 'black')
                    x_label.place(x=180,y=50+30*(i+1))
                    
                    fx_label = Label(window, text = '                -        \
       ',
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
            error_code_j.place(x=10,y = 50+45*n)
    
def draw(a,s,eps,f):
    all_roots = calc_roots(a,s,eps,f)
    d = list_get(a)
    x = np.linspace(d[0],d[1],500000)
    y = []
    for i in x:
        y.append(F(i))
    plt.cla()
    plt.title('$sin(x)$')
    plt.grid(True)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    
    plt.plot(x,y,'b')
    
    extr_list_x = list()
    extr_list_y = list()
    for i in range(1,499999):
        if abs(Fi(x[i]))<= 0.0001 and Fi(x[i-1])*Fi(x[i+1]):
            extr_list_x.append(x[i])
            extr_list_y.append(F(x[i]))


    plt.scatter(extr_list_x,extr_list_y,color = 'red',label='Extremums')
    plt.scatter(all_roots[1],all_roots[2],color = 'green',label='Roots')

    plt.legend(loc = 'lower left')
    plt.show()

windows = Tk()
windows.geometry('500x280+500+200')
windows.title('Ввод значений')
frame1 = Frame(windows)
frame2 = Frame(windows)
frame3 = Frame(windows)
frame4 = Frame(windows)
frame5 = Frame(windows)
frame6 = Frame(windows)

range_entry = Entry(frame1)
shag_entry = Entry(frame2)
eps_entry = Entry(frame3)
iter_entry = Entry(frame4)

label_f = Label(frame6, text = 'Уточнение корней методом хорд; \
y = sin(x)')
range_label = Label(frame1, text = 'Правая и левая граница(через пробел)')
shag_label = Label(frame2, text = 'Введите шаг')
eps_label = Label(frame3, text = 'Введите точность epsilon')
iter_label = Label(frame4, text = 'Введите максимальное число итераций')



label_f.pack(side = 'left', padx = 10)

range_label.pack(side = 'left', padx = 10)
range_entry.pack(side = 'left')

shag_label.pack(side = 'left', padx = 8)
shag_entry.pack(side = 'left', padx = 2)

eps_label.pack(side = 'left', padx = 10)
eps_entry.pack(side = 'left')

iter_label.pack(side = 'left', padx = 10)
iter_entry.pack(side = 'left')

frame6.pack(padx = 10, pady = 10)
frame1.pack(padx = 10, pady = 10)
frame2.pack(padx = 10, pady = 10)
frame3.pack(padx = 10, pady = 10)
frame4.pack(padx = 10, pady = 10)
frame5.pack(padx = 10, pady = 10)


#Кнопки(Найти корни, построить график, выход)
find_roote = Button(windows, text='Найти корни',width = 15,height = 1,
                   bg = 'white',fg = 'black',
                   command=lambda: find_root(range_entry,shag_entry,
                                             eps_entry,iter_entry))
find_roote.place(anchor = 'center',x=100, y=250)

draw_graf = Button(windows, text='Построить график',width = 15,height = 1,
                   bg = 'white',fg = 'black',
                   command = lambda: draw(range_entry,shag_entry,
                                          eps_entry,iter_entry))
draw_graf.place(anchor = 'center',x=250, y=250)

exit_but =  Button(windows, text='Выход',width = 15,height = 1,
                   bg = 'white',fg = 'black',
                   command = lambda: windows.destroy())
exit_but.place(anchor = 'center',x=400, y=250)
windows.mainloop()