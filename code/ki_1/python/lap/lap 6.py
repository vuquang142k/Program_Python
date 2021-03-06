#Программа сделана Ву Минь Куанг ИУ7-14Б
#Написать программу, которая позволит с использованием меню:
#1.Проинициализировать список первыми N элементами заданного ряда
#2.Добавить элемент в произвольное место списка
#3.Удалить произвольный элемент из списка
#4.Очистить список
#5.Найти значение K-го экстремума в списке, если он является списком чисел
#6.Найти наиболее длинную последовательность чисел по варианту
#7.Найти последовательность, включающую в себя наибольшее количествоэлементов-строк по варианту


group=[]
choice=None
def check(po, lo = 0):
    try:
        if lo == 0: s = float(po)
        else: s = int(po)
        return 1
    except:
        return 0
def is_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return 1
    return 0
A=['u','e','o','a','i','U','E','O','A','I']
while choice!='0':
    print(
    '''
    1.Проинициализировать список первыми N элементами заданного ряда
    2.Добавить элемент в произвольное место списка
    3.Удалить произвольный элемент из списка
    4.Очистить список
    5.Найти значение K-го экстремума в списке, если он является списком чисел
    6.Найти наиболее длинную последовательность чисел по варианту
        Убывающая последовательность отрицательных чисел, модуль которых является простым числом.
    7.Найти последовательность, включающую в себя наибольшее количество элементов-строк по варианту
        Строк, содержащих удвоенные согласные
    0.Вывод
    '''
    )
    choice=input('Выбор: ')
    if choice=='0':
        print('Вывод')
    else:
        if choice=='1':
            N = int(input())
            if check(N) and 0 < int(N):
                group=[0]*N
                for i in range(N):
                    group[i]=input()
            else:
                print('N не положительное число')
        elif choice=='2':
            index=int(input('Место элемента: '))
            val=input('Добавить элемент: ')
            if index >=0:
                group.insert(index,val)
        elif choice=='3':
            x = input('Место элемента: ')
            if check(x):
                group.pop(int(x))
            else:
                print('Место не число')
        elif choice=='4':
            group=[]
        elif choice=='5':
            ok = 1
            for x in group:
                if not check(x):
                    ok = 0
                    break
            if ok == 0:
                print('Это не список чисел')
            else:
                ok = 0
                k = input('Введите число k: ')
                if not check(k):
                    print('k не число')
                    continue
                for x in range(1, len(b) - 1):
                    if float(group[x]) > float(group[x - 1]) and float(group[x]) > float(group[x + 1]):
                        ok += 1
                    elif float(group[x]) < float(group[x - 1]) and float(group[x]) < float(group[x + 1]):
                        ok += 1
                    if ok == int(k):
                        print('Значение {:g}-ого экстремума в списке: {:g}'.format(int(k), float(b[x])))
                        break
                if ok < int(k):
                    print('Нет {:g}-ого экстремума в списке.'.format(int(k)))
        elif choice=='6':
            a=[]
            for i in range(len(group)):
                if int(group[i])<0 and is_prime(abs(int(group[i])))==1 and check(group[i], 1) :
                    a.append(group[i])
                a.sort(reverse=True)
            print(len(a))
                
        elif choice=='7':
            b = []
            for s in group:
                j = 0
                for i in range(len(s)):
                    if s[i].isalpha() and s[i] not in A:
                        j += 1
                if j * 2 == len(s):
                    b.append(s)
            print(max(b))
        else:
            print('Введенного номера нет',choice)
print(group)
