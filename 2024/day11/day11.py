from collections import Counter, defaultdict
import math

stone_cache = {}

# Here I tried to optimize by correctly presuming some stones will be present more than once
# However I missed the fact that having exponantial ammount of stones in memory could not
# be handled even with cache hits. We needed to keep how many times each stone appeared rather
# than caching the calculation for it. 
# In other words the bottle neck was looping over 2^n ammount of elements
# how fast the function was applied to that element did not matter
def get_next_cached(stone: int):
    if stone in stone_cache:
        return stone_cache[stone]

    result = get_next(stone)
    stone_cache[stone] = result
    return result


def get_next(stone: int):
    if stone == 0:
        return 1
    if (int(math.log10(stone)) + 1) % 2 == 0:
        as_str = str(stone)
        return (int(as_str[: len(as_str) // 2]), int(as_str[len(as_str) // 2 :]))
    return 2024 * stone


with open("2024/day11/input.txt", "r") as f:
    stones = [int(x) for x in f.read().split()]
    stones = dict(Counter(stones))
    stones = defaultdict(int, stones)
    part1 = None

    # We use dict to hold the rocks as keys
    # The value for the key indicates the number of time that rock is present 
    # If we have a key K1 which has value V, applying the function to K1
    # produces K2. Since we know that K1 exists V number of times, 
    # K2 will also be produced V number of times
    # So we can say for the next iteration 
    # dict[K2] += V 
    # (if key K2 is not present default dict will assign 0 to it and then add our result)

    for i in range(75):
        new = defaultdict(int)
        if i == 25:
            part1 = sum(stones.values())
        for k, v in stones.items():
            match get_next_cached(k):
                case (a, b):
                    new[a] += v
                    new[b] += v
                case one_rock:
                    new[one_rock] += v
        stones = new

    part2 = sum(stones.values())
    print(part1)
    print(part2)
