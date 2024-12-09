from dataclasses import dataclass
from typing import List


def checksum(nums):
    return sum([x * i for i, x in enumerate(nums) if x])


@dataclass
class FileItem:
    is_file: bool
    size: int
    id: int | None

    def __repr__(self):
        if self.is_file:
            return f"File: {self.id} {self.size}"
        else:
            return f"Free: {self.size}"


@dataclass
class FileSystem:
    layout: List[FileItem]

    def append_file(self, file: FileItem):
        if file.size == 0:
            return
        self.layout.append(file)

    def move_file_into_free_space(self, idx_of_free, idx_of_file):
        file = self.layout[idx_of_file]
        self.layout[idx_of_file] = FileItem(False, file.size, None)
        self.layout.insert(idx_of_free, file)
        if self.layout[idx_of_free + 1].size > file.size:
            self.layout[idx_of_free + 1].size -= file.size
        else:
            self.layout.pop(idx_of_free + 1)

        self.defragment()

    def defragment(self):
        new_layout = []
        free = 0
        for item in self.layout:
            if item.is_file:
                if free > 0:
                    new_layout.append(FileItem(False, free, None))
                    free = 0
                new_layout.append(item)
            else:
                free += item.size
        self.layout = new_layout

    def into_memory(self):
        memory = []
        for file_item in self.layout:
            if file_item.is_file:
                memory.extend([file_item.id for _ in range(file_item.size)])
            else:
                memory.extend([None for _ in range(file_item.size)])
        return memory

    def compact_without_fragment(self):
        self.defragment()  # remove all free spaces at the end
        next_id = self.layout[-1].id
        while next_id >= 0:
            right_idx, item = next(
                (i, v) for i, v in enumerate(self.layout) if v.id == next_id
            )
            next_id -= 1

            for left_idx in range(right_idx):
                free_item = self.layout[left_idx]
                if free_item.is_file:
                    continue
                if free_item.size >= item.size:
                    self.move_file_into_free_space(left_idx, right_idx)
                    break


with open("2024/day9/input.txt", "r") as f:
    data = f.read()
    disk = []
    better_disk = FileSystem([])
    file_state = True
    file_idx = 0
    for char in data:
        digit = int(char)

        if file_state:
            disk.extend([file_idx for _ in range(digit)])
            better_disk.append_file(FileItem(True, digit, file_idx))
            file_idx += 1
        else:
            disk.extend([None for _ in range(digit)])
            better_disk.append_file(FileItem(False, digit, None))

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

    better_disk.compact_without_fragment()
    memory = better_disk.into_memory()
    part2 = checksum(memory)
    print(part2)
