with open( "2022-Python/day17/example.txt", "r") as file:
   winds = file.read()

ROCK1 = [
   ['#', '#', '#', '#', '.', '.', '.']
]

ROCK2 = [
   ['.', '#', '.', '.', '.', '.', '.'],
   ['#', '#', '#', '.', '.', '.', '.'],
   ['.', '#', '.', '.', '.', '.', '.'],
]

ROCK3 = [
   ['.', '.', '#', '.', '.', '.', '.'],
   ['.', '.', '#', '.', '.', '.', '.'],
   ['#', '#', '#', '.', '.', '.', '.'],
]

ROCK4 = [
   ['#', '.', '.', '.', '.', '.', '.'],
   ['#', '.', '.', '.', '.', '.', '.'],
   ['#', '.', '.', '.', '.', '.', '.'],
   ['#', '.', '.', '.', '.', '.', '.'],
]

ROCK5 = [
   ['#', '#', '.', '.', '.', '.', '.'],
   ['#', '#', '.', '.', '.', '.', '.'],
]

class Simulation():
   def __init__(self, winds):
      self.winds = winds
      self.chamber = [["."]*7 for _ in range(4)]
      self.highest_rock = 0
      self.rock_selector = self.select_rock()

   def add_rock(self):
      rock = next( self.rock_selector )
      self.chamber.extend(rock[::])

   def add_height(self, h):
      for _ in range(h):
         self.chamber.append(["."]*7)

   def print_chamber(self):
      for line in self.chamber[::-1]:
         print(line)
      print("---------")
      print("")
   
   def select_rock(self):
      i = 0
      rocks = [ROCK1, ROCK2, ROCK3, ROCK4, ROCK5]
      while True:
         yield rocks[i]
         i+=1
         i%=5


sim = Simulation(winds)
sim.print_chamber()
sim.add_rock()
sim.print_chamber()
sim.add_rock()
sim.print_chamber()