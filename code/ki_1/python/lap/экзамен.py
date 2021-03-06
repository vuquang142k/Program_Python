file_in1=open('in1.txt','r')
file_in2=open('in2.txt','r')
file_out=open('out.txt','w')
file_out1=open('out1.txt','w')
    

a=file_in1.readline().strip()
b=file_in2.readline().strip()

while True:
    if int(a)>int(b):
        file_out.write(str(b)+'\n')
        b=file_in1.readline().strip()
    else:
        file_out.write(str(a)+'\n')
        a=file_in2.readline().strip()
    if a=='' or b=='':
        break
while a=='' and b!='':
    file_out.write(str(b)+'\n')
    b=file_in2.readline().strip()
while a!='' and b=='':
    file_out.write(str(a)+'\n')
    a=file_in1.readline().strip()
file_in1.close()
file_in2.close()
file_out.close()

inn = open('out.txt', 'r')
a = inn.readline().strip()
maxlen = -1
while a != '':
    s = ''
    x=int(a)
    while x > 1000:
        s += 'M'
        x -= 1000
    while x >= 900:
        s += 'CM'
        x -= 900
    while x >= 500:
        s += 'D'
        x -= 500
    while x >= 400:
        s += 'CD'
        x -= 400
    while x >= 100:
        s += 'C'
        x -= 100
    while x >= 90:
        s += 'XC'
        x -= 90
    while x >= 50:
        s += 'L'
        x -= 50
    while x >= 40:
        s += 'XL'
        x -= 40
    while x >= 10:
        s += 'X'
        x -= 10
    while x >= 9:
        s += 'IX'
        x -= 9
    while x >= 5:
        s += 'V'
        x -= 5
    while x >= 4:
        s += 'IV'
        x -= 4
    while x >= 1:
        s += 'I'
        x -= 1
    if len(s) < maxlen:
        k = len(s)
    maxlen = max(maxlen, len(s))
    a = inn.readline().strip()
inn.close()
inn = open('out.txt', 'r')
a = inn.readline().strip()
while a != '':
    s = ''
    x=int(a)
    while x > 1000:
        s += 'M'
        x -= 1000
    while x >= 900:
        s += 'CM'
        x -= 900
    while x >= 500:
        s += 'D'
        x -= 500
    while x >= 400:
        s += 'CD'
        x -= 400
    while x >= 100:
        s += 'C'
        x -= 100
    while x >= 90:
        s += 'XC'
        x -= 90
    while x >= 50:
        s += 'L'
        x -= 50
    while x >= 40:
        s += 'XL'
        x -= 40
    while x >= 10:
        s += 'X'
        x -= 10
    while x >= 9:
        s += 'IX'
        x -= 9
    while x >= 5:
        s += 'V'
        x -= 5
    while x >= 4:
        s += 'IV'
        x -= 4
    while x >= 1:
        s += 'I'
        x -= 1
    st=''
    if (maxlen - k) % 2 == 0:
        st= ' ' * ((maxlen-k)//2) + s + ' ' * ((maxlen-k)//2)
    else:
        st=' ' * ((maxlen-k)//2+1) + s + ' ' * ((maxlen-k)//2)
    file_out1.write(st + '\n')
    a = inn.readline().strip()
inn.close()
file_out1.close()
    
