filename = 'day4_input.txt'
#filename = 'day4_test.txt'

f = open(filename, 'r')

lines = []

def setup():
    for line in f:
        line = line.strip("\n")
        lines.append(line)

    for (i, line) in enumerate(lines):
        lines[i] = list(line)



setup()
COL_LEN = len(lines[0])
ROW_LEN = len(lines)

def check(lines, r, c):
    if r >= ROW_LEN or r < 0:
        return 0

    if c >= COL_LEN or c < 0:
        return 0

    return int(lines[r][c] == '@')

def part1():
    count = 0

    for r in range(ROW_LEN):

        res = 0
        for c in range(COL_LEN):
            if (lines[r][c] == '@'):

                d1 = check(lines, r-1, c)
                d2 = check(lines, r+1, c)
                d3 = check(lines, r, c-1)
                d4 = check(lines, r, c+1)
                d5 = check(lines, r+1, c+1)
                d6 = check(lines, r+1, c-1)
                d7 = check(lines, r-1, c+1)
                d8 = check(lines, r-1, c-1)

                res = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8

                if res < 4:
                    count += 1

    print("DAY 4 PART 1:", count)


def remove_rolls():
    count = 0 
    removed = []
    for r in range(ROW_LEN):
        res = 0
        for c in range(COL_LEN):
            if (lines[r][c] == '@'):

                d1 = check(lines, r-1, c)
                d2 = check(lines, r+1, c)
                d3 = check(lines, r, c-1)
                d4 = check(lines, r, c+1)
                d5 = check(lines, r+1, c+1)
                d6 = check(lines, r+1, c-1)
                d7 = check(lines, r-1, c+1)
                d8 = check(lines, r-1, c-1)

                res = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8

                if res < 4:
                    removed.append((r, c))
                    count += 1

    for (r, c) in removed:
        lines[r][c] = '.'

    return count

def part2():
    rolls = -1
    total = 0 

    while rolls != 0:
        rolls = remove_rolls()
        total += rolls

    print("DAY 4 PART 2:", total)

def main():
    part1()
    part2()

main()
