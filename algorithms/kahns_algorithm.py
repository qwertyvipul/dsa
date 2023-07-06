from collections import defaultdict
from typing import List

class Graph:
    def __init__(self, vertices: int):
        self.graph = defaultdict(list) # Adjacency list
        self.V = vertices # No. of vertices
        
    def addEdge(self, u: int, v: int):
        self.graph[u].append(v)
        
    def topologicalSort(self) -> List[int]:
        inDegree = [0] * self.V
        
        for u in self.graph:
            for v in self.graph[u]:
                inDegree[v] += 1
            
        # Enqueue all vertices with indegree 0
        queue = []
        for i in range(self.V):
            if inDegree[i] == 0:
                queue.append(i)
                
        count = 0
        order = []
        
        while queue:
            u = queue.pop(0)
            order.append(u)
            
            for v in self.graph[u]:
                inDegree[v] -= 1
                
                if inDegree[v] == 0:
                    queue.append(v)
            
            count += 1
            
        if count != self.V:
            print("COUNT = ", count)
            raise Exception("There exists a cycle in the graph")
            
        return order
    
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
              
g.topologicalSort()