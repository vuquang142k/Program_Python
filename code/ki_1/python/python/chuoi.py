stra='HowKteam'
strb=stra[None:None:2] 	#[start:end:buoc nhay]
print(strb)
#Hwta

strA=int('69')+5
strB=str(69)+'5'
strC=int(6.9)
print(strA) 	# 74
print(strB) 	#695
print(strC) 	#6

a= 'My name is %s'%('Quang')
print(a)
#My name is Quang

a= 'I am %s%s years old'%(2,0)
print(a)
#I am 20 years old

a= '%s'%([1,2,3])
print(a)
#[1, 2, 3]

a= '%d'%(3.9)
print(a)
#3

a= '%3f'%(3.999999)
print(a)
#4

a= '%2f'%(3.563545)
print(a)
#3.56

print(f'a\tb')
#a   b

k='Kteam'
result=f'{k}-Free enducation'
print(result)
#Kteam-Free enducation

name='Quang'
address='Ha Noi'
phone='0123456789'
result=f'Student: {name}\nAddress: {address}\nPhone: {phone}'
print(result)
#Student: Quang
#Address: Ha Noi
#Phone: 0123456789

r='1: {1},2: {0}'.format(111,222)
print(r)
#1: 111, 2: 222

a='You {:^10} me'.format('aaaa') #căn giữa
print(a)
#You    aaaa    me
a='{:<10}'.format('aaaa') #căn lề trái
print(a)
#aaaa      
a='{:>10}'.format('aaaa') #căn lề phải
print(a)
#      aaaa
a='{:*>10}'.format('aaaa') #căn lề trái, thay thế khoảng trắng bằng kí tự *
print(a)
#******aaaa
a='{:*<10}'.format('aaaa') #căn lề phải, thay thế khoảng trắng bằng kí tự *
print(a)
#aaaa******

strA='HowKteam'
strA=strA[None:1]+'0'+strA[2:None]
print(strA)
#H0wKteam

a='how Kteam-Free enducation'
b=a.capitalize()
c=a.upper()
d=a.lower()
e=a.swapcase()
f=a.title()
print(a) #how Kteam-Free enducation
print(b) #How kteam-free enducation-chi viet in hoa chu cai dau
print(c) #HOW KTEAM-FREE ENDUCATION
print(d) #how kteam-free enducation
print(e) #HOW kTEAM-fREE ENDUCATION
print(f) #How Kteam-Free Enducation-sau moi khoang trang la viet hoa

a='Kteam'
b=a.center(10,'*') # b=a.center(width,[fillchar])
c=a.rjust(10,'*') #*****Kteam
d=a.ljust(10,'*') #Kteam*****
print(b)
#**Kteam***

a='and'
b=a.join(['1','2','3']) #1and2and3
c=a.replace('n','U') #aUd

a='how kteam free enducation'
b=a.split(' ') #['how', 'kteam', 'free', 'enducation']
# b=a.split(' ',2)  2- la so lan cat
c=a.partition('k') #('how ', 'k', 'team free enducation')-cat chuoi truoc ,sau va chuoi can lay
d=a.count('e',None,None) #4 -co 4 chu e trong chuoi
e=a.startswith('how',None,None) #True- chuoi co xuat phat bang chu how khong
#tuong tu voi endswith
f=a.find('t') #5-neu tim khong thay ra kqua -1

for _ in strA:
	print(_,end='')
# doi tu list sang string

#de in ra ki tu trong bang ASI
print(ord('a'))
#97

print (any(c.isalnum()  for c in s))