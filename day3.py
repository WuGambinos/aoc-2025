#filename = 'day3_input.txt'
filename = 'day3_test.txt'

f = open(filename, 'r')

lines = []

def setup():
    for line in f:
        line = line.strip("\n")
        lines.append(line)

setup()


class Joltage:
    def __init__(self):
        self.i1 = 0
        self.i2 = 0
        self.m1 = 0
        self.m2 = 0


    def print(self):
        print(f"I:{self.i1} M:{self.m1}")
        print(f"I:{self.i2} M:{self.m2}")


def part1():
    result = 0

    for bank in lines:
        new_bank = [int(x) for x in bank.strip()]
    

        j = Joltage()

        for (i, n) in enumerate(new_bank):
            # num greater than current max and not at end of array
            if n > j.m1 and i != len(new_bank) - 1:
                j.i1 = i
                j.m1 = n
    

        for (i, n) in enumerate(new_bank):
            # num greater than current max and greater index than first max
            if n > j.m2 and i > j.i1:
                j.i2 = i
                j.m2 = n


        num = str(j.m1) + str(j.m2)

        print(num)
        j.print()
        print()

        result += int(num)

    print("DAY 3 PART 1 RESULT: ", result)


"""
Think about it as turning off minimums

class NumInfo:
    def __init__(self, index, num):
        self.index = index
        self.num = num

    def print(self):
        print(f"INDEX: {self.index} NUM: {self.num}")

class Disable:
    def __init__(self):
        self.n1 = NumInfo(-1, 99999)
        self.n2 = NumInfo(-1, 99999)
        self.n3 = NumInfo(-1, 99999)

    def print(self):
        self.n1.print()
        self.n2.print()
        self.n3.print()
"""

def part2():

    result = 0
    for (_idx, bank) in enumerate(lines):
        new_bank = [int(x) for x in bank.strip()]
        remove_cnt = 0

        i = 0
        while (i < len(new_bank) - 1):
            print(f"I: {i} LEFT: {new_bank[i]} RIGHT: {new_bank[i+1]}")
            if remove_cnt == 3:
                break

            if (new_bank[i] <= new_bank[i+1]):
                """
                print("POP:", i,  "NUM: ", new_bank[i])
                print(new_bank)
                print()
                """
                new_bank.pop(i);
                remove_cnt += 1
                continue


            i += 1


        result += int("".join(map(str, new_bank)))
        print(new_bank)
        print()


    print("DAY 3 PART 2 RESULT: ", result)


part1()
part2()
