def checkdocument(a):
    x=[]
    y=[]
    x=[i for i in a.split()]
    if x[0][0]=='0' and x[0][1]!='0':        #Междугородные
        y=['Local','0.00','0.00']
        y.insert(0,x[0]) #номер телефона
        y.insert(2,x[0][1:]) #номер абонента
        y.insert(3,x[1]) #продолжительности разговора
        print(' '.join(y))
    elif x[0][0]=='0' and x[0][1]=='0':
        z=x
        t=-1
        for i in range(len(s)):
            if s[i][0]== x[0][:len(s[i][0])]:
               t=i
        if t==-1:           # " Неизвестно "
            z.insert(1,'Unknown')
            z.append(' ')
            z.append(' ')
            z.append('-1.00')
            print(' '.join(z))
        else:               #Международные
            m=[]
            z.insert(1,s[t][1])
            for j in range(len(s[t][0]),len(x[0])):
                m.append(x[0][j])
            n=''.join(m)
            z.insert(2,n)
            z.append(str(float(s[t][2])/100)) #цены за минуту разговора
            r=round(float(z[3])*float(z[4]),2) #стоимость разговора
            z.append(str(r))

            print(' '.join(z))

    elif a!='#':                   # " Неизвестно "
        z=x
        z.insert(1,'Unknown')
        z.append(' ')
        z.append(' ')
        z.append('-1.00')
        print(' '.join(z))
s=[]
a=''
print('Введите коды страны+ страны +цены за минуту разговора:')
while a!='000000':
    a=input()
    if a!='000000':
        b=[]
        for i in range(len(a)):
            if a[i]=='$': #Замена '$' ->' '
                b.append(' ')
            else:
                b.append(a[i])
        c=''.join(b)
        s.append([i for i in c.split()])
print(s) #Список документов каждого человека
print('Номер телефона+пункта назначения+номер абонента+продолжительности разговора+цены за минуту разговора+стоимость разговора')
while a!='#':
    a=input('Введите номер телефона + продолжительности разговора: ')
    checkdocument(a)



