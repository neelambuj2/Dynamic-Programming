from operator import attrgetter
from collections import defaultdict
import sys
class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

Graph = dict()
visited = dict()
dist = dict()

def add_edge(s,e,w):
    if s not in Graph:
        Graph[s] = list()
    Graph[s].append(Edge(s, e, w))
    if s not in visited:
        dist[s] = sys.maxsize
        visited[s] = False
    if e not in visited:
        dist[e] = sys.maxsize
        visited[e] = False

# alternate of getteratter
# node = min(Graph[source], key= temp)
# def temp(x):
#     return x.weight

def findmin(distance, visited):
    min_node = -1
    distance[-1] = sys.maxsize
    visited[-1] = False
    for key in distance.keys():
        if visited[key] is False and  distance[key]< distance[min_node]:
            min_node = key
    return min_node








def Dijkstras(Graph,source, n, visited, dist):
    dist[source] = 0
    while n > 1:
        minm_node = findmin(dist, visited)
        visited[source] = True
        if visited[minm_node] is False:
            visited[minm_node] = True
            source = minm_node
        for edge in Graph[source]:
            if edge.weight + dist[edge.start] < dist[edge.end]:
                dist[edge.end] = edge.weight + dist[edge.start]


        # minm_node = min(Graph[source], key= lambda x: x.weight)

        n = n-1
    print(dist)


n, m = map(int, input().rstrip().split(" "))
for i in range(m):
    s, e, w = map(int, input().rstrip().split(" "))
    add_edge(s, e, w)
source = int(input())

Dijkstras(Graph, source, n, visited, dist)

