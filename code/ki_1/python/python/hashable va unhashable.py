n=69
print(n)
print(n+1)
print(n._add_(1)) #tuong duong n+1
print(n._sub_(1)) #tuong duong n-1
print(n._mul_(2)) #tuong duong n*2
print(n._radd_(1)) #1+n
print(n._neg_())   #-n

s_1='HowKteam'
s_2='Free enducation'

s_1=s_1+'pyhton'
s_2+='python'
print(id(s_1))
print(id(s_2))

s_1=[1,2]
s_2=[3,4]

s_1=s_1+[0]
s_2+=[0]           #khong thay doi id

s_1._add_([3,4])   #giong +=, khong thay doi id

print(id(s_1))
print(id(s_2))


s_1=[1,2]
s_1.append(3) #[1,2,3]

s_1=(1,2)
s_1+=(3,)    #(1,2,3)
