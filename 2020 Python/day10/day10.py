class CPU:
   def __init__(self):
      self.cycle = 0
      self.register = 1
      self.signal_sum = 0
      self.__signal_cycle = 0 # keep count of how many time we have measured the signal strength
      
      self.render_screen =  "" # part2

   def draw_crt(self): # part2
      self.render_screen += " #" if abs(self.register - (self.cycle-1)%40) <= 1 else " ."

      if self.cycle%40 == 0:
         self.render_screen += "\n"

   def increment_cycle(self):
      self.cycle += 1
      self.update_signal_sum()
      self.draw_crt()

   def update_signal_sum(self):
      if self.__signal_cycle > 6 : return
      if (self.cycle + 20)//40 > self.__signal_cycle:
         assert(self.cycle%40 == 20)
         self.__signal_cycle += 1
         self.signal_sum += self.cycle * self.register

   def addx(self, num):
      self.increment_cycle()
      self.increment_cycle()
      self.register += num

   def noop(self):
      self.increment_cycle()

def main():
   cpu = CPU()
   with open("input.txt", "r") as file:
      for line in file:
         match line.split():
            case ["addx", num]:
               cpu.addx(int(num))
            case ["noop"]:
               cpu.noop()

   print(cpu.signal_sum)
   print(cpu.render_screen) # part2

main()