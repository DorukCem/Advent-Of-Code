import re


with open("2024/day3/input.txt", "r") as f:
    data = f.read()
    matches = re.findall("mul\((\d+),(\d+)\)", data)
    products = [int(capture[0]) * int(capture[1]) for capture in matches]
    part1 = sum(products)
    print(part1)

    # part2
    matches_with_do = re.findall("mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data)
    products = []
    state = "DO"
    for capture in matches_with_do:
        match capture:
            case (m1, m2, "", ""):
                if state == "DO":
                    products.append(int(m1) * int(m2))

            case ('', '', '', "don't()"):
                state = "DONT"

            case ('', '', 'do()', ''):
                state = "DO"

    part2 = sum(products)
    print(part2)
