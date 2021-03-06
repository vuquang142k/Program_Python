numbers = []
file_in = open('in.txt', 'r')
while True:
	a = file_in.readline()
	if a == '':
		break
	a = a.split(' ')
	for i in a:
	    isAdd = True
	    for j in i:
	        if j not in ['1','2','3','4','5','6','7','0','.']:
	            isAdd = False
	            break
	    if isAdd:
	        numbers.append(i)
file_in.close()
file_out = open('out.txt','w')
for number in numbers:
	file_out.write(number + '\n')
file_out.write('\n')
for number in numbers:
	bina = ''
	for a in number:
		if a == '.':
			bina += '.'
		elif a == '0':
			bina += '000'
		elif a == '1':
			bina += '001'
		elif a == '2':
			bina += '010'
		elif a == '3':
			bina += '011'
		elif a == '4':
			bina += '100'
		elif a == '5':
			bina += '101'
		elif a == '6':
			bina += '110'
		elif a == '7':
			bina += '110'
	if '.' in bina:
		parts = bina.split('.')
	else:
		parts = bina
	if len(parts) == 2:
		a = parts[0]
		hexa01 = ''
		a = a.lstrip('0')
		while len(a)%4:
			a = '0' + a
		for i in range(0,len(a),4):
			if a[i:i+4] == '0000':
				hexa01 += '0'
			if a[i:i+4] == '0001':
				hexa01 += '1'
			if a[i:i+4] == '0010':
				hexa01 += '2'
			if a[i:i+4] == '0011':
				hexa01 += '3'
			if a[i:i+4] == '0100':
				hexa01 += '4'
			if a[i:i+4] == '0101':
				hexa01 += '5'
			if a[i:i+4] == '0110':
				hexa01 += '6'
			if a[i:i+4] == '0111':
				hexa01 += '7'
			if a[i:i+4] == '1000':
				hexa01 += '8'
			if a[i:i+4] == '1001':
				hexa01 += '9'
			if a[i:i+4] == '1010':
				hexa01 += '10'
			if a[i:i+4] == '1011':
				hexa01 += 'A'
			if a[i:i+4] == '1100':
				hexa01 += 'B'
			if a[i:i+4] == '1101':
				hexa01 += 'C'
			if a[i:i+4] == '1110':
				hexa01 += 'D'
			if a[i:i+4] == '1111':
				hexa01 += 'E'
		b = parts[1]
		hexa02 = ''
		while len(b)%4:
			b += '0'
		for i in range(0,len(b),4):
			if b[i:i+4] == '0000':
				hexa02 += '0'
			if b[i:i+4] == '0001':
				hexa02 += '1'
			if b[i:i+4] == '0010':
				hexa02 += '2'
			if b[i:i+4] == '0011':
				hexa02 += '3'
			if b[i:i+4] == '0100':
				hexa02 += '4'
			if b[i:i+4] == '0101':
				hexa02 += '5'
			if b[i:i+4] == '0110':
				hexa02 += '6'
			if b[i:i+4] == '0111':
				hexa02 += '7'
			if b[i:i+4] == '1000':
				hexa02 += '8'
			if b[i:i+4] == '1001':
				hexa02 += '9'
			if b[i:i+4] == '1010':
				hexa02 += '10'
			if b[i:i+4] == '1011':
				hexa02 += 'A'
			if b[i:i+4] == '1100':
				hexa02 += 'B'
			if b[i:i+4] == '1101':
				hexa02 += 'C'
			if b[i:i+4] == '1110':
				hexa02 += 'D'
			if b[i:i+4] == '1111':
				hexa02 += 'E'
		file_out.write(hexa01 + '.' + hexa02 + '\n')
	else:
		a = parts
		hexa01 = ''
		a = a.lstrip('0')
		while len(a)%4:
			a = '0' + a
		for i in range(0,len(a),4):
			if a[i:i+4] == '0000':
				hexa01 += '0'
			if a[i:i+4] == '0001':
				hexa01 += '1'
			if a[i:i+4] == '0010':
				hexa01 += '2'
			if a[i:i+4] == '0011':
				hexa01 += '3'
			if a[i:i+4] == '0100':
				hexa01 += '4'
			if a[i:i+4] == '0101':
				hexa01 += '5'
			if a[i:i+4] == '0110':
				hexa01 += '6'
			if a[i:i+4] == '0111':
				hexa01 += '7'
			if a[i:i+4] == '1000':
				hexa01 += '8'
			if a[i:i+4] == '1001':
				hexa01 += '9'
			if a[i:i+4] == '1010':
				hexa01 += '10'
			if a[i:i+4] == '1011':
				hexa01 += 'A'
			if a[i:i+4] == '1100':
				hexa01 += 'B'
			if a[i:i+4] == '1101':
				hexa01 += 'C'
			if a[i:i+4] == '1110':
				hexa01 += 'D'
			if a[i:i+4] == '1111':
				hexa01 += 'E'
		file_out.write(hexa01 + '\n')
file_out.close()