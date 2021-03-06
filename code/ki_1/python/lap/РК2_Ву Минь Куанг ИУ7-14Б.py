#Программа сделана Ву Минь Куанг ИУ7-14Б

n=int(input('Введите число n: '))
s=[]
print('Введите каждую строку матрицы: ')
for i in range(n):
    s.append([])
    for j in range(n):
        s[i].append(0)

for i in range(n):
    a=input()
    for j in range(len(a)):
        s[i][j]=a[j]

for i in range(n):
    for j in range(n):
        if i+j<n-1:
            s[n-1-j][n-1-i]=s[i][j]

for i in range(n):
    for j in range(n):
        if i>j:
            s[j][i]=s[i][j]

for i in s:
    for j in i:
        print(j,end='')
    print()
print()
for j in range(n-1,-1,-1):
    mn=0
    imn=0
    for k in range(j+1):
        cnt=0
        for l in  range(n):
            if s[l][k]=='.':
                cnt+=1
        if cnt>mn:
            mn=cnt
            imn=k
    for k in range(n):
        s[k][j],s[k][imn]=s[k][imn],s[k][j]
for i in s:
    for j in i:
        print(j,end='')
    print()
print()
                

