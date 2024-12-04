from typing import List


def search_around(word_to_search: str, lines: List[str], x_idx, y_idx) -> int:
    word_len = len(word_to_search)

    # Check if enough space in these directions
    up = y_idx >= word_len
    left = x_idx >= word_len
    right = (len(lines[0]) - x_idx) >= word_len + 1
    down = (len(lines) - y_idx) >= word_len + 1

    count = 0

    if up:
        count += int(search_direction(word_to_search, "up", lines, x_idx, y_idx))
    if up and left:
        count += int(search_direction(word_to_search, "up-left", lines, x_idx, y_idx))
    if up and right:
        count += int(search_direction(word_to_search, "up-right", lines, x_idx, y_idx))
    if left:
        count += int(search_direction(word_to_search, "left", lines, x_idx, y_idx))
    if right:
        count += int(search_direction(word_to_search, "right", lines, x_idx, y_idx))
    if down and left:
        count += int(search_direction(word_to_search, "down-left", lines, x_idx, y_idx))
    if down:
        count += int(search_direction(word_to_search, "down", lines, x_idx, y_idx))
    if down and right:
        count += int(
            search_direction(word_to_search, "down-right", lines, x_idx, y_idx)
        )

    return count


def search_direction(
    word_to_serch: str, direction: str, lines: List[str], x_idx, y_idx
) -> bool:
    if len(word_to_serch) == 0:
        return True

    next_x, next_y = None, None
    match direction:
        case "up":
            next_x, next_y = x_idx, y_idx - 1
        case "down":
            next_x, next_y = x_idx, y_idx + 1
        case "left":
            next_x, next_y = x_idx - 1, y_idx
        case "right":
            next_x, next_y = x_idx + 1, y_idx
        case "up-left":
            next_x, next_y = x_idx - 1, y_idx - 1
        case "up-right":
            next_x, next_y = x_idx + 1, y_idx - 1
        case "down-left":
            next_x, next_y = x_idx - 1, y_idx + 1
        case "down-right":
            next_x, next_y = x_idx + 1, y_idx + 1
        case unknown:
            raise ValueError(unknown)

    assert next_x != None
    assert next_y != None

    assert next_x >= 0
    assert next_y >= 0
    assert next_y < len(lines)
    assert next_x < len(lines[0])

    next_letter = lines[next_y][next_x]
    head, *tail = word_to_serch

    if next_letter != head:
        return False

    return search_direction(tail, direction, lines, next_x, next_y)


with open("2024/day4/input.txt", "r") as f:
    lines = f.readlines()
    count = 0
    for y_idx, line in enumerate(lines):
        for x_idx, letter in enumerate(line):
            if letter == "X":
                count += search_around("MAS", lines, x_idx, y_idx)
    part1 = count
    print(part1)

    count2 = 0
    for y_idx, line in enumerate(lines):
        for x_idx, letter in enumerate(line):
            if (
                y_idx < 1
                or x_idx < 1
                or y_idx >= len(lines) - 1
                or x_idx >= len(lines[0]) - 1
            ):
                continue

            if letter == "A":
                forward = [
                    search_direction("M", "up-left", lines, x_idx, y_idx),
                    search_direction("M", "down-left", lines, x_idx, y_idx),
                    search_direction("S", "up-right", lines, x_idx, y_idx),
                    search_direction("S", "down-right", lines, x_idx, y_idx),
                ]

                backwards = [
                    search_direction("S", "up-left", lines, x_idx, y_idx),
                    search_direction("S", "down-left", lines, x_idx, y_idx),
                    search_direction("M", "up-right", lines, x_idx, y_idx),
                    search_direction("M", "down-right", lines, x_idx, y_idx),
                ]

                top_m = [
                    search_direction("M", "up-left", lines, x_idx, y_idx),
                    search_direction("M", "up-right", lines, x_idx, y_idx),
                    search_direction("S", "down-left", lines, x_idx, y_idx),
                    search_direction("S", "down-right", lines, x_idx, y_idx),
                ]

                top_s = [
                    search_direction("S", "up-left", lines, x_idx, y_idx),
                    search_direction("S", "up-right", lines, x_idx, y_idx),
                    search_direction("M", "down-left", lines, x_idx, y_idx),
                    search_direction("M", "down-right", lines, x_idx, y_idx),
                ]

                if all(forward) or all(backwards) or all(top_m) or all(top_s):
                    count2 += 1

    part2 = count2
    print(part2)
