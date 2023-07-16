import re

def manhattan_dist(x1, y1, x2, y2):
   return abs(x1 - x2) + abs(y1 - y2)

target_row = 2_000_000
sensors = set()
beacons_on_row = set()
empty_positions_on_row = set()

with open("input.txt", "r") as file:
   lines = file.readlines()

   for line in lines:
      numbers = re.findall(r'-?\b\d+\b', line)
      numbers = [int(i) for i in numbers]
      sx, sy, bx, by = numbers
      radius = manhattan_dist(sx, sy, bx, by)
      sensors.add((sx, sy, radius))

      y_dist_to_row = abs(sy - target_row)
      # half width of points from circle intersection with target_row
      x_dist = radius - y_dist_to_row
      # Take note of all positions on the target_row that are contained by sensors
      for x in range(sx - x_dist, sx + x_dist + 1):
         empty_positions_on_row.add(x)
      # Take note of all the beacons that are on target_row
      if sy == target_row:
         beacons_on_row.add(bx)

# part2
def find_tuning_freq(sensors):
   for sx, sy, radius in sensors:
      # itearte trough all the points that are 1 distance out of reach from the sensor
      # arund the sensors radius
      for dx in range(radius + 1):
         dy = radius + 1 - dx 
         for x, y in [
                (sx + dx, sy + dy),
                (sx + dx, sy - dy),
                (sx - dx, sy + dy),
                (sx - dx, sy - dy),
            ]:
            if not (0 <= x and x <= 4_000_000 and 0 <= y <= 4_000_000):
               continue
            if check_point(x, y, sensors):
               return 4_000_000 * x + y
            
def check_point(x, y, sensors):
   for sx, sy, radius in sensors:
      if manhattan_dist(x, y, sx, sy) <= radius:
         return False
   return True


part1 = len(empty_positions_on_row) - len(beacons_on_row)
print(f"Part 1: {part1}")

print(f"Part 2: {find_tuning_freq(sensors)}")