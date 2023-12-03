import sys
import math

# Prim's Algorithm
def prims(graph, n):
    mstset = [False] * n
    mst = [None] * n
    keys = [sys.maxsize] * n
    keys[0] = 0
    mst[0] = -1
    for x in range(n - 1):
        u = find_min_key_vertex(keys, mstset, n)
        mstset[u] = True
        for v in range(n):
            if (graph[u][v] > 0) and (mstset[v] == False) and (keys[v] > graph[u][v]):
                keys[v] = graph[u][v]
                mst[v] = u
    return mst

# Helper method for Prim's                
def find_min_key_vertex(keys, mstset, n):
    min_key = sys.maxsize
    min_key_vertex = -1
    for v in range(n):
        if (keys[v] < min_key) and (mstset[v] == False):
            min_key = keys[v]
            min_key_vertex = v
    return min_key_vertex

# Depth First Traversal
def dfs(mst, start, visited, tour, n):
    tour.append(start)
    visited[start] = True
    for i in range(n):
        if (mst[start][i] == 1) and (not visited[i]):
            dfs(mst, i, visited, tour, n)
    return tour

# Predecessor to Adjacency Matrix
def predecessor_to_matrix(predecessors):
    n = len(predecessors)
    mst_matrix = [[0 for i in range(n)] for j in range(n)]
    for v in range(n):
        predecessor = predecessors[v]
        if predecessor != -1:
            mst_matrix[predecessor][v] = 1
            mst_matrix[v][predecessor] = 1
    return mst_matrix

# Compute total edge cost of tour
def total_edge_cost(graph, tour):
    cost = 0
    for v in range(len(tour)-1):
        cost = cost + graph[tour[v]][tour[v+1]]
    return cost

# Read input parameters
dataset = sys.argv[1]
cutoff = sys.argv[2]
random_seed = sys.argv[3]

# Read dataset
infile = open(dataset, 'r')
name = infile.readline().strip().split()[1] # NAME
comment = infile.readline().strip().split()[1] # COMMENT
dimension = infile.readline().strip().split()[1] # DIMENSION
edge_weight_type = infile.readline().strip().split()[1] # EDGE_WEIGHT_TYPE
infile.readline()
nodelist = []
N = int(dimension)
for i in range(0, N):
    x, y = infile.readline().strip().split()[1:]
    nodelist.append([float(x), float(y)])
infile.close()

# Create adjacency matrix representation graph
graph = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        a = nodelist[i]
        b = nodelist[j]
        graph[i][j] = round(math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2))

# Find MST of graph using Prim's Algorithm
mst_predecessors = prims(graph, N)
mst = predecessor_to_matrix(mst_predecessors)

# Perform a preorder tree walk on MST
visited = [False] * N
tour = []
tour = dfs(mst, 0, visited, tour, N)
tour.append(tour[0])

# Output final solution
quality = total_edge_cost(graph, tour)
sol = [None] * len(tour)
for v in range(len(tour)):
    sol[v] = 'v' + str(tour[v]+1)
output = (quality, sol)

print(output[0])
print(output[1])