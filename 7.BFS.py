from collections import defaultdict as dd

class Graph:

    def __init__(self):
        self.graph = dd(list)

    def addEdgetoGraph(self, x, y):
        self.graph[x].append(y)

    def BFSearch(self, n):
        visited_vertices = (len(self.graph))*[False]
        queue = []
        visited_vertices[n] = True
        queue.append(n)

        while queue:
            n = queue.pop(0)
            print(n, end = " ")

            for v in self.graph[n]:
                if visited_vertices[v] == False:
                    queue.append(v)
                    visited_vertices[v] = True

graph = Graph()
graph.addEdgetoGraph(0, 1)
graph.addEdgetoGraph(1, 1)
graph.addEdgetoGraph(2, 2)
graph.addEdgetoGraph(3, 1)
graph.addEdgetoGraph(4, 3)
graph.addEdgetoGraph(5, 4)

print("The Breadth First Search Traversal for The Graph is as Follows:")
graph.BFSearch(3)
