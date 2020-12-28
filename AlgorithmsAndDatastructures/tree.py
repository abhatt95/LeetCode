class Node:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

    
class BinarySearchTree:

    def __init__(self):
        pass

    def insert(self,root,value):
        if not root:
            root = Node(value)
            return root
        if root.val <= value:
            if root.right:  
                self.insert(root.right,value)
            else:
                root.right = Node(value)
            return root
        if root.left:  
            self.insert(root.left,value)
        else:
            root.left = Node(value)
        return root      
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def BFS(self,root):
        q = [root]
        while q:
            current = q.pop(0)
            if current: print(current.val)
            if current.left: q.append(current.left)
            if current.right: q.append(current.right)

    # preorder() print, left, right 
    # postorder() left, right, print 

bst = BinarySearchTree()

inputs = [7,8,9,3,1,2,4]
root = None
for num in inputs:
    root = bst.insert(root,num)

bst.inorder(root)
print("BFS")
bst.BFS(root)
