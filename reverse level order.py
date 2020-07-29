"""

Deekshitha is leaning about binary tree and she read about level order traversal of tree and came across a task as follows:

Given a binary trees with n nodes and the task is to print the level wise nodes of the tree in each line in reverse order of levels.

i.e, if the tree has two levels then nodes in 2nd level prints first and nodes in first level prints last.

Constraints:

1<=n<=10000

Input:

Input indicates the nodes of binary tree

Output:

print the nodes in each level in seperate lines

Example:

Input:

1 2 3 4 5 6 7 8 9

Output:
8 9
4 5 6 7
2 3
1

Explanation:
The nodes in 4th level are 8 9 and in 3rd level are 4 5 6 7 and in 2nd level are 2 3 and in 1st level are 1 

Input:

1 2 3 null 5 6 null null null 8 9

Output:
8 9
5 6
2 3
1
"""
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def insertIntoDictionary(dict, key, value):
    dict.setdefault(key, []).append(value)

def preorder(root, level, dict):
    if root is None:
        return
    insertIntoDictionary(dict, level, root.key)
    if root.left:
        if root.left.key!="null":
            preorder(root.left, level + 1, dict)
    if root.right:
        if root.right.key!="null":
            preorder(root.right, level + 1, dict)

def levelOrderTraversal(root):
    dict = {}
    preorder(root, 1, dict)

    for i in range(len(dict), 0, -1):
        print(*(dict.get(i)))
        
def insertLevelOrder(arr, root, i, n): 
    if i < n: 
        temp = Node(arr[i])  
        root = temp  
        root.left = insertLevelOrder(arr, root.left,2 * i + 1, n) 
        root.right = insertLevelOrder(arr, root.right,2 * i + 2, n) 
    return root

x=list(map(str,input().split()))
root=None
root=insertLevelOrder(x,root,0,len(x))
levelOrderTraversal(root)
