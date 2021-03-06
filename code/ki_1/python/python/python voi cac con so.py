#Sau đây là một số thủ thuật với thư viện random:

import random
values = [1,2,3,4,5,6]


#Lấy ngẫu nhiên phần tử trong mảng
a=random.choice(values)
#1

a=random.choice(values)
#5


#Lấy ngẫu nhiên vài phần tử:
a=random.sample(values, 2)
#[2,3]


#Trộn mảng theo thứ tự tuỳ ý ngẫu nhiên:
a=random.shuffle(values)
#[1,3,2,6,5,4]


#Sinh ra 1 số nguyên ngẫu nhiên trong phạm vi 0, n
a=random.randint(0, 100)
#34

a=random.randint(0, 100)
#27


#Sinh số ngẫu nhiên trong khoảng 0,1:
a=random.random()
#0.9792036310388545



#Trong python, khi làm việc với các mảng số, thì bạn nên sử dụng thư viện NumPy vì nó được tối ưu cho tính toán với ma trận, cùng với các phép toán được tích hợp rất đầy đủ. 
#Bạn hãy cài đặt numpy tại https://numpy.org. Dưới đây là một số ví dụ cơ bản.


#Giả sử trong Python bạn có list sau:
x = [1,2,3,4,5]
#Nếu ta gọi:
a=x * 2
#[1,2,3,4,5,1,2,3,4,5]


#Trong khi đó:
a=x + 2

#----------------------------------------------------
#TypeError      	Traceback (most recent call last)
#<ipython-input-6-2c7a9192c558> in <module>
#----> 1 x + 2
#TypeError: can only concatenate list (not "int") to list



#Tuy nhiên nếu dùng Numpy
import numpy as np
#Khởi tạo mảng một chiều với kiểu dữ liệu các phần tử là Integer
arr = np.array([1,3,4,5,6], dtype = int)

#Khởi tạo mảng một chiều với kiểu dữ liệu mặc định
arr = np.array([1,3,4,5,6])
print(arr)


x = np.array([1,2,3,4,5])


#Nhân mỗi phần tử với 2:

x * 2
#array([ 2,  4,  6,  8, 10])


#Bình phương:
x * x
#array([ 1,  4,  9, 16, 25])


#Thực hiện tính toán phức tạp:
x * x + 2*x + 1
#array([ 4,  9, 16, 25, 36])


#NumPy cực kì mạnh mẽ với các tính toán số học trên các ma trận nhiều chiều
#Tạo ma trận 0, 2 chiều 1 triệu phần tử: N=M=1000:

np.zeros(shape=(1000,1000), dtype=float)

 #array([[0., 0., 0., ..., 0., 0., 0.],
    #[0., 0., 0., ..., 0., 0., 0.],
   	#[0., 0., 0., ..., 0., 0., 0.],
   	#...,
   	#[0., 0., 0., ..., 0., 0., 0.],
   	#[0., 0., 0., ..., 0., 0., 0.],
   	#[0., 0., 0., ..., 0., 0., 0.]])



np.zeros(shape=(1000,1000), dtype=float) + 10

#array([[10., 10., 10., ..., 10., 10., 10.],
   	#[10., 10., 10., ..., 10., 10., 10.],
   	#[10., 10., 10., ..., 10., 10., 10.],
   	#...,
   	#[10., 10., 10., ..., 10., 10., 10.],
   	#[10., 10., 10., ..., 10., 10., 10.],
   	#[10., 10., 10., ..., 10., 10., 10.]])


#Tạo ma trận 3 hàng 5 cột với các giá trị từ 1-15
array([[ 0,  1,  2,  3,  4],

   	[ 5,  6,  7,  8,  9],

   	[10, 11, 12, 13, 14]])


#Tạo mảng tùy ý:
x = np.array([(1.5,2,3), (4,5,6)])
#array([[1.5, 2. , 3. ],
   	#[4. , 5. , 6. ]])

#Khi đó ta có thể truy cập vào các mảng con như sau:

x[0]
#array([1.5, 2. , 3. ])

#Trong khi đó truy cập vào cột như sau:
x[:,0]
#array([1.5, 4. ])

#Thay đổi 1 phần của mảng:
#Lấy ra 2 cột đầu tiên
x[:,:2]
#array([[1.5, 2. ],
   	#[4. , 5. ]])


#Thay đổi, cộng thêm 2 vào 2 cột đầu:
x[:,:2] += 2
print(x)
  #array([[3.5, 4. , 3. ],
   	#[6. , 7. , 6. ]])


#Cộng theo từng cột:
x = np.array([(1.5,2,3), (4,5,6)])
x[:,:2] + [3,2]
  #array([[4.5, 4. ],
   	#[7. , 7. ]])

#Tạo mảng mới từ mảng đang có với câu điều kiện:
np.where(x >= 5, x, x + 5)


#Tạo mảng mới gồm các phần tử x >= 5, nếu nhỏ hơn 5 ta sẽ cộng thêm 5
array([[6.5, 7. , 8. ],
   	[9. , 5. , 6. ]])


#Với Ma trận:
#Trường hợp bạn muốn sử dụng các phép toán của ma trận hãy dùng np.matrix:
m = np.matrix([[1, 3, 3],
          	[1, 4, 3],
          	[1, 3, 4]])  


#Khi đó ma trận chuyển vị sẽ là:
m.T

  #matrix([[1, 1, 1],
    	#[3, 4, 3],
    	#[3, 3, 4]])

  #matrix([[ 7., -3., -3.],
    	#[-1.,  1.,  0.],
    	#[-1.,  0.,  1.]])



#Ma trận nghịch đảo:
m.T

  #matrix([[ 7., -3., -3.],
    	#[-1.,  1.,  0.],
    	#[-1.,  0.,  1.]])


#Tích 2 ma trận với ma trận nghịch đảo ra ma trận đơn vị:
m * m.I

  #matrix([[1., 0., 0.],
    	#[0., 1., 0.],
    	#[0., 0., 1.]])

#Doi so sang he nhi phan
print(bin(6)[2:])
#Doi so sang he bat phan
print(oct(6)[2:])
#Doi so sang he thap luc
print(hex(6)[2:])
#bin-2,oct-8,dec-10,hex-16