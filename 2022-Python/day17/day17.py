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
      yield rocks[i][::]
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

def drop_rock(rock, chamber, wind_selector):
   down_collision = False
   while not down_collision:
      left_collision = False
      right_collision = False
      for x,y in rock:
         if y-1 < 1 or (x, y-1) in chamber:
            down_collision = True
         if x-1 < 1 or (x-1, y-1) in chamber: # ! ?? 
            left_collision = True
         if x+1 > 7 or (x+1, y-1) in chamber:
            right_collision = True
         
      wind = next(wind_selector)
      for pos in rock:
         if not down_collision:
            pos[1] -= 1
         if wind == '<' and not left_collision:
            pos[0] -= 1
         if wind == '>' and not right_collision:
            pos[0] += 1
            
      print(rock)

   for pos in rock:
      chamber.add(tuple(pos)) 


rock_selector = select_rock()
wind_selector = select_wind()
chamber = set()
max_height = 0

for i in range(2):
   print("----- new_rock -------")
   new_rock = next(rock_selector)   
   set_rock_pos(max_height, new_rock)
   print(new_rock)
   drop_rock(new_rock, chamber, wind_selector)
   max_height_of_rock = max(new_rock, key=lambda x:x[1])[1]
   max_height = max(max_height, max_height_of_rock)

print(max_height)