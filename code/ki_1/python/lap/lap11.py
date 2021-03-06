from pickle import dump, load

def menu() :
    print('''\
        1. Создание БД.
        2. Добавление записи в БД.
        3. Вывод всей БД.
        4. Поиск записи по одному полю.
        5. Поиск записи по двум полям.
        0. Завершить программу 
        '''
        )
def key_in_db(db_file, req_key):
    global keys_count
    with open(db_file, 'rb') as db:
        # Начинаем чтение
        for _ in range(keys_count):
            cur_key = list(load(db).keys())[0]  # Название текущей записи
            # Если нашли запись
            if cur_key == req_key:
                return True
        # Если не нашли
        return False 

def add_to_db(db_file, new_note):    
    with open(db_file, 'ab') as db:
        dump(new_note, db)  # Добавляем новую запись в файл

def get_all_boxes_names(db_file):
    global keys_count
    with open(db_file, 'rb') as db:
        boxes = []  
        for _ in range(keys_count):
            cur_line = load(db)  
            cur_key = list(cur_line.keys())[0]  
            for b in cur_line[cur_key]:
                if b not in boxes:
                    boxes.append(b)
        return boxes

def search_boxes(db_file, *req_boxes):
    keys = []  
    with open(db_file, 'rb') as db:
        for _ in range(keys_count):
            cur_line = load(db)                 # Текущая запись с полями
            cur_key = list(cur_line.keys())[0]  # Название текущей записи
            # Пробегаемся по искомым полям и их значениям
            for i in range(0, len(req_boxes), 2):
                req_box, req_value = req_boxes[i: i + 2]  # Название искомого поле и его искомое значение
                # Если этого поля нет, или его значение отличется от искомого, завершаем цикл
                if req_box not in cur_line[cur_key] or cur_line[cur_key][req_box] != req_value:
                    break
            # Если цикл прошел без остановки, добавляем имя записи в список
            else:
                keys.append(cur_key)
        return keys

choice = ''     # Номер команды
file_name = ''  # Имя файла
keys_count = 0  # Количество записей в текущей базе данных

while choice != '0':
    menu()
    choice = input('Введите команду: ').strip()
    while not choice or choice not in map(str, range(6)):
        print('Некорректый ввод команды. Повторите попытку')
        choice = input('Введите команду: ').strip()

    if choice == '1':
        new_file_name = input('Введите название файла: ').strip()  # Название нового файла
        # Если ввели непустую строку
        if new_file_name:
            file_name = new_file_name  # Меняем имя файл
            open(file_name, 'wb').close()  # Создаем новый файл
            print('Создана база данных "{}"'.format(file_name))
            keys_count = 0
        else:
            print('Вы ввели пустую строку')

    elif choice == '2':
        # Если мы знаем, с каким файлом работать
        if file_name:
            add_key = True  # True, если нужно добавить еще одну запись
            while add_key:
                new_key = input('Введите название новой записи: ').strip()
                while not new_key or key_in_db(file_name, new_key):
                    if not new_key:
                        print('Вы ввели пустую строку. Повторите попытку')
                    else:
                        print('Данная запись уже присутствует в базе данных. Повторите попытку')
                    new_key = input('Введите название новой записи: ').strip()
                new_line = {new_key: {}}
                add_box = True  # True, если нужно добавить еще одно поле
                # Вводим новые поля
                while add_box:
                    # Вводим корректное название нового поля
                    new_box = input('Введите название нового поля: ').strip()
                    # Пока название - пустая строка, или это поле уже присутствует в записи
                    while not new_box or new_box in new_line[new_key]:
                        if not new_box:
                            print('Вы ввели пустую строку. Повторите попытку')
                        else:
                            print('Данное поле уже присутствует в базе данных. Повторите попытку')
                        new_box = input('Введите название нового поля: ').strip()
                    value = input('Введите значение нового поля: ').strip()
                    while not value:
                        print('Вы ввели пустую строку. Повторите попытку')
                        value = input('Введите значение нового поля: ').strip()
                    new_line[new_key][new_box] = value
                    # Спрашиваем пользователя, нужно ли добавить в запись еще одно поле
                    answer = input('Добавить новое поле (y/n)? ').strip().lower()
                    while not answer or answer not in ['y', 'n']:
                        print('Некорректный ответ. Повторите попытку')
                        answer = input('Добавить новое поле (y/n)? ').strip().lower()
                    if answer == 'n':
                        add_box = False
                add_to_db(file_name, new_line)
                keys_count += 1
                print('Добавлена запись')
                answer = input('Добавить новую запись (y/n)? ').strip().lower()
                while not answer or answer not in ['y', 'n']:
                    print('Некорректный ответ. Повторите попытку')
                    answer = input('Добавить новую запись (y/n)? ').strip().lower()
                if answer == 'n':
                    add_key = False
        else:
            print('Для начала создайте новый файл')

    elif choice == '3':
        if file_name:
            with open(file_name, 'rb') as file:
                unique_boxes = get_all_boxes_names(file_name)
                if keys_count:
                    print('-' * (15 + (16 * len(unique_boxes))))
                    print(' ' * 15, end='')
                    for box in unique_boxes:
                        print('|{:^15}'.format(box), end='')
                    print()
                    print('-' * (15 + (16 * len(unique_boxes))))
                    for c in range(keys_count):
                        line = load(file)  
                        key = list(line.keys())[0] 
                        print('{:^15}'.format(key), end='')
                        for box in unique_boxes:
                            element = '-'
                            if box in line[key]:
                                element = line[key][box]
                            print('|{:^15}'.format(element), end='')
                        print()
                        print('-' * (15 + (16 * len(unique_boxes))))
                else:
                    print('База данных пуста')
        else:
            print('Для начала создайте новый файл')

    elif choice == '4':
        # Если знаем, с каким файлом работать
        if file_name:
            # Если база данных не пуста
            if keys_count:
                # Вводим корректные данные
                required_box = input('Введите искомое поле: ').strip()  # Искомое поле
                required_value = input('Введите искомое значение: ').strip()  # Искомое значения поля
                while not required_value or not required_box:
                    print('Некорректные введенные данные. Повторите попытку')
                    required_box = input('Введите искомое поле: ').strip()
                    required_value = input('Введите искомое значение: ').strip()
                result = search_boxes(file_name, required_box, required_value)  # Записи с искомыми параметрами
                # Если записи найдены
                if result:
                    print('Найденные записи: {}'.format(', '.join(result)))
                else:
                    print('Ничего не найдено')
            else:
                print('База данных пуста')
        else:
            print('Для начала создайте новый файл')

    elif choice == '5':
        # Если знаем, с каким файлом работать
        if file_name:
            # Если база данных не пуста
            if keys_count:
                # Вводим корректные данные
                required_box_1 = input('Введите первое искомое поле: ').strip()  # Первое искомое поле
                required_value_1 = input('Введите искомое значение этого поля: ').strip()  # Искомое значение поля
                required_box_2 = input('Введите второе искомое поле: ').strip()  # Второе искомое поле
                required_value_2 = input('Введите искомое значение этого поля: ').strip()
                while not required_value_1 or not required_box_1 or not required_value_2 or not required_box_2:
                    print('Некорректные введенные данные. Повторите попытку')
                    required_box_1 = input('Введите первое искомое поле: ').strip()
                    required_value_1 = input('Введите искомое значение этого поля: ').strip()
                    required_box_2 = input('Введите второе искомое поле: ').strip()
                    required_value_2 = input('Введите искомое значение этого поля: ').strip()
                # Ищем записи с искомыми параметрами
                result = search_boxes(file_name, required_box_1, required_value_1, required_box_2, required_value_2)
                # Если записи найдены
                if result:
                    print('Найденные записи: {}'.format(', '.join(result)))
                else:
                    print('Ничего не найдено')
            else:
                print('База данных пуста')
        else:
            print('Для начала создайте новый файл')
    
# Если пользователь ввел 0, завершаем работу
print('Завершение работы...')
