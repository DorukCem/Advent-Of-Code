stacks = [[] for i in range(9)]
stacks_part2 = [[] for i in range(9)]
with open("input.txt","r") as file:
   for i, line in enumerate(file):
      # get stack contents
      if i<8:
         for j, char in enumerate(line):
            if j%4 == 1 and not char.isspace():
               index = (j-1)//4  
               stacks[index].insert(0, char)
               #part2
               stacks_part2[index].insert(0, char)


      # get instuctions
      if i> 9:
         l = line.split()
         ammount = int(l[1])
         from_stack = int(l[3])
         to_stack = int(l[5])
         #part1
         for _ in range(ammount):
            item = stacks[from_stack-1].pop()
            stacks[to_stack-1].append(item)
         #part2
         stack = stacks_part2[from_stack-1]
         items = stack[-ammount:]
         for _ in range(ammount):
            stack.pop() 
         stacks_part2[to_stack-1].extend(items)
         
   result = ""
   for stack in stacks:
      result += stack[-1]
   print(result)
   
   #part 2
   result = ""
   for stack in stacks_part2:
      result += stack[-1]
   print(result)