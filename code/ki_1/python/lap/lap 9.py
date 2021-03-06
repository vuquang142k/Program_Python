#Программа сделана Ву Минь Куанг, группа ИУ7-14Б
#Программа позволит с использованием меню
#1-Ввод строки
#2-Настройка шифрующего алгоритма
#3-Шифрование строки, используя шифр Виженера
#4-Расшивание строки
#0-Вывод


choise=None  #Команда
while choise!='0':
    print(
        '''
        1-Ввод строки
        2-Настройка шифрующего алгоритма
        3-Шифрование строки, используя шифр Виженера
        4-Расшивание строки
        0-Вывод
        ''')
    choise=input('Выбор: ')
    if choise=='0':         #Вывод
        print('Вывод')
    elif choise=='1': 
        a=input('Ввод строки: ')    #строка
    elif choise=='2':
        key=input('Ввод кодовое слово: ') #шифрующий алгоритм
        key.lower()
        print()
    elif choise=='3': #Шифрование строки
        b=[]
        for i in range(len(a)): 
            if a[i]!=' ': #a[i]!=' '
                if a[i].islower():  #a[i]='a-z'-маленькая буква
                    t=chr((ord(a[i])-97+ord(key[i%len(key)])-97)%26+97)
                    b.append(t)
                else:               #a[i]='A-Z'-большая буква
                    t=chr((ord(a[i])-65+ord(key[i%len(key)].lower())-97)%26+65)
                    b.append(t)
            else: #a[i]==' '
                b.append(' ')
        print(''.join(b))
    elif choise=='4': #Расшивание строки
        c=[]
        for i in range(len(a)):
            if a[i]!=' ':           #a[i]!=' '
                if a[i].islower():  #a[i]='a-z'-маленькая буква
                    t=chr((ord(a[i])-97-ord(key[i%len(key)])+97+26)%26+97)
                    c.append(t)
                else:               #a[i]='A-Z'-большая буква
                    t=chr((ord(a[i])-65-ord(key[i%len(key)].lower())+97+26)%26+65)
                    c.append(t)
            else:                   #a[i]==' '
                c.append(' ')
        print(''.join(c))
    else:
        print('Введенного номера нет')
