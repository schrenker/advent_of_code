from collections import Counter, defaultdict


# Part two is visual display in the terminal of the part one, thus meaningless
test_results = {"part_one": {1: 6}, "part_two": {1: 0}}


class display:
    def __init__(self, maxx, maxy):
        self.d = defaultdict(bool)
        self.maxx = maxx
        self.maxy = maxy

    def rect(self, y, x):
        for i in range(x):
            for j in range(y):
                self.d[(i, j)] = True

    def rotate(self, method, no, amount):
        if method == "column":
            self.rotate_column(no, amount)
        else:
            self.rotate_row(no, amount)

    def rotate_column(self, no, amount):
        tmp = set()
        for i in range(self.maxx):
            if self.d[(i, no)]:
                tmp.add((i, no))
        for t in tmp:
            self.d[t] = False
        for t in tmp:
            if t[0] + amount >= self.maxx:
                self.d[((t[0] + amount) - self.maxx, t[1])] = True
            else:
                self.d[(t[0] + amount, t[1])] = True

    def rotate_row(self, no, amount):
        tmp = set()
        for i in range(self.maxy):
            if self.d[(no, i)]:
                tmp.add((no, i))
        for t in tmp:
            self.d[t] = False
        for t in tmp:
            if t[1] + amount >= self.maxy:
                self.d[(t[0], (t[1] + amount) - self.maxy)] = True
            else:
                self.d[(t[0], t[1] + amount)] = True

    def display(self):
        result = ""
        for i in range(self.maxx):
            for j in range(self.maxy):
                if self.d[(i, j)]:
                    result += "#"
                else:
                    result += " "
            result += "\n"
        return result


def part_one(input: str, test_run=False):
    d = display(3 if test_run else 6, 7 if test_run else 50)
    for i in input.splitlines():
        spl = i.split()
        match spl[0]:
            case "rect":
                tmp = [int(x) for x in spl[1].split("x")]
                d.rect(tmp[0], tmp[1])
            case "rotate":
                d.rotate(spl[1], int(spl[2].split("=")[1]), int(spl[4]))
    return Counter(d.d.values())[True]


def part_two(input: str, test_run=False):
    d = display(3 if test_run else 6, 7 if test_run else 50)
    for i in input.splitlines():
        spl = i.split()
        match spl[0]:
            case "rect":
                tmp = [int(x) for x in spl[1].split("x")]
                d.rect(tmp[0], tmp[1])
            case "rotate":
                d.rotate(spl[1], int(spl[2].split("=")[1]), int(spl[4]))
    return 0 if test_run else d.display()
