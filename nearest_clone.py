from copy import deepcopy
import sys
n,m = map(int, input().split(" "))
graph = {}
visited={}
for i in range(m):
    g_from, g_to = map(int, input().split(" "))
    if g_from not in graph:
        graph[g_from] = []
        visited[g_from] = False
    if g_to not in graph:
        graph[g_to] = []
        visited[g_to] = False
    graph[g_from].append(g_to)
    graph[g_to].append(g_from)
color = [int(i) for i in input().rstrip().split(" ")]
val = int(input())
node_list = []
for i in range(len(color)):
    if color[i] == val:
        node_list.append(i+1)
def BFS_util(start_node):
    temp_visit = deepcopy(visited)
    queue = [start_node]
    res = BFS(graph,temp_visit, {start_node:0}, queue, start_node)
    return res

def BFS(graph, visited, d, queue,start_node):
    while(queue):
        node = queue.pop(0)
        visited[node] = True
        if node in node_list and node!=start_node:
            return d[node]
        for i in graph[node]:
            d[i] = d[node]+1
            if visited[i] == False:
                queue.append(i)

dist = sys.maxsize
for i in node_list:
    try:
        dist = min(dist, BFS_util(i))
    except Exception as e:
        continue
if dist == sys.maxsize:
    print(-1)
else:
    print(dist)
