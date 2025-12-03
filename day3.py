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
    jolatages = []
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


def part2():
    result = 0
    print("DAY 3 PART 2 RESULT: ", result)
    pass


part1()
part2()
