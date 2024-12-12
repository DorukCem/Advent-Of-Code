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


with open("2024/day12/example1.txt", "r") as f:
    garden = f.read().split()
    width = len(garden[0])
    heigth = len(garden)

    region_idx_to_areas = defaultdict(int)
    region_idx_to_param = defaultdict(int)
    plant_idx_to_region_idx = {}

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

            num_params_of_plant = 4
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if not in_bounds(x + dx, y + dy, width, heigth):
                    continue
                neighbor_plant = garden[y + dy][x + dx]
                if neighbor_plant == plant:
                    num_params_of_plant -= 1
            region_idx_to_param[current_region_idx] += num_params_of_plant

    total_price = 0
    bulk_price = 0

    for region_idx in region_idx_to_areas.keys():
        total_price += region_idx_to_param[region_idx] * region_idx_to_areas[region_idx]
    part1 = total_price
    print(f"part1: {part1}")

    # Part2
    sides = defaultdict(lambda: 4)  # set default value as this
    regions = defaultdict(list)
    
    for k, v in plant_idx_to_region_idx.items():
        regions[v].append(k)
    for region_idx, indices in regions.items():
        indices_x = [x for x, _ in indices]
        indices_y = [y for _, y in indices]
        min_x, min_y = min(indices_x), min(indices_y)
        max_x, max_y = max(indices_x), max(indices_y)
        rect_w = max_x - min_x
        rect_h = max_y - min_y
        # Rect area after filling the empty squares
        rect_area = rect_h * rect_w

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                if plant_idx_to_region_idx[(x, y)] == region_idx:
                    continue
                else:
                    # A square has been removed here
                    # Gain sides equal to the number of paramters that are colliding with the region of our shape
                    count = 0
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        if not in_bounds(x + dx, y + dy, width, heigth):
                            continue
                        if plant_idx_to_region_idx[(x + dx, y + dy)] == region_idx:
                            count += 1
                    sides[region_idx] += count

    for region_idx in region_idx_to_areas.keys():
        bulk_price += sides[region_idx] * region_idx_to_areas[region_idx]
    part2 = bulk_price

    print(sides)
    print(f"{part2}: part2")
