def take_input() -> dict:
   with open("example.txt", "r") as file:

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
      
def part_one():
   tile_map = take_input()

part_one()