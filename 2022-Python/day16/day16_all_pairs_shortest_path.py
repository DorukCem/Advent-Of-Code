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
flow_rates = {} # flow_rate of valve x -> flow_rates[x]
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

# distance from valve x to valve y : distances[x][y]
distances =  all_pairs_shortest_path( adjaceny_matrix_from_graph(graph) ) 
non_zero = [i for i in range(len(distances)) if flow_rates[i]]


all_paths = [] 
# DFS
visit = set()
stack = [start]
while stack:
   current = stack.pop()
   if current not in visit:
      visit.add(current)

# * Something like this might be useful if I am going to use DFS
# Remove current vertex from path[] and mark it as unvisited
#   path.pop()
#   visited[u]= False
# ! If we are going with DFS I have to figure the visit algorithm
# https://stackoverflow.com/questions/9535819/find-all-paths-between-two-graph-nodes