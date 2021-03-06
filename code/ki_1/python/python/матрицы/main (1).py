import random


def mturn(a, lenght):
    b = []
    for i in range(lenght):
        b.append([])
        for j in range(lenght):
            b[i].append(0)
    for i in range(lenght // 2):
        a[i], a[lenght - i - 1] = a[lenght - i - 1], a[i]
    for i in range(lenght):
        for j in range(lenght):
            b[i][j] = a[j][i]
    return b


n = int(input(''))

k = 0
a = []
for i in range(n):
    a.append([])
    for j in range(n):
        k += 1
        a[i].append(k)

for i in a:
    for j in i:
        print(j, end=' ')
    print()

m = []
for i in range(2 * n):
    m.append([])
    for j in range(2 * n):
        m[i].append(0)

for i in range(n):
    for j in range(n):
        m[i][j] = a[i][j]

a = mturn(a, n)

for i in range(n):
    for j in range(n):
        m[i][n + j] = a[i][j]

a = mturn(a, n)

for i in range(n):
    for j in range(n):
        m[n + i][n + j] = a[i][j]

a = mturn(a, n)

for i in range(n):
    for j in range(n):
        m[n + i][j] = a[i][j]

for i in m:
    print(i)

k = 1
listNumbers = []
for k in range(n * n + 1):
    num = random.randint(1, 4)
    listNumbers.append([num, 0])

for i in range(2 * n):
    for j in range(2 * n):
        elem = m[i][j]
        listNumbers[elem][1] += 1
        if listNumbers[elem][1] == listNumbers[elem][0]:
            m[i][j] = 0

for i in range(2 * n):
    for j in range(2 * n):
        print(m[i][j], end=' ')
    print()


str = input("Введите строку: ")
array = []
for i in range(2 * n):
    array.append([])
    for j in range(2 * n):
        array[i].append(0)

k = 0
for i in range(2*n):
    for j in range(2*n):
        if m[i][j] == 0 and k < len(str):
            array[i][j] = str[k]
            k += 1

if k < len(str):
    m = mturn(m, n*2)
    for i in range(2*n):
        for j in range(2*n):
            if m[i][j] == 0 and k < len(str):
                array[i][j] = str[k]
                k += 1


if k < len(str):
    m = mturn(m, n*2)
    for i in range(2*n):
        for j in range(2*n):
            if m[i][j] == 0 and k < len(str):
                array[i][j] = str[k]
                k += 1

if k < len(str):
    m = mturn(m, n*2)
    for i in range(2*n):
        for j in range(2*n):
            if m[i][j] == 0 and k < len(str):
                array[i][j] = str[k]
                k += 1


for i in array:
    print(i)

















