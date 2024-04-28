class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
 

def printTopViewOfBinaryTree(root):
    result = []
 
    Q = [[root, 0]]
    #Q = [[12, -1], [10, 3], [14, 2], [56, 10]]
    store = dict()
    while len(Q) > 0:
        currPair = Q.pop(0)
        # [address, hd] 
        node = currPair[0]
        hd = currPair[1]
 
        # something to insert into our result 
        if hd not in store:
            store[hd] = node.data 
 
        if node.left != None:
            Q.append([node.left, hd - 1])
 
        if node.right != None:
            Q.append([node.right, hd + 1])
 
    # key: value
    # {0: 18, -1: 15, 1: 20, -2: 25, 2: 80}
    # allKeys = [0, -1, 1, -2, 2]
    # allKeys = [-2, -1, 0, 1, 2]
    # Top view of binary-tree is:
    # []
    #print(store)
    allKeys = sorted(store.keys())
    for eachKey in allKeys:
        result.append(store[eachKey])
 

    print(*result)

 
# 1. objects creation (memory allocation) 
root = TreeNode(11)
# root:
# data = 15 
# left = None 
# right = None 
obj2 = TreeNode(7)
obj3 = TreeNode(5)
obj4 = TreeNode(9)
obj5 = TreeNode(3)
obj6 = TreeNode(8)
obj7 = TreeNode(10)
obj8 = TreeNode(15)
obj9 = TreeNode(13)
obj10 = TreeNode(20)
obj11 = TreeNode(12)
obj12 = TreeNode(14)
obj13 = TreeNode(18)
obj14 = TreeNode(25)
#    18 
#   15  20 
# 25 30 45 80
 
 
# 2- establishing links between nodes 
root.left = obj2 
root.right = obj8
 
obj2.left = obj3 
obj2.right = obj4
 
obj3.left = obj5

obj4.left = obj6
obj4.right = obj7

obj8.left = obj9
obj8.right = obj10

obj9.left = obj11
obj9.right = obj12

obj10.left = obj13
obj10.right = obj14
printTopViewOfBinaryTree(root)
