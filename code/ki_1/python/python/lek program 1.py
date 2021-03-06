#Сформировать массив из чисел,деляющихся на
#число два без остатка
#input in string
A=list(map(int,input('input list: ').split()))
print(A)
B=[]
for x in A:
    if x%2==0:
        B.append(x)
print(B)
print()

d=[t for t in A if t%2==0]
print(t)
pritn()

#Траниционный способ
k=-1
N=len(A)
W=[0]*N
for i in range(N):
    if A[i]%2==0:
        k+=1
        W[k]=A[i]
        print(k,'  ',W[k])
print()
for j in range(k+1)
print(W[j])





#Max in List
X=[]
X=list(map(int,input().split()))

#Найти максимальный элемент
XMax=X[0]
for R in X:
    if R>XMax:
        XMax=R
print(XMax)

#Найти максимальный элемент и его номер
XMax=X[0]
NMax=0
for i in range(1,len(X)):
    if X[i]>XMax:
        XMax]=X[i]
        NMax=i
print(XMax,NMax)

#Другой способ
NMax=0
for i in range(1,len(X)):
    if X[i]>X[NMax]
        NMax=i
print(X[NMax],'  ',NMax)

#max,index Python
XMax=max(X)
NMax=X.index(XMax)
print(XMax, RMax)



#Search
X=[1,4,9,3,2]
R=5
k=0
N=len(X)
while k<N and X[k] !=R:
    k+=1
if(k<N):
    print(k)
else:
    print('нет элемента')

X=[1,4,9,3,2]
R=2
X.append(R)
while X[k]!=R:
    k+=1
if k==len(X)-1:
    print('No')
else:
    print(k)

