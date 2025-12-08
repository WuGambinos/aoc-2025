#filename = 'day7_input.txt'
filename = 'day7_test.txt'

f = open(filename, 'r')

def print_list(lst):
    for row in lst:
        print(row)

lines = []
for line in f:
    line = line.strip()
    char_list = list(line)
    lines.append(char_list)


print_list(lines)

start = None
for (i, line) in enumerate(lines):
    for (j, c) in enumerate(line):
        if c == 'S':
            start = i, j
            break

print(start)


"""
def recurse(grid, r, c, acc):
    if (r < 0 or r >= len(grid)):
        return acc
    if (c < 0 or c >= len(grid[0])):
        return acc

    if grid[r][c] == '.':
        grid[r][c] = '|'
        return recurse(grid, r+1, c, acc)
    elif grid[r][c] == '^':
        acc = recurse(grid, r, c+1, acc+1)
        acc = recurse(grid, r, c-1, acc)
        return acc
    return acc
"""
def recurse(grid, r, c, acc):
    if (r < 0 or r >= len(grid)):
        return acc
    if (c < 0 or c >= len(grid[0])):
        return acc

    if grid[r][c] == '.':
        grid[r][c] = '|'
        return recurse(grid, r+1, c, acc)
    elif grid[r][c] == '^':
        for _ in range(2):
            acc = recurse(grid, r, c-1, acc)
            acc = recurse(grid, r, c+1, acc)
        return acc
    return acc


def part1():
    if start != None:
        print("DAY 7 PART 1", recurse(lines, start[0]+1, start[1], 0))
        print_list(lines)


part1()
