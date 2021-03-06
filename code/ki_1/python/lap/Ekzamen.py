#В файле in.txt записана прямоугольная символьная матрица
#(размер не превышает 9x9, символы в строках разделены пробелами).
#Символ > показывает направление вправо, < - влево, ^ - вверх, v - вниз.
#Требуется найти самую длинную непрерывную "дорожку" из этих символов и
#добавить к матрице строку, содержащую числа - количества символов,
#входящих в эту дорожку, в соответствующих столбцах.
#Затем отсортировать столбцы матрицы по убыванию найденных количеств и
#записать результат в файл out.txt.
def read(el,i,j):
    if el == '>':
        j += 1
    elif el == '<':
        j -=
    elif el == 'v':
        i += 1
    elif el == '^':
        i -= 1
    else:
        return i,j,False
    return i,j,True


o = open('out.txt','w')
f = open('in.txt')
matrix = []
for line in f:
    matrix.append(line.replace('\n','').split())
f.close()
stolbs = [0 for j in range(len(matrix[0]))]
stolbs_max_road = [0 for j in range(len(matrix[0]))]
road_count = 1
max_road_count = 1
for x in matrix:
    print(x)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        road_count = 0
        stolbs = [0 for j in range(len(matrix[0]))]
        if matrix[i][j] == 'v' or matrix[i][j] == '^' or matrix[i][j] == '<' or matrix[i][j] == '>':
            while True:
                try:
                    i,j,flag = read(matrix[i][j],i,j)
                    if flag == False:
                        if road_count > max_road_count:
                            max_road_count = road_count
                            stolbs_max_road = stolbs[:]
                        break
                    road_count += 1
                    stolbs[j] += 1
                except IndexError:
                    if road_count > max_road_count:
                        max_road_count = road_count
                        stolbs_max_road = stolbs[:]
                    break
print(stolbs_max_road)
matrix.append(stolbs_max_road)
for n in range(len(matrix)):
    for j in range(len(matrix[0])-1-n):
        if matrix[len(matrix)-1][j] < matrix[len(matrix)-1][j+1]:
            for i in range(len(matrix)):
                matrix[i][j],matrix[i][j+1] = matrix[i][j+1],matrix[i][j]



for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        o.write(str(matrix[i][j])+' ')
    o.write('\n')

f.close()
o.close()
