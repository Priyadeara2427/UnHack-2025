from cmath import sqrt


def rotate_90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def rotate_180(matrix):
    return [row[::-1] for row in matrix[::-1]]

def rotate_270(matrix):
    return [list(col) for col in zip(*matrix)][::-1]

def to_zero_orientation(matrix, current_orientation):
    if current_orientation == 0:
        return matrix
    elif current_orientation == 90:
        return rotate_270(matrix)
    elif current_orientation == 180:
        return rotate_180(matrix)
    elif current_orientation == 270:
        return rotate_90(matrix)
    else:
        raise ValueError("Invalid orientation. Use one of 0, 90, 180, 270.")


with open(r"Students\Dataset\M2\T9\INPUT.txt", 'r') as input_file:
    lines_input = input_file.readlines()

with open(r"Students\Dataset\M2\T9\MATRIX.csv", 'r') as matrix_file:
    lines_matrix = matrix_file.readlines()

data = []
for i in range(len(lines_input)):
    if 'DIESIZE' in lines_input[i]:
        die_size = lines_input[i][lines_input[i].find(':') + 1:].removesuffix('\n').split(',')
        die_ht = die_size[0]
        die_wt = die_size[1]
    elif 'DISTANCE' in lines_input[i]:
        distance = lines_input[i][lines_input[i].find(':') + 1:].removesuffix('\n')
    if 'GOOD_DIE' in lines_input[i]:
        good_die = lines_input[i][lines_input[i].find(':') + 1:].removesuffix('\n')
    elif i == 4:
        active_bad_die = lines_input[i][lines_input[i].find(':') + 1:].removesuffix('\n')
    elif i == 5:
        inactive_bad_die = lines_input[i][lines_input[i].find(':') + 1:].removesuffix('\n')
    elif 'ORIENTATION' in lines_input[i]:
        orientation = int(lines_input[i][lines_input[i].find(':') + 1:])
    elif 'ROWDATA' in lines_input[i]:
        values = lines_input[i][lines_input[i].find(':') + 1:].split()
        data.append(values)

if orientation != 0:
    data = to_zero_orientation(data, orientation)

row_ink = len(data)
col_ink = len(data[0])


matrix_data = []
for i in lines_matrix:
    i = i.removesuffix('\n')
    matrix_data.append(i.split(','))

row_matrix = len(matrix_data)
col_matrix = len(matrix_data[0])

diff_col = col_matrix - col_ink
diff_row = row_matrix - row_ink

row_insert = diff_row // 2
col_insert = diff_col // 2

temp = ['000'] * col_ink
for i in range(row_insert):
    data.insert(i, temp)
    data.append(temp)

if diff_row % 2 != 0:
    data.append(temp)


temp_first = ['000'] * col_insert
if diff_col % 2 != 0:
    temp_last = ['000'] * (col_insert+1)
else:
    temp_last = ['000'] * (col_insert)

for i in range(len(data)):
    data[i] = temp_first + data[i] + temp_last

print("Diff: ", diff_col)
print("Row: ",len(data), row_matrix)
print("Col: ",len(data[0]), col_matrix)


# marking invalid dies with '000'
for i in range(row_matrix):
    for j in range(col_matrix):
        if matrix_data[i][j] == '0':
            data[i][j] = "000"
        elif data[i][j] == good_die:
            data[i][j] = '00G'
        elif data[i][j] == inactive_bad_die:
            data[i][j] = '00B'
        # elif data[i][j] == active_bad_die:
        #     data[i][j] = '00F'

# for i in data:
#     print(i)

print("Die Height: ", die_ht)
print("Die Width: ", die_wt)
print("Distance: ", distance)
height_count = int(distance) // int(die_ht) + 1
if int(distance) % height_count ==  0:
    height_count -= 1
weight_count = int(distance)//int(die_wt) + 1
if int(distance) % weight_count == 0:
    weight_count -= 1
diagonal_count = max(height_count, weight_count)
print(height_count, weight_count, diagonal_count)


for i in range(row_matrix):
    for j in range(col_matrix):
        if data[i][j] == active_bad_die:
            #data[i][j] = '00F'
            for rows_i in range(-height_count, height_count+1):
                for col_j in range(-weight_count, weight_count+1):
                    if i == 0 and j == 0:
                        continue
                    else:
                        if (i+rows_i) >= 0 and (i+rows_i) < row_matrix and (j+col_j) >= 0 and (j+col_j) < col_matrix:
                            if data[i+rows_i][j+col_j] != '00B' and data[i+rows_i][j+col_j] != '00C' and data[i+rows_i][j+col_j] != '000' and data[i+rows_i][j+col_j] != active_bad_die:
                                print(data[i+rows_i][j+col_j], end = " ")
                                data[i+rows_i][j+col_j] = '00C'



# for i in data:
#     print(i)
for i in range(row_matrix):
    for j in range(col_matrix):
        if data[i][j] == active_bad_die:
            data[i][j] = '00B'

no_of_good_die = 0
no_of_bad_die = 0
no_of_contaminated_dies = 0


# mapping from matrix to ink file.
for i in data:
    for j in i:
        if j == '00G':
            no_of_good_die += 1
        elif j == '00B':
            no_of_bad_die += 1
        elif j == '00C':
            no_of_contaminated_dies += 1

with open(r"Students\Dataset\M2T9.txt", 'w') as output_file:
    output_file.write('NO OF GOOD DIES:' + str(no_of_good_die) +'\n')
    output_file.write('NO OF BAD DIES:' + str(no_of_bad_die)+'\n')
    output_file.write('NO OF CONTAMINATED DIES:' + str(no_of_contaminated_dies) + '\n')
    for i in range(len(data)):
        if (i != len(data)-1):
            val = ' '.join(data[i])
            output_file.write(str('ROWDATA:' + val) + '\n')
        else:
            val = ' '.join(data[i])
            output_file.write(str('ROWDATA:' + val))
