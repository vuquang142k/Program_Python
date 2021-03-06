#được giới hạn bởi cặp ngoặc ()
#Các phần tử của tuple được phân cách nhau bởi dấu ,
#tuple có khả năng chưuas mọi giá trị
#tốc độ truy xuất của tuple nhanh hơn list
#dung lượng chiếm trong bộ nhớ nhỏ hơn list
#bảo vệ dữ liệu của bạn không bị thay đổi
#có thể dùng lạm key của dictionary

tup=(i for i in range(10) if i%2==0)
a=tuple(tup) #(0,2,4,6,8)

tup=(1,5,9)
tup*=2 #(1,5,9,1,5,9)
a=1 in tup #True
a=tup[2] #5
a=len(tup) #3
a=tup.count(1) #1
a=tup.index(9) #2

print(a)