def take_input():
   lists = []
   with open("input.txt", "r") as file:
      for line in file:
         if line != "\n":
            arr =  eval(line)
            lists.append(arr)
      return lists
   
def part_one():
   lists = take_input()
   for i in range(len(lists)-1):
      left = lists[i]
      right = lists[i+1]

      if isinstance(left, int) and isinstance(right, int):
         pass

      elif isinstance(left, list) and isinstance(right, list):
         pass

      else:
         pass

part_one()