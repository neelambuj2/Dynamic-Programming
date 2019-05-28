from collections import defaultdict
import copy

graph = defaultdict(list)
visited = defaultdict(list)

def addEdge(u , v, w):
    graph[u].append({'start':u, 'end': v, 'weight': w})
    if u not in visited:
        visited[u] = False
    if v not in visited:
        visited[v] = False

def BFS_util(node, visited):
    queue = []
    queue.append(node)
    visited[node] = True
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for i in graph[s]:
            if visited[i['end']] is False:
                queue.append(i['end'])
                visited[i['end']] = True

def DFS_util(node):
    visited[node['end']] = True
    print(node['start'] ,node['end'], node['weight'])
    s = graph[node['end']]
    for i in s:
        if visited[i['end']] is False:
            DFS_util(i)


def DFS(s,e,w):
    DFS_util({'start':s,'end':e,'weight':w})


def BFS(node):
    BFS_util(node, visited)

addEdge(0, 1, 1)
addEdge(0, 2, 2)
addEdge(1, 2, 2)
addEdge(2, 10, 3)
addEdge(2, 4, 0)
addEdge(4, 6, 2)
addEdge(10, 5, 4)
addEdge(10,6, 7)
addEdge(6, 9, 5)
addEdge(5, 9, 4)
#BFS(0)
DFS(0, 1, 1)
