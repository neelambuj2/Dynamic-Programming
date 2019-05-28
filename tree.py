import sys
import os
import copy
class tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data



    def insert(self, data):


        if self.data < data:
            if self.right == None:
                self.right = tree(data)
            else:
                self.right.insert(data)


        elif self.data > data:
            if self.left == None:
                self.left = tree(data)
            else:
                self.left.insert(data)

    def Print(self):
        if self.left:
            self.left.Print()
        print(self.data, end=" ")
        if self.right:
            self.right.Print()



    def findmin(self):
        while self.left:
            self = self.left
        return self.data

    def findmax(self):
        while self.right:
            self = self.right
        return self.data

    def findmin_recursion(self):
        if self.left:
            return (min(self.left.findmin_recursion(),self.data))
        else:
            return self.data
    def findmax_recursion(self):
        if self.right:
            return(max(self.right.findmax_recursion(),self.data))

        else:
            return self.data


def maxDepth(node):
    if node is None:
        return 0;

    else:

        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        # Use the larger one
        if (lDepth > rDepth):
            return lDepth + 1
        else:
            return rDepth + 1

def find_min(root):
    while root.left:
        root = root.left
    return root

def height( node):
    if node is None:
        return(-1)

    else:
        return (max(height(node.left), height(node.right))+1)


def print_preorder(node):
    if node is None:
        return
    print(node.data, end= " ")
    print_preorder(node.left)
    print_preorder(node.right)

def print_postorder(node):
    if node:
        print_postorder(node.left)
        print_postorder(node.right)
        print(node.data, end=" ")

def print_level_order(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while (bool(queue)):
        print(queue[0].data, end=" ")
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


def printLevelOrder(root):
    if root is None:
        return

# Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while (bool(queue) > 0):
        # Print front of queue and remove it from queue
        print
        queue[0].data,
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

            # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


def delete(root, data):

    if root is None:
        return
    elif data < root.data:
        root.left = delete(root.left, data)

    elif data > root.data:
        root.right = delete(root.right, data)

    else:  # found the node to be deleted
        if root.left is None :
            temp = root
            root = root.right
            del(temp)
        elif root.right is None :
            temp = root
            root = root.left
            del(temp)
        else:
            node = find_min(root.right)
            root.data = node.data
            root.right = delete(root.right, node.data)
    return root

intmax = sys.maxsize
intmin = -sys.maxsize
def IsBstutil(root, mini, maxi):
    if root is None:
        return True
    if root.data >maxi or root.data < mini:
        return False
    return IsBstutil(root.left,mini, root.data-1 ) and IsBstutil(root.right,root.data+1, maxi)

def IsBinarySearchTree(root):
    if IsBstutil(root, intmin, intmax):
        print("It is a BST")
    else:
        print("Not a bst")

def left_boundary(root):
    if root:
        if root.left:
            print(root.data, end=" ")
            left_boundary(root.left)

        elif root.right:
            print(root.data, end=" ")
            left_boundary(root.right)


def right_boundary(root):
    if root:
        print(root.data, end= " ")
        if root.right:
            left_boundary(root.right)
        elif root.left:
            left_boundary(root.left)

def leaf_nodes(root):
    if root is None:
        return
    leaf_nodes(root.left)
    leaf_nodes(root.right)
    if root.left is None and root.right is None:
        print(root.data, end= " ")


def findminroot(root):
    while root.left :
        root = root.left
    return root

def findroot(root, data):
    if data < root.data:
        return findroot(root.left, data)
    elif data > root.data:
        return findroot(root.right, data)

    else:
        return root

def inorder_succesor(root, data):
    current = findroot(root, data)

    if current is None:
        return
    elif current.right is not None:
        node = findminroot(current.right)
        print(node.data)
    elif current.right is None:

        while current != root:
            if current.data<root.data:
                succesor = root
                root = root.left
            else:
                root = root.right

        print(succesor.data)

class lst:
    def __init__(self):
        self.arr=[]
array = lst()
def findpath(root, data):
    if root is None:
        return False
    if root.data < data:

        if findpath(root.right, data):
            array.arr.append(root.data)
            return True

    if root.data > data:

        if findpath(root.left, data):
            array.arr.append(root.data)
            return True


    else:
        array.arr.append(root.data)
        return True

def find_path(root, data, path):
    if root is None:
        return False
    if root.data < data:
        path = find_path(root.right, data, path)

        if bool(path):
            path.insert(0,root.data)
            return path

    if root.data > data:
        path = find_path(root.left, data, path)

        if bool(path):
            path.insert(0,root.data)
            return path


    if root.data == data:
        path.insert(0,root.data)
        return path

def find_path_test(root, data, path):
    if root is None:
        return False
    if root.data < data:
        if find_path(root.right, data, path):
            path.insert(0,root.data)
            return True

    if root.data > data:
        if find_path(root.left, data, path):
            path.insert(0,root.data)
            return True


    if root.data == data:
        path.insert(0,root.data)
        return True



def find_lowest_common_ancestor(root,node1, node2):
    p1=find_path(root,node1,[])
    p2=find_path(root,node2,[])
    l=min(len(p1),len(p2))
    for i in range(0,l):

        if p1[i]!=p2[i]:
            break
    return p1[i-1]

def all_paths_toleaf(root,path):
    if root is None:
        return
    path.append(root.data)
    all_paths_toleaf(root.left, copy.deepcopy(path))
    # if root.left is None and root.right is None:
    #     print(path)
    all_paths_toleaf(root.right, copy.deepcopy(path))

    if root.left is None and root.right is None:
        print(path)

def spiral_traversal(root):
    if root is None:
        return
    queue1 = []
    queue2 = []

    queue1.append(root)

    while(bool(queue1) or bool(queue2)):
        while(bool(queue1)):

            node = queue1.pop()
            print(node.data, end=" ")
            if node.right is not None:
                queue2.append(node.right)
            if node.left is not None:
                queue2.append(node.left)
        while(bool(queue2)):
            node = queue2.pop()
            print(node.data, end=" ")
            if node.left is not None:
                 queue1.append(node.left)
            if node.right is not None:
                queue1.append(node.right)


def find_min_height(root):
    if root is None:
        return intmax


    if root.left is None and root.right is None:
        return 0
    else:
        return min(find_min_height(root.left)+1, find_min_height(root.right)+1)

def check_balanced(root):
    if root is None:
        return 0
    l = check_balanced(root.left)
    r = check_balanced(root.right)
    if l is False or r is False:
        return False
    if abs(l-r)>1:
        return False
    else:
        return max(l,r)+1

def print_level_order2(root):
    h= height(root)
    for i in range(1,h+2):
        printGivenLevel(root, i, [0])

def printGivenLevel(root, i, s):
    if root is None:
        return
    if i==1 and s[0]==0:
        s[0]=1
        print(root.data, end=" ")
    elif i>1:
        printGivenLevel(root.left, i-1,s)
        printGivenLevel(root.right, i-1, s
                        )
def PrintLeftView(root, level, max_level):
    if root is None:
        return

    if max_level[0]<level:
        print(root.data, end=" ")
        max_level[0]= level
    PrintLeftView(root.left, level+1,max_level)
    PrintLeftView(root.right, level+1, max_level)

def PrintRightView(root, level, max_level):
    if root is None:
        return

    if max_level[0] < level:
        print(root.data, end=" ")
        max_level[0] = level
    PrintLeftView(root.right, level + 1, max_level)
    PrintLeftView(root.left, level + 1, max_level)

def VerticalTraversAL(root, level, traversal):
    if root is None:
        return
    if level not in traversal.keys():
        traversal[level] = []
    traversal[level].append(root.data)
    VerticalTraversAL(root.left,level+1, traversal)
    VerticalTraversAL(root.right, level-1, traversal)


def getVerticalOrder(root, hd, m):
    # Base Case
    if root is None:
        return

    # Store current node in map 'm'
    try:
        m[hd].append(root.data)
    except:
        m[hd] = [root.data]

        # Store nodes in left subtree
    getVerticalOrder(root.left, hd - 1, m)

    # Store nodes in right subtree
    getVerticalOrder(root.right, hd + 1, m)


# The main function to print vertical order of a binary
# tree ith given root
def printVerticalOrder(root):
    # Create a map and store vertical order in map using
    # function getVerticalORder()
    m = dict()
    hd = 0
    getVerticalOrder(root, hd, m)

    # Traverse the map and print nodes at every horizontal
    # distance (hd)
    for index, value in enumerate(sorted(m)):
        for i in m[value]:
            print(i, end=" ")


def VerticaltraversalLevelOrder(root):
    if root is None:
        return

# Create an empty queue for level order traversal
    queue = []
    vdict = {}
    level = 0
    # Enqueue Root and initialize height
    queue.append({0: root})
    vdict[0] = [root.data]


    while (bool(queue) > 0):
        # Print front of queue and remove it from queue
        #print(queue[0].data, end=" ")
        temp = queue.pop(0)
        level =list(temp.keys())[0]
        node = temp[level]
        print(node.data, end=" ")
        # Enqueue left child
        if node.left is not None:
            level=level+1
            if level not in vdict.keys():
                vdict[level] = []
            vdict[level].append(node.left.data)
            queue.append({level:node.left})
            level = level -1

            # Enqueue right child
        if node.right is not None:
            level = level -1
            if level not in vdict.keys():
                vdict[level] = []
            vdict[level].append(node.right.data)
            queue.append({level:node.right})

    return vdict

def check_sum_tree(root):
    lsum =0
    rsum =0
    if root.left:
        lsum = check_sum_tree(root.left)
        if lsum is False:
            return False
    if root.right:
        rsum = check_sum_tree(root.right)
        if lsum is False:
            return False

    if not root.left and not root.right:
        return root.data

    if lsum + rsum != root.data:
        return False
    return lsum+rsum+root.data

def check_sum_tree2(root, indicator):
    if indicator[0] is False:
        return
    lsum =0
    rsum =0
    if root.left:
        lsum = check_sum_tree2(root.left, indicator)
    if root.right:
        rsum = check_sum_tree2(root.right, indicator)


    if not root.left and not root.right:
        return root.data

    if lsum + rsum != root.data:
        indicator[0] = False
        return 0
    return lsum+rsum+root.data



root = tree(12)
root.insert(6)
root.insert(16)
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(13)
root.insert(14)
root.insert(11)
root.insert(7)
root.insert(8)
# root.Print()
# print(root.findmin())
# print(root.findmax())
# print(root.findmin_recursion())
# print(root.findmax_recursion())
# print(height(root),"**")
# print(maxDepth(root))
#print_preorder(root)
# print_postorder(root)
# print_level_order(root)
# left_boundary(root)
# leaf_nodes(root)
# right_boundary(root.right)

#printLevelOrder()

# delete(root, 11)
# print_level_order(root)
# IsBinarySearchTree(root)
# inorder_succesor(root,6)
# a=[]
# findpath(root,14)
# print(array.arr)
# print(find_lowest_common_ancestor(root,5,6))
# path=[]
# find_path_test(root, 8, path)
# print(path)
# all_paths_toleaf(root,[])
# spiral_traversal(root)
# print(find_min_height(root))
# print(check_balanced(root))
#print_level_order2(root)
#PrintRightView(root,1,[0])
# traversal ={}
# VerticalTraversAL(root, 0 , traversal)
# print(traversal)
# keylist = list(traversal.keys())
# keylist.sort(reverse=True)
# for key in keylist:
#     print(traversal[key], end= " ")
#
# printVerticalOrder(root)
# res = (VerticaltraversalLevelOrder(root))
# k = list(res.keys())
# k.sort(reverse=True)
print("****")
# for i in k:
#     for j in res[i]:
#         print(j , end=" ")
# k = list(res.keys())
# k.sort(reverse=True)
# for i in k:
#     print(res[i][0], end=" ")
root = tree(26)
root.left = tree(10)
root.right = tree(3)
root.left.left= tree(4)
root.left.right = tree(6)
root.right.right = tree(3)
# print_level_order(root)

result = check_sum_tree(root)
if not result:
    print("Not a sum tree")
if type(result) is int:
    print("IS a sum tree")