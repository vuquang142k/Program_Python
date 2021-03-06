#Защита
#Программа сделана Ву Минь Куанг группа ИУ7-14Б
#Построить графику y=sin(2*x)-1

from math import *

m=float(input("Введите начальное значение M: "))

n=float(input("Введите конечное значение N: "))

i=float(input("Введите диапазон изменения переменной i: "))

j=int(input("Введите количество засечек j (от 4 до 8): "))
while ((j<4) or (j>8)):
    print("J должен быть от 4 до 8")
    j=int(input("Введите количество засечек j снова: "))

s=0                                                                                 
for h in range(round(m*10**7),round(n*10**7+1),round(i*10**7)):
    h=round(h*10**-7,7) 
    y=sin(2*h)-1
    s+=y
maxy=miny=round(s/((n-m)/i+1),2)                                                  
for h in range(round(m*10**7),round(n*10**7+1),round(i*10**7)):
    h=round(h*10**-7,7) 
    y=sin(2*h)-1
    if y>maxy: maxy=round(y,2)
    if y<miny: miny=round(y,2)
d=(maxy-miny)/(j-1)                                                               
print(" "*10,end="")
for k in range(0,j):                                                                
    l=miny+k*d                                                                     
    if (abs(l)>=10**-6):
            print("{:5.2g}".format(l)," "*14,end=" ")
    else: print("{:6.2g}".format(l)," "*17,end=" ")
print(sep=" ")
print("     x "+" "*8,end="")
for k in range(0,j):
    print(chr(9524)+chr(9472)*20,end="")                                            
print(sep=" ")
vtymax=int(round(16+21*(j-1),0))                                                   

vt0=int(round(((-miny)/(maxy-miny))*(vtymax-16),0))
if vt0==0: vt0+=1
do=(maxy-miny)/(21*(j-1))                                                        
if ((miny>0) or (maxy<0)):
    for h in range(round(m*10**7),round(n*10**7+1),round(i*10**7)):
        h=round(h*10**-7,7) 
        y=sin(2*h)-1
        x=(y-miny)/(maxy-miny)
        vty=int(x*(vtymax-16))                                                     
        print("{:8.2g}".format(h)+7*" "+vty*" "+"*")                                

else:
    for h in range(round(m*10**7),round(n*10**7+1),round(i*10**7)):
        h=round(h*10**-7,7) 
        y=sin(2*h)-1
        x=(y-miny)/(maxy-miny)
        vty=int(round(x*(vtymax-16),0))                                             
        if (y<0):                                                                  
            if (-y)<do:                                                            
                print("{:8.2g}".format(h)+chr(9474)+7*" "+(vt0)*" "+"*")
            else:                                                                   
                print("{:8.2g}".format(h)+chr(9474)+7*" "+vty*" "+"*"+(vt0-vty-1)*" "+(chr(9474)))
        if (y==10**-8):                                                           
            print("{:8.2g}".format(h)+chr(9474)+7*" "+vty*" "+("*"))
        if (y>0):                                                                  
            if (y1<do):                                                             
                print("{:8.2g}".format(h)+chr(9474)+7*" "+vt0*" "+"*")
            else:                                                                   
                print("{:8.2g}".format(h)+chr(9474)+7*" "+vt0*" "+(chr(9474))+(vty-vt0-1)*" "+"*")
