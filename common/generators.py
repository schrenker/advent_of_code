from typing import Generator


def addition_combinations(
    destination: int, start: int, size: int
) -> Generator[list[int], None, None]:
    """Generator, that returns all possible combinations of numbers that add up to destination.

    destination :: number that is being added up to
    start :: minimal value that each combination starts from
    size :: list size of each combination

    For destination 5, start 1 and size 3, generator will return: [1, 1, 3], [1, 2, 2], [1, 3, 1]...
    """

    def __gen_combo(destination: int, start: int, depth: int, cur: list):
        if depth == 1:
            for i in range(start, destination - sum(cur) + 1):
                tmp = list(cur)
                tmp.append(i)
                if sum(tmp) == destination:
                    yield tmp
                else:
                    continue
        else:
            for i in range(start, destination - sum(cur) + 1):
                tmp = list(cur)
                tmp.append(i)
                yield from __gen_combo(destination, start, depth - 1, tmp)

    for i in range(start, destination + 1):
        yield from __gen_combo(destination, start, size - 1, [i])
