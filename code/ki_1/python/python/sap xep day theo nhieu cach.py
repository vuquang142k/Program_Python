
s1=[4,8,2,5,9,1]
s2=[4,8,2,9,5,1]
s3=[-4,-3,-2,-1,4,8,2,9,5,1]
s4=[10,-4,-3,-2,-1,4,8,2,9,5,1]
s5=[10,-4,-3,-2,-1,4,8,2,9,5,1]
s6=[4,8,2,9,5,1]
s7=[4,8,2,9,5,1]
s8=[4,8,2,9,5,1]

#sort
#Сортировка выбором
def selectionsort(arr):
	for i in range(len(arr)):
		minind=i
		for j in range(i+1,len(arr)):
			if arr[j]<arr[minind]:
				minind=j
		arr[i],arr[minind]=arr[minind],arr[i]
		print(i,':',*arr)
	return arr

#Метод пузырька
def bubblesort(arr):
	n=len(arr)
	for i in range(n-1):
		for j in range(n-1-i):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
		print(i,':',*arr)
	return arr

#Метод пузырька с флагом
def bubblesortwithflag(arr):
	n=len(arr)
	for i in range(n-1):
		flag=True
		for j in range(n-1-i):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
			flag=False
		if flag:
			break
		print(i,':',*arr)
	return arr

#Шейкер-сортировка
def shakersort(arr):
	left=0
	right=len(arr)-1
	print(left,right)
	while left<right:
		r_new=left
		for i in range(left,right):
			if arr[i]>arr[i+1]:
				arr[i],arr[i+1]=arr[i+1],arr[i]
				r_new=i
			right=r_new
			print(*arr,'|',left,right)
		l_new=right
		for i in range(right-1,left-1,-1):
			if arr[i]>arr[i+1]:
				arr[i],arr[i+1]=arr[i+1],arr[i]
				l_new=i
			left=l_new
			print(*arr,'|',left,right)
	return arr

#Сортировка вставками
def insertionsort(arr):
	for i in range(1,len(arr)):
		cur=arr[i]
		j=i-1
		while j>=0 and cur<arr[j]:
			arr[j+1]=arr[j]
			j=j-1
		arr[j+1]=cur
		print(i,':',arr[:i],'|',arr[i:])
	return arr

#Метод Вставками с бинарным поиском
def insertionsortwithbinsearch(arr):
	for i in range(1,len(arr)):
		cur=arr[i]
		lo=0
		hi=i
		if lo==hi:lo+=1
		else:
			while lo<hi:
				mid=(lo+hi)//2
				if cur<arr[mid]:hi=mid
				else:lo=mid+1
		j=i
		while j>lo and j>0:
			arr[j]=arr[j-1]
			j=j-1
		arr[lo]=cur
		print(i,':',*arr)
	return arr

#Метод Шелла
def Shellsort(arr):
	inc=len(arr)//2
	while inc:
		for i,el in enumerate(arr):
			while i>=inc and arr[i-inc]>el:
				arr[i]=arr[i-inc]
				i-=inc
			arr[i]=el
			print(i,':',*arr,'|',inc)
		if inc==2:
			inc=1
		else:
			inc=int(inc*5.0/11)
	return arr

#Быстрая сортировка
import random as r
def quicksort(arr,start=0,end=None):
	if len(arr)==0:
		return arr
	pind=r.randint(start,end-1)
	pivot=arr[pind]
	left=[x for x in arr if x<pivot]
	right=[x for x in arr if x>pivot]
	print('pivot: ',pind,pivot)
	print('left: ',left)
	print('right: ',right)
	return quicksort(left,0,len(left))+[pivot]+quicksort(right,0,len(right))

selectionsort(s1)
print()
bubblesort(s2)
print()
bubblesortwithflag(s3)
print()
shakersort(s4)
print()
insertionsort(s5)
print()
insertionsortwithbinsearch(s6)
print()
Shellsort(s7)
print()
a=quicksort(s8,0,len(s8))
print(a)
print()
