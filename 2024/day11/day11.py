import math

stone_cache = {}


def get_next_cached(stone: int):
    if stone in stone_cache:
        return stone_cache[stone]

    result = get_next(stone)
    stone_cache[stone] = result
    return result


def get_next(stone: int):
    if stone == 0:
        return 1
    if (int(math.log10(stone)) + 1) % 2 == 0:
        as_str = str(stone)
        return (int(as_str[: len(as_str) // 2]), int(as_str[len(as_str) // 2 :]))
    return 2024 * stone

def flatten(l):
    new = []
    for x in l:
        match x:
            case (a, b):
                new.append(a)
                new.append(b)
            case c:
                new.append(x)
    return new

with open("2024/day11/example.txt", "r") as f:
    stones = [int(x) for x in f.read().split()]
    part1 = None
    for i in range(75):
        if i == 25:
            part1 = len(stones)
        new = [get_next_cached(x) for x in stones]
        stones = flatten(new)
        print(i)
    part2 = len(stones)
    print(part1)
    print(part2)