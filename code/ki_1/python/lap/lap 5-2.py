Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
s=input()
while True:
    try:
        num=float(s)
        print("OK")
    except:
        print('NOT OK')
    break

x=s.strip()
N=len(x)
a=1
b=x.count('-')
c=x.count('e')
d=x.count('.')
if b>=3 or c>=2 or d>=2:
    a=0
else:
    if x[0] == '-' or x[0] == '+':
        if x[1]=='e'or x[1]=='E':
            a=0
    for i in range(1, N):
        if '0'<=x[i]<='9':
            continue
        elif x[i]=='-' or x[i]=='+'or x[i]=='e'or x[i]=='E':
            if x[i]=='e'or x[i]=='E':
                for j in range(i+2,N):
                    if x[j]=='-' or x[j]=='+':
                        a=0
                        break
        else:
            a=0
            break


if a==0:
    print('NOT OK')
else:
    print('OK')
