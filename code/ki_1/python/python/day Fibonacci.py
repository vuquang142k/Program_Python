"""
 * Tính số fibonacci thứ n
 *
 * @param n: chỉ số của số fibonacci tính từ 0
 *           vd: F0 = 0, F1 = 1, F2 = 1, F3 = 2
 * @return số fibonacci thứ n
 """
def fibonacci(n):
    f0 = 0;
    f1 = 1;
    fn = 1;
 
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        for i in range(2, n):
            f0 = f1;
            f1 = fn;
            fn = f0 + f1;
        return fn;
 
print("10 số đầu tiên của dãy số fibonacci: ");
sb = "";
for i in range(0, 10):
    sb = sb + str(fibonacci(i)) + ", ";
print(sb)










"""
 * Tính số fibonacci thứ n
 *
 * @param n: chỉ số của số fibonacci tính từ 0
 *           vd: F0 = 0, F1 = 1, F2 = 1, F3 = 2
 * @return số fibonacci thứ n
"""
def fibonacci(n):
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2);
 
print("10 số đầu tiên của dãy số fibonacci: ");
sb = "";
for i in range(0, 10):
    sb = sb + str(fibonacci(i)) + ", ";
print(sb)
