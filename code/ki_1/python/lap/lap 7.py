#Программа сделана Ву Минь Куанг ИУ7-14Б
#Найти среднее арифметическое положительных элементов каждого столбца матрицы S(x,y)
#Результаты запомнить в массиве У.Если в столбце нет положительных элементов, то в массиве У не будет элемента
#В сформированном массиве У поменять местами максимальный элемент с последним
#Напечагать матрицу S в виде матрицы и сфор. массив У

s=[]
n=[]
x=int(input('Введите количество строк: '))
y=int(input('Введите количество столбцов: '))
print('Введите каждую строку матрицы: ')
for i in range(x):
    t=[i for i in input().split()]
    s.append(t)
for i in range(y):
    m,k=0,0
    for j in range(x):
        if float(s[j][i])>0:
            m+=float(s[j][i])
            k+=1
    if m!=0:
        n.append(str(float(m/k)))
    else:
        continue
print('Матрица S:')
for i in range(x):
    for j in range(y):
        print('{:^5}'.format(s[i][j]),end='')
    print()
print()
print(' '.join(n))
print('Значение максимального элемента: ',max(n))
for i in range(len(n)):
    if n[i]==max(n):
        n[i],n[len(n)-1]=n[len(n)-1],n[i]
        break
print('Массив Y: ',' '.join(n))

