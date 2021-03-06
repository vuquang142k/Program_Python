#Set la 1 container,tuy nhien ko su dung nhieu bang list hay tuple
#Duoc gioi han boi {}, tat ca nhung gi nam trong do la nhung phan tu cua Set
#Cac phan tu cua Set duoc phan cach nhau boi dau ,
#Set khong chua nhieu hon 1 phan tu trung lap
#chi chua hashable object

set_1={69,96}
print(set_1)    #{96,69}

set_2={'HowKteam'}
print(set_2)  #{'HowKteam'}
#unhashable type:list
#khong chay voi list
#khong chay voi set trong set

set_2={1,2,{'HowKteam'}}    #Typeerror

set_2={1,1,1}
print(set_2)     #{1}

set_2=set((1,2,3))  #{1,2,3}
set_2=set('HowKteam') #{'t','m','H','o','e','a','K','w'}

print({1,2,3,4}-{2,3})  #{1,4}
print({1,2,3,4} & {{4,5}) #{4}
print({1,2,3} | {4,5})     #{1,2,3,4,5}

print({1,2,3}^{3,4})      #{1,2,4}
set1={1,2,3,4}
set1.remove(1)  #{2,3,4}
set1.discard(5)  #{1,2,3,4},giong remove nhung phan tu ko co trong set ko bao loi
set1.add(5)     #{1,2,3,4,5}
