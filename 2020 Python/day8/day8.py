def take_input(file_name) -> list[list[int]]:
   with open(file_name, "r") as file:
      return [list(line.rstrip('\n')) for line in file]
   

def search(array, row : int, column : int) -> bool:
   
   current_tree_len = array[row][column]
   
   if row ==  0 or row == len(array)-1 or column == 0 or column == len(array[0])-1:
      return True
   
   left,right,up,down = True,True,True,True

   for i in range(column+1, len(array)):
      if current_tree_len <= array[row][i]: right = False
   
   for i in range(column-1, -1, -1):
      if current_tree_len <= array[row][i]: left = False

   for j in range(row+1, len(array)):
      if current_tree_len <= array[j][column]: up = False
   
   for j in range(row-1, -1, -1):
      if current_tree_len <= array[j][column]: down = False

   return left or right or up or down

# part2

def search_and_count(array, row : int, column : int) -> int:
   current_tree_len = array[row][column]
   
   if row ==  0 or row == len(array)-1 or column == 0 or column == len(array[0])-1:
      return 0
   
   num1, num2, num3, num4 = 0, 0, 0, 0
   for i in range(column+1, len(array)):
      num1+=1
      if current_tree_len <= array[row][i]: 
         break
   
   for i in range(column-1, -1, -1):
      num2+=1
      if current_tree_len <= array[row][i]:
         break

   for j in range(row+1, len(array)):
      num3+=1
      if current_tree_len <= array[j][column]:
         break
   
   for j in range(row-1, -1, -1):
      num4+=1
      if current_tree_len <= array[j][column]:
         break
   
   return num1*num2*num3*num4

def part1():
      ans = 0
      arr = take_input("input.txt")
      for i in range(len(arr)):
         for j in range(len(arr[0])):
            ans += int(search(arr,i,j))
      print(ans)

def part2():
   ans = 0
   arr = take_input("input.txt")
   for i in range(len(arr)):
         for j in range(len(arr[0])):
            ans = max(ans, search_and_count(arr,i,j) )
   print(ans)

part1()
part2()