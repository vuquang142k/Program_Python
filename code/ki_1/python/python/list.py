# giới hạn bằng cặp ngoặc vuông []
# các phần tử của list cách nhau bằng dấu ,
# List có khả năng chưuas mọi giá trị của python
# và bao gồm chính nó
a=[[1,2],3,[5,'Kteam']]

a=[i for i in range(10)] #[0,1,2,3,4,5,6,7,8,9]
b=[[n,n*1,n*2] for n in range(1,4)] #[[1, 1, 2], [2, 2, 4], [3, 3, 6]]
c=list('Kteam') #['K', 't', 'e', 'a', 'm']

a=[1,2,3,4,[5,6]]
b=a[0] #1
c=a[4][1] #6
d=a[1:3] #[2,3]

a=[1,1,1,4,8,9,7]
b=a.count(1) #3
c=a.index(8) #4

a=[1,2,3]
a.append([4,5]) #[1, 2, 3, [4,5]]
a.extend([4,5]) #[1,2,3,4,5]
a.insert(0,9) #[9,1,2,3]
b=a.pop(1)
print(a) #[1,3]
print(b) #2
#Nếu trống trong() thì tự động chuyển thành vị trí cuối
c=a.remove(1) #xoa so 1 trong list
a.reverse() #dao nguoc cua list
a.sort(reverse=False) #sap xep list tu be den lon
a.sort(reverse=True) #sap xep list tu be den lon
#muon sap xep phai cung 1 kieu du  lieu


