import scipy.optimize as optimize
import numpy as np
from time import time

def dx(x):
    return np.fabs(0 - f(x))

def f(x):
    return np.sin(x)


def pf(x):
    return np.cos(x)


def opt_newton(a, b, eps):
    x = (a + b) / 2
    delt = dx(x)
    iter = 1
    while delt > eps:
        x = x - f(x)/pf(x)
        delt = dx(x)
        iter += 1
    x = optimize.newton(f, (a+b)/2, fprime=pf, tol=eps)
    return x, f(x), iter


def comb(a, b, eps):
    x0 = a
    xn = b
    x = b - h/10
    iter = 1
    while x0 >= a and x0 <= b and x >= a and x <= b and abs(x0-x) >= eps:
        x1n = x0
        x0 = x1n - f(x1n)*(b-x1n)/(f(b)-f(x1n))
        t = x
        x = x - f(x)*(x-xn)/(f(x)-f(xn))
        xn = t
        iter += 1
    if x0 < a or x0 > b or x < a or x > b:
        x0 = b
        xn = a
        x = a + h/10
        iter = 1
        while x0 >= a and x0 <= b and x >= a and x <= b and abs(x0-x) >= eps:
            x1n = x0
            x0 = x1n - f(x1n)*(x1n-a)/(f(x1n)-f(a))
            t = x
            x = x - f(x)*(x-xn)/(f(x)-f(xn))
            xn = t
            iter += 1
    return x,f(x),iter


left = float(input('Введите левую границу: '))
right = float(input('Введите правую границу: '))
h = float(input('Введите шаг: '))
#accuracy = float(input('Введите точность e: '))
accuracy = 0.001
#maxiter = int(input('Введите максимальное количество итераций: '))
maxiter = 1000


print(chr(9484) + chr(9472)*2 + chr(9516) + chr(9472)*13 + chr(9516) +
      chr(9472)*28 + chr(9516) + chr(9472)*28 + chr(9516) + chr(9472)*2 +
      chr(9488) + '\n' + chr(9474) + ' №' + chr(9474) + '   Граница   ' +
      chr(9474) + '    Комбинированный метод   ' + chr(9474) +
      '        Метод Ньютона       ' + chr(9474) + 'КО' + chr(9474), sep='')
print(chr(9474)+'  '+chr(9500)+chr(9472)*6+chr(9516)+chr(9472)*6+chr(9532)+
      chr(9472)*9+chr(9516)+chr(9472)*6+chr(9516)+chr(9472)*5+chr(9516)+
      chr(9472)*5+chr(9532)+chr(9472)*9+chr(9516)+chr(9472)*6+chr(9516)+
      chr(9472)*5+chr(9516)+chr(9472)*5+chr(9508)+'  '+chr(9474)+'\n'+chr(9474)+'  '+
      chr(9474)+' Левая'+chr(9474)+'Правая'+chr(9474)+'  Корень '+chr(9474)+
      ' Знач.'+chr(9474)+'Итер.'+chr(9474)+'Время'+chr(9474)+'  Корень '+
      chr(9474)+' Знач.'+chr(9474)+'Итер.'+chr(9474)+'Время'+chr(9474)+'  '+
      chr(9474),sep='')

        
edg = left
k = 0
while edg < right:
    edg_prev = edg
    edg += h
    if edg > right:
        edg = right
    if f(edg_prev)*f(edg) < 0 or f(edg_prev) == 0:
        er = 0
        k += 1
        t1 = time()
        for j in range(1000):
            a1,b1,c1 = comb(edg_prev,edg, accuracy)
        t1 = time() - t1
        t2 = time()
        for j in range(1000):
            a2,b2,c2 = opt_newton(edg_prev,edg, accuracy)
        t2 = time() - t2
        if (a1 < edg_prev or a1 > edg) and (a2 < edg_prev or a2 > edg):
            er = 3
        elif a1 < edg_prev or a1 > edg:
            er = 1
            print(chr(9500) + chr(9472) * 2 + chr(9532) + chr(9472) * 6 +
                  chr(9532) + chr(9472) * 6 + chr(9532) + chr(9472) * 9 +
                  chr(9532) + chr(9472) * 6 + chr(9532) + chr(9472) * 5 +
                  chr(9532) + chr(9472) * 5 + chr(9532) + chr(9472) * 9 +
                  chr(9532) + chr(9472) * 6 + chr(9532) + chr(9472) * 5 +
                  chr(9532) + chr(9472) * 5 + chr(9532) + chr(9472) * 2 +
                  chr(9508) + '\n' + chr(9474) + '{:2d}'.format(k) + chr(9474)+
                  '{:6.2f}'.format(edg_prev) + chr(9474)+'{:6.2f}'.format(edg)+
                  chr(9474) + ' '*9 +chr(9474) +' '*6 + chr(9474) + ' '*5 +
                  chr(9474) + ' '*5 + chr(9474) + '{:9.5f}'.format(a2) +
                  chr(9474) + '{:6.0e}'.format(b2)+ chr(9474) +
                  '{:5d}'.format(c2)+chr(9474)+'{:5.3f}'.format(t2)+chr(9474)+
                  '{:2d}'.format(er) + chr(9474), sep='')
        elif a2 < edg_prev or a2 > edg:
            er = 2
            print(chr(9500) + chr(9472) * 2 + chr(9532) + chr(9472) * 6 +
                  chr(9532) + chr(9472) * 6 + chr(9532) + chr(9472) * 9 +
                  chr(9532) + chr(9472) * 6 + chr(9532) + chr(9472) * 5 +
                  chr(9532) + chr(9472) * 5 + chr(9532) + chr(9472) * 9 +
                  chr(9532) + chr(9472) * 6 + chr(9532) + chr(9472) * 5 +
                  chr(9532) + chr(9472) * 5 + chr(9532) + chr(9472) * 2 +
                  chr(9508) +'\n'+ chr(9474) + '{:2d}'.format(k) + chr(9474) +
                  '{:6.2f}'.format(edg_prev)+chr(9474)+'{:6.2f}'.format(edg) +
                  chr(9474)+'{:9.5f}'.format(a1)+chr(9474)+'{:6.0e}'.format(b1)
                  +chr(9474)+'{:5d}'.format(c1)+chr(9474)+'{:5.3f}'.format(t1)+
                  chr(9474) + ' '*9 + chr(9474) + ' '*6 + chr(9474) + ' '*5 +
                  chr(9474) + ' '*5 + chr(9474) + ' 2' + chr(9474), sep='')
        else:
            print(chr(9500)+chr(9472)* 2+chr(9532)+chr(9472)* 6+chr(9532)+
                  chr(9472)* 6+chr(9532)+chr(9472)* 9+chr(9532)+chr(9472)* 6+
                  chr(9532)+chr(9472)*5 +chr(9532)+chr(9472)* 5+chr(9532)+
                  chr(9472)* 9+chr(9532)+chr(9472)* 6+chr(9532)+chr(9472)* 5+
                  chr(9532)+chr(9472)*5 +chr(9532)+chr(9472)* 2+chr(9508)+'\n'+
                  chr(9474)+'{:2d}'.format(k)+chr(9474)+
                  '{:6.2f}'.format(edg_prev)+chr(9474)+'{:6.2f}'.format(edg)+
                  chr(9474)+'{:9.5f}'.format(a1)+chr(9474)+'{:6.0e}'.format(b1)
                  +chr(9474)+'{:5d}'.format(c1)+chr(9474)+'{:5.3f}'.format(t1)+
                  chr(9474)+'{:9.5f}'.format(a2)+chr(9474)+'{:6.0e}'.format(b2)
                  +chr(9474)+'{:5d}'.format(c2) +chr(9474)+'{:5.3f}'.format(t2)
                  +chr(9474)+'{:2d}'.format(er) +chr(9474), sep='')
if k == 0:
    print(chr(9500) + chr(9472) * 2 + chr(9532) + chr(9472) * 6 + chr(9532) +
          chr(9472) * 6 + chr(9532) + chr(9472) * 9 + chr(9532) + chr(9472) * 6 +
          chr(9532) + chr(9472) * 5 + chr(9532) + chr(9472) * 5 + chr(9532) +
          chr(9472) * 9 + chr(9532) + chr(9472) * 6 + chr(9532) + chr(9472) * 5 +
          chr(9532) + chr(9472) * 5 + chr(9532) + chr(9472) * 2 + chr(9508) + '\n' +
          chr(9474) + '  ' + chr(9474) + ' '*6 +
          chr(9474) + ' '*6 + chr(9474) + ' '*9 +
          chr(9474) + ' '*6 + chr(9474) + ' '*5 +
          chr(9474) + ' '*5 + chr(9474) + ' '*9 +
          chr(9474) + ' '*6 + chr(9474) + ' '*5 +
          chr(9474) + ' '*5 + chr(9474) + ' 4' + chr(9474), sep='')

print(chr(9492)+chr(9472)* 2+chr(9524)+chr(9472)* 6+chr(9524)+chr(9472)* 6 +
      chr(9524)+chr(9472)* 9+chr(9524)+chr(9472)* 6+chr(9524)+chr(9472)* 5 +
      chr(9524)+chr(9472)* 5+chr(9524)+chr(9472)* 9+chr(9524)+chr(9472)* 6 +
      chr(9524)+chr(9472)* 5+chr(9524)+chr(9472)* 5+chr(9524)+chr(9472)* 2 +
      chr(9496), sep='')
print('\nКоды ошибок:\n\
0 - нет ошибок\n\
1 - невозможно вычислить корень комбинированным методом из-за его особенностей\
\n2 - невозможно вычислить корень методом Ньютона из-за его особенностей\n\
3 - невозможно вычислить корень данными методами из-за их особенностей\n\
4 - на отрезке нет корней')
