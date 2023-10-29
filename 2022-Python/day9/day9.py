
# Tail must allways be next to or diagonally next to head
# Tail has move in any direction including diagonal to keep this distance 
# if and only if the head is not next to it diagonally next to it
# When moving the head will chose the tile that is next to the head over diagonal tiles
# The head may be in the same tile as the Tail

def is_close(head_pos, tail_pos) -> bool:
   return abs(head_pos[0] - tail_pos[0]) <= 1 and abs(head_pos[1] - tail_pos[1]) <= 1

def sign_of_num(num):
   if num == 0 : return num
   if num >  0 : return  1
   if num <  0 : return -1

def move_tail(head_pos, tail_pos):
   tail_pos[0] += sign_of_num(head_pos[0] - tail_pos[0])
   tail_pos[1] += sign_of_num(head_pos[1] - tail_pos[1])


def part1():
   with open("input.txt", "r") as file:

      head_pos = [0, 0]
      tail_pos = [0, 0]
      visit = set()
      visit.add((0,0))
      for line in file:
         direction, ammount = line.split()
         for _ in range(int(ammount)):
            if direction == "L":
               head_pos[0] -= 1
            if direction == "R":
               head_pos[0] += 1
            if direction == "D":
               head_pos[1] -= 1
            if direction == "U":
               head_pos[1] += 1
            
            if not is_close(head_pos, tail_pos):
               move_tail(head_pos, tail_pos)
               visit.add(tuple(tail_pos))
      
      print(len(visit))

part1()

# Part2 
# Head <- 1 <- 2 <- 3 .. <- 9

def part2():
   with open("input.txt", "r") as file:

      rope = [[0,0] for _ in range(10)]  # rope = [head[ , ], one[ , ],  ... nine[ , ]]
      visit = set()
      visit.add((0,0))
      for line in file:
         direction, ammount = line.split()
         for _ in range(int(ammount)):
            if direction == "L":
               rope[0][0] -= 1
            if direction == "R":
               rope[0][0] += 1
            if direction == "D":
               rope[0][1] -= 1
            if direction == "U":
               rope[0][1] += 1
            
            for i, _ in enumerate(rope):
               if i == 0: continue
               if not is_close(rope[i-1], rope[i]):
                  move_tail(rope[i-1], rope[i])
            visit.add(tuple(rope[9]))

      print(len(visit))

part2()