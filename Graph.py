
class AdjNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj_list = [None] * self.V

    def add_edge(self, src, dest):
        node = AdjNode(dest)
        if self.adj_list[src] is None:
            self.adj_list[src] = node

        self.adj_list[src].next = node
        self.adj_list[src] = node


        node = AdjNode(src)
        if self.adj_list[dest] is None:
            self.adj_list[dest] = node
        self.adj_list[dest].next = node
        self.adj_list[dest] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.adj_list[i]
            while temp:
                print(" -> {}".format(temp.data), end="")
                temp = temp.next
            print(" \n")

    def BFS(self, s):
        visited = [False]* (self.V)
        queue = []
        queue.append(s)
        visited[s] = True
        while(queue):
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.adj_list[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


V =5
graph = Graph(V)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.print_graph()
#graph.BFS(2)

