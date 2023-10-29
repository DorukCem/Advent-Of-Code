from functools import cmp_to_key

def take_input():
   with open("input.txt", "r") as file:
      # The pairs are being compared not the list orders
      arrs = []
      for line in file:
         if line != "\n":
            arrs.append(eval(line))               
      return arrs
   
def part_one():
   count = 0
   arrs : list = take_input()
   for i in range(0, len(arrs), 2):
      left = arrs[i]
      right = arrs[i+1]
      if compare(left, right) == 1:
         count += i//2 + 1
   print(count)

def compare(first, second):
   first, second = first.copy(), second.copy() # To make this a pure function
   while first and second:
      left = first.pop(0)
      right = second.pop(0)

      if isinstance(left, int) and isinstance(right, int):
         if left < right:
            return 1

         elif left > right:
            return -1
         
      elif isinstance(left, list) and isinstance(right, list):
         comparison = compare(left, right)
         if comparison == 1 or comparison == -1:
            return comparison
      
      #If exactly one value is an integer
      elif isinstance(left, int):
         comparison = compare([left], right)
         if comparison == 1 or comparison == -1:
            return comparison
         
      elif isinstance(right, int):
         comparison = compare(left, [right])
         if comparison == 1 or comparison == -1:
            return comparison

   if not first and second:
      return 1
   elif first and not second:
      return -1
   else:
      return 0
   
def part_two():
   arrs : list = take_input()
   arrs.append([[2]])
   arrs.append([[6]])
   arrs.sort(key = cmp_to_key(compare), reverse=True) 
   first = arrs.index([[2]]) + 1
   second = arrs.index([[6]]) + 1
   print(first * second)

         
part_one()
part_two()

