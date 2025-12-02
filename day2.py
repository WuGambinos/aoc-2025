filename = 'day2_input.txt'
#filename = 'day2_test.txt'

f = open(filename, 'r')

lines = []
def setup():
    for line in f:
        line = line.strip(",")
        lines.append(line)

setup()


def find_substrings(s):
    res = []

    for i in range(len(s)):
        inner = ""
        for j in range(len(s)):
            res.append(s[i: j-i+1])

    return res

"""Returns False is id is invalid"""
def check_id(n):
    s = str(n)

    half_len = len(s) // 2 
    first_half = s[0:half_len]
    second_half = s[half_len:]

    return first_half == second_half


def check_id_2(n):
    s = str(n)

    return (s+s).find(s, 1) != len(s)


ranges = []
for line in lines:
    line = line.strip()
    ran = line.split(",")
    ranges.extend(ran)


def day1():
    result = 0
    for r in ranges:
        first_id, last_id = r.split("-")
        first_id, last_id = int(first_id), int(last_id)

        for num in range(first_id, last_id+1):
            invalid = check_id(num)
            if invalid: 
                result += num

    print("DAY 1: ", result)

def day2():
    result = 0
    for r in ranges:
        first_id, last_id = r.split("-")
        first_id, last_id = int(first_id), int(last_id)

        for num in range(first_id, last_id+1):
            invalid = check_id_2(num)
            if invalid: 
                result += num

    print("DAY 2: ", result)
    pass

day1()
day2()
