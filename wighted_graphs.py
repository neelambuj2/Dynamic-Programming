from collections import defaultdict
import copy

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = defaultdict(list)

    def addEdge(self, u , v, wt):
        temp =[v, wt]
        self.graph[u].append(temp)
        if u not in self.visited:
            self.visited[u] = False
        if v not in self.visited:
            self.visited[v] = False

    def BFS(self, s):
        queue = []
        queue.append(s)
        self.visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if self.visited[i[0]] is False:
                    self.visited[i[0]] = True
                    queue.append(i[0])

    def DFSUtil(self, s, visited):
        visited[s] = True
        print(s, end=" ")

        for i in self.graph[s]:
            if visited[i[0]] is False:
                self.DFSUtil(i[0], visited)

    def DFS(self, v):

        # Mark all the vertices as not visited

        # Call the recursive helper function to print
        # DFS traversal
        self.DFSUtil(v, self.visited)
    def find_min(self, shrt_dist, visited):
        min = 99999
        for i in shrt_dist:
            if shrt_dist[i] < min and visited[i] is False:
                min =shrt_dist[i]

        return min

    def Dijkstras(self, v, shrt_dist, prev_vert):
        self.visited[v] = True
        shrt_dist[v] = 0
        for i in self.graph:
            min_ind = self.find_min(shrt_dist, self.visited)
        self.visited[min_ind] = True



g = Graph()
g.addEdge(0, 1,1)
g.addEdge(0, 2,1)
g.addEdge(1, 2,1)
g.addEdge(2, 10,1)
g.addEdge(2, 4,1)
g.addEdge(4, 6,1)
g.addEdge(10, 5,1)
g.addEdge(10,6,1)
g.addEdge(6, 9,1 )
g.addEdge(5, 9,1)
#g.BFS(2)
g.DFS(2)