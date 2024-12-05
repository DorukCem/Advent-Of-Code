from collections import defaultdict
from functools import cmp_to_key
import re
from typing import List


def verify_orderings(numbers, all_numbers_before):
    # After we see a number, all numbers that are supposed to come before it are banned
    banned = set()

    for num in numbers:
        if num in banned:
            return False
        banned = banned.union(set(all_numbers_before[num]))
    return True


def reorder(numbers, all_numbers_before):
    def cmp_items(n1, n2):
        return compare(n1, n2, all_numbers_before)

    return sorted(numbers, key=cmp_to_key(cmp_items))


def compare(n1, n2, all_numbers_before):
    if n2 in all_numbers_before[n1]:
        # n1 > n2
        return 1

    if n1 in all_numbers_before[n2]:
        # n1 < n2
        return -1

    return 0


def find_mid(list):
    return list[len(list) // 2]


with open("2024/day5/input.txt", "r") as f:
    data = f.read()
    page_ordering, page_numbers = data.split("\n\n")

    orderings = re.findall("(\d+)\|(\d+)", page_ordering)
    all_numbers_before = defaultdict(list)
    for x, y in orderings:
        all_numbers_before[y].append(x)

    # O(n) solution btw
    count = 0
    lines = [line.split(",") for line in page_numbers.splitlines()]
    correct = [line for line in lines if verify_orderings(line, all_numbers_before)]
    part1 = sum([int(find_mid(line)) for line in correct])
    print(part1)

    # part2
    incorrect_lines = [
        line for line in lines if not verify_orderings(line, all_numbers_before)
    ]
    reordered = [reorder(x, all_numbers_before) for x in incorrect_lines]
    part2 = sum([int(find_mid(line)) for line in reordered])
    print(part2)
