"""
Tanya is learning about binary tree and she needs to solve a task. The task is as follows

Given a binary tree of n nodes.you need to print the path from leaf to root for all leaves in the tree

Constraints:

1<=n<=1000

Input:
Firstline consists of integer n
Secondline indicates the tree nodes of binary tree

Output:
print  all the paths from leaf to root

Example:

Input:
9
1 2 3 4 5 6 7 8 9

Output:
8 -> 4 -> 2 -> 1
9 -> 4 -> 2 -> 1
5 -> 2 -> 1
6 -> 3 -> 1
7 -> 3 -> 1

"""
from collections import deque
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def isLeaf(node):
    return node.left is None and node.right is None

def insertLevelOrder(arr, root, i, n): 
    if i < n: 
        temp = Node(arr[i])  
        root = temp  
        root.left = insertLevelOrder(arr, root.left,2 * i + 1, n) 
        root.right = insertLevelOrder(arr, root.right,2 * i + 2, n) 
    return root 
def printPathIterative(leafNode, dict):
    curr = leafNode
    while dict[curr]:
        print(curr.data, end=" -> ")
        curr = dict[curr]

    print(curr.data)

def postorderIterative(root):
    stk = deque()
    dict = {}
    dict[root] = None
    stk.append(root)
    while stk:
        curr = stk.pop()
        if isLeaf(curr):
            printPathIterative(curr, dict)
        if curr.right:
            stk.append(curr.right)
            dict[curr.right] = curr

        if curr.left:
            stk.append(curr.left)
            dict[curr.left] = curr
n=int(input())
x=list(map(int,input().split()))
root=None
root=insertLevelOrder(x,root,0,len(x))
postorderIterative(root)

