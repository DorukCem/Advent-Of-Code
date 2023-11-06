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

def search(distances, non_zero, flow_rates):
   max_flow = 0
   def dfs(current_valve, time_remaining, total_flow, visited_valves : set):
      nonlocal max_flow

      visited_valves.add(current_valve)
      total_flow += time_remaining * flow_rates[current_valve]

      max_flow = max(max_flow, total_flow)

      for valve in non_zero:
         if valve in visited_valves:
            continue
         time_to_reach_valve = distances[current_valve][valve]
         if time_remaining - time_to_reach_valve - 1 > 0:
            dfs(valve, time_remaining - time_to_reach_valve - 1, total_flow, visited_valves)        

      visited_valves.remove(current_valve)
   # ---
   dfs(0, 30, 0, set())
   print(max_flow)
# Since time remaining is limited, we will not be going down every path

graph = defaultdict(set) # x -> ( a, b, c)
flow_rates = {} # flow_rate of valve x -> flow_rates[x]
# Parsing the input into a graph 
# ---------
with open( "example.txt", "r") as file:
   lines = file.readlines()
for i, line in enumerate(lines):
   line = line.split()
   valve, rate = line[1], line[4]
   tunnels = line[9:]

   # string formating
   tunnels = [i.strip(",") for i in tunnels]
   rate = int(   rate.strip("rate=").strip(";")   )
   
   for tunnel in tunnels:
      graph[valve].add(tunnel)
   flow_rates[i] = rate
# ---------

# distance from valve x to valve y : distances[x][y]
distances =  all_pairs_shortest_path( adjaceny_matrix_from_graph(graph) ) 
non_zero_valves = {i for i in range(len(distances)) if flow_rates[i]} 

search(distances, non_zero_valves, flow_rates)

# * My algorithm is overshooting