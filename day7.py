def take_input(file_name) -> list[str]:
   with open(file_name, "r") as file:
      return [i.rstrip('\n') for i in file]

# Directory names are not unique
# I can say for example xyz/zzz/xyz
# Here xyz and xyz do not refer to the same directory

def parse_lines(lines : list[str]):
   directories : dict[str : int] = {}
   current_path = []
   files = set()

   for line in lines:
      match line.strip().split(" "):
         case ['$', 'cd', '/']:
            current_path.clear()
         
         case ['$', 'cd', '..']:
            current_path.pop()
         
         case ['$', 'cd', dir_name]:
            current_path.append(dir_name)
         
         case ['$', 'ls']:
            continue

         case ['dir', directory]:
            full_director_name = "/".join(current_path) + "/" + directory if current_path else directory

            if full_director_name not in directories:
               directories[full_director_name] = 0      
         
         case [size, file]:
            full_file_name = "/".join(current_path) + "/" + file if current_path else file
            if full_file_name not in files:
               files.add(full_file_name  )
               for i, _ in enumerate(current_path):
                  dir_path = current_path[:i+1]
                  dir_name = "/".join(dir_path)
                  directories[dir_name] += int(size)
      
   return directories

def sum_sizes(directories : dict[str: int]) -> int:
   sum = 0
   for value in directories.values():
      if value <= 100000 :
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