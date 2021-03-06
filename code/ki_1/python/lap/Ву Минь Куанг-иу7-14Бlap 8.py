#Вычислить интергнал методом правых прямоугольников, методом 3/8
#Программа сделана Ву Минь Куанг группа ИУ7-14Б


from math import*
# Вычесление значения производной
def f(x):
    return 5


# Вычесление значения первообразной
def F(x):
    return 5*x

# Вычисление интеграла методом правых прямоугольников
def Integral_right_rect(n, start, stop):
    integral = 0
    h = (stop - start) / n
    for i in range(1, n + 1):
        integral += h * f(start + i * h)
    return integral

# Вычисление интеграла методом 3/8
def Integral_38(n, start, end):
    if n % 3 != 0:
        return '—'
    I1 = 0
    I2 = 0
    h = abs(start - end) / n

    for i in range(1, int(n), 3):
        I1 += f(start + i * h)
        i += 1
        I1 += f(start + i * h)

    for i in range(3, int(n), 3):
        I2 += f(start + i * h)

    return 3 * h / 8 * (f(start) + f(end) + 3 * I1 + 2 * I2)


n1 = int(input('Введите кол-во участков n1: '))
n2 = int(input('Введите кол-во участков n2: '))
a = float(input('Введите начало интегрирования: '))
b = float(input('Введите конец интегрирования: '))

I=F(b)-F(a)

I1_n1=Integral_right_rect(n1,a,b)
I1_n2=Integral_right_rect(n2,a,b)
I2_n1=Integral_38(n1,a,b)
I2_n2=Integral_38(n2,a,b)

print(f'\nМетод          n1 = {n1}           n2 = {n2}')
print('пр. прям. ' + '{:14.7f}'.format(I1_n1) + '{:19.7f}'.format(I1_n2))
if n1 % 3 != 0 or n2 % 3 != 0:
    if n1 % 3 != 0:
        print('3/8            ' + I2_n1, end='         ')
    else:
        print('3/8' + '{:22.7f}'.format(I2_n1), end='')
    if n2 % 3 != 0:
        print('        ' + I2_n2)
    else:
        print('{:18.7f}'.format(I2_n2))
else:
    print('3/8' + '{:21.7f}'.format(I2_n1) + '{:19.7f}'.format(I2_n2))

print(f'\nТочное значение: {I}')

if I2_n1 != '—' and I2_n2 != '—':
    my_dict = {I2_n1: 'I2_n1', I2_n2: 'I2_n2',I1_n1: 'I1_n1', I1_n2: 'I1_n2'}
elif I2_n1 == '—' and I2_n2 != '—':
    my_dict = {I2_n2: 'I2_n2', I1_n1: 'I1_n1', I1_n2: 'I1_n2'}
elif I2_n1 != '—' and I2_n2 == '—':
    my_dict = {I2_n1: 'I2_n1', I1_n1: 'I1_n1', I1_n2: 'I1_n2'}
else:
    my_dict = {I1_n1: 'I1_n1', I1_n2: 'I1_n2'}

d = 0
Integ_not_exect_name = None
for e in my_dict:
    if abs(I - e) > d:
        d = abs(I - e)
        Integ_not_exect_name = my_dict[e]  # в Integ_not_exect_name запоминаем наимен. наименее точного интеграла
        Integ_not_exect = e  # в Integ_not_exect запоминаем значение наименее точного интеграла

if Integ_not_exect_name == 'I2_n1':
    print(f'\nНаименее точный результат дал метод 3/8 при n1 = {n1}\n')
    k = n1;
    k1 = n1
elif Integ_not_exect_name == 'I2_n2':
    print(f'\nНаименее точный результат дал метод 3/8 при n2 = {n2}\n')
    k = n2;
    k1 = n1
elif Integ_not_exect_name == 'I1_n1':
    print(f'\nНаименее точный результат дал метод правых треугольников при n1 = {n1}\n')
    k = n1;
    k1 = n1
elif Integ_not_exect_name == 'I1_n2':
    print(f'\nНаименее точный результат дал метод правых треугольников при n2 = {n2}\n')
    k = n2;
    k1 = n1

# Уточняем значение менее точного интеграла до точности eps
flag = False
eps = float(input('Введите точность eps: '))
if Integ_not_exect_name == 'I2_n1' or Integ_not_exect_name == 'I2_n2':
    while abs(Integral_38(2 * k, a, b) - Integral_38(k, a, b)) > eps:
        k *= 2
else:
    flag = True
    while abs(Integral_right_rect(2 * k, a, b) - Integral_right_rect(k, a, b)) > eps:
        k *= 2

print(f'\nТочности eps удалось достичь при увеличении кол-ва участков с {k1} до {k}')
if flag:
    print('Вычисленное значение интеграла: ' '{:10.7f}'.format(Integral_right_rect(k, a, b)))
else:
    print('Вычисленное значение интеграла: ' '{:10.7f}'.format(Integral_38(k, a, b)))

print(f'\nАбсолютная погрешность: {abs(I - Integ_not_exect)}')
print(f'Относительная погрешность: {abs((I - Integ_not_exect) / I)}')
