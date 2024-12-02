with open("2024/day1/day1.py", "r") as f:
    left_col = []
    right_col = []
    for line in f.readlines():
        l, r = [int(x) for x in line.split("  ")]
        left_col.append(l)
        right_col.append(r)

    left_col.sort()
    right_col.sort()

    part1 = sum(
        [abs(x - y) for x, y in zip(left_col, right_col)],
    )

    part2 = sum([num * right_col.count(num) for num in set(left_col)])

    print(part1)
    print(part2)
