from copy import deepcopy
n = int(input())

class edge:
    def __init__(self, start, end, w):
        self.start = start
        self.end = end
        self.w = w
        self.visited = False


tree = dict()

for i in range(n - 1):
    s, e, w = input().rstrip().split(" ")
    tree[s] = (s, e, w)

print(tree)


def DFS(node, path, coll):
    if node.visited is True:
        return coll
    node.visited = True
    path.append(node.s)
    nxt = tree[node.e]
    coll = DFS(nxt, deepcopy(path))

    return coll


print(DFS(tree['1'] ,[],{}))



