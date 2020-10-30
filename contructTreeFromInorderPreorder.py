class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder) :
    if len(preorder) != len(inorder) or len(inorder) == 0:
        return
    ind = 0
    hs = {}
    for i in range(len(inorder)):
        hs[inorder[i]] = i

    def constructTree(l, r):
        nonlocal ind
        if l == r:
            return None
        curRoot = preorder[ind]
        root = TreeNode(curRoot)
        i = hs[curRoot]
        ind += 1
        root.left = constructTree(l, i)
        root.right = constructTree(i + 1, r)
        return root

    return constructTree(0, len(inorder))


def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.val)
    printInorder(node.right)

inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
root = buildTree( preOrder,inOrder)
print("Inorder traversal of the constructed tree is")
printInorder(root)
