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
            if not item is None:
                leftNumber = item
                node.left = TreeNode(leftNumber)
                nodeQueue.append(node.left)

            if index >= len(inputValues):
                break

            item = inputValues[index]
            index = index + 1
            if not item is None :
                rightNumber = item
                node.right = TreeNode(rightNumber)
                nodeQueue.append(node.right)
    
        
    def height(self, head = -1):
        if head == -1: head = self.root
        if head is None: return -1
        return 1 + max(self.height(head.left),self.height(head.right))
    
    def vertices(self, head = -1):
        if head==-1: head = self.root
        if head is None: return 0
        print(head.val)
        return 1 + self.vertices(head.left) + self.vertices(head.right)

    def insert(self, val, head = -1):
        if head == -1: head = self.root
        if not head : return TreeNode(val)
        elif head.val > val:
            head.left = self.insert(val, head.left)
            return head.left
        else:
            head.right = self.insert(val, head.right)
            return head.right

    #def delete(self, val):


u = BST([2,0,4])
print(u.vertices())
    


    


