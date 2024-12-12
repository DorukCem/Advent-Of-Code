from collections import defaultdict


def in_bounds(x, y, w, h):
    return 0 <= x < w and 0 <= y < h


def find_region_area(x, y, idx_to_region_map, garden, region_idx):
    plant = garden[y][x]
    count = 0

    def dfs(x, y):
        if garden[y][x] != plant:
            return

        idx_to_region_map[(x, y)] = region_idx
        nonlocal count
        count += 1

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if not in_bounds(x + dx, y + dy, width, heigth):
                continue
            if (x + dx, y + dy) in idx_to_region_map:
                continue
            dfs(x + dx, y + dy)

    dfs(x, y)
    return count


def count_corners(x, y, garden):
    plant = garden[y][x]
    shape = []
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if not in_bounds(x + dx, y + dy, width, heigth):
            continue
        if garden[y + dy][x + dx] == plant:
            shape.append((dx, dy))
    
    diagonals = []
    for ddx, ddy in [(-1,-1), (1,1), (-1, 1), (1,-1)]:
        if not in_bounds(x + ddx, y + ddy, width, heigth):
            continue
        if garden[y + ddy][x + ddx] == plant:
            diagonals.append((y + ddy,x + ddx))

    match len(shape):
        case 0:
            return 4
        case 1:
            return 2
        case 2:
            a, b = shape
            if a[0] == b[0] or a[1] == b[1]:
                return 0
            else:
                inside_x, inside_y = (a[0] + b[0], a[1] + b[1])
                if garden[y + inside_y][x + inside_x] != plant:
                    return 2
                return 1

        case 3:
            return 2
        case 4:
            return 0
                    


with open("2024/day12/example2.txt", "r") as f:
    garden = f.read().split()
    width = len(garden[0])
    heigth = len(garden)

    region_idx_to_areas = defaultdict(int)
    region_idx_to_param = defaultdict(int)
    plant_idx_to_region_idx = {}
    sides = defaultdict(int)

    region_idx = 0  # We assign a number to each region

    for y, row in enumerate(garden):
        for x, plant in enumerate(row):
            if (x, y) not in plant_idx_to_region_idx:
                region_idx += 1
                print(f"{region_idx} : {plant}")
                area = find_region_area(
                    x, y, plant_idx_to_region_idx, garden, region_idx
                )
                region_idx_to_areas[region_idx] += area

            current_region_idx = plant_idx_to_region_idx[(x, y)]

            sides[current_region_idx] += count_corners(x, y, garden)

            num_params_of_plant = 4
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if not in_bounds(x + dx, y + dy, width, heigth):
                    continue
                neighbor_plant = garden[y + dy][x + dx]
                if neighbor_plant == plant:
                    num_params_of_plant -= 1
            region_idx_to_param[current_region_idx] += num_params_of_plant

    total_price = 0

    for region_idx in region_idx_to_areas.keys():
        total_price += region_idx_to_param[region_idx] * region_idx_to_areas[region_idx]
    part1 = total_price
    print(f"part1: {part1}")

    # Part2

    bulk_price = 0
    for region_idx in region_idx_to_areas.keys():
        bulk_price += sides[region_idx] * region_idx_to_areas[region_idx]
    part2 = bulk_price

    print(sides)
    print(f"part2: {part2}")
