def new_collect(name):
    file = open(name, 'w')
    count = int(input("Введите количество строк: "))
    for i in range(count):
        st = input()
        if len(st) > 0 and st != len(st) * ' ' and st != len(st) * '    ':
            file.write(st + '\n')
    file.close()


def add(name):
    file = open(name, 'a')
    count = int(input("Введите количество строк: "))
    for i in range(count):
        st = input("Введите строку: ")
        if len(st) > 0 and st != len(st) * ' ' and st != len(st) * '	':
            file.write(st + '\n')
    file.close()


def search_one(name):
    arr = []
    file = open(name, 'r')
    number = int(input("Введите номер стобца: "))
    find = input("Введите запрос: ")
    for line in file:
        arr.append(line.split())
    k = 0
    for i in range(len(arr)):
        if arr[i][number - 1] == find:
            print(*arr[i])
            k = 1
    if not k:
        print('Не найдено элементов')
    file.close()


def search_two(name):
    arr = []
    file = open(name, 'r')
    numb1, numb2 = map(int, input("Введите номера стобцов через пробел: ,"
                                  ).split())
    find = list(map(str, input("Введите два запроса: ").split()))
    for line in file:
        arr.append(line.split())
    k = 0
    for i in range(len(arr)):
        if arr[i][numb1 - 1] == find[0] and arr[i][numb2 - 1] == find[1]:
            print(*arr[i])
            k = 1
    if not k:
        print('Не найдено элементов')
    file.close()


def sort_one(name):
    try:
        file = open(name)
    except:
        print('Ошбибка при открытии файла.')
        return
    tarr = []
    number = int(input("Введите номер стобца: "))
    for line in file:
            tarr.append(line.split())
    file.close()

    for i in range(len(tarr)-1):
        for j in range(len(tarr)-i-1):
            try:
                 int(tarr[j][number-1])
                 ch = True
            except:
                ch = False
            if ch:
                if tarr[j][number-1] < tarr[j+1][number-1]:
                    tarr[j],tarr[j+1] = tarr[j+1],tarr[j]
            else:
                if tarr[j][number-1] > tarr[j+1][number-1]:
                    tarr[j],tarr[j+1] = tarr[j+1],tarr[j]

    try:
        file = open(name,'w')
    except:
        print('Ошибка при открытии файла.')
        return
    for i in range(len(tarr)):
        for j in range(len(tarr[i])):
            file.write('{:15s}'.format(tarr[i][j] + ' '))
        file.write('\n')
    file.close()
    output(name)


def sort_two(name):
    try:
        file = open(name)
    except:
        print('Ошибка при открытии файла.')
        return
    tarr = []
    num_column1, num_column2 = map(int, input("Введите номера стобцов: "
                                              ).split())
    for o in file:
            tarr.append(o.split())
    file.close()

    for i in range(len(tarr)-1):
        for j in range(len(tarr)-i-1):
            try:
                 int(tarr[j][num_column2-1])
                 ch = True
            except:
                ch = False
            if ch:
                if tarr[j][num_column2-1] < tarr[j+1][num_column2-1]:
                    tarr[j],tarr[j+1] = tarr[j+1],tarr[j]
            else:
                if tarr[j][num_column2-1] > tarr[j+1][num_column2-1]:
                    tarr[j],tarr[j+1] = tarr[j+1],tarr[j]

    for i in range(len(tarr)-1):
        for j in range(len(tarr)-i-1):
            try:
                 int(tarr[j][num_column1-1])
                 ch = True
            except:
                ch = False
            if ch:
                if tarr[j][num_column1-1] < tarr[j+1][num_column1-1]:
                    tarr[j],tarr[j+1] = tarr[j+1],tarr[j]
            else:
                if tarr[j][num_column1-1] > tarr[j+1][num_column1-1]:
                    tarr[j],tarr[j+1] = tarr[j+1],tarr[j]

    try:
        file = open(name,'w')
    except:
        print('Ошибка при открытии файла.')
        return
    for i in range(len(tarr)):
        for j in range(len(tarr[i])):
            file.write('{:15s}'.format(tarr[i][j] + ' '))
        file.write('\n')
    file.close()
    output(name)


def output(name):
    file = open(name, 'r')
    print('\n')
    for i in file:
        x = i.split()
        for j in range(len(x)):
            print('{:15s}'.format(x[j]), end='')
        print()
    print('\n')
    file.close()






file_name = 0

print('1. Выбор файла.')
print('2. Создание в файле нового набора.')
print('3. Добавление записи.')
print('4. Вывод всех записей.')
print('5. Поиск по одному полю.')
print('6. Поиск по двум полям.')
print('7. Сортировка по одному полю.')
print('8. Сортировка по двум полям. ')
print('0. Выход.')
while True:
    command = input('Выберете команду : ')

    if not (command.isdigit()):
        print("Введите корректную  команду")

    elif int(command) == 1 or file_name == 0:
        try:
            print("Необходимо выбрать файл")
            file_name = input('Введите имя файла: ')
            file = open(file_name)
        except FileNotFoundError:
            print("Неверное имя файла")
            file_name = 0
        file.close()

    elif int(command) == 2:
        new_collect(file_name)

    elif int(command) == 3:
        add(file_name)

    elif int(command) == 4:
        output(file_name)

    elif int(command) == 5:
        search_one(file_name)

    elif int(command) == 6:
        search_two(file_name)

    elif int(command) == 7:
        sort_one(file_name)

    elif int(command) == 8:
        sort_two(file_name)

    elif int(command) == 0:
        print("Завершение работы")
        break

    else:
        print("Команды не найдено. Введите команду из списка")
