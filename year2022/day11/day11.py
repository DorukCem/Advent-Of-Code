from functools import cache
class Monkey:
   def __init__(self):
      self.id = 0
      self.items = []
      self.operation_function = None
      self.test_number = None
      # Send to these monkeys after test
      self.true_item_reciver = None 
      self.false_item_reciver = None 

   @cache
   def test(self, item):
      return item % self.test_number == 0

def take_input():
   with open("input.txt", "r") as file:
      monkey_strings = file.read().split("\n\n")

      monkeys = []

      for string in monkey_strings:
         monkey = Monkey()
         for line in string.split("\n"):
            match line.split():
               case ["Monkey", num_txt]:
                  monkey.id = int(num_txt[0])

               case ["Starting", "items:", *rest]:
                  monkey.items = [int(i.strip(",")) for i in rest]
                  
               case ["Operation:", "new", "=", old, op, var2]:
                  # Create and assign the function at runtime 
                  monkey.operation_function = eval(f"lambda {old} : {old} {op} {var2}") 

               case ["Test:", "divisible", "by", num_txt]:
                  monkey.test_number = int(num_txt.strip(":"))
               
               case ["If", "true:", "throw", "to", "monkey", id]:
                  monkey.true_item_reciver = int(id)

               case ["If", "false:", "throw", "to", "monkey", id]:
                  monkey.false_item_reciver = int(id)

         monkeys.append(monkey)
      return monkeys

def main(rounds, divide):
   monkeys = take_input()
   count = {monkey.id : 0 for monkey in monkeys}

   for _ in range(rounds):
      for monkey in monkeys:
         for item in monkey.items:
            item = monkey.operation_function(item)
            item //= divide

            target = monkey.true_item_reciver if monkey.test(item) else monkey.false_item_reciver
            monkeys[target].items.append(item)
            count[monkey.id] += 1

         monkey.items.clear()
   
   arr = [i for i in count.values()]
   arr.sort(reverse=True)
   print(arr[0]*arr[1])

main(20, 3)
main(1000, 1)
print("done")