from operator import attrgetter

class Edge:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight
def findparent(parent, v):
    if parent[v] == v:
        return v
    return findparent(parent, parent[v])

def kruskals(graph, n):
    graph.sort(key=lambda x: x.weight, reverse=True)
    count = 0
    i=0
    parent = [int(i) for i in range(n)]
    output = list()


    while count!=n-1:
        curr_edge = graph[i]
        src_parent = findparent(parent, curr_edge.source)
        dest_parent = findparent(parent, curr_edge.dest)

        if src_parent!=dest_parent:
            output.append(curr_edge)
            count +=1
            parent[src_parent] = dest_parent
        i+=1

    for i in output:
        print(i.__dict__)


n = int(input())
e = int(input())
graph = []
for i in range(e):
    s, d, w = [int(i) for i in input().strip().split(' ')]
    graph.append(Edge(s, d, w))
kruskals(graph, n)



