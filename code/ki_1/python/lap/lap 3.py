#Программа сделана Ву Минь Куанг группа ИУ7-14Б
#Если треугольник непрямсугольник, то вывести начальные координаты вершины, которую можно переместить на минимальное расстояние
#чтоб треугольник стал прямоугольником, а так же координаты той точки, в которую надо переместить вершину
from math import sqrt,fabs

xA,yA=map(float,input('Введите координат А: ').split(' '))
xB,yB=map(float,input('Введите координат B: ').split(' '))
xC,yC=map(float,input('Введите координат C: ').split(' '))

a=sqrt((xC-xB)**2+(yC-yB)**2)                       #Вычисляет длину BC
b=sqrt((xA-xC)**2+(yA-yC)**2)                       #Вычисляет длину AC
c=sqrt((xA-xB)**2+(yA-yB)**2)                       #Вычисляет длину АВ


if(fabs(a+b-c)<=10**-6) or (fabs(b+c-a)<=10**-6) or (fabs(a+c-b)<=10**-6):               #не является треугольником
    print('не является треугольником')

else:                                               #треугольник ABC
     # Если a**2+b**2==c**2 ,то существует прямоугольный треугольник с катетами a и b и гипотенузой c
    if(fabs(a**2+b**2-c**2)<=10**-6) or (fabs(a**2+c**2-b**2)<=10**-6) or(fabs(b**2+c**2-a**2)<=10**-6):
        print('треугольник является прямоугольным')
    else:
        print('треугольник не является прямоугольным')
        xM=(xA+xB)/2                        #координаты точки M является серединой АВ
        yM=(yA+yB)/2
        CM=sqrt((xM-xC)**2+(yM-yC)**2)      #медина CM,которая является диаметром с центром M
        d1=fabs(CM-c/2)
        
        xN=(xA+xC)/2                        #координаты точки N является серединой AC
        yN=(yA+yC)/2
        BN=sqrt((xN-xB)**2+(yN-yB)**2)      #медина BN,которая является диаметром с центром N
        d2=fabs(BN-b/2)
        
        xP=(xB+xC)/2                        #координаты точки P является серединой BC
        yP=(yB+yC)/2
        AP=sqrt((xP-xA)**2+(yP-yA)**2)      #медина AP,которая является диаметром с центром P
        d3=fabs(AP-a/2)
        
        p=(a+b+c)/2
        hA=2*sqrt(p*(p-a)*(p-b)*(p-c))/a    #высота из А
        if b>c:
            d4=sqrt(c**2-hA**2)
        else:
            d4=sqrt(b**2-hA**2)
            
        hB=2*sqrt(p*(p-a)*(p-b)*(p-c))/b    #высота из B
        if a>c:
            d5=sqrt(c**2-hB**2)
        else:
            d5=sqrt(a**2-hB**2)
        
        hC=2*sqrt(p*(p-a)*(p-b)*(p-c))/c    #высота из C
        if b>a:
            d6=sqrt(a**2-hC**2)
        else:
            d6=sqrt(b**2-hC**2)
        #print(d1,' ',d2,' ',d3,' ' ,d4,' ',d5,' ',d6)
        r=min(d1,min(d2,d3))
        s=min(d4,min(d5,d6))
        d=min(r,s)
        #print(d)
        if(fabs(d-d1)<=10**-6):
           xI=xM+(c/(2*CM))*(xC-xM)
           yI=yM+(c/(2*CM))*(yC-yM)
        if(fabs(d-d2)<=10**-6):
           xI=xN+(b/(2*BN))*(xB-xN)
           yI=yN+(b/(2*BN))*(yB-yN)
        if(fabs(d-d3)<=10**-6):
           xI=xP+(a/(2*AP))*(xA-xP)
           yI=yP+(a/(2*AP))*(yA-yP)
        if(fabs(d-d4)<=10**-6):
            if b>c:
               xI=xA+(d4/a)*(xB-xC)
               yI=yA+(d4/a)*(yB-yC)
            else:
               xI=xA+(d4/a)*(xC-xB)
               yI=yA+(d4/a)*(yC-yB)
        if(fabs(d-d5)<=10**-6):
            if a>c:
               xI=xB+(d5/b)*(xA-xC)
               yI=yB+(d5/b)*(yA-yC)
            else:
               xI=xB+(d5/b)*(xC-xA)
               yI=yB+(d5/b)*(yC-yA)
        if(fabs(d-d6)<=10**-6):
            if b>a:
               xI=xC+(d6/c)*(xB-xA)
               yI=yC+(d6/c)*(yB-yA)
            else:
               xI=xC+(d6/c)*(xA-xB)
               yI=yC+(d6/c)*(yA-yB)

        print('координат новой точки: {:g} {:g}'.format(xI,yI))
