import operator
from functools import reduce

class Monkey:
   def __init__(self):
      self.id = 0
      self.items = []
      self.test_number : int = None
      self.operation_function : function = None
      # Send to these monkey ids after test
      self.true_item_receiver : int = None 
      self.false_item_receiver : int = None 


def take_input() -> list[Monkey]:
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
                  monkey.true_item_receiver = int(id)

               case ["If", "false:", "throw", "to", "monkey", id]:
                  monkey.false_item_receiver = int(id)

         monkeys.append(monkey)
      return monkeys
   

def main(iteration, division):
   monkeys = take_input()
   count = {monkey.id : 0 for monkey in monkeys}
   for _ in range(iteration):
         run_round(monkeys,count, division)
   arr = [i for i in count.values()]
   arr.sort(reverse=True)
   print(arr[0]*arr[1])



def run_round(monkeys, count, worry_divider):
   mod_cap = reduce(operator.mul, [monkey.test_number for monkey in monkeys], 1)
   for monkey in monkeys:
      for item in monkey.items:
         new = monkey.operation_function(item) // worry_divider % mod_cap
         if new % monkey.test_number == 0:
                monkeys[monkey.true_item_receiver].items.append(new)
         else:
               monkeys[monkey.false_item_receiver].items.append(new)
         count[monkey.id] += 1
      monkey.items.clear()


main(20, 3)
main(10000, 1)
print("done")