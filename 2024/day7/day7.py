import re


def apply_dfs(target, numbers):
    return dfs(numbers[0], 1, target, numbers)


def dfs(current_sum, index, target, numbers):
    if current_sum == target and index == len(numbers):
        return True
    if current_sum > target:
        return False
    if index >= len(numbers):
        return False

    add = current_sum + numbers[index]
    multiply = current_sum * numbers[index]

    return dfs(add, index + 1, target, numbers) or dfs(
        multiply, index + 1, target, numbers
    )


def apply_dfs_with_concat(target, numbers):
    return dfs_with_concat(numbers[0], 1, target, numbers)


def dfs_with_concat(current_sum, index, target, numbers):
    if current_sum == target and index == len(numbers):
        return True
    if current_sum > target:
        return False
    if index >= len(numbers):
        return False

    add = current_sum + numbers[index]
    multiply = current_sum * numbers[index]
    concat = int(f"{current_sum}{numbers[index]}")

    return (
        dfs_with_concat(add, index + 1, target, numbers)
        or dfs_with_concat(multiply, index + 1, target, numbers)
        or dfs_with_concat(concat, index + 1, target, numbers)
    )


with open("2024/day7/input.txt") as f:
    data = f.readlines()
    part1 = 0
    part2 = 0
    for line in data:
        test_val, *remaining_vals = [int(x) for x in re.findall("\d+", line)]
        if apply_dfs(test_val, remaining_vals):
            part1 += test_val
        if apply_dfs_with_concat(test_val, remaining_vals):
            part2 += test_val

    print(part1)
    print(part2)
