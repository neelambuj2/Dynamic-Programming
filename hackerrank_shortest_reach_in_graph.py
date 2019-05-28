from collections import defaultdict
import sys

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = defaultdict(list)

    def connect(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

        if u not in self.visited:
            self.visited[u] = False
        if v not in self.visited:
            self.visited[v] = False

    def BFSUtil(self, visited, l, queue):
        while queue:
            s = queue.pop(0)
            for i in self.graph[s]:
                if visited[i] is False:
                    visited[i] = True
                    l[i] = l[s]+6
                    queue.append(i)

    def BFS(self, v):

        # Mark all the vertices as not visited

        # Call the recursive helper function to print
        # DFS traversal
        d = {}
        d[v] = 0
        queue = []
        queue.append(v)
        self.visited[s] = True
        self.BFSUtil(self.visited, d, queue)
        return d


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph()
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x, y)
    s = int(input())
    d = graph.BFS(s)
    d.pop(s)
    data = list()
    for i in range(1, n + 1):
        try:
            if i != s:
                data.append(d[i])
        except KeyError as ke:
            data.append(-1)
    print(*data, sep=" ")



