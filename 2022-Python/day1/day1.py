file = open("input.txt", "r")
max_num = 0
cur = 0
arr = []
for line in file:
	if line != '\n':
		cur+= int(line)
	else:
		max_num = max(max_num, cur)
		arr.append(cur)
		cur = 0
arr.sort(reverse=True)
print(max_num) #part1
print(sum(arr[:3]))  #part2