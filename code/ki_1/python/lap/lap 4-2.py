# Определить также частное между минимальным y1  и максимальным y2  значением С
# Программа сделана Ву Минь Куанг группа ИУ7-14Б
# y1=9.45*h**4+5*h**3-4.37*h**2-0.28*h-0.35
# y2=(h-1)**2-0.5* **h
# h=0.2(0.02)0.6
# Оператор FOR

from math import *

A = []
B = []
m=float(input("Введите начальное значение M: "))

n=float(input("Введите конечное значение N: "))

i=float(input("Введите диапазон изменения переменной i: "))

j=int(input("Введите количество засечек j (от 4 до 8): "))
while ((j<4) or (j>8)):
    print("J должен быть от 4 до 8")
    j=int(input("Введите количество засечек j снова: "))
print(chr(9484),chr(9472) * 63,chr(9488))
print(chr(9474), 4*' ', 'x', 6*' ', chr(9474), 8*' ', 'y1', 8*' ', chr(9474),
      9*' ', 'y2', 11*' ', chr(9474))
print(chr(9500), chr(9472) * 63, chr(9508))
for h in range(round(m*10**7),round(n*10**7+1),round(i*10**7)):
    h=round(h*10**-7,7) 
    a = 9.45 * (h) ** 4 + 5 * (h ) ** 3 - 4.37 * (h ) ** 2 - 0.28 * (h ) - 0.35
    b = ((h ) - 1) ** 2 - 0.5 * exp((h ))
    A.append(a)
    B.append(b)

    print(chr(9474), '{:7.2g}'.format(h ),5*' ', chr(9474),2*' ','{:12.5g}'.format(a),4*' ', chr(9474),2*' ', '{:12.5g}'.format(b),8*' ', chr(9474))
print(chr(9492),chr(9472) * 63,chr(9496))
c = min(A)
d = max(B)
print('минимальное значение функции y1: {:g}'.format(c))
print('максимальное значение функции y2: {:g}'.format(d))
if c==0:
    print('ERROR')
else:
    print('частное между минимальным y1  и максимальным y2  значением: С= {:g}'.format(d / c))




print('\nПостроит Функцию 1')

print("\n")
s=0                                                                                 #Сумма значении функции
for h in range(round(m*10**7),round(n*10**7+1),round(i*10**7)):
    h=round(h*10**-7,7) 
    y1=9.45*h**4+5*h**3-4.37*h**2-0.28*h-0.35
    s+=y1
maxy1=miny1=round(s/((n-m)/i+1),2)                                                  #Вычислить среднее значение
for h in range(round(m*10**7),round(n*10**7+1),round(i*10**7)):
    h=round(h*10**-7,7) 
    y1=9.45*h**4+5*h**3-4.37*h**2-0.28*h-0.35
    if y1>maxy1: maxy1=round(y1,2)
    if y1<miny1: miny1=round(y1,2)
d=(maxy1-miny1)/(j-1)                                                               #Шаг значения y1  
print(" "*10,end="")
for k in range(0,j):                                                                #нарисовать ось Oy
    l=miny1+k*d                                                                     #Значения y на Oy
    if (abs(l)>=10**-6):
            print("{:5.2g}".format(l)," "*13,end=" ")
    else: print("{:6.2g}".format(l)," "*17,end=" ")
print(sep=" ")
print("     x "+" "*8,end="")
for k in range(0,j):
    print(chr(9524)+chr(9472)*20,end="")                                            #┴────────────────────
print(sep=" ")
vtymax=int(round(16+21*(j-1),0))                                                    #Положение максимального значения

vt0=int(round(((-miny1)/(maxy1-miny1))*(vtymax-16),0))
if vt0==0: vt0+=1
do=(maxy1-miny1)/(21*(j-1))                                                         #Значение пустого места
if ((miny1>0) or (maxy1<0)):
    for h in range(round(m*10**7),round(n*10**7+1),round(i*10**7)):
        h=round(h*10**-7,7) 
        y1=9.45*h**4+5*h**3-4.37*h**2-0.28*h-0.35
        x=(y1-miny1)/(maxy1-miny1)
        vty=int(x*(vtymax-16))                                                      #Определить место точки
        print("{:8.2g}".format(h)+7*" "+vty*" "+"*")                                #Рисовать точку
#Обратно:
else:
    for h in range(round(m*10**7),round(n*10**7+1),round(i*10**7)):
        h=round(h*10**-7,7) 
        y1=9.45*h**4+5*h**3-4.37*h**2-0.28*h-0.35
        x=(y1-miny1)/(maxy1-miny1)
        vty=int(round(x*(vtymax-16),0))                                             #Определить место точки
        if (y1<0):                                                                  #Точка лежит на слева Ox
            if (-y1)<do:                                                            #Точка принадлежает в пустом месте
                print("{:8.2g}".format(h)+chr(9474)+7*" "+(vt0)*" "+"*")
            else:                                                                   #Точка принадлежает в другом пустом месте
                print("{:8.2g}".format(h)+chr(9474)+7*" "+vty*" "+"*"+(vt0-vty-1)*" "+(chr(9474)))
        if (y1==10**-8):                                                            #Точка лежит на Ox
            print("{:8.2g}".format(h)+chr(9474)+7*" "+vty*" "+("*"))
        if (y1>0):                                                                  #Точка лежит на справа Ox
            if (y1<do):                                                             #Точка принадлежает в пустом месте
                print("{:8.2g}".format(h)+chr(9474)+7*" "+vt0*" "+"*")
            else:                                                                   #Точка принадлежает в другом пустом месте
                print("{:8.2g}".format(h)+chr(9474)+7*" "+vt0*" "+(chr(9474))+(vty-vt0-1)*" "+"*")
