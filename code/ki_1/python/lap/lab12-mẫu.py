def alig_width(extxt, txt, mlen):
    change_line = []
    add_probels = []
    probels = 0
    for el in txt:
        for letter in el:
            if letter == ' ':
                probels += 1
        add_probels.append(probels)
        probels = 0
    for i in range(len(txt)):
        if len(extxt[i]) != mlen:
            main_p = (mlen - len(txt[i])) // add_probels[i]
            dop_p = (mlen - len(txt[i])) % add_probels[i]
            for letter in txt[i]:
                if letter != ' ':
                    change_line.append(letter)
                else:
                    if dop_p != 0:
                        change_line.append(' ' * (main_p + 2))
                        dop_p -= 1
                    else:
                        change_line.append(' ' * (main_p + 1))
            extxt[i] = ''.join(change_line)
            change_line = []
    for el in extxt:
        print(el)


def alig_left(extxt, txt):
    line = ''
    check = False
    for i in range(len(txt)):
        for element in txt[i]:
            if element != ' ':
                check = True
            if check is False:
                pass
            else:
                line += element
        extxt[i] = line
        check = False
        line = ''
    for el in extxt:
        print(el)


def alig_right(extxt, txt, mlen):
    line = ''
    for i in range(len(txt)):
        for j in range(mlen - len(txt[i])):
            line += ' '
        for element in txt[i]:
            line += element
        extxt[i] = line
        line = ''
    for el in extxt:
        print(el)


def replace(extxt, txt):
    chek = False
    while True:
        try:
            choice = input('Введите через пробел два слова:' +
                           ' сначала - то, что нужно заменить' + '\n').split()
            if len(choice) == 2:
                break
        except:
            print('Введите два слова через пробел!')
    line = ''
    for i in range(len(txt)):
        for element in txt[i].split():
            if (element == choice[0] or element == choice[0] + ','
                    or element == choice[0] + '.' or element == choice[0] + '!'
                    or element == choice[0] + '?'):
                if element != choice[0]:
                    line += choice[1] + element[-1] + ' '
                    chek = True
                else:
                    line += choice[1] + ' '
                    chek = True
            else:
                line += element + ' '
        extxt[i] = line
        line = ''
    if chek:
        for el in extxt:
            print(el)
    else:
        print('Не найдено слово, которое нужно заменить')


def remove(extxt, txt):
    chek = False
    while True:
        try:
            choice = input('Введите слово которое нужно удалить: ')
            if len(choice.split()) == 1:
                break
            print('Введите одно слово!')
        except:
            pass
    line = ''
    for i in range(len(txt)):
        for element in txt[i].split():
            if (element == choice or element == choice + ','
                    or element == choice + '.' or element == choice + '!'
                    or element == choice + '?'):
                if element != choice:
                    line = line[:-1]
                    line += element[-1] + ' '
                    chek = True
                else:
                    chek = True
            else:
                line += element + ' '
        extxt[i] = line
        line = ''
    if chek:
        for el in extxt:
            print(el)
    else:
        print('Не найдено слово, которое нужно удалить')


def calcu(extxt, txt):
    line = []
    operations = ['+', '-']
    nextPass = False
    add = False
    add_n = 0
    for i in range(len(txt)):
        nextPass = False
        fline = txt[i].split()
        add = False
        add_n = 0
        for j in range(len(fline)):
            if nextPass is True:
                nextPass = False
            elif fline[j] not in operations:
                line.append(fline[j])
                add = False
            else:
                if add is True:
                    nextPass = True
                    add_n = int(line[-1])
                    line = line[:-1]
                    if type(fline[j + 1]) == int:
                        if fline[j] == '+':
                            try:
                                line.append(str(add_n + int(fline[j + 1])))
                            except:
                                line.append(str(add_n + int(fline[j + 1][:-1])) + '.')
                        else:
                            try:
                                line.append(str(add_n - int(fline[j + 1])))
                            except:
                                line.append(str(add_n - int(fline[j + 1][:-1])) + '.')
                    else:
                        nextPass = False
                        add = False
                        add_n = 0
                        line.append(fline[j - 1] + ' ' + fline[j])
                else:
                    nextPass = True
                    breakp = False
                    try:
                        add_n = int(line[-1])
                    except:
                        breakp = True
                    if not breakp:
                        line = line[:-1]
                        if fline[j] == '+':
                            try:
                                line.append(str(int(fline[j - 1]) + int(fline[j + 1])))
                            except:
                                line.append(str(int(fline[j - 1]) + int(fline[j + 1][:-1])) + '.')
                        else:
                            try:
                                line.append(str(int(fline[j - 1]) - int(fline[j + 1])))
                            except:
                                line.append(str(int(fline[j - 1]) - int(fline[j + 1][:-1])) + '.')
                        add = True
                    else:
                        line.append(fline[j - 1] + ' ' + fline[j] + ' ' + fline[j + 1])
        extxt[i] = ' '.join(line)
        line = []
    for el in extxt:
        print(el)


def sort(txt):
    predl_lst = ['']
    probels_lst = []
    probels = 0
    ind = 0
    for el in txt:
        for symb in el:
            if symb == ' ':
                probels += 1
            if symb == '–':
                probels -= 1
            if symb != '.':
                predl_lst[ind] += (symb)
            elif symb == '.':
                predl_lst[ind] += (symb)
                predl_lst.append('')
                ind += 1
                probels_lst.append(probels)
                probels = 0
        predl_lst[ind] += ' '
    for i in range(len(probels_lst)):
        for j in range(i + 1, len(probels_lst)):
            if probels_lst[i] < probels_lst[j]:
                probels_lst[i], probels_lst[j] = probels_lst[j], probels_lst[i]
                predl_lst[i], predl_lst[j] = predl_lst[j], predl_lst[i]
    for i in range(len(predl_lst)):
        lst = predl_lst[i].split()
        string = ''
        for j in range(len(lst)):
            if len(string) + len(lst[j]) < 80:
                string += lst[j] + ' '
            else:
                print(string)
                string = ''
                string += lst[j] + ' '
        print(string)


text = ['Today is Monday,',
        'the last Monday of the year 2019,',
        'and only 2 days in this year.',
        'Wish everyone have a good new year.',
        'Next year will be year 2019 + 1 ,',
        'there are 366 days next year, one day more than 2017, 2018, 2019.',
        'Happy new year !!!']

NewText = []
print()
print('Исходный текст:')
for el in text:
    print(el)
    NewText.append(el)
max_len = -1
print()
for el in text:
    if max_len < len(el) < 80:
        max_len = len(el)

while True:
    print('\n1. Выровнить по ширине.')
    print('2. Выровнить по левому краю.')
    print('3. Выровнить по правому краю.')
    print('4. Замена одного слова другим.')
    print('5. Удаление слова.')
    print('6. Замена арифметических выражений.')
    print('7. Вывод предложений по убыванию количества слов.')
    print('0. Заверишить работу программы.\n')
    command = input('Введите номер команды : ')

    if not (command.isdigit()):
        print("Введите номер команды!")

    elif command == '1':
        alig_width(text, NewText, max_len)

    elif command == '2':
        alig_left(text, NewText)

    elif command == '3':
        alig_right(text, NewText, max_len)

    elif command == '4':
        replace(text, NewText)

    elif command == '5':
        remove(text, NewText)

    elif command == '6':
        calcu(text, NewText)

    elif command == '7':
        sort(NewText)

    elif int(command) == 0:
        print("Завершение работы.")
        break
    else:
        print("Введите команду из списка!")
