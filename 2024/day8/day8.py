from collections import defaultdict
from typing import Tuple


def vec_diff(p1: Tuple[int, int], p2: Tuple[int, int]):
    return (p1[0] - p2[0], p1[1] - p2[1])


def vec_add(p1: Tuple[int, int], p2: Tuple[int, int]):
    return (p1[0] + p2[0], p1[1] + p2[1])


def multiply(p1: Tuple[int, int], scalar: int):
    return (p1[0] * scalar, p1[1] * scalar)


def is_in_bound(point, width, height):
    x, y = point
    return 0 <= x < width and 0 <= y < height


with open("2024/day8/input.txt", "r") as f:
    data = f.read().split("\n")
    width = len(data[0])
    height = len(data)
    positions = defaultdict(list)
    for y, row in enumerate(data):
        for x, char in enumerate(row.strip()):
            if char != ".":
                positions[char].append((x, y))

    antinodes = set()
    for _, v in positions.items():
        if len(v) <= 1:
            continue
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                p1, p2 = v[i], v[j]
                diff = vec_diff(p2, p1)
                p3 = vec_add(p1, multiply(diff, -1))
                p4 = vec_add(p2, diff)
                if is_in_bound(p3, width, height):
                    antinodes.add(p3)
                if is_in_bound(p4, width, height):
                    antinodes.add(p4)

    part1 = len(antinodes)
    print(part1)
