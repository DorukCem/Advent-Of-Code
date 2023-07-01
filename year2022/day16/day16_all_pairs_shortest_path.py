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


graph = defaultdict(set) # x -> ( a, b, c)
flow_rates = {}
 
start = None

with open( "example.txt", "r") as file:
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
pressure_gains = [0] * len(distances) # The ammount of pressure we get by moving to that node and opening it

minute = 30
current_index = 0 
accumulated_pressure = 0
while minute:
   minute -= 1
   dist_from_current_to_others = distances[current_index]
   for i, cost in enumerate(dist_from_current_to_others):
      if i in open_valves: 
         continue
      else:
         pressure_gains[i] = (minute - cost) * flow_rates[i]

   best_valve_to_open = pressure_gains.index( max(pressure_gains) )
   open_valves.add(best_valve_to_open)
   time_to_open_valve = dist_from_current_to_others[best_valve_to_open]
   minute -= time_to_open_valve

   for v in open_valves:
      accumulated_pressure += flow_rates[v]
   
   pressure_gains = [0] * len(distances)
   
   print(accumulated_pressure)

print(accumulated_pressure)
print(distances[0][9])