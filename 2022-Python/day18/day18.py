with open( "2022-Python/day18/ex.txt", "r") as file:
   inp = file.read()

positions = set(map(lambda x : tuple(map(lambda y: int(y), x.split(","))), inp.split("\n")))

p1_count = 0
p2_count = 0
for x,y,z in positions: 
   nearby = [
      (x+1, y, z), (x-1, y, z),
      (x, y+1, z), (x, y-1, z),
      (x, y, z+1), (x, y, z-1)       
   ]
   
   connected = [p for p in nearby if p not in positions]
   p1_count += len(connected)

   if len(connected) != 6:
      p2_count += len(connected) 


print(f"part1: {p1_count}")
print(f"part2: {p2_count}")