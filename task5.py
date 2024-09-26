class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(node):
    if node:
        print(node.value)
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Preorder Traversal:")
preorder(root)

print("\nInorder Traversal:")
inorder(root)

print("\nPostorder Traversal:")
postorder(root)


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs_stack(root):
    if not root:
        return
    
    stack = [root]
    
    while stack:
        current = stack.pop()
        print(current.value)
        
        for child in reversed(current.children):
            stack.append(child)

root = Node(1)
root.children = [Node(2), Node(3)]
root.children[0].children = [Node(4), Node(5)]
root.children[1].children = [Node(6)]

dfs_stack(root)
