# -*- coding: utf-8 -*-
import os
import math
import time

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


