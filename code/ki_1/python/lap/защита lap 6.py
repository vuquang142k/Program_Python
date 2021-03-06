#Защита лаб 6
#Программа сделана Ву Минь Куанг ИУ7-14Б
n=int(input('Введите N: '))
s=[i for i in input('ВВедите массив: ').split()]
t=[]
a=0
b,c=0,0
m,n=0,0
for i in range(1,len(s)):
    if float(s[i])>float(s[i-1]):
        c=i
    else:
        if c-b+1>a:
            a=c-b+1
            m=b
            n=c
        b=c=i
if c-b+1>a:
    a=c-b+1
    m=b
    n=c
if a==len(s):
    print('Все элементы удалят.')
else:
    for i in range(len(s)):
        if i<m or i>n:
            t.append(s[i])
    print(' '.join(t))
