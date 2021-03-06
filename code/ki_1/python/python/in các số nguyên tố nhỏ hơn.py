from math import sqrt
n=int(input())
def isPrimeNumber(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False

    # check so nguyen to khi n >= 2
    squareRoot = int(sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False
    return True
sb =[]
if (n >= 2):
    sb.append(2)
for i in range(3, n + 1):
    if (isPrimeNumber(i)):
        sb.append(i)
    i = i + 2
print(sb)
