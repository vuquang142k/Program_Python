"""
принять на вход матрицу
принять на вход ось симметрии -- индекс столбца
развернуть элементы матрицы относительно оси симметрии
излишние стобцы обнулить
"""

y = int(input('Введите количество строк матрицы: '))
x = int(input('Введите количество столбцов матрицы: '))
matrix = []

for line in range(y):
    temp_line = []
    print('Построчно введите элементы строки №{}'.format(line))
    for elem in range(x):
        temp_line.append(int(input('{}: '.format(elem))))
    matrix.append(temp_line)

print('Вы ввели следующую матрицу:')
for line in matrix:
    for elem in line:
        print('{:^5}'.format(elem), end='')
    print()
print()

index = int(input('Введите индекс симметрии: '))

arm = min(index, x - index - 1)

for line in matrix:
    for elem_index in range(x):
        if abs(index - elem_index) > arm:
            line[elem_index] = 0
        else:
            if elem_index < index:
                line[elem_index], line[2*index - elem_index] = line[2*index - elem_index], line[elem_index]


print('Обработанная матрица:')
for line in matrix:
    for elem in line:
        print('{:^5}'.format(elem), end='')
    print()
print()   
