# -*- coding: utf-8 -*-
import os
import math
import time
class Graph:
    def __init__(self, filename):
        self.nl_city=[]
        path="DATA\\"+filename
        infile=open(path, 'r')  
        Name=infile.readline().strip().split()[1] # NAME
        Comment=infile.readline().strip().split()[1] # COMMENT
        Dimension=infile.readline().strip().split()[1] # DIMENSION
        EdgeWeightType=infile.readline().strip().split()[1] # EDGE_WEIGHT_TYPE
        infile.readline()
        N = int(Dimension)
        for i in range(0, N):
            x,y = infile.readline().strip().split()[1:]
            self.nl_city.append([float(x), float(y)])
        infile.close()

    def edst(self, srcn, dstn) -> int:
        return round(math.sqrt((dstn[0] - srcn[0])**2 + (dstn[1] - srcn[1])**2))
    
    def graph_representation(self) -> list: 
        N = len(self.nl_city)
        graph=[]
        for srci in range(N):
            dstv=[]
            for dsti in range(N):
                if(srci < dsti):
                    dstv.append(self.edst(self.nl_city[srci],self.nl_city[dsti]))
                if(srci == dsti):
                    dstv.append(float('inf'))
                if(srci > dsti):
                    dstv.append(graph[dsti][srci])
            graph.append(dstv)
        return graph
    
class Algorithm:
    def __init__(self):
        self.visited=[]
        self.tot_len=0
        self.pr_time=0
        
    def brute_force(self, start, nl, graph, max_time) -> None:
        start_time=time.time()
        curri=start
        for i in range(len(nl)):
            self.visited.append(curri+1)
            if time.time() - start_time > max_time:
                print("Time out")
                break
            else:
                nxti,nxtv = min(list(enumerate(graph[curri])), key = lambda k: k[1])
                if(nxtv != float('inf')):
                    self.tot_len = self.tot_len + graph[curri][nxti]
                    graph[curri] = [float('inf')]*len(graph[curri])
                    for nxta in range(len(nl)):
                        graph[nxta][curri] = float('inf')
                    curri = nxti
        self.pr_time = time.time() - start_time
        
if __name__ == "__main__":
    nl=Graph('Atlanta.tsp')
    graph=nl.graph_representation()
    alg = Algorithm()
    bf = alg.brute_force(1, nl.nl_city, graph, 300)
    print(alg.visited)
    print(alg.tot_len)
    print(alg.pr_time)


