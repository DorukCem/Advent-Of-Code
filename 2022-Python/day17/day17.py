import copy

with open( "2022-Python/day17/example.txt", "r") as file:
   winds = file.read()

ROCK1 = [[1,0], [2,0], [3,0], [4,0]]

ROCK2 = [       
                [2,2], 
         [1,1], [2,1], [3,1], 
                [2,0]
] 

ROCK3 = [
                 [3,2], 
                 [3,1], 
   [1,0], [2,0], [3,0]
]

ROCK4 = [
   [1,3], 
   [1,2], 
   [1,1], 
   [1,0]
]

ROCK5 = [
   [1,1], [2,1], 
   [1,0], [2,0]
]

def select_rock():
   i = 0
   rocks = [ROCK1, ROCK2, ROCK3, ROCK4, ROCK5]
   while True:
      yield copy.deepcopy(rocks[i]) # deep copy is improtant here because if we do a shallow copy the lists inside the lists will not coppied immutably 
      i+=1
      i%=5

def select_wind():
   i = 0
   while True:
      yield winds[i]
      i+=1
      i %= len(winds)

def set_rock_pos(max_height, rock):
   for pos in rock:
      pos[0] += 2
      pos[1] += max_height + 4

def drop_rock(rock, chamber, wind_selector, column_heights):
   down_collision = False
   while not down_collision:
      left_collision = False
      right_collision = False
      for x,y in rock:
         if x-1 < 1 or (x-1, y) in chamber: 
            left_collision = True
         if x+1 > 7 or (x+1, y) in chamber:
            right_collision = True
      
      wind = next(wind_selector)
      for pos in rock:
         if wind == '<' and not left_collision:
            pos[0] -= 1
         if wind == '>' and not right_collision:
            pos[0] += 1
         
      for x,y in rock:
         if y-1 < 1 or (x, y-1) in chamber:
            down_collision = True

      if not down_collision:
         for pos in rock:  
            pos[1] -= 1
            
   for x,y in rock:
      chamber.add( (x, y) ) 
      column_heights[x-1] = max(column_heights[x-1], y)

def get_surface_shape(column_heights):
   lowest = min(column_heights)
   return tuple( [h - lowest for h in column_heights] )

# Part1

rock_selector = select_rock()
wind_selector = select_wind()
chamber = set()
max_height = 0
rock_id, wind_id = -1, -1
cache = set()
column_heights = [0 for _ in range(7)] # We will keep track of this so that we can find the surface profile at any given moment
# We will that use that surface profile to generate a unique key

cycle_height, cycle_mod = None, None

TARGET = 1000000000000

for i in range(5_000):
   new_rock = next(rock_selector)  
   set_rock_pos(max_height, new_rock)
   drop_rock(new_rock, chamber, wind_selector, column_heights)
   max_height_of_rock = max(new_rock, key=lambda x:x[1])[1]
   max_height = max(max_height, max_height_of_rock)
   shape = get_surface_shape(column_heights)
   #-----
   rock_id = (rock_id + 1) % 5
   wind_id = (wind_id + 1) % len(winds)
   key = (shape, wind_id, rock_id)
   
   if i == 70:
      a = max_height

   if key in cache:
      print(f"found cycle at iter: {i}, key: {key}")
      cycle_mod = i
      cycle_height = max_height
      break
   else:
      cache.add(key)

print(max_height)
d,m = divmod(TARGET, cycle_mod)
print(d, m)
print(d*cycle_height + a)
