#filename = 'day2_input.txt'
filename = 'day2_test.txt'
f = open(filename, 'r')

lines = []
def setup():
    for line in f:
        line = line.strip()
        lines.append(line)

setup()
