#Программа сделана Ву Минь Куанг, ИУ7-24Б

from tkinter import *
import tkinter.messagebox as box
import random
import time

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
	return arr

def time_ordered(arr):
    temp_arr = sorted(arr)
    t0 = time.time()
    insertionsortwithbinsearch(temp_arr)
    return time.time() - t0

def time_random(arr):
    random.shuffle(arr)
    t0 = time.time()
    insertionsortwithbinsearch(arr)
    return time.time() - t0

def time_back_ordered(arr):
    temp_arr = sorted(arr)
    temp_arr.reverse()
    t0 = time.time()
    insertionsortwithbinsearch(temp_arr)
    return time.time() - t0

def calc1():
    if innumEntry.get()=='' or innumEntry1.get()=='':
        box.showinfo("Error", "Input error")
        return 1
    else:
        arr=list(map(float, innumEntry1.get().split(' ')))
        innumEntry01.delete(0, END)
        innumEntry01.insert(0, time_ordered(arr)*1000)
        innumEntry04.delete(0, END)
        innumEntry04.insert(0, time_random(arr)*1000)
        innumEntry07.delete(0, END)
        innumEntry07.insert(0, time_back_ordered(arr)*1000)

def calc2():
    if innumEntry3.get()=='' or innumEntry4.get()=='':
        box.showinfo("Error", "Input error")
        return 1
    else:
        arr1=list(map(float, innumEntry4.get().split(' ')))
        innumEntry02.delete(0, END)
        innumEntry02.insert(0, time_ordered(arr1)*1000)
        innumEntry05.delete(0, END)
        innumEntry05.insert(0, time_random(arr1)*1000)
        innumEntry08.delete(0, END)
        innumEntry08.insert(0, time_back_ordered(arr1)*1000)

def calc3():
    if innumEntry6.get()=='' or innumEntry7.get()=='':
        box.showinfo("Error", "Input error")
        return 1
    else:
        arr2=list(map(float, innumEntry7.get().split(' ')))
        innumEntry03.delete(0, END)
        innumEntry03.insert(0, time_ordered(arr2)*1000)
        innumEntry06.delete(0, END)
        innumEntry06.insert(0, time_random(arr2)*1000)
        innumEntry09.delete(0, END)
        innumEntry09.insert(0, time_back_ordered(arr2)*1000)

def calc():
    calc1()
    calc2()
    calc3()

def random1():
    innumEntry1.delete(0, END)
    if(innumEntry.get() != ''):
        try:
            n1 = int(innumEntry.get())
            if innumEntry2.get() == '' :
                box.showinfo("Error", "Input range")
                return 1
        except:
            box.showinfo("Error", "Input N1 again")
    if innumEntry2.get() != '':
        try:
            l, r = map(float, innumEntry2.get().split())
            if l > r:
                box.showinfo("Error", "Range is wrong")    
                return 1
            if innumEntry.get() == '':
                box.showinfo("Error", "Input N1")
                return 1
            try:
                a = []
                n1 = int(innumEntry.get())
                for x in range(n1):
                    k = random.randint(l*10, r * 10)
                    a.append(str(1.0 * k / 10))
                innumEntry1.insert(0, ' '.join(a))
            except:
                box.showinfo("Error", "Input N1 again")
                return 1
        except:
            box.showinfo("Error", "Input range list1 again")
            return 1
    if(len(list(innumEntry2.get().split())) == 1):
        box.showinfo("Error", "Input range")
        return 1
    return 0

def random2():
    innumEntry4.delete(0, END)
    if(innumEntry3.get() != ''):
        try:
            n1 = int(innumEntry3.get())
            if innumEntry5.get() == '' :
                box.showinfo("Error", "Input range")
                return 1
        except:
            box.showinfo("Error", "Input N2 again")
    if innumEntry5.get() != '':
        try:
            l, r = map(float, innumEntry5.get().split())
            if l > r:
                box.showinfo("Error", "Range is wrong")    
                return 1
            if innumEntry3.get() == '':
                box.showinfo("Error", "Input N2")
                return 1
            try:
                a = []
                n1 = int(innumEntry3.get())
                for x in range(n1):
                    k = random.randint(l*10, r * 10)
                    a.append(str(1.0 * k / 10))
                innumEntry4.insert(0, ' '.join(a))
            except:
                box.showinfo("Error", "Input N2 again")
                return 1
        except:
            box.showinfo("Error", "Input range list2 again")
            return 1
    if(len(list(innumEntry5.get().split())) == 1):
        box.showinfo("Error", "Input range")
        return 1
    return 0

def random3():
    innumEntry7.delete(0, END)
    if(innumEntry8.get() != ''):
        try:
            n1 = int(innumEntry6.get())
            if innumEntry8.get() == '' :
                box.showinfo("Error", "Input range")
                return 1
        except:
            box.showinfo("Error", "Input N3 again")
    if innumEntry8.get() != '':
        try:
            l, r = map(float, innumEntry2.get().split())
            if l > r:
                box.showinfo("Error", "Range is wrong")    
                return 1
            if innumEntry6.get() == '':
                box.showinfo("Error", "Input N3")
                return 1
            try:
                a = []
                n1 = int(innumEntry6.get())
                for x in range(n1):
                    k = random.randint(l*10, r * 10)
                    a.append(str(1.0 * k / 10))
                innumEntry7.insert(0, ' '.join(a))
            except:
                box.showinfo("Error", "Input N3 again")
                return 1
        except:
            box.showinfo("Error", "Input range list3 again")
            return 1
    if(len(list(innumEntry8.get().split())) == 1):
        box.showinfo("Error", "Input range")
        return 1
    return 0

def showinfo1():
    box.showinfo('Info', 'Программа сделана Ву Минь Куанг.')

window = Tk()
window.geometry("1000x400+200+200")

innumLabel = Label(window, text = 'N1 = ')
innumEntry = Entry(window, width= 10)
innumLabel.place(x = 0, y = 100)
innumEntry.place(x = 30, y = 100)
innumLabel1 = Label(window, text = '; list 1: ')
innumLabel1.place(x = 90, y = 100)
innumEntry1 = Entry(window, width= 70)
innumEntry1.place(x = 140, y = 100)
innumEntry2 = Entry(window, width= 20)
innumEntry2.place(x = 570, y = 100)
RandomButton1=Button(window,text='Random New',command=random1)
RandomButton1.place(x = 700, y = 100)

innumLabel2 = Label(window, text = 'N2 = ')
innumEntry3 = Entry(window, width= 10)
innumLabel2.place(x = 0, y = 130)
innumEntry3.place(x = 30, y = 130)
innumLabel3 = Label(window, text = '; list 2: ')
innumLabel3.place(x = 90, y = 130)
innumEntry4 = Entry(window, width= 70)
innumEntry4.place(x = 140, y = 130)
innumEntry5 = Entry(window, width= 20)
innumEntry5.place(x = 570, y = 130)
RandomButton2=Button(window,text='Random New',command=random2)
RandomButton2.place(x = 700, y =130)

innumLabel4 = Label(window, text = 'N3 = ')
innumEntry6 = Entry(window, width= 10)
innumLabel4.place(x = 0, y = 160)
innumEntry6.place(x = 30, y = 160)
innumLabel5 = Label(window, text = '; list 3: ')
innumLabel5.place(x = 90, y = 160)
innumEntry7= Entry(window, width= 70)
innumEntry7.place(x = 140, y = 160)
innumEntry8 = Entry(window, width= 20)
innumEntry8.place(x = 570, y = 160)
RandomButton3=Button(window,text='Random New',command=random3)
RandomButton3.place(x = 700, y =160)

calcButton=Button(window,text='Calc',command=calc)
calcButton.place(x = 60, y =190)

innumLabel6 = Label(window, text = 'Упорядоченный массив: ', font=("Arial", 10))
innumLabel6.place(x = 0, y = 270)
innumLabel7 = Label(window, text = 'Случайный массив: ', font=("Arial", 10))
innumLabel7.place(x = 0, y = 310)
innumLabel8 = Label(window, text = 'Обратно упорядоченный массив: ', font=("Arial", 10))
innumLabel8.place(x = 0, y = 350)
innumLabel8 = Label(window, text = 'N1')
innumLabel8.place(x = 300, y = 230)
innumLabel8 = Label(window, text = 'N2')
innumLabel8.place(x = 400, y = 230)
innumLabel8 = Label(window, text = 'N3')
innumLabel8.place(x = 500, y = 230)

innumLabel9 = Label(window, text = 'insertion sort with bin search & caculate time (ms)', font=("Arial", 15))
innumLabel9.place(x = 250, y = 30)
innumLabel10 = Label(window, text = 'Table', font=("Arial", 15))
innumLabel10.place(x = 390, y = 200)

innumEntry01 = Entry(window, width= 10)
innumEntry01.place(x = 270, y = 270)
innumEntry02= Entry(window, width= 10)
innumEntry02.place(x = 370, y = 270)
innumEntry03 = Entry(window, width= 10)
innumEntry03.place(x = 470, y = 270)
innumEntry04 = Entry(window, width= 10)
innumEntry04.place(x = 270, y = 310)
innumEntry05 = Entry(window, width= 10)
innumEntry05.place(x = 370, y = 310)
innumEntry06 = Entry(window, width= 10)
innumEntry06.place(x = 470, y = 310)
innumEntry07 = Entry(window, width= 10)
innumEntry07.place(x = 270, y = 350)
innumEntry08 = Entry(window, width= 10)
innumEntry08.place(x = 370, y = 350)
innumEntry09 = Entry(window, width= 10)
innumEntry09.place(x = 470, y = 350)

menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=window.destroy)
menubar.add_cascade(label='File', menu = filemenu)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu = editmenu)

infomenu = Menu(menubar, tearoff=0)
infomenu.add_command(label='О авторе', command=showinfo1)
menubar.add_cascade(label='Info', menu = infomenu)

window.config(menu=menubar)

window.mainloop()