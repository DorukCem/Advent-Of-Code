def checksum(nums):
    return sum([x * i for i, x in enumerate(nums)])


with open("2024/day9/input.txt", "r") as f:
    data = f.read()
    disk = []
    better_disk = []
    file_state = True
    file_idx = 0
    for char in data:
        digit = int(char)

        if file_state:
            disk.extend([file_idx for _ in range(digit)])
            file_idx += 1
            better_disk.append((True, file_idx, digit))
        else:
            disk.extend([None for _ in range(digit)])
            better_disk.append((False, None, digit))

        file_state = not file_state

    compact_disk = []
    reverse_idx = len(disk) - 1
    for left_idx, bit in enumerate(disk):
        if left_idx > reverse_idx:
            break

        if bit != None:
            compact_disk.append(bit)
        else:
            while disk[reverse_idx] == None:
                reverse_idx -= 1
            compact_disk.append(disk[reverse_idx])
            reverse_idx -= 1

    part1 = checksum(compact_disk)
    print(part1)

    non_fragmented_disk = []
    for is_file, file_idx, size in better_disk[::-1]:
        if not is_file:
            continue
        
