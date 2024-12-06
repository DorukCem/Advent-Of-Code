from dataclasses import dataclass
import time
from typing import Set, Tuple


@dataclass
class Guard:
    x: int
    y: int
    direction: str

def find_route(start_pos, rocks, width, height):
    guard = Guard(*start_pos, "up")

    visit: Set[Tuple[int, int]] = set()
    visit.add((guard.x, guard.y))
    
    loop: Set[Tuple[int, int, str]] = set()
    loop.add((guard.x, guard.y, "up"))

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

        if (guard.x, guard.y, guard.direction) in loop:
            return None, True

        if guard.x < 0 or guard.y < 0 or guard.x >= width or guard.y >= height:
            return len(visit), False

        visit.add((guard.x, guard.y))
        loop.add((guard.x, guard.y, guard.direction))


with open("2024/day6/input.txt", "r") as f:
    data = f.readlines()
    width = len(data[0])
    height = len(data)

    rocks = set()
    start_pos = None

    for y, row in enumerate(data):
        for x, pos in enumerate(row):
            match pos:
                case ".":
                    continue
                case "#":
                    rocks.add((x, y))
                case "^":
                    start_pos = (x,y)

    count, _ = find_route(start_pos, rocks, width, height)

    part1 = count
    print(part1)

    loop_count = 0

    start_time = time.time()
    for y in range(height):
        for x in range(width):
            if (x,y) not in rocks:
                add_rock = {(x,y)}.union(rocks)
                _, is_loop = find_route(start_pos, add_rock, width, height)
                if is_loop:
                    loop_count += 1
    end_time = time.time()
    part2 = loop_count
    print(part2)
    print(f"Time elapsed for part2 is {end_time - start_time}")