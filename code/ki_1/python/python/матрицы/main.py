import random


def mturn(a):
    b = []
    for i in range(n):
        b.append([])
        for j in range(n):
            b[i].append(0)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]
    for i in range(n):
        for j in range(n):
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

a = mturn(a)

for i in range(n):
    for j in range(n):
        m[i][n + j] = a[i][j]

a = mturn(a)

for i in range(n):
    for j in range(n):
        m[n + i][n + j] = a[i][j]

a = mturn(a)

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



























