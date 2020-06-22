class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None



class BST:
    def __init__(self,inputValues):
        self.root = TreeNode(int(inputValues[0]))
        nodeQueue = [self.root]
        front = 0
        index = 1
        while index < len(inputValues):
            node = nodeQueue[front]
            front = front + 1

            item = inputValues[index]
            index = index + 1
            if item:
                leftNumber = item
                node.left = TreeNode(leftNumber)
                nodeQueue.append(node.left)

            if index >= len(inputValues):
                break

            item = inputValues[index]
            index = index + 1
            if item :
                rightNumber = item
                node.right = TreeNode(rightNumber)
                nodeQueue.append(node.right)
    
        
    def height(self):
        head = self.root
        if not head: return -1
        return 1 + max(head.left.height(),head.right.height())
    
    def vertices(self):
        head = self.root
        if not head: return 0
        return 1 + head.left.vertices() + head.right.vertices()

    def insert(self, val):
        if not self.root : return TreeNode(val)
        elif self.root.val > val:
            self.root.left = self.root.left.insert(val)
            return self.root.left
        else:
            self.root.right = self.root.right.insert(val)
            return self.root.right
    


    


