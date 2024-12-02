from typing import List


def is_safe(levels: List[int]) -> bool:
    all_decending = all([(levels[i] < levels[i - 1]) for i in range(1, len(levels))])
    all_acending = all([(levels[i] > levels[i - 1]) for i in range(1, len(levels))])
    all_gradual = all(
        [3 >= abs(levels[i] - levels[i - 1]) >= 1 for i in range(1, len(levels))]
    )

    return (all_acending or all_decending) and all_gradual


def is_safe_with_dampener(levels: List[int]) -> bool:
    for index in range(len(levels)):
        with_one_item_removed = levels[:index] + levels[index + 1 :]
        if is_safe(with_one_item_removed):
            return True

    return False


with open("2024/day2/input.txt", "r") as f:
    data = [[int(num) for num in line.split(" ")] for line in f.readlines()]

    safeness = [1 for levels in data if is_safe(levels)]
    part1 = sum(safeness)
    print(part1)

    safeness_with_damp = [1 for levels in data if is_safe_with_dampener(levels)]
    part2 = sum(safeness_with_damp)
    print(part2)
