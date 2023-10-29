capital =  {chr(i):i-65+27 for i in range(65, 91)}
lowercase = {chr(i):i-96 for i in range(97, 123)}
prio = {**capital, **lowercase}


sum = 0
with open("input.txt", "r") as file:
   for line in file:
      s = line
      first = s[:len(s)//2]
      second = s[len(s)//2:]

      lets1 = set(first)
      lets2 = set(second)

      ans = lets1.intersection(lets2)
      let = ans.pop()
      sum += prio[let]
print(sum)


# part2
sum = 0
with open("input.txt", "r") as file:
   s = set()
   for i, line in enumerate(file):
      if i%3 == 0:
         s = set(line)
      else:
         s = s.intersection(set(line))
      
      if i%3 == 2:
         s.discard('\n')
         let = s.pop()
         sum += prio[let]
print(sum)