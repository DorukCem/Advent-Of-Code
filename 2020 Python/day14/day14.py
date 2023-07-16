def take_input() -> dict:
   with open("input.txt", "r") as file:

      tile_map = {}

      for line in file:
         positions = [pos.split(",") for pos in line.strip().split(" -> ")]
         for i, _ in enumerate(positions):
            if i == 0 : continue
            first_p_x, first_p_y, second_p_x, second_p_y = int(positions[i-1][0]), int(positions[i-1][1]), int(positions[i][0]), int(positions[i][1])
            
            if first_p_x != second_p_x:
               left_p  = min(first_p_x , second_p_x)
               right_p = max(first_p_x , second_p_x)
               for x_pos in range(left_p, right_p + 1):
                  position = (x_pos, first_p_y)
                  tile_map[position] = "Rock"

            elif first_p_y != second_p_y:
               up_p   = min(first_p_y , second_p_y)
               down_p = max(first_p_y , second_p_y)
               for y_pos in range(up_p, down_p + 1):
                  position = (first_p_x, y_pos)
                  tile_map[position] = "Rock"
         
      return tile_map
      
def drop_sand(tile_map, y_limit) -> bool:
   sand_x, sand_y = 500, 0
   moving = True

   while moving:
      if sand_y > y_limit:
         return True

      position = (sand_x, sand_y)
      position_below = (sand_x, sand_y + 1)
      position_below_left = (sand_x - 1, sand_y + 1)
      position_below_right = (sand_x + 1, sand_y + 1)

      if position_below not in tile_map:
         sand_y += 1
      
      elif position_below_left not in tile_map:
         sand_y += 1
         sand_x -= 1
      
      elif position_below_right not in tile_map:
         sand_y += 1
         sand_x += 1
      
      else:
         moving = False
         tile_map[position] = "Sand"
   
   return False


def part_one():
   tile_map = take_input()
   lowest_point = max(list(tile_map.keys()), key = lambda x: x[1])
   y_limit = lowest_point[1] + 2

   flowing = False
   count = 0
   while not flowing:
      flowing = drop_sand(tile_map, y_limit)
      if not flowing : count += 1
   
   print(count)

def drop_sand_in_infinite(tile_map, y_limit) -> bool:
   sand_x, sand_y = 500, 0
   moving = True

   while moving:
      if sand_y == y_limit:
         moving = False
         tile_map[position] = "Sand"

      position = (sand_x, sand_y)
      position_below = (sand_x, sand_y + 1)
      position_below_left = (sand_x - 1, sand_y + 1)
      position_below_right = (sand_x + 1, sand_y + 1)

      if position_below not in tile_map:
         sand_y += 1
      
      elif position_below_left not in tile_map:
         sand_y += 1
         sand_x -= 1
      
      elif position_below_right not in tile_map:
         sand_y += 1
         sand_x += 1
      
      else:
         moving = False
         tile_map[position] = "Sand"
   
   return (500, 0) in tile_map


def part_two():
   tile_map = take_input()
   lowest_point = max(list(tile_map.keys()), key = lambda x: x[1])
   y_limit = lowest_point[1] + 2

   flowing = False
   count = 0
   while not flowing:
      flowing = drop_sand_in_infinite(tile_map, y_limit)
      count += 1
   print(count)

part_one()
part_two()