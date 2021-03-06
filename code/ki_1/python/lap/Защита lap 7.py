#Ву Минь Куанг ИУ-14Б
# Задача:

# Вычислить сумму ряда с заданной точностью
# и вывести таблицу промежуточних значений с
# заданным шагом.

# Ряд: z = 4*(1-1/3+1/5-...)

from math import pi

print("z = 4*(1-1/3+1/5-...)",end="\n\n")

x = float(input("Input x-value: ")) 

eps = float(input("Input precision: ")) 

step = int(input("Input step for the table: ")) 

max_iter = int(input("Input value of max iterations: ")) #
res1 = 0 # t
res2 = float("inf")

z = res1

print()
print(chr(9484),chr(9472) * 63,chr(9488))
print(chr(9474), 4*' ', 'n', 6*' ', chr(9474), 8*' ', 't', 9*' ', chr(9474),
      9*' ', 's', 12*' ', chr(9474))
print(chr(9500), chr(9472) * 63, chr(9508))

i = 1
while abs(res1-res2)>=eps:
	res2 = res1
	res1 = ((-1)**(i+1)*x/(2*i-1))
	z += res1
	if (i)%step == 0:
		print(chr(9474), '{:7.2g}'.format(i),5*' ', chr(9474),2*' ','{:12.5g}'.format(res1*4),4*' ', chr(9474),2*' ', '{:12.5g}'.format(z*4),8*' ', chr(9474))
	i += 1
	if i==max_iter:
		break


print(chr(9492),chr(9472) * 63,chr(9496))
print("Calculated sum: {:10g}".format(4*z))
