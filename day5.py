#filename = 'day5_input.txt'
filename = 'day5_test.txt'

f = open(filename, 'r')

class Range:
    def __init__(self, start, end):
        self.start = start 
        self.end = end

    def __lt__(self, other):
        return self.start < other.start

    def print(self):
        #print(f"START: {self.start} END: {self.end}")
        print(f"[{self.start}, {self.end}]")


    def overlaps(self, r2):
        if self.end >= r2.start and self.end <= r2.end:
            return True

        if self.start <= r2.end and self.start >= r2.start:
            return True
        return False

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __hash__(self):
        return hash((self.start, self.end))

class RangePair():
    def __init__(self, r1, r2):
        self.r1  = r1
        self.r2 = r2

    def print(self):
        print("RANGE PAIR")
        self.r1.print()
        self.r2.print()


id_ranges = []
available_ids = []

def setup():
    parse_ingredients = False
    for line in f:
        line = line.strip("\n")
        print(len(line))
        if len(line) == 0:
            parse_ingredients =  True
            continue

        if parse_ingredients:
            available_ids.append(int(line))
            
        else:
            line = line.strip("\n")
            ran = line.split("-")
            start, end = int(ran[0]), int(ran[1])
            r = Range(start, end)
            id_ranges.append(r)


setup()

def part1():
    fresh  =0 
    seen = []
    for id in available_ids:

        for r in id_ranges:
            if (id >= r.start and id <= r.end and id not in seen):
                seen.append(id)
                fresh += 1


    print("PART 1: ", fresh)


def combine_range(r1, r2):
    if r1.start >= r2.start and r1.start <= r2.end:
        new_range= Range(r2.start, r1.end)
        combine_range(new_range, r1)
    else:
        return r1


def recurse(ranges, r1, check):

    if check:
        for r2 in ranges:
            if r1 == r2:
                continue

            if r1.start >= r2.start and r1.start <= r2.end:
                new_range= Range(r1.start, r1.end)
                recurse(ranges, new_range, True)
            else:
                recurse(ranges, r1, False)
    else: 
        return
            


    
def part2():
    for (i, r1) in enumerate(id_ranges):
            recurse(id_ranges, r1, True)


    """
    for (i, r1) in enumerate(id_ranges):
        for (j, r2) in enumerate(id_ranges):
            if (i != j):
                #if r1.overlaps(r2):

                if r1.start >= r2.start and r1.start <= r2.end:
                    r = combine_range(r1, r2)
                    print("COMBINE")
                    r1.print()
                    r2.print()
                    print()
                    if r != None:
                        r.print()
    """

    """
    track = set()
    for r in id_ranges:
        for n in range(r.start, r.end+1):
            track.add(n)

    print("PART 2: ", len(track))
    """

    """
    seen = []
    res = 0
    for (i, r1) in enumerate(id_ranges):
        did_overlap = False
        for (j, r2) in enumerate(id_ranges):
            if (i != j):

                if sorted([r1, r2]) not in seen:
                    temp = sorted([r1, r2])
                    seen.append(temp)

                    if r1.overlaps(r2):
                        d1 = (r1.end - r1.start) + 1
                        d2 = (r2.end - r2.start) + 1
                        print("OVERLAP")
                        r1.print()
                        r2.print()
                        diff = (d1 + d2) - (r1.end - r2.start + 1)
                        res += diff
                        print(f"({d1}+ {d2}) - ({r1.end} - {r2.start} + 1)")
                        print("DIFF", diff)
                        print("RES", res)
                        did_overlap = True
                    print()

        if not did_overlap:
            diff = (r1.end - r1.start) + 1
            print("NO OVERLAP")
            r1.print()
            print("DIFF", diff)
            res += diff
            print()
    
    print("res", res)
    """

"""
for r in id_ranges:
    r.print()
print(available_ids)
"""

part1()
part2()
