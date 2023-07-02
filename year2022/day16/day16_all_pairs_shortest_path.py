from collections import defaultdict

def adjaceny_matrix_from_graph(graph) -> list[list]:
   matrix = [[float("inf")]*len(graph) for _ in graph]
   for i, _ in enumerate(graph):
      matrix[i][i] = 0

   indices = {v:i for i, v in enumerate(graph.keys())}
   for i, vertex in enumerate(indices):
      neighbors =  graph[vertex]
      for n in neighbors:
         j = indices[n]
         matrix[i][j] = 1
   return matrix

def all_pairs_shortest_path(matrix : list[list]) -> list[list]:
   v = len(matrix)
   for k in range(0, v):
      for i in range(0, v):
         for j in range(0, v):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
               matrix[i][j] = matrix[i][k] + matrix[k][j]
   return matrix

def travelling_salesman(matrix, rates, budget = 30, current_index = 0, open_valves = set() , accumulated_pressure = 0):
   pass

graph = defaultdict(set) # x -> ( a, b, c)
flow_rates = {}
start = None

with open( "input.txt", "r") as file:
   lines = file.readlines()
for i, line in enumerate(lines):
   line = line.split()
   valve, rate = line[1], line[4]
   tunnels = line[9:]

   if not start : start = valve # set starting valve
   # string formating
   tunnels = [i.strip(",") for i in tunnels]
   rate = int(   rate.strip("rate=").strip(";")   )
   
   for tunnel in tunnels:
      graph[valve].add(tunnel)
   flow_rates[i] = rate

distances =  all_pairs_shortest_path( adjaceny_matrix_from_graph(graph) )
open_valves = set()

minute = 0
current_index = 0 
accumulated_pressure = 0
while minute < 30:
   minute += 1
   pressure_gains = [0] * len(distances) # The ammount of pressure we get by moving to that node and opening it

   for v in open_valves:
      accumulated_pressure += flow_rates[v] 
   
   dist_from_current_to_others = distances[current_index]
   for i, cost in enumerate(dist_from_current_to_others):
      if i in open_valves: 
         continue
      else:
         pressure_gains[i] = ((30 - minute) - cost) * flow_rates[i]

   best_valve_to_open = pressure_gains.index( max(pressure_gains) )
   time_doing_task = dist_from_current_to_others[best_valve_to_open]
   
   while time_doing_task and minute <= 30:
      time_doing_task -= 1
      minute += 1 
      for v in open_valves:
         accumulated_pressure += flow_rates[v] 

   print(current_index)
   open_valves.add(best_valve_to_open)
   current_index = best_valve_to_open
     
print(accumulated_pressure)

# ** When given the correct path order we can calculate the pressure gains correctly
# ! We cannot find the optimal path
# TODO I guess we need to implement a way of doing this top down DP problem
# ! I really do not know how this relates to DP, feel mostly like a travlling salesman problem