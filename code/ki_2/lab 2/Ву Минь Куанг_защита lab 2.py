from tkinter import *
def bubblesort(arr):
	n=len(arr)
	for i in range(n-1):
		for j in range(n-1-i):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
	return arr
def calc():
    s=[i for i in n1_in.get().split()]
    a=[]
    b=[]
    for k in range(len(s)):
        try:
            t=int(s[k])
            a.append(t)
        except:
            b.append(s[k])    
    a=bubblesort(a)
    b=bubblesort(b)
    t=''
    for i in a:
        t=t+str(i)+' '
    for i in b:
        t=t+i+' '
    n2_in.delete(0,END)
    n2_in.insert(0, t)
window = Tk()
window.title("test")
window.configure(bg = "#f0f0f0")
window.geometry("1200x600")

n1 = Label(window, text =  "ввод ")
n1.grid(row = 0, column = 0)

n1_in = Entry(window, width = 50)
n1_in.grid(row = 0, column = 1, padx = 10)

n2 = Label(window, text =  "результат ")
n2.grid(row = 1, column = 0)
n2_in = Entry(window, width = 50)
n2_in.grid(row = 1, column = 1, padx = 10)
work = Button(window, text = 'calc', command = calc)
work.grid(row = 3, column = 2)
