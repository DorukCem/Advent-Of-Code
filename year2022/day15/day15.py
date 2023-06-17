import re
def take_input():
   with open("input.txt", "r") as file:
      positions = []
      for line in file:
         numbers = re.findall(r'-?\b\d+\b', line)
         numbers = [int(i) for i in numbers]
         positions.append(numbers)
      return positions

def merge_intervals(intervals : list[tuple[int, int]]) -> list[tuple[int, int]]:
   sorted_intervals = sorted(intervals)
   merged_intervals = []

   current_merge = []

   for interval in sorted_intervals:
      if current_merge:
         if interval[0] - 1 <= current_merge[1]:
            current_merge[1] = max(interval[1], current_merge[1])
         else:
            merged_intervals.append(current_merge.copy())
            current_merge = list(interval)
      else:
         current_merge = list(interval)

   if current_merge:
      merged_intervals.append(current_merge.copy())

   return merged_intervals

def count_intervals(intervals) -> int:
   count = 0
   for interval in intervals:
      count += 1 + interval[1] - interval[0] 
   return count 

def part_one(Y : int):
   positions = take_input()
   intervals = []
   beacons_on_y_axis = set()
   for pos in positions:
      sensor_x, sensor_y, beacon_x, beacon_y = pos
      radius = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)
      if beacon_y == Y : beacons_on_y_axis.add((beacon_x, beacon_y))

      # Find where sensors intersact the y = 2000000 line
      distance = abs(Y - sensor_y)
      if distance <= radius:
         var =  abs(radius - distance) 
         lower_range, upper_range = sensor_x - var, sensor_x + var
         intervals.append( (lower_range, upper_range) )
     
   merged_intervals = merge_intervals(intervals)
   print(merged_intervals)
   count = count_intervals(merged_intervals)
   count -= len(beacons_on_y_axis)

   print(count)


part_one(2000000)
#print(merge_intervals([(1,3), (2,5), (7,13), (3,4), (0,0), (14, 15)]))