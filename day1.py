filename = 'day1_input.txt'
#filename = 'day1_test.txt'
f = open(filename, 'r')


lines = []
def setup():
    for line in f:
        line = line.strip()
        lines.append(line)

MIN = 0
MAX = 99




# DAY 1 PART 1
def part1():
    result = 0
    current = 50
    debug = True
    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        if (direction == "L"):
            current = ((current - distance) % (MAX+1))

        elif (direction == "R"):
            current = (current + distance) % (MAX+1)

        if (current == 0):
            result += 1

    print("DAY 1: ", result)

"""
def part2():
    result = 0
    current = 50
    debug = True
    for line in lines:
        overflow = False
        direction = line[0]
        distance = int(line[1:])

        if (direction == "L"):
            print(direction, distance)
            print("RESULT: ", result)
            print("(BEFORE) CURRENT", current)

            if (current - distance) < 0 and current != 0:
                overflow = True
                print("(1) RESULT INC")
                result += 1

            current = ((current - distance) % (MAX+1))
            print("(AFTER) CURRENT", current)

            if (current == 0 and not overflow):
                print("(2) RESULT INC")
                result += 1

        elif (direction == "R"):
            print(direction, distance)
            print("RESULT: ", result)
            print("(BEFORE) CURRENT", current)

            if (current + distance) > MAX and current != 0:
                overflow = True
                print("(1) RESULT INC")
                result += 1

            current = (current + distance) % (MAX+1)
            print("(AFTER) CURRENT", current)

            if (current == 0 and not overflow):
                print("(2) RESULT INC")
                result += 1


        print()

    print("DAY 2: ", result)
"""

def part2():
    result = 0
    current = 50
    debug = True
    test = False
    for line in lines:
        overflow = False
        direction = line[0]
        distance = int(line[1:])

        if (direction == "L"):
            print(direction, distance)
            print("RESULT: ", result)
            print("(BEFORE) CURRENT", current)

            # During rotation
            overflow = (current - distance) < 0 and current != 0
            if (overflow):
                result += abs((current - distance) // (MAX+1))
                #result += abs((current - distance) // (MAX))

            current = ((current - distance) % (MAX+1))
            print("(AFTER) CURRENT", current)

            # End of rotation
            result += (current == 0 and not overflow)

        elif (direction == "R"):
            print(direction, distance)
            print("RESULT: ", result)
            print("(BEFORE) CURRENT", current)

            # During rotation
            #overflow = (current + distance) > MAX and current != 0
            overflow = (current + distance) > MAX
            if (overflow):
                result += (current + distance) // (MAX+1)
                #result += (current + distance) // (MAX)

            current = (current + distance) % (MAX+1)
            print("(AFTER) CURRENT", current)

            # End of rotation
            result += (current == 0 and not overflow)


        print()
    print("DAY2: ", result)


setup()
#part1()
part2()

