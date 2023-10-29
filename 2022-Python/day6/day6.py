def take_input(file_name) -> str : 
   with open(file_name+".txt", "r") as file:
      data = file.read()
      return data

def is_unqiue(substring : str) -> bool:
   return len(substring) == len(set(substring))

def find_unique(string, num_unique : int) -> int:
   for i in range(len(string)-num_unique-1):
      if is_unqiue(string[i:i+num_unique]):
         return i+num_unique
   return -1


def part1():
   print(
      find_unique(
         take_input("input"), 4
         )
   )
   
def part2():
   print(
      find_unique(
         take_input("input"), 14
         )
   )

part1()
part2()