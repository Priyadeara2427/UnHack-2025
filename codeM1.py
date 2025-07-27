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


with open(r"Students\Dataset\M1\T3\INPUT.txt", 'r') as input_file:
    lines_input = input_file.readlines()

with open(r"Students\Dataset\M1\T3\MATRIX.csv", 'r') as matrix_file:
    lines_matrix = matrix_file.readlines()

row = len(lines_matrix)
col = len(lines_matrix[0].split(','))

data = []
for i in range(len(lines_input)):
    if 'GOOD_DIE' in lines_input[i]:
        good_die = lines_input[i][lines_input[i].find(':') + 1:].removesuffix('\n')
    elif 'BAD_DIE' in lines_input[i]:
        bad_die = lines_input[i][lines_input[i].find(':') + 1:].removesuffix('\n')
    elif 'ORIENTATION' in lines_input[i]:
        orientation = int(lines_input[i][lines_input[i].find(':') + 1:])
    elif 'ROWDATA' in lines_input[i]:
        values = lines_input[i][lines_input[i].find(':') + 1:].split()
        data.append(values)



print("Orientation: ", orientation)
if orientation != 0:
    data = to_zero_orientation(data, orientation)

matrix_data = []
for i in lines_matrix:
    i = i.removesuffix('\n')
    matrix_data.append(i.split(','))

no_of_good_die = 0
no_of_bad_die = 0

for i in range(row):
    for j in range(col):
        if matrix_data[i][j] == '0':
            data[i][j] = "000"

for i in data:
    for j in i:
        if j == good_die:
            no_of_good_die += 1
        elif j == bad_die:
            no_of_bad_die += 1

with open(r"Students\Dataset\M1T3.txt", 'w') as output_file:
    output_file.write('NO OF GOOD DIES:' + str(no_of_good_die) +'\n')
    output_file.write('NO OF BAD DIES:' + str(no_of_bad_die)+'\n')
    for i in data:
        if (i != data[-1]):
            val = ' '.join(i)
            output_file.write(str('ROWDATA:' + val) + '\n')
        else:
            val = ' '.join(i)
            output_file.write(str('ROWDATA:' + val))

