''' Ву Минь Куанг - ИУ7И-24Б '''


from math import floor
from tkinter import *
window = Tk()
window.title('Программа перевода числа из 10-й системы счисления в 5-ю и обратно.')
window.geometry("600x200")
import tkinter.messagebox as box
num10 = ['1','2','3','4','5','6','7','8','9','.','0','-']
num5 = ['1','2','3','4','.','0','-']
def aboutme():
    box.showinfo('About me','Ву Минь Куанг - ИУ7И-24Б')
def DecToFive(number):
    number_10 = str(number).split('.')
    if len(number_10) == 2:
        if number_10[0][0] != '-':
            number_10[1] = float('0' + '.' + number_10[1])
            number_10[0] = int(number_10[0])
            number_5 = list()
            temp = list()
            flag = True
            while flag:
                temp.append(str(number_10[0] % 5))
                number_10[0] = number_10[0] // 5
                if number_10[0] < 5:
                    temp.append(str(number_10[0]))
                    flag = False
            temp = ''.join(temp)
            if temp[-1] == '0':
                number_5.append(temp[::-1][1:])
            else:
                number_5.append(temp[::-1])
            flag = True
            temp = list()
            for i in range(0,6):
                temp.append(str(floor(number_10[1]*5)))
                number_10[1] = number_10[1]*5 - floor(number_10[1]*5)
            temp = ''.join(temp)
            number_5.append(temp)
            return (number_5[0] + '.' + number_5[1])
        else:
            number_10[1] = float('0' + '.' + number_10[1])
            number_10[0] = int(number_10[0][1:])
            number_5 = list()
            temp = list()
            flag = True
            while flag:
                temp.append(str(number_10[0] % 5))
                number_10[0] = number_10[0] // 5
                if number_10[0] < 5:
                    temp.append(str(number_10[0]))
                    flag = False
            temp = ''.join(temp)
            if temp[-1] == '0':
                number_5.append('-' + temp[::-1][1:])
            else:
                number_5.append('-' + temp[::-1])
            flag = True
            temp = list()
            for i in range(0,6):
                temp.append(str(floor(number_10[1]*5)))
                number_10[1] = number_10[1]*5 - floor(number_10[1]*5)
            temp = ''.join(temp)
            number_5.append(temp)
            return (number_5[0] + '.' + number_5[1])

    if len(number_10) == 1:
        if number_10[0][0] != '-':
            number_10[0] = int(number_10[0])
            print(number_10[0])
            temp = list()
            flag = True
            while flag:
                temp.append(str(number_10[0] % 5))
                number_10[0] = number_10[0] // 5
                if number_10[0] < 5:
                    temp.append(str(number_10[0]))
                    flag = False
            temp = ''.join(temp)
            if temp[-1] == '0':
                return temp[::-1][1:]
            else:
                return temp[::-1]  
        else:
            number_10[0] = int(number_10[0][1:])
            temp = list()
            flag = True
            while flag:
                temp.append(str(number_10[0] % 5))
                number_10[0] = number_10[0] // 5
                if number_10[0] < 5:
                    temp.append(str(number_10[0]))
                    flag = False
            temp = ''.join(temp)
            if temp[-1] == '0':
                return '-' + temp[::-1][1:]
            else:
                return '-' + temp[::-1] 
def FiveToDec(number):
    number_5 = number.split('.')
    if len(number_5) == 1:
        if (number_5[0][0]) != '-':
            sum = 0
            number_5[0] = number_5[0][::-1]
            for i,ele in enumerate(number_5[0]):
                sum += int(ele)*pow(5,i)
            return str(sum)
        else:
            sum = 0
            number_5[0] = number_5[0][1:][::-1]
            for i,ele in enumerate(number_5[0]):
                sum += int(ele)*pow(5,i)
            return '-' + str(sum)
            
    if len(number_5) == 2:
        if number_5[0][0] != '-':
            sum = 0
            number_5[0] = number_5[0][::-1]
            for i,ele in enumerate(number_5[0]):
                sum += int(ele)*pow(5,i)
            for i,ele in enumerate(number_5[1]):
                sum += int(ele)*pow(5,-i-1)
            return '{:.5f}'.format(sum)
        else:
            sum = 0

            number_5[0] = number_5[0][1:][::-1]
            for i,ele in enumerate(number_5[0]):
                sum += int(ele)*pow(5,i)
            for i,ele in enumerate(number_5[1]):
                sum += int(ele)*pow(5,-i-1)
            return '-{:.5f}'.format(sum) 


 
def From10to5():

    From10to5 = Tk()
    From10to5.title('Из 10-й системы счисления в 5-ю')

    # Экран калкуляртора
    ent = Entry(From10to5, width = 35, borderwidth=5)
    ent.grid(row = 0, column = 0, columnspan= 3, padx = 10, pady = 10)

    def button_add(num):
        ent.insert(END, num)
    def button_DEL():
        temp = ent.get()
        ent.delete(0,END)
        ent.insert(0,temp[:-1])
    def button_AC():
        ent.delete(0,END)
    def button_equal():
        temp = ent.get()
        if len(temp) == 0:
            box.showwarning('Warning','Пустой ввод.')
        else:
            if temp[0] == '.' or temp[-1] == '.' or temp.count('.')>1 or (temp[0]=='-' and temp[1]=='.'):
                box.showwarning('Warning','Нет правильного ввода.')
            else:
                for i in range(len(temp)):
                    if temp[i] not in num10 or ('-' in temp and temp.index('-')!=0) or temp.count('-')>1:
                        box.showwarning('Warning','Нет правильного ввода.')
                        break
                else:
                    box.showinfo('Результат',DecToFive(temp))



    # Кнопки
    btn1 = Button(From10to5,text = '1',padx = 40, pady = 20, command =lambda:  button_add('1'))
    btn2 = Button(From10to5,text = '2',padx = 40, pady = 20, command =lambda:  button_add('2'))
    btn3 = Button(From10to5,text = '3',padx = 40, pady = 20, command =lambda:  button_add('3'))
    btn4 = Button(From10to5,text = '4',padx = 40, pady = 20, command =lambda:  button_add('4'))
    btn5 = Button(From10to5,text = '5',padx = 40, pady = 20, command =lambda:  button_add('5'))
    btn6 = Button(From10to5,text = '6',padx = 40, pady = 20, command =lambda:  button_add('6'))
    btn7 = Button(From10to5,text = '7',padx = 40, pady = 20, command =lambda:  button_add('7'))
    btn8 = Button(From10to5,text = '8',padx = 40, pady = 20, command =lambda:  button_add('8'))
    btn9 = Button(From10to5,text = '9',padx = 40, pady = 20, command =lambda:  button_add('9'))
    btn0 = Button(From10to5,text = '0',padx = 40, pady = 20, command =lambda:  button_add('0'))
    btnMinus = Button(From10to5,text = '-',padx = 40, pady = 20, command =lambda:  button_add('-'))
    btnDEL = Button(From10to5,text = 'DEL',padx = 35, pady = 20, command = button_DEL)
    btnAC = Button(From10to5,text = 'AC',padx = 35, pady = 20, command = button_AC)
    btndot = Button(From10to5,text = '.',padx = 40, pady = 20, command =lambda:  button_add('.'))
    btnequal = Button(From10to5,text = '=',padx = 40, pady = 20, command = button_equal)

    btn7.grid(row = 1, column = 0)
    btn8.grid(row = 1, column = 1)
    btn9.grid(row = 1, column = 2)

    btn4.grid(row = 2, column = 0)
    btn5.grid(row = 2, column = 1)
    btn6.grid(row = 2, column = 2)

    btn1.grid(row = 3, column = 0)
    btn2.grid(row = 3, column = 1)
    btn3.grid(row = 3, column = 2)

    btn0.grid(row = 4, column = 0)
    btnDEL.grid(row = 4, column = 1)
    btnAC.grid(row = 4, column = 2)

    btnMinus.grid(row = 5, column = 0)
    btndot.grid(row = 5, column=1)
    btnequal.grid(row = 5, column = 2)

    From10to5.mainloop()

def From5to10():
    From10to5 = Tk()
    From10to5.title('Из 5-й системы счисления в 10-ю')

    # Экран калкуляртора
    ent = Entry(From10to5, width = 35, borderwidth=5)
    ent.grid(row = 0, column = 0, columnspan= 3, padx = 10, pady = 10)

    def button_add(num):
        ent.insert(END, num)
    def button_DEL():
        temp = ent.get()
        ent.delete(0,END)
        ent.insert(0,temp[:-1])
    def button_AC():
        ent.delete(0,END)
    def button_equal():
        temp = ent.get()
        if len(temp) == 0:
            box.showwarning('Warning','Пустой ввод.')
        else:

            if temp[0] == '.' or temp[-1] == '.' or temp.count('.')>1 :
                box.showwarning('Warning','Нет правильного ввода.')
            else:
                for i in range(len(temp)):
                    if temp[i] not in num5 or ('-' in temp and temp.index('-')!=0) or temp.count('-')>1:
                        box.showwarning('Warning','Нет правильного ввода.')
                        break
                else:
                    box.showinfo('Результат',FiveToDec(temp))

    # Кнопки
    btn1 = Button(From10to5,text = '1',padx = 40, pady = 20, command =lambda:  button_add('1'))
    btn2 = Button(From10to5,text = '2',padx = 40, pady = 20, command =lambda:  button_add('2'))
    btn3 = Button(From10to5,text = '3',padx = 40, pady = 20, command =lambda:  button_add('3'))
    btn4 = Button(From10to5,text = '4',padx = 40, pady = 20, command =lambda:  button_add('4'))
    btn5 = Button(From10to5,text = '5',padx = 40, pady = 20, command =lambda:  button_add('5'))
    btn6 = Button(From10to5,text = '6',padx = 40, pady = 20, command =lambda:  button_add('6'))
    btn7 = Button(From10to5,text = '7',padx = 40, pady = 20, command =lambda:  button_add('7'))
    btn8 = Button(From10to5,text = '8',padx = 40, pady = 20, command =lambda:  button_add('8'))
    btn9 = Button(From10to5,text = '9',padx = 40, pady = 20, command =lambda:  button_add('9'))
    btn0 = Button(From10to5,text = '0',padx = 40, pady = 20, command =lambda:  button_add('0'))
    btnMinus = Button(From10to5,text = '-',padx = 40, pady = 20, command =lambda:  button_add('-'))
    btnDEL = Button(From10to5,text = 'DEL',padx = 35, pady = 20, command = button_DEL)
    btnAC = Button(From10to5,text = 'AC',padx = 35, pady = 20, command = button_AC)
    btndot = Button(From10to5,text = '.',padx = 40, pady = 20, command =lambda:  button_add('.'))
    btnequal = Button(From10to5,text = '=',padx = 40, pady = 20, command = button_equal)

    btn7.grid(row = 1, column = 0)
    btn8.grid(row = 1, column = 1)
    btn9.grid(row = 1, column = 2)

    btn4.grid(row = 2, column = 0)
    btn5.grid(row = 2, column = 1)
    btn6.grid(row = 2, column = 2)

    btn1.grid(row = 3, column = 0)
    btn2.grid(row = 3, column = 1)
    btn3.grid(row = 3, column = 2)

    btn0.grid(row = 4, column = 0)
    btnDEL.grid(row = 4, column = 1)
    btnAC.grid(row = 4, column = 2)

    btnMinus.grid(row = 5, column = 0)
    btndot.grid(row = 5, column=1)
    btnequal.grid(row = 5, column = 2)

    From10to5.mainloop()

lbl1 = Label(window, text = 'Добро пожаловать в программу перевода числа из 10-й системы счисления в 5-ю и обратно.').grid(row = 0, column = 0)
bnt0 = Button(window, text = 'Перевод числа из 10-й системы счисления в 5-ю.',command = From10to5)
bnt0.grid(row = 1,column = 0)
bnt1 = Button(window, text = 'Перевод числа из 5-й системы счисления в 10-ю.',command = From5to10)
bnt1.grid(row = 2,column = 0)
bnt2 = Button(window, text = 'About me',command = aboutme)
bnt2.grid(row = 3,column = 0)


window.mainloop()
