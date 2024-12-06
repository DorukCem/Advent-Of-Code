from dataclasses import dataclass
from typing import Set, Tuple


@dataclass
class Guard:
    x: int
    y: int
    direction: str


with open("2024/day6/input.txt", "r") as f:
    data = f.readlines()
    width = len(data[0])
    height = len(data)

    rocks = set()
    guard = None

    for y, row in enumerate(data):
        for x, pos in enumerate(row):
            match pos:
                case ".":
                    continue
                case "#":
                    rocks.add((x, y))
                case "^":
                    guard = Guard(x, y, "up")  #! hardcoded up

    visit: Set[Tuple[int, int]] = set()
    visit.add((guard.x, guard.y))

    while True:
        next_pos = None
        match guard.direction:
            case "up":
                next_pos = (guard.x, guard.y - 1)
            case "down":
                next_pos = (guard.x, guard.y + 1)
            case "left":
                next_pos = (guard.x - 1, guard.y)
            case "right":
                next_pos = (guard.x + 1, guard.y)

        if next_pos in rocks:
            match guard.direction:
                case "up":
                    guard.direction = "right"
                case "down":
                    guard.direction = "left"
                case "left":
                    guard.direction = "up"
                case "right":
                    guard.direction = "down"
        else:
            guard.x, guard.y = next_pos

        if guard.x < 0 or guard.y < 0 or guard.x >= width or guard.y >= height:
            break

        visit.add((guard.x, guard.y))

    part1 = len(visit)
    print(part1)
