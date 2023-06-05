def take_input(file_name) -> list[str]:
   with open(file_name, "r") as file:
      return [i.rstrip('\n') for i in file]


def parse_lines(lines : list[str]):
   directories : dict[str : int] = {}
   current_path = []

   for line in lines:

      match line.strip().split(" ", maxsplit=1):
         case ['$', command]:
            match command.split(" "):
               case ['cd', '/']:
                  current_path.clear()
               case ['cd', '..']:
                  current_path.pop()
               case ['cd', dir_name]:
                  current_path.append(dir_name)
               case ['ls']:
                  pass
               
         
         case ['dir', directory]:
            if directory not in directories:
               directories[directory] = 0
         
         case [size, file]:
            for dir in current_path:
               directories[dir] += int(size)

   return directories

def sum_sizes(directories : dict[str: int]) -> int:
   sum = 0
   for value in directories.values():
      if value < 100000 :
         sum+= value
   return sum

def part1():
   print(
      sum_sizes(
         parse_lines(
            take_input("input.txt")
            )
         )
      )

part1()