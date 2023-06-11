from collections import deque

def take_input():
   with open("input.txt", "r") as file:
      grid = []
      start = None
      end = None
      for i, line in enumerate(file):
         row = []
         for j,char in enumerate(line.strip()):
            if char == "S":
               start = (i,j)
               row.append(ord('a')-97)
            elif char == "E":
               end = (i,j)
               row.append(ord('z')-97)
            else:
               row.append(ord(char)-97)
         grid.append(row)
      
      return grid, start, end

# Breadth first search  
def part_one():
   
   grid, start, end = take_input()
   visit = set()
   queue = deque()
   queue.append(start)
   prev = {start : None}

   while queue:
      current = queue.popleft()
      if current not in visit:
         if current == end:
            print(path_len(prev, current))
            break
         visit.add(current)
         i,j = current

         adjacent = get_adjacent(i, j, grid, False)
         for adj in adjacent:
            if adj not in visit:
               prev[adj] = current
               queue.append(adj)

# Breadth first search from E to any a
def part_two():
   grid, _, end = take_input()
   visit = set()
   queue = deque()
   queue.append(end)
   prev = {end : None}

   while queue:
      current = queue.popleft()
      i,j = current
      if current not in visit:
         if grid[i][j] == 0:
            print(path_len(prev, current))
            break
         visit.add(current)
         adjacent = get_adjacent(i, j, grid, reverse=True)
         for adj in adjacent:
            if adj not in visit:
               prev[adj] = current
               queue.append(adj)
         
# Reverse determines if we are doing the search form start to end or form end to start
def get_adjacent(i,j, grid, reverse = False) -> list:
   grid_height = len(grid)
   grid_width = len(grid[0])
   arr = []

   if i > 0 and is_reachable(grid, (i,j), (i-1, j), reverse):
      arr.append((i-1, j))

   if j > 0 and is_reachable(grid, (i,j), (i, j-1), reverse):
      arr.append((i, j-1))

   if i < grid_height - 1 and is_reachable(grid, (i,j), (i+1, j), reverse):
      arr.append((i+1, j))

   if j < grid_width -1 and is_reachable(grid, (i,j), (i, j+1), reverse):
      arr.append((i, j+1))

   return arr

def is_reachable(grid, current, other, reverse) -> bool:
   i,j  = current
   cur = grid[i][j]
   x,y = other
   oth = grid[x][y]

   # for part2 
   # Going from start to end we can go up only one tile at a time
   # So going from end to start we can only go down one tile a time
   if reverse:
      return cur - oth  <= 1
   else:
      return oth - cur <= 1


def is_reachable_reverse(grid, current, other):
   i,j  = current
   cur = grid[i][j]
   x,y = other
   oth = grid[x][y]
   

def path_len(dic, key) -> int:
   i = 0
   prev = dic[key]
   while prev != None:
      prev = dic[prev]
      i+=1
   return i


part_one()
part_two()