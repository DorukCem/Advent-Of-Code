def contains(a,b,c,d):
   return (c <= a and b <= d) or (a <= c and d <= b)
def overlaps(a,b,c,d):
   set1, set2 = set(range(a,b+1)), set(range(c,d+1))
   return bool(set1.intersection(set2))

ans1 = 0
ans2 = 0
with open("input.txt", "r") as file:
   for line in file:
      s = line

      first, second = s.split(',')
      first = first.split('-')
      second = second.split('-')
      a,b = first
      c,d = second
      a,b,c,d = map(int, [a,b,c,d])
      ans1+=int(contains(a,b,c,d))
      ans2+=int(overlaps(a,b,c,d))
print(ans1)
print(ans2)
