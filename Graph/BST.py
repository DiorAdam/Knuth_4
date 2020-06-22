class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None



class BST:
    def __init__(self):
        
    def insert(root, val):
        if not root : return TreeNode(val)
        elif root.val > val:
            root.left = insert(root.left,val)
            return root.left
        else:
            root.left = insert(root.right,val)
            return root.right
    


