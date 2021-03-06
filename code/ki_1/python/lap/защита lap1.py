#Защита
#Программа сделана Ву Минь Куанг группа ИУ7-14Б
#Даны 3 вершины треугольника с целчисленными координатами
#Определить длину медины из наибольшего угла

from math import sqrt,fabs
eps=10**-8
xA,yA=map(float,input('Введите координат А: ').split(' '))
xB,yB=map(float,input('Введите координат B: ').split(' '))
xC,yC=map(float,input('Введите координат C: ').split(' '))

a=sqrt((xC-xB)**2+(yC-yB)**2)                       #Вычисляет длину BC
b=sqrt((xA-xC)**2+(yA-yC)**2)                       #Вычисляет длину AC
c=sqrt((xA-xB)**2+(yA-yB)**2)                       #Вычисляет длину АВ

print('Длина стороны AB= {:g}'.format(c))
print('Длина стороны BC= {:g}'.format(a))
print('Длина стороны AC= {:g}'.format(b))
if fabs(c - b +a) <= eps or fabs(c + b - a) <= eps or fabs(a + b - c) <= eps:
    print('Это не треугольник')
else:

    # Медиана из А: АМ = sqrt((2*(AB*AB+AC*AC) - BC*BC)/4)
    median = 0
    if c >= a and c >= b:
        median = sqrt((2*(b*b+a*a) - c*c)/4)      # Угол С наибольший, то вычисляет медиану из С
    elif b >= c and b >= a:
        median = sqrt((2*(c*c+a*a) - b*b)/4)      # Угол В наибольший, то вычисляет медиану из B
    elif a >= c and a >= b:
        median = sqrt((2*(c*c+b*b) - a*a)/4)      # Угол А наибольший, то вычисляет медиану из A
    print('Медиана из наибольшего угла треугольника: {:g}'.format(median))
