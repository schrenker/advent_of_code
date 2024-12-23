from collections import defaultdict


test_results = {"part_one": {1: 2660}, "part_two": {1: 1564}}


class Reindeer:
    def __init__(self, speed: int, time: int, rest: int):
        self.speed = speed
        self.time = time
        self.rest = rest
        self.driven = 0

        self.score = 0
        self.driving = True
        self.state = 0

    def run_race(self, seconds: int):
        elapsed = 0
        while elapsed < seconds:
            if elapsed + self.time >= seconds:
                self.driven += self.speed * (seconds - elapsed)
                return self.driven
            else:
                self.driven += self.speed * self.time
                elapsed += self.rest + self.time
        return self.driven

    def step(self):
        if self.driving:
            self.driven += self.speed
            self.state += 1
            if self.state == self.time:
                self.state = 0
                self.driving = False
        else:
            self.state += 1
            if self.state == self.rest:
                self.state = 0
                self.driving = True
        return self.driven


def parse_input(input):
    result = list()
    for i in input.splitlines():
        tmp = i.split(" ")
        result.append(Reindeer(int(tmp[3]), int(tmp[6]), int(tmp[13])))
    return result


def part_one(input: str):
    reindeers = parse_input(input)
    return max([x.run_race(2503) for x in reindeers])


def part_two(input: str):
    reindeers = parse_input(input)
    for _ in range(2503):
        top = defaultdict(list)
        for r in reindeers:
            tmp = r.step()
            top[tmp].append(r)
        for t in top[max(top.keys())]:
            t.score += 1

    return max([x.score for x in reindeers])
