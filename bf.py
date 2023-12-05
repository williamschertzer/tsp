import os
import math
import time

#Brute-force(vertexList, distMatrix):
#    Initialize an array Path
#    Initialize a float variable to store total path length
#    Select a starting point
#    for cnt in range length(vertexList):
#        if current vertex is not visited:
#            add current vertex to path
#            set closest adjacent vertex as next vertex
#            if next vertex not visited:
#                set next vertex as current vertex
#                add distance between the vertices to total path length

#Function to read file
def read(filename):
    nl_city=[]
    path="DATA/"+filename
    infile=open(path, 'r')  
    Name=infile.readline().strip().split()[1] # NAME
    Comment=infile.readline().strip().split()[1] # COMMENT
    Dimension=infile.readline().strip().split()[1] # DIMENSION
    EdgeWeightType=infile.readline().strip().split()[1] # EDGE_WEIGHT_TYPE
    infile.readline()
    N=int(Dimension)
    for i in range(0, N):
        x,y=infile.readline().strip().split()[1:]
        nl_city.append([float(x), float(y)])
    infile.close()
    return nl_city

#Function to calculate distance
def edst(srcn, dstn) -> int:
    return round(math.sqrt((dstn[0] - srcn[0])**2 + (dstn[1] - srcn[1])**2))

#Function to create distance matrix
def graph_representation(filename) -> list: 
    nl_city=read(filename)
    N=len(nl_city)
    graph=[]
    for srci in range(N):
        dstv=[]
        for dsti in range(N):
            if(srci < dsti):
                dstv.append(edst(nl_city[srci],nl_city[dsti]))
            if(srci == dsti):
                dstv.append(float('inf'))
            if(srci > dsti):
                dstv.append(graph[dsti][srci])
        graph.append(dstv)
    return graph

def brute_force(filename, max_time, start=0) -> None:
    visited=[]
    tot_len=0
    nl=read(filename)
    graph=graph_representation(filename)
    start_time=time.time()
    curri=start
    for i in range(len(nl)):
        visited.append(curri+1)
        if time.time() - start_time > max_time:
            return visited, tot_len       
#            print("Time out")
        else:
            nxti,nxtv = min(list(enumerate(graph[curri])), key = lambda k: k[1])
            if(nxtv != float('inf')):
                tot_len=tot_len + graph[curri][nxti]
                graph[curri]=[float('inf')]*len(graph[curri])
                for nxta in range(len(nl)):
                    graph[nxta][curri]=float('inf')
                curri=nxti
#    self.pr_time = time.time() - start_time
    return visited, tot_len

#Example
#path, length = brute_force("NYC.tsp", 30)
#print(path)
#print(length)
