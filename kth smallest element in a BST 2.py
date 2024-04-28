class Treenode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertintoBST(root,ele):
    if root == None:
        newnode = Treenode(ele)
        return newnode

    if root.data > ele :
        root.left = insertintoBST(root.left,ele)
    else:
        root.right = insertintoBST(root.right,ele)
    return root

def fillInorder(inorder,root):
    if root == None:
        return
    fillInorder(inorder,root.left)
    inorder.append(root.data)
    fillInorder(inorder,root.right)
num = int(input())
l = list(map(int,input().split()))
index = int(input())
root = None
for ele in l:
    root = insertintoBST(root,ele)
k = index
inorder = []
fillInorder(inorder,root)
print(inorder[k-1])
