#thay doi kich thuoc cua ma tran
A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(A.reshape(3, 3))

#Hạng của ma trận
A = np.array([[-2, 1, 0, 2, 3, -1], [4, 2, -1, 0, -2, 1], [6, 5, -2, 2, -1, 1], [-6, -1, 1, 2, 5, -2]])
print(np.linalg.matrix_rank(A))

#Vết của ma trận (tổng các phần tử trên đường chéo chính)
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# trace
print(np.trace(A))
print(A.trace())

#Chuẩn của ma trận
#chuẩn hàng
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(np.linalg.norm(A, ord=np.inf)) #33.0
#chuẩn cột
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(np.linalg.norm(A, ord=1)) #30.0
#chuẩn Frobenius
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(np.linalg.norm(A))
#tính theo vết ma trận để tính chuẩn Frobenius
import math as mt
import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(mt.sqrt(np.trace(A.T @ A))) #25.495097567963924

#Trị riêng và vector riêng của ma trận
A = np.array([[2, 1, 0], [1, 3, 1], [0, 1, 2]])
w, v = np.linalg.eig(A)
print("Eigenvalues: \n", w)  # trị riêng
print("Eigenvectors: \n", v)  # vector riêng

#Một vài hàm thao tác với hàng, cột và trên toàn ma trận
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.sum(A)) #45

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.sum(A, axis=0)) #[12 15 18]

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.sum(A, axis=1)) #[ 6 15 24]

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.min(A))

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.mean(A))
print(np.mean(A, axis=0))
print(np.mean(A, axis=1))
#5.0
#[4. 5. 6.]
#[2. 5. 8.]

