from typing import List, Tuple


def get_score(trail_map: List[List[int]], trail_head: Tuple[int, int], width, height):
    score = 0
    distinc_score = 0
    reached = set()
    def dfs(trail_map: List[List[int]], idx: Tuple[int, int], expected_val : int):
        nonlocal score
        nonlocal distinc_score
        x, y = idx

        if not (0 <= x < width and 0 <= y < height):
            return


        pos = trail_map[y][x]
        if pos != expected_val:
            return

        if pos == 9:
            distinc_score += 1
            if idx in reached:
                return
            reached.add(idx)
            score += 1
            return

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(trail_map, (x + dx, y + dy), expected_val + 1)

    dfs(trail_map, trail_head, 0)
    return score, distinc_score


with open("2024/day10/input.txt", "r") as f:
    trail_map = [[int(x) for x in line.strip()] for line in f.read().split("\n")]
    height = len(trail_map)
    width = len(trail_map[0])

    trailhead_indices = []
    for y, row in enumerate(trail_map):
        for x, val in enumerate(row):
            if val == 0:
                trailhead_indices.append((x, y))

    scores = 0
    distinct_scores = 0
    for head in trailhead_indices:
        score, distinct_score = get_score(trail_map, head, width, height)
        distinct_scores += distinct_score
        scores += score

    part1 = scores
    part2 = distinct_scores
    print(part1)
    print(part2)