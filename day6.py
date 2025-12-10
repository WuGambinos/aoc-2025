#filename = 'day6_input.txt'
from os import wait


filename = 'day6_test.txt'

f = open(filename, 'r')
lines = []

def square_transpose(m):
    for i in range(len(m)):
        for j in range(i + 1, len(m[0])):  # Start from i+1, not 0
            m[i][j], m[j][i] = m[j][i], m[i][j]  # Swap simultaneously

def transpose(og_matrix):
    rows = len(og_matrix)
    cols = len(og_matrix[0])
    result_matrix = [['0' for _ in range(rows)] for _ in range(cols)]
    for (i, row) in enumerate(og_matrix):
        for (j, _item) in enumerate(row):
            result_matrix[j][i] = og_matrix[i][j]

    return result_matrix

def print_list(lst):
    for row in lst:
        print(row)

def setup():
    for line in f:
        #line = line.strip()
        lines.append(line)

setup()


# More Setup
operations = lines.pop()
matrix = []
max_digits = 0

get_len = lines[0].split(" ")
relevant = []
for e in get_len:
    if e and e != '\n':
        relevant.append(e)

num_cols = len(relevant)
print("NUMBER COLS", num_cols)
print()

for line in lines:
    line = line.split(" ")
    for num in line:
        num = num.strip()
        if len(num) > max_digits:
            max_digits = len(num)

    line  = ['0' if x == ''  else x for x in line]
    #line.pop()
    print(line)
    matrix.append(line)

print("MAX DIGITS", max_digits)
print()

new_lst = []

for row in matrix:
    s = ""
    for item in row:
        s += item

    new_lst.append(list(s))

print_list(new_lst)

# numbers = []
# for row in new_lst:
#     curr_num = ""
#     print("ROW", row)
#     for (j, item) in  enumerate(row):
#         print("J: ", j, "len", len(row))
#         curr_num += item
#         if len(curr_num) == max_digits:
#             print("CURR NUM", curr_num)
#             numbers.append(curr_num)
#             curr_num = ""
#         elif len(curr_num) == max_digits - 1 and j == len(row) - 1:
#             curr_num += '0'
#             numbers.append(curr_num)
#             curr_num = ""
#     print("NUM", curr_num)
#     if (curr_num):
#         numbers.append(curr_num)
#
# print(numbers)

#
# new_numbers = []
#
# inner = []
# for n in numbers:
#     inner.append(n)
#     if len(inner) > num_cols:
#         new_numbers.append(inner)
#         inner = []
#
# print(new_numbers)

"""
def transpose(og_matrix):
    rows = len(og_matrix)
    cols = len(og_matrix[0])
    result_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    for (i, row) in enumerate(og_matrix):
        for (j, _item) in enumerate(row):
            result_matrix[j][i] = og_matrix[i][j]

    return result_matrix


transposed = transpose(matrix)

for line in transposed:
    print(line)


operations = operations.split(" ")
operations = [x for x in operations if x]
print(operations)

def part1():
    total = 0
    for (i, row) in enumerate(transposed):
        result = 0

        if operations[i] == '*':
            result = 1
        for num in row:
            if operations[i] == '*':
                result *= num
            elif operations[i] == '+':
                result += num
        total += result

        print("RESULT", result)
    print("DAY 6 PART 1 Result", total)


def part2(m):
    max = 0

    m = transpose(m) 
    for block in m:
        for n in block:
            if len(str(n)) > max:
                max = len(str(n))

     
    temp = [[str(col) for col in row] for row in m]

    for (i,block) in enumerate(m):
        for (j, n) in enumerate(block):
            temp_str = str(n)
            num_digits = len(temp_str)
            if num_digits != max:
                for _ in range(max - num_digits):
                    #temp_str = "0" + temp_str
                    temp_str =  temp_str + "0"

                #transposed[i][j] = int(temp_str)
                temp[i][j] = temp_str

    #new_matrix = [[list(str(col)) for col in row] for row in transposed]
    new_matrix = [[list(col) for col in row] for row in temp]
    print()
    print(new_matrix)


    #Flip Array
    temp_matrix = []
    for (i,block) in enumerate(new_matrix):
        inner = []
        for (j, n) in enumerate(block):
            inner.append(list(reversed(n)))
        temp_matrix.append(inner)

    for block in temp_matrix:
        for n in block:
            print(n)
        print()




    final_matrix = []
    for block in intermed_matrix:
        inner = []
        for row in block:
            inner.append(int("".join(row)))

        final_matrix.append(inner)

    print(final_matrix)

    total = 0
    for (i, row) in enumerate(final_matrix):
        result = 0

        if operations[i] == '*':
            result = 1
        for num in row:
            if operations[i] == '*':
                result *= num
            elif operations[i] == '+':
                result += num
        total += result

        print("RESULT", result)
    print("DAY 6 PART 2 Result", total)



#part1()
part2(matrix)
"""

