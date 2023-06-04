file = open("input.txt", "r")
max_num = 0
cur = 0
for line in file:
	if line != '\n':
		cur+= int(line)
	else:
		max_num = max(max_num, cur)
		cur = 0

print(max_num)